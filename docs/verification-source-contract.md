# ScholarEgine — Verification Source Contract

ScholarEgine is the research/source-ingestion side of the shared Truth system.

## Source classes

- `primary`: official records, original research, standards, statutes, first-party documentation
- `reference`: encyclopedic/reference material such as Wikipedia
- `secondary`: reporting or analysis derived from primary material
- `anecdotal`: user/community reports requiring verification
- `unknown`: source type not established

## Wikipedia policy

Wikipedia may be retrieved and cited as a reference source. It is never promoted automatically to `primary` or treated as conclusive truth. Material claims should be corroborated with stronger evidence where available.

## Handoff to THE-BRAIN-V1

ScholarEgine supplies source records and evidence excerpts. THE-BRAIN-V1 determines verification status, contradiction state, provenance, and confidence metadata. Godspeed consumes the resulting gate decision.

## Required source metadata

Each source record should preserve:

- canonical URL or source identifier
- source class
- publisher/author when available
- publication or revision date when available
- retrieval timestamp
- evidence excerpt or structured evidence pointer
- notes about limitations

No secrets or private API credentials are committed to this repository.
