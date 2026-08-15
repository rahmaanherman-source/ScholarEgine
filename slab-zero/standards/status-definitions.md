# Status Definitions

- ALPHA_VERIFIED: authoritative source establishes the recorded claim within explicit scope.
- ALPHA_SOURCE_AVAILABLE: authoritative evidence path exists but the claim has not yet been independently inspected enough for Alpha verification.
- SYSTEM_VERIFIED: the project Gatekeeper independently proved the claim.
- DUAL_VERIFIED: both Alpha authority and system verification cover the claim.
- VERIFIED: generic proven state used for project capabilities that do not require Alpha authority.
- CURRENT: the verified proof remains valid against its recorded dependency/state snapshot.
- STALE: historical proof remains intact but relevant state has drifted; re-verification is required.
- UNVERIFIED: insufficient proof.
- BLOCKED: verification cannot proceed because a declared prerequisite is unavailable.
- REJECTED: a submitted proof failed a required control.
