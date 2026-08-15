import hashlib
from pathlib import Path

def check_standard_state(policy_path, recorded_hash):
    actual=hashlib.sha256(Path(policy_path).read_bytes()).hexdigest()
    return {"ok":actual==recorded_hash,"current_hash":actual}
