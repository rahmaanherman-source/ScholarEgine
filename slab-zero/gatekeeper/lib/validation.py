ALLOWED = {"ALPHA_VERIFIED","ALPHA_SOURCE_AVAILABLE","SYSTEM_VERIFIED","DUAL_VERIFIED","VERIFIED","STALE","UNVERIFIED","BLOCKED","REJECTED"}

def validate_entry(entry):
    errors=[]
    required={"item_id","claim","status","temporal_state","weight","evidence","verification_hash","last_verified_at"}
    errors.extend(f"missing:{k}" for k in sorted(required-set(entry)))
    if entry.get("status") not in ALLOWED: errors.append("invalid:status")
    if entry.get("temporal_state") not in {"CURRENT","STALE"}: errors.append("invalid:temporal_state")
    if not isinstance(entry.get("weight"),(int,float)) or entry.get("weight",0)<=0: errors.append("invalid:weight")
    evidence=entry.get("evidence",{})
    for key in ("commit_sha","evidence_hash","evidence_locator","test_result"):
        if not evidence.get(key): errors.append(f"missing:evidence.{key}")
    if evidence.get("test_result") != "PASS": errors.append("invalid:evidence.test_result")
    if entry.get("status") in {"VERIFIED","SYSTEM_VERIFIED","DUAL_VERIFIED","ALPHA_VERIFIED"} and entry.get("temporal_state") != "CURRENT": errors.append("verified_must_be_current")
    return errors
