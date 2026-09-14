"""Bundled with the generated SDK via bin/postprocess-python.sh.

Lives at build/python-client/maytes_api_client/webhook_verifier.py after a
`make generate-python`. Exported from maytes_api_client/__init__.py.

Verifies the `X-Maytes-Signature` header on an inbound webhook delivery and
returns the parsed event. Merchants must never hand-roll this — see the four
sharp edges below, each of which silently produces either a security hole or
an outage:

  1. RAW BODY. The signature covers the exact bytes we sent. Verifying against
     re-serialised JSON (json.dumps(request.json)) fails for any body whose key
     order or number formatting differs after a parse/emit round-trip. This is
     the single most common webhook integration bug.
  2. MULTIPLE `v1=` ENTRIES. During a signing-secret rotation grace window the
     header carries TWO signatures (current secret first, previous second) and
     the delivery is valid if EITHER matches. A verifier that reads only the
     first `v1=` works perfectly until the first rotation, then rejects live
     traffic. See §7 of the webhook spec.
  3. CONSTANT-TIME COMPARISON. A plain `==` on digests leaks how much of a
     forged signature was correct, which is enough to recover a valid
     signature one byte at a time.
  4. REPLAY WINDOW. The `t=` timestamp is the anti-replay anchor; a captured
     delivery stays valid forever without a freshness check.

Verification and JSON parsing are deliberately fused into ONE call: the
function takes raw bytes and hands back the parsed event, so there is no
intermediate state in which a caller can parse first and verify second.

Algorithm (webhook spec §6.1):
    signed_payload = f"{t}.{raw_body}"
    signature      = lowercase_hex( HMAC_SHA256(signing_secret, signed_payload) )
"""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

#: Default anti-replay window, in seconds (webhook spec §6.1 advises ~5 min).
DEFAULT_TOLERANCE_SECONDS = 300

#: Why a delivery failed verification. Log it; never echo it to the caller.
#:   "malformed_header"            — header absent or missing `t=` / `v1=`
#:   "timestamp_out_of_tolerance"  — `t=` too far from now; possible replay
#:   "no_matching_signature"       — wrong secret, or the body was modified
#:   "invalid_json"                — signature valid but body wasn't JSON
WebhookSignatureErrorReason = str


class WebhookSignatureError(Exception):
    """Raised when an inbound delivery is not authentic.

    Respond 400 and do NOT act on the body.
    """

    def __init__(self, reason: WebhookSignatureErrorReason, message: str) -> None:
        super().__init__(message)
        self.reason = reason


@dataclass(frozen=True)
class MaytesWebhookEvent:
    """A verified webhook event (webhook spec §6).

    `data` is left as an open dict because its shape varies per `type` —
    branch on `type`, then read the fields that event documents. Ignore
    unrecognised fields: additive changes do NOT bump `api_version`.
    """

    #: Stable event id — identical across every retry. Deduplicate on this.
    id: str
    #: e.g. "checkout.authorized", "checkout.voided", "webhook.test".
    type: str
    #: Envelope schema version, e.g. "2026-06". Bumped only on breaking changes.
    api_version: str
    #: When the event occurred.
    created_at: str
    #: Per-event payload.
    data: Dict[str, Any] = field(default_factory=dict)


def verify_webhook_signature(
    raw_body: Union[bytes, bytearray, str],
    signature_header: Optional[str],
    signing_secret: str,
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
) -> MaytesWebhookEvent:
    """Verify an inbound Maytes webhook delivery and return the parsed event.

    Pass the **raw** request body — the exact bytes, before any JSON parsing.

        from flask import Flask, request
        from maytes_api_client import verify_webhook_signature, WebhookSignatureError

        @app.post("/webhooks/maytes")
        def maytes_webhook():
            try:
                event = verify_webhook_signature(
                    request.get_data(),                     # raw bytes
                    request.headers.get("X-Maytes-Signature"),
                    os.environ["MAYTES_WEBHOOK_SECRET"],
                )
            except WebhookSignatureError:
                return "", 400
            # ... handle event.type
            return "", 200

    `tolerance_seconds=0` skips the freshness check entirely — TEST ONLY, for
    replaying a stored delivery in a fixture. Never 0 in production: it makes
    any captured delivery replayable forever.

    :raises WebhookSignatureError: if the delivery is not authentic.
    """
    timestamp, signatures = _parse_signature_header(signature_header)

    if tolerance_seconds > 0:
        try:
            age_seconds = abs(time.time() - int(timestamp))
        except ValueError:
            raise WebhookSignatureError(
                "malformed_header",
                "X-Maytes-Signature carries a non-numeric t= value.",
            )
        if age_seconds > tolerance_seconds:
            raise WebhookSignatureError(
                "timestamp_out_of_tolerance",
                f"Webhook timestamp is outside the {tolerance_seconds}s tolerance "
                "— possible replay.",
            )

    # Bytes, not str: the HMAC covers what was on the wire, so a body that
    # isn't UTF-8-clean can't be mangled by a decode before hashing.
    body = raw_body.encode("utf-8") if isinstance(raw_body, str) else bytes(raw_body)
    signed_payload = timestamp.encode("utf-8") + b"." + body
    expected = hmac.new(
        signing_secret.encode("utf-8"), signed_payload, hashlib.sha256
    ).hexdigest()

    # ANY match wins — during a rotation grace window the current secret's
    # signature and the previous secret's signature are both present.
    if not any(hmac.compare_digest(expected, candidate) for candidate in signatures):
        raise WebhookSignatureError(
            "no_matching_signature",
            "No v1 signature matched the computed HMAC — wrong signing secret, "
            "or the body was modified in transit.",
        )

    return _parse_envelope(body)


def _parse_signature_header(header: Optional[str]) -> Tuple[str, List[str]]:
    if not header:
        raise WebhookSignatureError(
            "malformed_header", "Missing X-Maytes-Signature header."
        )

    timestamp: Optional[str] = None
    signatures: List[str] = []

    for part in header.split(","):
        trimmed = part.strip()
        if trimmed.startswith("t="):
            timestamp = trimmed[2:]
        elif trimmed.startswith("v1="):
            signatures.append(trimmed[3:])
        # Unknown schemes (a future v2=) are ignored, not fatal — forward
        # compatibility: we may add a scheme alongside v1 before removing v1.

    if not timestamp or not signatures:
        raise WebhookSignatureError(
            "malformed_header",
            "X-Maytes-Signature is malformed — expected `t=<unix>,v1=<hex>`.",
        )

    return timestamp, signatures


def _parse_envelope(body: bytes) -> MaytesWebhookEvent:
    try:
        parsed = json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        raise WebhookSignatureError(
            "invalid_json", "Signature verified but the body is not valid JSON."
        )

    return MaytesWebhookEvent(
        id=str(parsed.get("id", "")),
        type=str(parsed.get("type", "")),
        api_version=str(parsed.get("api_version", "")),
        created_at=str(parsed.get("created_at", "")),
        data=parsed.get("data") or {},
    )
