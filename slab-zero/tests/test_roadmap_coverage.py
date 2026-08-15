import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RoadmapCoverageTests(unittest.TestCase):
    def test_all_roadmap_sections_have_explicit_verification_artifacts(self):
        roadmap = json.loads((ROOT / "roadmap.json").read_text())
        required = {
            "CONTRACT": ["tests/test_manifest.py", "schema.json", "policy.json"],
            "HASHING": ["tests/test_hashing.py"],
            "SIGNATURES": ["tests/test_signatures.py"],
            "EVIDENCE": ["tests/test_alpha_verification.py", "tests/test_provenance.py"],
            "PROBES": ["tests/test_probes.py"],
            "GATEKEEPER": ["tests/test_gatekeeper.py", "tests/test_state_machine.py"],
            "FRAUD": ["tests/test_fraudulent_green.py", "tests/test_provenance_gate.py"],
            "DRIFT": ["tests/test_drift.py", "drift-watch/drift_watch.py"],
            "CI": [".github/workflows/slab-zero-tests.yml", ".github/workflows/verify.yml"],
            "DOCS": ["../docs/architecture/SLAB-ZERO-ARCHITECTURE.md", "../identity/repository.json"],
            "BASELINE": ["audits/slab-zero-baseline.json", "../.github/workflows/slab-zero-provenance.yml"],
        }
        item_ids = [item["item_id"] for item in roadmap["items"]]
        self.assertEqual(set(item_ids), set(required))
        missing = []
        for item_id, paths in required.items():
            for rel in paths:
                path = ROOT / rel
                if not path.exists():
                    missing.append(f"{item_id}:{rel}")
        self.assertEqual(missing, [])

    def test_roadmap_dependencies_form_declared_order(self):
        roadmap = json.loads((ROOT / "roadmap.json").read_text())
        position = {item["item_id"]: i for i, item in enumerate(roadmap["items"])}
        violations = []
        for item in roadmap["items"]:
            for dependency in item["dependencies"]:
                if position[dependency] >= position[item["item_id"]]:
                    violations.append(f"{item['item_id']} depends on {dependency}")
        self.assertEqual(violations, [])

    def test_baseline_is_explicitly_not_certified(self):
        baseline = json.loads((ROOT / "audits/slab-zero-baseline.json").read_text())
        self.assertEqual(baseline["certification_status"], "NOT_CERTIFIED")
        self.assertEqual(baseline["verified_items"], 0)
        self.assertTrue(baseline["requires_ci_reproduction"])

if __name__ == "__main__":
    unittest.main()
