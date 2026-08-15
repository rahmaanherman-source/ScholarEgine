import unittest
from gatekeeper.gatekeeper import append_verified_entry,derive_percentages
class StateTests(unittest.TestCase):
 def entry(self,id,w): return {"item_id":id,"claim":"claim","status":"SYSTEM_VERIFIED","temporal_state":"CURRENT","weight":w,"evidence":{"commit_sha":"a"*40,"evidence_hash":"b"*64,"evidence_locator":"https://e","test_result":"PASS"},"verification_hash":"c"*64,"last_verified_at":1}
 def test_weighted_percentage(self):
  m={"verified_items":[self.entry("A",10)],"history":[]}; roadmap={"items":[{"item_id":"A","weight":10},{"item_id":"B","weight":90}]}; derive_percentages(m,roadmap); self.assertEqual(m["completion_percentage"],10.0)
 def test_unauthorized_writer_rejected(self):
  m={"verified_items":[],"history":[]}; roadmap={"items":[{"item_id":"A","weight":10}]};
  with self.assertRaises(ValueError): append_verified_entry(m,self.entry("A",10),{"authorized_writer":"MANUAL","accepted":True},roadmap)
if __name__=="__main__": unittest.main()
