# Memory Slab / Slab-Zero Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Build ScholarEgine into Slab-Zero, a fail-closed verification ledger that admits only proven state into Verified Memory, records Alpha authoritative evidence paths, cryptographically binds proofs to repository state, and detects drift.

**Architecture:** A JSON schema and manifest define the ledger; a Gatekeeper performs deterministic verification and signs accepted state transitions; a probe library checks code, dependencies, tests/runtime, external sources, standards, and evidence; Drift Watch changes CURRENT verified records to STALE when relevant state changes. Source material and raw evidence remain separate from the verified ledger.

**Tech Stack:** Python 3, POSIX shell, Git, JSON, SHA-256, Ed25519-compatible signing interface, pytest, GitHub Actions.

## Global Constraints

- Fail closed: missing, inconsistent, or unreproducible proof cannot produce VERIFIED state.
- `evidence_locator` is mandatory for every `ALPHA_VERIFIED` record.
- Completion percentage is derived from roadmap verification state; it is never authoritative input.
- Historical verification is preserved when current state becomes STALE.
- Manual edits cannot create VERIFIED state.
- Authoritative verification is scoped to exactly what the authority established; uncovered claims require system verification.
- Original ScholarEgine history must not be rewritten.

---

### Task 1: Create the repository contract and schemas

**Files:**
- Create: `slab/schema.json`
- Create: `slab/policy.json`
- Create: `roadmap/schema.json`
- Create: `standards/verification-law.md`
- Create: `standards/evidence-requirements.md`
- Create: `standards/status-definitions.md`
- Create: `standards/drift-policy.md`

**Interfaces:**
- Produces the authoritative field names and validation rules consumed by the manifest, Gatekeeper, and tests.

- [ ] Step 1: Write schema tests covering required fields, enum states, Alpha evidence requirements, and rejection of unknown verification states.
- [ ] Step 2: Run `pytest tests/test_manifest.py -v` and confirm the tests fail because schemas do not exist.
- [ ] Step 3: Write the JSON schemas and policy documents using the approved design.
- [ ] Step 4: Run `pytest tests/test_manifest.py -v` and confirm schema validation passes for valid fixtures and rejects invalid fixtures.
- [ ] Step 5: Commit with `git add slab roadmaps standards tests/test_manifest.py && git commit -m "feat: define memory slab verification contract"`.

### Task 2: Build the manifest and canonical hashing library

**Files:**
- Create: `slab/manifest.json`
- Create: `gatekeeper/__init__.py`
- Create: `gatekeeper/lib/__init__.py`
- Create: `gatekeeper/lib/canonicalize.py`
- Create: `gatekeeper/lib/hashing.py`
- Create: `tests/test_hashing.py`

**Interfaces:**
- `canonicalize(value) -> bytes`
- `sha256_bytes(data: bytes) -> str`
- `verification_hash(item_id: str, commit_sha: str, evidence_hash: str, timestamp: str, verifier_signature: str) -> str`

- [ ] Step 1: Write failing tests for deterministic canonical JSON and stable SHA-256/verification hashes.
- [ ] Step 2: Run `pytest tests/test_hashing.py -v` and confirm failure.
- [ ] Step 3: Implement canonicalization and hashing without network dependencies.
- [ ] Step 4: Run the focused tests and confirm PASS.
- [ ] Step 5: Commit the manifest skeleton and hashing implementation.

### Task 3: Build signature and validation primitives

**Files:**
- Create: `gatekeeper/lib/signatures.py`
- Create: `gatekeeper/lib/validation.py`
- Create: `tests/test_signatures.py`

**Interfaces:**
- `sign_digest(private_key, digest: str) -> str`
- `verify_signature(public_key, digest: str, signature: str) -> bool`
- `validate_entry(entry: dict) -> list[str]`

- [ ] Step 1: Write tests proving valid signatures verify and altered digests/signatures fail.
- [ ] Step 2: Run focused tests and confirm failure.
- [ ] Step 3: Implement the signature adapter and strict entry validation.
- [ ] Step 4: Run focused tests and confirm PASS.
- [ ] Step 5: Commit cryptographic primitives.

### Task 4: Build evidence bundles and Alpha verification

**Files:**
- Create: `gatekeeper/proof.py`
- Create: `gatekeeper/provenance.py`
- Create: `tests/test_alpha_verification.py`
- Create: `slab/proofs/.gitkeep`
- Create: `slab/evidence/.gitkeep`

**Interfaces:**
- `build_evidence_bundle(item_id, artifacts) -> dict`
- `verify_alpha_record(record) -> VerificationResult`
- `verify_evidence_locator(locator) -> LocatorResult`

- [ ] Step 1: Write tests for a valid Alpha record, missing `evidence_locator`, out-of-scope authority claims, and changed evidence.
- [ ] Step 2: Run focused tests and confirm failure.
- [ ] Step 3: Implement evidence hashing, locator validation, and Alpha scope checks.
- [ ] Step 4: Run focused tests and confirm PASS.
- [ ] Step 5: Commit Alpha evidence-chain support.

### Task 5: Build Git and test/runtime probes

**Files:**
- Create: `gatekeeper/probes/__init__.py`
- Create: `gatekeeper/probes/git.py`
- Create: `gatekeeper/probes/dependencies.py`
- Create: `gatekeeper/probes/tests.py`
- Create: `gatekeeper/probes/runtime.py`
- Create: `gatekeeper/probes/evidence.py`
- Create: `tests/test_probes.py`

