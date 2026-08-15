import subprocess


def detect_git_drift(last_verified_sha, repo_path="."):
    """Return (changed, detail) for repository state drift."""
    if not last_verified_sha:
        return True, "No verified commit SHA recorded"
    result = subprocess.run(
        ["git", "diff", "--quiet", last_verified_sha, "HEAD", "--", repo_path],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return True, f"Git state differs from {last_verified_sha}"
    return False, "Git state matches verified commit"
