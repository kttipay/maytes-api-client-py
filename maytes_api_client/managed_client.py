"""Bundled with the generated SDK via bin/postprocess-python.sh.

Lives at build/python-client/maytes_api_client/managed_client.py after a
`make generate-python`. Exported from maytes_api_client/__init__.py.

Adds OAuth2 client_credentials credential management on top of the raw
DefaultApi using a **reactive 401-retry** pattern:

  1. First authed call mints a token via GetOAuthToken (a @auth([]) op) and
     caches it.
  2. Subsequent calls send the cached token as-is — no client-side expiry
     math, no proactive refresh.
  3. If the server returns 401, _ManagedApiClient catches the ApiException,
     refreshes the token, and retries the call once. If the retry also 401s,
     the error propagates.

Concurrent 401s deduplicate via `refresh_if_stale(stale_token)`: only the
first caller to acquire the lock mints; others see the cache already updated
and use that token instead.
"""

from __future__ import annotations

import threading
from typing import Any, Optional

from uuid import UUID

from .api.default_api import DefaultApi
from .api_client import ApiClient
from .configuration import Configuration
from .exceptions import ApiException
from .models.o_auth_token_request import (
    OAuthTokenRequest,
)


class OAuthTokenProvider:
    """Caches an OAuth2 client_credentials token; refreshes only on demand.

    Threadsafe — concurrent refreshes serialize behind a lock and dedup
    via the `stale_token` snapshot.
    """

    def __init__(
        self,
        endpoint: str,
        client_id: str,
        client_secret: str,
        initial_token: Optional[str] = None,
    ) -> None:
        self._endpoint = endpoint
        self._client_id = client_id
        self._client_secret = client_secret
        self._token: Optional[str] = initial_token
        self._lock = threading.Lock()
        self._unauthed_api = DefaultApi(ApiClient(Configuration(host=endpoint)))

    def get(self) -> str:
        if self._token is not None:
            return self._token
        with self._lock:
            if self._token is not None:
                return self._token
            return self._mint_unlocked()

    def refresh_if_stale(self, stale_token: Optional[str]) -> str:
        """Mint a new token only if the cache still holds the stale one the
        caller observed. If another concurrent caller already refreshed,
        return that newer token instead — no second mint.
        """
        with self._lock:
            if self._token is not None and self._token != stale_token:
                return self._token
            return self._mint_unlocked()

    def _mint_unlocked(self) -> str:
        response = self._unauthed_api.get_o_auth_token(
            OAuthTokenRequest(
                grant_type="client_credentials",
                client_id=UUID(self._client_id),
                client_secret=self._client_secret,
            )
        )
        assert response.access_token is not None
        self._token = response.access_token
        return self._token


class _ManagedConfiguration(Configuration):
    """Configuration whose access_token always delegates to the provider.

    Property + setter combo so Configuration.__init__'s `self.access_token =
    access_token` doesn't blow up — the setter just no-ops.
    """

    def __init__(self, provider: OAuthTokenProvider, *, host: str) -> None:
        super().__init__(host=host)
        object.__setattr__(self, "_provider", provider)

    @property  # type: ignore[override]
    def access_token(self) -> str:
        return self._provider.get()

    @access_token.setter
    def access_token(self, value: Optional[str]) -> None:
        # Configuration.__init__ sets self.access_token = None — accept + ignore.
        pass


class _ManagedApiClient(ApiClient):
    """ApiClient that intercepts 401 *responses* (status code, not exception)
    inside call_api, refreshes the token, and replays the request once with
    the new Authorization header.

    Recent openapi-generator-cli Python templates split the HTTP layer in two:
    `call_api` performs the request and returns a raw RESTResponse (status +
    headers + body); the downstream `response_deserialize` is what turns a
    non-2xx status into an ApiException. So the retry has to live inside
    `call_api` — by the time `response_deserialize` raises, we no longer have
    the request parameters needed to replay.
    """

    def __init__(self, configuration: Configuration, provider: OAuthTokenProvider) -> None:
        super().__init__(configuration)
        self._provider = provider

    def call_api(
        self,
        method: str,
        url: str,
        header_params: Optional[dict] = None,
        body: Any = None,
        post_params: Any = None,
        _request_timeout: Any = None,
    ) -> Any:
        # Snapshot the token actually used on the wire so refresh_if_stale can
        # dedup against concurrent refreshes. Parsed from the Authorization
        # header rather than re-asking the provider, because by the time we
        # get here the header has already been built upstream.
        stale_token: Optional[str] = None
        if header_params and isinstance(header_params.get("Authorization"), str):
            auth = header_params["Authorization"]
            if auth.startswith("Bearer "):
                stale_token = auth[len("Bearer "):]

        response = super().call_api(
            method, url,
            header_params=header_params,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout,
        )

        if response.status != 401 or stale_token is None:
            return response

        # 401 — refresh, rebuild auth header, retry once. If the retry also
        # 401s, return that response and let response_deserialize raise.
        new_token = self._provider.refresh_if_stale(stale_token)
        retry_headers = dict(header_params) if header_params else {}
        retry_headers["Authorization"] = "Bearer " + new_token
        return super().call_api(
            method, url,
            header_params=retry_headers,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout,
        )


def create_maytes_api_client(
    endpoint: str,
    client_id: str,
    client_secret: str,
    initial_token: Optional[str] = None,
) -> DefaultApi:
    """Returns a fully managed DefaultApi.

    Tokens are minted on first authed call, cached, and refreshed reactively
    when the server returns 401. Operations declared @auth([]) in the Smithy
    (getHealth, getOAuthToken) carry no security requirement and skip the Authorization header.

        from maytes_api_client import create_maytes_api_client
        api = create_maytes_api_client(
            endpoint="https://api.maytes.co",
            client_id="...",
            client_secret="...",
        )
        result = api.create_checkout(CreateCheckoutRequest(...))

    `initial_token` is an SDK-test-only escape hatch — seeds the cache with a
    pre-minted JWT. Used by the E2E test path to verify the wrapper's reactive
    401-retry behavior when the seeded token expires. Production callers omit
    this; the first authed call will mint via /oauth/token.
    """
    provider = OAuthTokenProvider(endpoint, client_id, client_secret, initial_token)
    config = _ManagedConfiguration(provider, host=endpoint)
    return DefaultApi(_ManagedApiClient(config, provider))
