import unittest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from gatekeeper.lib.signatures import sign_digest, verify_signature
class SignatureTests(unittest.TestCase):
 def test_valid_signature(self):
  key=Ed25519PrivateKey.generate(); raw=key.private_bytes(serialization.Encoding.Raw,serialization.PrivateFormat.Raw,serialization.NoEncryption()); pub=key.public_key().public_bytes(serialization.Encoding.Raw,serialization.PublicFormat.Raw); sig=sign_digest(raw,"abc"); self.assertTrue(verify_signature(pub,"abc",sig)); self.assertFalse(verify_signature(pub,"tampered",sig))
if __name__=="__main__": unittest.main()