**Interfaces:**
- `check_git_state(repo_path, expected_sha, paths) -> ProbeResult`
- `check_dependencies(repo_path, recorded_hashes) -> ProbeResult`
- `run_declared_tests(repo_path, command) -> TestResult`
- `check_runtime(environment_spec) -> ProbeResult`
- `check_evidence_integrity(bundle) -> ProbeResult`

- [ ] Step 1: Write failing tests for matching and mismatching Git SHA, dependency hash, test result, runtime specification, and evidence hash.
- [ ] Step 2: Run focused tests and confirm failure.
- [ ] Step 3: Implement deterministic probes with explicit nonzero failure results.
- [ ] Step 4: Run focused tests and confirm PASS.
- [ ] Step 5: Commit probe library.

### Task 6: Build the Gatekeeper state machine

**Files:**
- Create: `gatekeeper/gatekeeper.py`
- Create: `gatekeeper/gatekeeper.sh`
- Create: `tests/test_gatekeeper.py`

**Interfaces:**
- `verify_item(item_id, repo_state, evidence_bundle) -> VerificationResult`
- `append_verified_entry(manifest, entry, seal) -> dict`
- CLI: `./gatekeeper/gatekeeper.sh verify <item-id>`

- [ ] Step 1: Write failing tests for successful verification and each fail-closed condition: missing proof, SHA mismatch, test mismatch, signature failure, and invalid Alpha scope.
- [ ] Step 2: Run focused tests and confirm failure.
- [ ] Step 3: Implement the state machine so only a complete proof bundle can produce VERIFIED/CURRENT.
- [ ] Step 4: Run focused tests and confirm PASS.
- [ ] Step 5: Commit Gatekeeper implementation.

### Task 7: Prove the system rejects fraudulent green claims

**Files:**
- Create: `tests/test_fraudulent_green.py`
- Create: `tests/fixtures/fraudulent_manifest.json`
- Create: `tests/fixtures/fraudulent_evidence.json`

- [ ] Step 1: Write attack fixtures for manual 100% claims, fake SHA, altered evidence, forged signature, stale dependency state, and mismatched runtime.
- [ ] Step 2: Run the attack suite and confirm the current implementation rejects every case.
- [ ] Step 3: Add any missing fail-closed checks exposed by the tests.
- [ ] Step 4: Run `pytest tests/test_fraudulent_green.py -v` and require all attack cases to PASS as rejection tests.
- [ ] Step 5: Commit the fraud-resistance suite.

### Task 8: Build Drift Watch

**Files:**
- Create: `drift-watch/drift_watch.py`
- Create: `drift-watch/config.json`
- Create: `gatekeeper/probes/api.py`
- Create: `gatekeeper/probes/standards.py`
- Create: `tests/test_drift.py`

**Interfaces:**
- `calculate_drift(item, current_state) -> DriftResult`
- `evaluate_temporal_state(item, drift_result) -> str`
- `check_api_state(locator, recorded_state) -> ProbeResult`
- `check_standard_state(policy, recorded_hash) -> ProbeResult`

- [ ] Step 1: Write failing tests for no drift, code drift, dependency drift, API drift, standards drift, and evidence drift.
- [ ] Step 2: Run focused tests and confirm failure.
- [ ] Step 3: Implement drift probes and the VERIFIED/CURRENT to STALE transition without deleting history.
- [ ] Step 4: Run focused tests and confirm PASS.
- [ ] Step 5: Commit Drift Watch.

### Task 9: Add CI enforcement and daily audit workflow

**Files:**
- Create: `.github/workflows/verify.yml`
- Create: `.github/workflows/drift-watch.yml`
- Create: `slab/audits/.gitkeep`
- Create: `slab/history/.gitkeep`

- [ ] Step 1: Add CI tests that run the complete verification and fraud-resistance suite on every relevant change.
- [ ] Step 2: Add a scheduled Drift Watch workflow that records an audit result and fails closed on verification errors.
- [ ] Step 3: Test workflow YAML syntax and local command paths.
- [ ] Step 4: Run the full local test suite.
- [ ] Step 5: Commit CI enforcement.

### Task 10: Add repository documentation and identity mapping

**Files:**
- Modify: `README.md`
- Create: `slab/README.md`
- Create: `docs/architecture/SLAB-ZERO-ARCHITECTURE.md`
- Create: `identity/repository.json`

- [ ] Step 1: Document where an AI should go first, how to read the Slab, how to follow evidence locators, and how statuses are interpreted.
- [ ] Step 2: Document repository identity history so future renames preserve historical references without destructive rewriting.
- [ ] Step 3: Run documentation path/link checks.
- [ ] Step 4: Commit documentation and identity map.

### Task 11: Full verification and release baseline

**Files:**
- Modify: `slab/manifest.json`
- Create: `slab/audits/slab-zero-baseline.json`

- [ ] Step 1: Run the entire test suite with `pytest -q`.
- [ ] Step 2: Run the Gatekeeper against the repository's own baseline verification items.
- [ ] Step 3: Run the fraudulent-green suite again after all integrations are enabled.
- [ ] Step 4: Verify the generated manifest, evidence hashes, signatures, and audit record against the final commit SHA.
- [ ] Step 5: Record only the verified baseline facts in the Slab and commit the baseline.
