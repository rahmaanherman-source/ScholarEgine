import platform,sys

def check_runtime(environment_spec):
    expected=environment_spec.get("python_major")
    if expected is not None and sys.version_info.major!=expected: return {"ok":False,"reason":"python_major_mismatch"}
    expected_os=environment_spec.get("system")
    if expected_os and platform.system()!=expected_os: return {"ok":False,"reason":"system_mismatch"}
    return {"ok":True,"python":platform.python_version(),"system":platform.system()}
