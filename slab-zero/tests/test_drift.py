import unittest
from drift_watch.drift_watch import calculate_drift,evaluate_temporal_state
class DriftTests(unittest.TestCase):
 def test_no_drift_current(self):
  r=calculate_drift({"state_snapshot":{"sha":"a"}},{"sha":"a"}); self.assertFalse(r["drift"]); self.assertEqual(evaluate_temporal_state({},r),"CURRENT")
 def test_code_drift_stale(self):
  r=calculate_drift({"state_snapshot":{"sha":"a"}},{"sha":"b"}); self.assertTrue(r["drift"]); self.assertEqual(evaluate_temporal_state({},r),"STALE")
if __name__=="__main__": unittest.main()
