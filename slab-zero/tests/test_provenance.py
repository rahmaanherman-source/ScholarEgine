import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import gatekeeper


class ProvenanceTests(unittest.TestCase):
    def test_rejects_wrong_repository_identity(self):
        proof = {
            "artifact_sha256": "a" * 64,
            "commit_sha": "b" * 40,
            "repository": "attacker/fork",
            "workflow_ref": "attacker/fork/.github/workflows/slab-zero-provenance.yml@refs/heads/main",
            "oidc_issuer": "https://token.actions.githubusercontent.com",
            "certificate_identity": "https://github.com/attacker/fork/.github/workflows/slab-zero-provenance.yml@refs/heads/main",
            "rekor_log_index": "123"
        }
        ok, _ = gatekeeper.validate_provenance_identity(
            proof,
            expected_repository="rahmaanherman-source/ScholarEgine",
            expected_commit="b" * 40,
            expected_workflow_ref="rahmaanherman-source/ScholarEgine/.github/workflows/slab-zero-provenance.yml@refs/heads/main",
        )
        self.assertFalse(ok)

    def test_rejects_wrong_commit(self):
        proof = {
            "artifact_sha256": "a" * 64,
            "commit_sha": "c" * 40,
            "repository": "rahmaanherman-source/ScholarEgine",
            "workflow_ref": "rahmaanherman-source/ScholarEgine/.github/workflows/slab-zero-provenance.yml@refs/heads/main",
            "oidc_issuer": "https://token.actions.githubusercontent.com",
            "certificate_identity": "https://github.com/rahmaanherman-source/ScholarEgine/.github/workflows/slab-zero-provenance.yml@refs/heads/main",
            "rekor_log_index": "123"
        }
        ok, _ = gatekeeper.validate_provenance_identity(
            proof,
            expected_repository="rahmaanherman-source/ScholarEgine",
            expected_commit="b" * 40,
            expected_workflow_ref="rahmaanherman-source/ScholarEgine/.github/workflows/slab-zero-provenance.yml@refs/heads/main",
        )
        self.assertFalse(ok)

    def test_accepts_exact_identity_binding(self):
        commit = "b" * 40
        workflow = "rahmaanherman-source/ScholarEgine/.github/workflows/slab-zero-provenance.yml@refs/heads/main"
        proof = {
            "artifact_sha256": "a" * 64,
            "commit_sha": commit,
            "repository": "rahmaanherman-source/ScholarEgine",
            "workflow_ref": workflow,
            "oidc_issuer": "https://token.actions.githubusercontent.com",
            "certificate_identity": "https://github.com/" + workflow,
            "rekor_log_index": "123"
        }
        ok, reason = gatekeeper.validate_provenance_identity(
            proof,
            expected_repository="rahmaanherman-source/ScholarEgine",
            expected_commit=commit,
            expected_workflow_ref=workflow,
        )
        self.assertTrue(ok, reason)

    def test_rejects_replayed_proof(self):
        commit = "b" * 40
        workflow = "rahmaanherman-source/ScholarEgine/.github/workflows/slab-zero-provenance.yml@refs/heads/main"
        proof = {
            "artifact_sha256": "a" * 64,
            "commit_sha": commit,
            "repository": "rahmaanherman-source/ScholarEgine",
            "workflow_ref": workflow,
            "oidc_issuer": "https://token.actions.githubusercontent.com",
            "certificate_identity": "https://github.com/rahmaanherman-source/ScholarEgine/.github/workflows/slab-zero-provenance.yml@refs/heads/main",
            "rekor_log_index": "123",
            "run_id": "old-run"
        }
        ok, _ = gatekeeper.validate_provenance_identity(
            proof,
            expected_repository="rahmaanherman-source/ScholarEgine",
            expected_commit=commit,
            expected_workflow_ref=workflow,
            expected_run_id="new-run",
        )
        self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main()
