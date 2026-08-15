import hashlib
from pathlib import Path

def check_dependencies(repo_path, recorded_hashes):
    for relative, expected in recorded_hashes.items():
        path=Path(repo_path)/relative
        if not path.exists(): return {"ok":False,"reason":"missing_lockfile","path":relative}
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        if actual!=expected: return {"ok":False,"reason":"dependency_drift","path":relative}
    return {"ok":True}
