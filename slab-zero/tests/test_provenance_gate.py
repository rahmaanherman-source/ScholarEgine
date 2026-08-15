import unittest
from gatekeeper.provenance import validate_provenance
class ProvenanceGateTests(unittest.TestCase):
 def p(self): return {"artifact_sha256":"a","commit_sha":"c","repository":"o/r","workflow_ref":"o/r/.github/workflows/v.yml@refs/heads/main","oidc_issuer":"https://token.actions.githubusercontent.com","certificate_identity":"https://github.com/o/r/.github/workflows/v.yml@refs/heads/main","rekor_log_index":"1","run_id":"7","signature_verified":True}
 def test_valid(self): self.assertTrue(validate_provenance(self.p(),"o/r","c","o/r/.github/workflows/v.yml@refs/heads/main","7")[0])
 def test_replay_rejected(self): self.assertFalse(validate_provenance(self.p(),"o/r","c","o/r/.github/workflows/v.yml@refs/heads/main","8")[0])
if __name__=="__main__": unittest.main()
