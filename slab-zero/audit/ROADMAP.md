# Slab-Zero Verification Flight Plan

> Proof → Pass → Seal → Next.

| Order | Section | Current audit state | Verification target |
|---:|---|---|---|
| 1 | CONTRACT | AUDITED | Revalidate schema, manifest, and policy against current main |
| 2 | HASHING | AUDITED | Reproduce canonicalization/hash tests |
| 3 | SIGNATURES | AUDITED | Reproduce signature verification and rejection tests |
| 4 | EVIDENCE | AUDITED | Verify evidence requirements and locators |
| 5 | PROBES | AUDITED | Reproduce Git/dependency/runtime/API/evidence probes |
| 6 | GATEKEEPER | AUDITED | Verify fail-closed state transitions |
| 7 | FRAUD | AUDITED | Execute fraudulent-green and replay rejection tests |
| 8 | DRIFT | AUDITED | Verify CURRENT/STALE behavior and scoped drift |
| 9 | CI | AUDITED | Verify clean-checkout automated enforcement and provenance |
| 10 | DOCS | AUDITED | Verify architecture and repository identity mapping |
| 11 | BASELINE | AUDITED | Verify baseline/provenance infrastructure |

## Project-memory rule

These infrastructure sections describe the verification system. They do not automatically certify APEX/ScholarEgine capabilities. Project claims enter a project Memory Slab only after their own evidence passes the Gatekeeper.

## Exact next target

**CONTRACT on the current `main` state.**

Before creating any VERIFIED project memory, merge the tested `slab-zero-complete-implementation` branch into `main` (or otherwise bring its exact tested state into the canonical branch), then run the Slab-Zero suite against that resulting commit. If the suite passes, promote only the infrastructure claims that the evidence actually covers; otherwise record the failure and stop promotion.
