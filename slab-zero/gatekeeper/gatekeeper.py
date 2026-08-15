import hashlib, json
from dataclasses import dataclass
from pathlib import Path
from .lib.validation import validate_entry

@dataclass
class VerificationResult:
    accepted: bool
    reason: str
    entry: dict | None = None

def merkle_root(items):
    leaves=sorted(i["verification_hash"] for i in items if i.get("status") in {"VERIFIED","SYSTEM_VERIFIED","DUAL_VERIFIED","ALPHA_VERIFIED"} and i.get("temporal_state")=="CURRENT")
    if not leaves: return None
    while len(leaves)>1:
        if len(leaves)%2: leaves.append(leaves[-1])
        leaves=[hashlib.sha256((leaves[i]+leaves[i+1]).encode()).hexdigest() for i in range(0,len(leaves),2)]
    return leaves[0]

def derive_percentages(manifest, roadmap):
    weights={i["item_id"]:i["weight"] for i in roadmap["items"]}
    total=sum(weights.values())
    current=sum(weights.get(i["item_id"],0) for i in manifest.get("verified_items",[]) if i.get("temporal_state")=="CURRENT" and i.get("status") in {"VERIFIED","SYSTEM_VERIFIED","DUAL_VERIFIED","ALPHA_VERIFIED"})
    stale=sum(weights.get(i["item_id"],0) for i in manifest.get("verified_items",[]) if i.get("temporal_state")=="STALE")
    manifest["verified_percentage"]=round(current/total*100,2) if total else 0.0
    manifest["completion_percentage"]=manifest["verified_percentage"]
    manifest["stale_percentage"]=round(stale/total*100,2) if total else 0.0
    manifest["merkle_root"]=merkle_root(manifest.get("verified_items",[]))
    return manifest

def verify_item(item_id, repo_state, evidence_bundle):
    required={"claim","commit_sha","evidence_hash","evidence_locator","test_result","provenance","weight","verification_hash"}
    missing=required-set(evidence_bundle)
    if missing: return VerificationResult(False,f"missing:{sorted(missing)}")
    if evidence_bundle["commit_sha"]!=repo_state["commit_sha"]: return VerificationResult(False,"commit_sha_mismatch")
    if evidence_bundle["test_result"]!="PASS": return VerificationResult(False,"test_not_pass")
    if not evidence_bundle["evidence_locator"]: return VerificationResult(False,"missing_evidence_locator")
    if evidence_bundle["provenance"].get("signature_verified") is not True: return VerificationResult(False,"provenance_not_verified")
    entry={"item_id":item_id,"claim":evidence_bundle["claim"],"status":"SYSTEM_VERIFIED","temporal_state":"CURRENT","weight":evidence_bundle["weight"],"evidence":{k:evidence_bundle[k] for k in ("commit_sha","evidence_hash","evidence_locator","test_result")},"verification_hash":evidence_bundle["verification_hash"],"last_verified_at":evidence_bundle.get("timestamp")}
    errors=validate_entry(entry)
    if errors: return VerificationResult(False,";".join(errors))
    return VerificationResult(True,"accepted",entry)

def append_verified_entry(manifest, entry, seal, roadmap):
    if seal.get("authorized_writer")!="CI_PROVENANCE_GATE" or seal.get("accepted") is not True:
        raise ValueError("unauthorized state transition")
    if validate_entry(entry): raise ValueError("invalid entry")
    manifest.setdefault("history",[]).append({"event":"VERIFIED","item_id":entry["item_id"],"verification_hash":entry["verification_hash"],"timestamp":entry["last_verified_at"]})
    manifest.setdefault("verified_items",[]).append(entry)
    return derive_percentages(manifest,roadmap)
