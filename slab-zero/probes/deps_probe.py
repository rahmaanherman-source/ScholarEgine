import hashlib
from pathlib import Path


def hash_lockfile(lockfile_path):
    path = Path(lockfile_path)
    if not path.exists() or not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def detect_deps_drift(expected_hashes, repo_root="."):
    """Compare explicitly tracked lockfile hashes. Missing files fail closed."""
    for relative, expected in expected_hashes.items():
        current = hash_lockfile(Path(repo_root) / relative)
        if current is None:
            return True, f"Tracked lockfile missing: {relative}"
        if current != expected:
            return True, f"Lockfile changed: {relative}"
    return False, "Dependency lockfiles match recorded evidence"
