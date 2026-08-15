import hashlib, json
from pathlib import Path

def build_evidence_bundle(item_id, artifacts):
    normalized=[]
    for artifact in artifacts:
        path=Path(artifact)
        normalized.append({"path":str(path),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    return {"item_id":item_id,"artifacts":normalized}

def verify_evidence_locator(locator):
    if not isinstance(locator,str) or not locator.strip(): return False
    return locator.startswith(("https://","http://","file://","github://","urn:")) or locator.startswith("OFFICIAL:")

def verify_evidence_integrity(bundle):
    for artifact in bundle.get("artifacts",[]):
        path=Path(artifact["path"])
        if not path.exists(): return False
        if hashlib.sha256(path.read_bytes()).hexdigest()!=artifact["sha256"]: return False
    return True

def verify_alpha_record(record):
    required={"authority","authoritative_scope","evidence_locator","record_id","retrieved_at"}
    missing=required-set(record)
    if missing: return False, f"missing:{sorted(missing)}"
    if not verify_evidence_locator(record["evidence_locator"]): return False, "invalid:evidence_locator"
    if not record["authoritative_scope"]: return False, "empty:authoritative_scope"
    return True, "ALPHA scope valid"
