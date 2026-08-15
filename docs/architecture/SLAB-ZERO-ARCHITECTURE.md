# Slab-Zero Architecture

The Memory Slab is a project-specific, fail-closed proof ledger. Roadmap items are independently verifiable and weighted. The Gatekeeper admits only complete evidence bundles with authorized provenance. Drift Watch changes only affected CURRENT records to STALE and preserves historical proof.

## State model

`UNVERIFIED -> VERIFIED/CURRENT -> STALE -> re-verification -> VERIFIED/CURRENT`

Authority-derived states (`ALPHA_VERIFIED`, `ALPHA_SOURCE_AVAILABLE`) record exactly what an external authority established. Claims outside that scope require system verification. `DUAL_VERIFIED` means both layers cover the claim.

## Percentage model

`verified_percentage = sum(weight of CURRENT verified items) / sum(all roadmap weights) * 100`.

`operational_percentage` is a separate derived measure and may never be inferred solely from verification. Dependencies determine whether a verified capability is deployable.

## Evidence chain

Claim -> authority/scope -> evidence locator -> artifact digest -> exact repository state -> verifier identity -> provenance -> Gatekeeper -> Memory Slab.
