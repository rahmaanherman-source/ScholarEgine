import json
from pathlib import Path

def calculate_drift(item,current_state):
    expected=item.get("state_snapshot",{})
    changes={k:(expected.get(k),current_state.get(k)) for k in set(expected)|set(current_state) if expected.get(k)!=current_state.get(k)}
    return {"drift":bool(changes),"changes":changes}

def evaluate_temporal_state(item, drift_result):
    if drift_result.get("drift"): return "STALE"
    return "CURRENT"

def run(manifest_path, state_provider):
    manifest=json.loads(Path(manifest_path).read_text())
    details=[]
    for item in manifest.get("verified_items",[]):
        if item.get("temporal_state")!="CURRENT": continue
        result=calculate_drift(item,state_provider(item))
        if result["drift"]: item["temporal_state"]="STALE"; item["status"]="STALE"
        details.append({"item_id":item["item_id"],**result})
    manifest["audit"]={"last_drift_check":__import__('time').time_ns()//1_000_000_000,"drift_detected":any(d["drift"] for d in details),"details":details}
    Path(manifest_path).write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
    return manifest
