import subprocess

def run_declared_tests(repo_path, command):
    result=subprocess.run(command,cwd=repo_path,shell=True,capture_output=True,text=True)
    return {"ok":result.returncode==0,"returncode":result.returncode,"stdout":result.stdout,"stderr":result.stderr}
