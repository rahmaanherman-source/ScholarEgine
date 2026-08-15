import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ManifestTests(unittest.TestCase):
 def test_contract_files_exist(self):
  for name in ("manifest.json","schema.json","policy.json","roadmap.json"):
   self.assertTrue((ROOT/name).exists(),name)
 def test_status_enum_and_fail_closed_policy(self):
  schema=json.loads((ROOT/"schema.json").read_text()); policy=json.loads((ROOT/"policy.json").read_text())
  self.assertIn("STALE",schema["$defs"]["item"]["properties"]["status"]["enum"])
  self.assertTrue(policy["verification_rules"]["fail_closed"])
  self.assertFalse(policy["verification_rules"]["allow_ai_only_promotion"])
 def test_empty_ledger_is_zero(self):
  manifest=json.loads((ROOT/"manifest.json").read_text())
  self.assertEqual(manifest["verified_items"],[]); self.assertEqual(manifest["completion_percentage"],0.0); self.assertIsNone(manifest["merkle_root"])
if __name__=="__main__": unittest.main()
