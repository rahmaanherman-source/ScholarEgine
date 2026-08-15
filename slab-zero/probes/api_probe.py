"""External API drift probe scaffold.

The first Slab-Zero release does not claim API stability without a configured
endpoint and expected schema/version. Configure an item-specific API probe
before enabling `api` in policy.json; otherwise the gatekeeper fails closed.
"""


def detect_api_drift(endpoint, expected_fingerprint=None):
    if not endpoint or not expected_fingerprint:
        return True, "API probe is not configured with an endpoint and expected fingerprint"
    raise NotImplementedError("API probe execution is intentionally deferred until configured")
