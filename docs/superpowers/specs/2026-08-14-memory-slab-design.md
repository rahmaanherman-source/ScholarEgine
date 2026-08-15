# Memory Slab / Slab-Zero Design

## Purpose

ScholarEgine is the historical origin repository for the Godspeed work and becomes Slab-Zero: the reference implementation of a fail-closed, evidence-backed Memory Slab.

The Memory Slab is not a general notes file. It is a machine-readable ledger of verified project state. Every project repository will eventually have its own Memory Slab.

## Core Law

Nothing enters Verified Memory unless the required evidence passes the verification gate.

A project does not need to be 100% complete to have verified memory. Completion is calculated from verified roadmap items. Unverified, working, and archival material may exist in the repository but is not represented as verified state.

Historical proof is preserved. If the underlying state changes, the historical verification remains intact but the current status becomes STALE until re-verification succeeds.

## Verification Classes

### ALPHA_VERIFIED
An authoritative external institution has established the exact claim within an identifiable scope. The record must identify the authority, the exact claim covered, the authority scope, the official record, and an evidence locator.

### ALPHA_SOURCE_AVAILABLE
An authoritative source exists and is addressable, but the system has not yet confirmed that the source establishes the exact claim.

### SYSTEM_VERIFIED
The local Gatekeeper independently reproduced the required evidence against the exact repository/runtime state.

### DUAL_VERIFIED
The claim is covered by authoritative verification and the applicable portion has also passed system verification.

### STALE
A previously verified claim is retained historically but current code, dependencies, external APIs, environment, standards, or evidence have drifted.

### UNVERIFIED / REJECTED
The claim has not passed the required gate or the evidence is insufficient/inconsistent.

## Alpha Evidence Chain

Every ALPHA_VERIFIED entry requires:

- authority
- exact_claim
- authority_scope
- official_record
- evidence_locator
- record_identifier
- retrieval_timestamp
- evidence_hash
- authority_status
- what_was_established
- what_was_not_established
- remaining_verification

The system follows the authoritative evidence path when practical. It does not duplicate authoritative work unnecessarily, but it independently verifies anything outside the authority's established scope.

## Cryptographic Binding

A verification record is bound to the state it proves. The verification hash is derived from the roadmap item ID, exact commit SHA, evidence hash, timestamp, and verifier signature. A changed code state, evidence bundle, or required verification context invalidates the current verification relationship and causes re-verification to be required.

The Memory Slab is treated as a signed state ledger rather than a manually editable completion list. The Gatekeeper is the only process authorized to create a VERIFIED state transition.

## Evidence Requirements

Evidence may include source files, tests, build output, runtime results, screenshots/images, videos, official records, certificates, API responses, or other addressable artifacts. Evidence must be referenced by a stable locator and cryptographically hashed where applicable.

A description is not proof. The evidence path is part of the proof.

## Drift Watch

The Drift Watch checks the dependencies of verified items. Initial probe classes are:

- Git/code state
- dependency lockfiles
- tests/build/runtime
- external API/schema state
- standards/policy definitions
- evidence integrity

No drift keeps a verified item CURRENT. Relevant drift changes the temporal state to STALE while preserving historical proof.

## Project Memory Slabs

Every repository receives its own slab. A project slab contains verified state for that project only, while preserving links to source material, evidence, history, and related repositories. Repository renames are handled through a canonical identity and alias/history map rather than destructive rewriting of historical records.

## Completion

Completion percentages are derived from roadmap state and verification status. They are never trusted as manually entered truth. A project can therefore report verified progress without implying that the entire project is complete.

## Fail-Closed Requirements

- Missing proof rejects verification.
- Missing evidence locator rejects ALPHA_VERIFIED.
- Commit/evidence mismatch rejects verification.
- Reproduction mismatch rejects verification.
- Invalid signature rejects verification.
- Manual edits cannot create VERIFIED state.
- Drift cannot silently preserve CURRENT status.
- Historical records are never silently rewritten.

## Initial Repository Boundary

ScholarEgine currently contains the original README and initial commit. That history is preserved as provenance. Slab-Zero is added without rewriting the original historical commit.
