import unittest
from gatekeeper.gatekeeper import verify_item
class FraudTests(unittest.TestCase):
 def base(self): return {"claim":"x","commit_sha":"abc","evidence_hash":"h","evidence_locator":"https://e","test_result":"PASS","provenance":{"signature_verified":True},"weight":10,"verification_hash":"0"*64,"timestamp":1}
 def test_wrong_commit_rejected(self):
  e=self.base(); e["commit_sha"]="wrong"; self.assertFalse(verify_item("X",{"commit_sha":"abc"},e).accepted)
 def test_missing_provenance_rejected(self):
  e=self.base(); e["provenance"]={}; self.assertFalse(verify_item("X",{"commit_sha":"abc"},e).accepted)
 def test_ai_only_claim_without_provenance_rejected(self):
  e=self.base(); e["provenance"]={"signature_verified":False}; self.assertFalse(verify_item("X",{"commit_sha":"abc"},e).accepted)
if __name__=="__main__": unittest.main()
