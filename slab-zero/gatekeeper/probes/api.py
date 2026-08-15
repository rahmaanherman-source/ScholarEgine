import urllib.request

def check_api_state(locator, recorded_state):
    try:
        req=urllib.request.Request(locator,method="HEAD")
        with urllib.request.urlopen(req,timeout=10) as response:
            state={"status":response.status,"etag":response.headers.get("ETag"),"last_modified":response.headers.get("Last-Modified")}
        return {"ok":state==recorded_state,"state":state}
    except Exception as exc:
        return {"ok":False,"reason":f"api_probe_error:{exc}"}
