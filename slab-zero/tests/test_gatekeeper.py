import unittest
from gatekeeper.gatekeeper import append_verified_entry, derive_percentages, verify_item

class GatekeeperTests(unittest.TestCase):
    def entry(self, item_id="AUTH-001", weight=10):
        return {
            "item_id": item_id,
            "claim": "A test claim",
            "status": "SYSTEM_VERIFIED",
            "temporal_state": "CURRENT",
            "weight": weight,
            "evidence": {
                "commit_sha": "a" * 40,
                "evidence_hash": "b" * 64,
                "evidence_locator": "https://example.invalid/evidence",
                "test_result": "PASS"
            },
            "verification_hash": "c" * 64,
            "last_verified_at": 1
        }

    def test_valid_complete_candidate_is_accepted(self):
        evidence = {
            "claim": "A test claim",
            "commit_sha": "a" * 40,
            "evidence_hash": "b" * 64,
            "evidence_locator": "https://example.invalid/evidence",
            "test_result": "PASS",
            "provenance": {"signature_verified": True},
            "weight": 10,
            "verification_hash": "c" * 64,
            "timestamp": 1
        }
        result = verify_item("AUTH-001", {"commit_sha": "a" * 40}, evidence)
        self.assertTrue(result.accepted)
        self.assertEqual(result.entry["temporal_state"], "CURRENT")

    def test_missing_proof_rejected(self):
        evidence = self.entry()
        result = verify_item("AUTH-001", {"commit_sha": "a" * 40}, evidence)
        self.assertFalse(result.accepted)

    def test_wrong_sha_rejected(self):
        evidence = {
            "claim": "A test claim", "commit_sha": "0" * 40,
            "evidence_hash": "b" * 64, "evidence_locator": "https://example.invalid/evidence",
            "test_result": "PASS", "provenance": {"signature_verified": True},
            "weight": 10, "verification_hash": "c" * 64, "timestamp": 1
        }
        self.assertFalse(verify_item("AUTH-001", {"commit_sha": "a" * 40}, evidence).accepted)

    def test_weighted_completion_is_derived(self):
        manifest = {"verified_items": [self.entry(weight=10)], "history": []}
        roadmap = {"items": [{"item_id": "AUTH-001", "weight": 10}, {"item_id": "OTHER", "weight": 90}]}
        derive_percentages(manifest, roadmap)
        self.assertEqual(manifest["completion_percentage"], 10.0)

    def test_unauthorized_writer_rejected(self):
        manifest = {"verified_items": [], "history": []}
        roadmap = {"items": [{"item_id": "AUTH-001", "weight": 10}]}
        with self.assertRaises(ValueError):
            append_verified_entry(manifest, self.entry(), {"authorized_writer": "MANUAL", "accepted": True}, roadmap)

if __name__ == "__main__":
    unittest.main()
