import subprocess

def check_git_state(repo_path, expected_sha, paths=None):
    current=subprocess.run(["git","rev-parse","HEAD"],cwd=repo_path,capture_output=True,text=True)
    if current.returncode or current.stdout.strip()!=expected_sha: return {"ok":False,"reason":"commit_sha_mismatch","current":current.stdout.strip()}
    if paths:
        for path in paths:
            result=subprocess.run(["git","diff","--quiet",expected_sha,"HEAD","--",path],cwd=repo_path)
            if result.returncode: return {"ok":False,"reason":"path_drift","path":path}
    return {"ok":True}
