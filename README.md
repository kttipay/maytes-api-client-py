# Maytes Python SDK

Official Python client for the [Maytes API](https://developers.maytes.co) — create,
capture and cancel checkouts, and verify inbound webhook signatures.

> **Generated package.** This repository is a build artefact, published from the
> Maytes API service definition. Pull requests here are not accepted — file
> issues instead, and fixes land upstream in the source model.

## Install

```bash
pip install maytes-api-client-py
```

## Usage

The client mints an OAuth2 `client_credentials` token on first use, caches it,
and — on a `401` — refreshes and retries the request once. There is no
client-side expiry maths to get wrong, and no proactive refresh to schedule.

```python
from maytes_api_client import create_maytes_api_client, verify_webhook_signature

client = create_maytes_api_client(endpoint, client_id, client_secret)
checkout = client.create_checkout(request)

event = verify_webhook_signature(raw_body, signature_header, signing_secret)
```

The PyPI project is `maytes-api-client-py`; the import package is
`maytes_api_client`.

### Verifying webhooks

Verify **before** parsing the body, and pass the raw request bytes — not a
re-encoded object. Re-serialising changes the bytes and the signature will not
match. The event id is stable across retries, so deduplicate on it.

## Documentation

Full integration docs: <https://developers.maytes.co>

## License

MIT — see [LICENSE](LICENSE).
