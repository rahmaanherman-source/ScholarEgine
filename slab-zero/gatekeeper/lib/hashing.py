import hashlib
from .canonicalize import canonicalize

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def verification_hash(item_id, commit_sha, evidence_hash, timestamp, verifier_signature):
    return sha256_bytes(canonicalize({"item_id":item_id,"commit_sha":commit_sha,"evidence_hash":evidence_hash,"timestamp":timestamp,"verifier_signature":verifier_signature}))
