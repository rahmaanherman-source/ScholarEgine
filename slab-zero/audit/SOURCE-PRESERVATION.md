# Source-Preservation Rule

This audit layer preserves the work already established in the conversation/feed and in the repository. It does not replace working code, prompts, screenshots, evidence, tests, architecture, roadmap material, or historical records merely because they are incomplete.

## Source categories

- conversation/feed audit material
- screenshots and images
- source code and tests
- prompts and implementation instructions
- repository files, commits, workflows, and artifacts
- authoritative records and certificates
- evidence locators and retrieval paths
- prior verification results
- roadmap and dependency decisions

## Hard distinction

`AUDITED` means the item is identified and must be checked.

`VERIFIED` means the required evidence passed the Gatekeeper for the exact state being claimed.

An audit entry must never promote itself to VERIFIED.

## Gap-fill rule

1. Inventory existing material first.
2. Preserve existing material.
3. Identify missing, stale, conflicting, or blocked pieces.
4. Add only what is missing or required to correct a proven defect.
5. Verify every addition before promotion.
6. Preserve historical proof when current state changes.

## Partial progress

A project may have verified sections without being completely verified. Percentages are derived from verified roadmap state and are never accepted as proof merely because a human or AI entered them.

## Evidence rule

If a source artifact is not available to the current verifier, record it as missing or blocked. Never reconstruct unseen evidence from memory or assumption.
