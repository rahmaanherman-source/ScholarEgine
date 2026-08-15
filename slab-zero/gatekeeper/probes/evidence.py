import hashlib
from pathlib import Path

def check_evidence_integrity(bundle):
    for artifact in bundle.get("artifacts",[]):
        path=Path(artifact["path"])
        if not path.exists(): return {"ok":False,"reason":"missing_artifact"}
        if hashlib.sha256(path.read_bytes()).hexdigest()!=artifact["sha256"]: return {"ok":False,"reason":"evidence_hash_mismatch"}
    return {"ok":True}
