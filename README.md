# ScholarEgine

**GODSPEED Scholar / Research Engine**

ScholarEgine is the research and source-ingestion surface for the shared APEX Truth / Scholar / GODSPEED architecture.

## Evidence-first role

ScholarEgine discovers and organizes candidate evidence. It does **not** declare a claim true merely because it found the claim.

```text
Approved sources
      ↓
ScholarEgine
research + source ingestion
      ↓
THE-BRAIN
knowledge + provenance + contradiction + confidence
      ↓
GODSPEED Truth Gate
fail-closed output authorization
```

## Wikipedia

Wikipedia is supported as a **secondary/reference source** for discovery, terminology, chronology, and locating underlying citations.

It is **not automatic truth**.

For Wikipedia-derived claims, preserve the article URL, retrieval metadata, revision information when available, cited references, and the resulting verification state. Prefer primary or official confirmation when appropriate.

Reference: https://www.wikipedia.org/

## Truth states

ScholarEgine may pass candidate material downstream with states such as:

- `OBSERVED`
- `REFERENCE_CHECKED`
- `INDEPENDENTLY_VERIFIED`
- `UNVERIFIED`

THE-BRAIN owns the knowledge/verification decision; GODSPEED owns final output gating.

## Canonical contracts

The shared contracts live in:

- APEX 365: `docs/architecture/APEX_TRUTH_SCHOLAR_GODSPEED.md`
- APEX 365: `docs/truth/WIKIPEDIA_SOURCE_POLICY.md`
- APEX 365: `schemas/source.schema.json`
- APEX 365: `schemas/claim.schema.json`

## Non-negotiable rule

**A model-generated answer is not evidence simply because a model generated it.**
