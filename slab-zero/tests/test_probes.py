import tempfile, unittest
from pathlib import Path
from gatekeeper.probes.runtime import check_runtime
from gatekeeper.probes.dependencies import check_dependencies
class ProbeTests(unittest.TestCase):
 def test_runtime(self): self.assertTrue(check_runtime({"python_major":3})["ok"])
 def test_dependency_hash_match(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"lock"; p.write_text("x"); import hashlib; h=hashlib.sha256(b"x").hexdigest(); self.assertTrue(check_dependencies(d,{"lock":h})["ok"])
 def test_dependency_hash_mismatch(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"lock"; p.write_text("x"); self.assertFalse(check_dependencies(d,{"lock":"0"*64})["ok"])
if __name__=="__main__": unittest.main()
