def validate_provenance(proof, expected_repository, expected_commit, expected_workflow_ref, expected_run_id):
    required={"artifact_sha256","commit_sha","repository","workflow_ref","oidc_issuer","certificate_identity","rekor_log_index","run_id","signature_verified"}
    missing=required-set(proof)
    if missing: return False, f"missing:{sorted(missing)}"
    checks=[
      (proof["repository"]==expected_repository,"repository"),
      (proof["commit_sha"]==expected_commit,"commit_sha"),
      (proof["workflow_ref"]==expected_workflow_ref,"workflow_ref"),
      (proof["run_id"]==expected_run_id,"run_id"),
      (proof["oidc_issuer"]=="https://token.actions.githubusercontent.com","oidc_issuer"),
      (proof["certificate_identity"]==f"https://github.com/{expected_workflow_ref}","certificate_identity"),
      (bool(str(proof["rekor_log_index"]).strip()),"rekor_log_index"),
      (proof["signature_verified"] is True,"signature_verified")]
    for ok,name in checks:
        if not ok: return False, f"mismatch:{name}"
    return True, "provenance valid"
