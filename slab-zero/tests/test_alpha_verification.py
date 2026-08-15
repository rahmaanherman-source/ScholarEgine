import unittest
from gatekeeper.proof import verify_alpha_record, verify_evidence_locator
class AlphaTests(unittest.TestCase):
 def test_valid_alpha_record(self):
  ok,_=verify_alpha_record({"authority":"USPTO","authoritative_scope":"record establishes filing","evidence_locator":"https://example.com/record","record_id":"X","retrieved_at":"2026-08-15"}); self.assertTrue(ok)
 def test_missing_locator_rejected(self):
  ok,_=verify_alpha_record({"authority":"USPTO","authoritative_scope":"record","record_id":"X","retrieved_at":"2026-08-15"}); self.assertFalse(ok)
 def test_locator_validation(self): self.assertTrue(verify_evidence_locator("https://example.com/x")); self.assertFalse(verify_evidence_locator("not-a-locator"))
if __name__=="__main__": unittest.main()
