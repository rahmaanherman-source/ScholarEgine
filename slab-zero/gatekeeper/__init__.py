from .gatekeeper import VerificationResult, verify_item, append_verified_entry, derive_percentages

def validate_provenance_identity(proof, expected_repository, expected_commit, expected_workflow_ref, expected_run_id=None):
    """Legacy identity-only compatibility check.

    This function is intentionally not the promotion gate. Promotion uses
    ``gatekeeper.provenance.validate_provenance`` and requires run identity plus
    cryptographic signature verification.
    """
    required = {"artifact_sha256", "commit_sha", "repository", "workflow_ref", "oidc_issuer", "certificate_identity", "rekor_log_index"}
    missing = required - set(proof)
    if missing:
        return False, f"Missing provenance fields: {sorted(missing)}"
    if proof["repository"] != expected_repository:
        return False, "Provenance repository identity mismatch"
    if proof["commit_sha"] != expected_commit:
        return False, "Provenance commit SHA mismatch"
    if proof["workflow_ref"] != expected_workflow_ref:
        return False, "Provenance workflow reference mismatch"
    if proof["certificate_identity"] != f"https://github.com/{expected_workflow_ref}":
        return False, "Provenance certificate identity mismatch"
    if proof["oidc_issuer"] != "https://token.actions.githubusercontent.com":
        return False, "Unexpected OIDC issuer"
    if not str(proof["rekor_log_index"]).strip():
        return False, "Missing transparency-log reference"
    if expected_run_id is not None and str(proof.get("run_id")) != str(expected_run_id):
        return False, "Provenance run identity mismatch (possible replay)"
    return True, "Provenance identity is exactly bound"
