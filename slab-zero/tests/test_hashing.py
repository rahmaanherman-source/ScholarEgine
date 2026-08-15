import unittest
from gatekeeper.lib.canonicalize import canonicalize
from gatekeeper.lib.hashing import sha256_bytes, verification_hash
class HashTests(unittest.TestCase):
 def test_canonicalization_is_deterministic(self):
  self.assertEqual(canonicalize({"b":2,"a":1}),canonicalize({"a":1,"b":2}))
 def test_sha_is_stable(self): self.assertEqual(sha256_bytes(b"x"),sha256_bytes(b"x"))
 def test_verification_hash_changes_when_commit_changes(self):
  a=verification_hash("A","1","2","3","4"); b=verification_hash("A","9","2","3","4"); self.assertNotEqual(a,b)
if __name__=="__main__": unittest.main()
