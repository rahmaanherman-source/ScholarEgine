import hashlib
import hmac
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ROOT))

import gatekeeper


class GatekeeperTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "evidence").mkdir()
        (self.root / "proofs").mkdir()
        self.manifest_path = self.root / "manifest.json"
        self.schema_path = self.root / "schema.json"
        self.policy_path = self.root / "policy.json"
        self.manifest_path.write_text(json.dumps({
            "project_id": "TEST",
            "schema_version": "1.1",
            "verified_items": [],
            "merkle_root": None,
            "last_verified_at": None,
            "completion_percentage": 0.0,
            "audit": {"last_drift_check": None, "drift_detected": False}
        }))
        self.schema_path.write_text(Path(ROOT / "schema.json").read_text())
        self.policy_path.write_text(Path(ROOT / "policy.json").read_text())
        self.original_paths = gatekeeper.configure_paths(self.manifest_path, self.schema_path, self.policy_path)
        os.environ["SLAB_VERIFIER_KEY"] = "test-secret"

    def tearDown(self):
        gatekeeper.restore_paths(self.original_paths)
        os.environ.pop("SLAB_VERIFIER_KEY", None)
        self.tmp.cleanup()

    def make_evidence(self, commit_sha=None, source_link="https://example.invalid/source", locator="OFFICIAL-001", test_result="PASS"):
        commit_sha = commit_sha or gatekeeper.current_commit_sha()
        evidence = {
            "commit_sha": commit_sha,
            "source_link": source_link,
            "evidence_locator": locator,
            "test_result": test_result,
            "claim": "A test claim"
        }
        payload = gatekeeper.canonical_json(evidence).encode()
        evidence["signature"] = hmac.new(b"test-secret", payload, hashlib.sha256).hexdigest()
        path = self.root / "evidence" / "item.json"
        path.write_text(json.dumps(evidence, indent=2))
        return path

    def test_missing_evidence_is_rejected(self):
        self.assertFalse(gatekeeper.verify_item("AUTH-001", self.root / "missing.json", claim="A test claim"))
        manifest = gatekeeper.load_json(self.manifest_path)
        self.assertEqual(manifest["verified_items"], [])

    def test_tampered_signature_is_rejected(self):
        path = self.make_evidence()
        data = json.loads(path.read_text())
        data["claim"] = "tampered"
        path.write_text(json.dumps(data))
        self.assertFalse(gatekeeper.verify_item("AUTH-001", path, claim="A test claim"))
        self.assertEqual(gatekeeper.load_json(self.manifest_path)["verified_items"], [])

    def test_valid_evidence_is_verified(self):
        path = self.make_evidence()
        self.assertTrue(gatekeeper.verify_item("AUTH-001", path, claim="A test claim"))
        manifest = gatekeeper.load_json(self.manifest_path)
        self.assertEqual(manifest["verified_items"][0]["status"], "VERIFIED")
        self.assertEqual(manifest["completion_percentage"], 100.0)
        self.assertIsNotNone(manifest["merkle_root"])

    def test_wrong_commit_is_rejected(self):
        path = self.make_evidence(commit_sha="0" * 40)
        self.assertFalse(gatekeeper.verify_item("AUTH-001", path, claim="A test claim"))
        self.assertEqual(gatekeeper.load_json(self.manifest_path)["verified_items"], [])


if __name__ == "__main__":
    unittest.main()
