#!/usr/bin/env python3
"""APEX Slab-Zero Gatekeeper.

Fail-closed verification ledger for project-specific Memory Slabs.

The provenance layer is intentionally separate from promotion: a signed CI
proof is necessary evidence, but the Gatekeeper must still validate claim
scope, commit binding, policy binding, and test evidence before VERIFIED.
"""

import argparse
import hashlib
import hmac
import json
import os
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = REPO_ROOT / "manifest.json"
SCHEMA_PATH = REPO_ROOT / "schema.json"
POLICY_PATH = REPO_ROOT / "policy.json"


def configure_paths(manifest, schema, policy):
    global MANIFEST_PATH, SCHEMA_PATH, POLICY_PATH
    old = (MANIFEST_PATH, SCHEMA_PATH, POLICY_PATH)
    MANIFEST_PATH, SCHEMA_PATH, POLICY_PATH = Path(manifest), Path(schema), Path(policy)
    return old


def restore_paths(old):
    global MANIFEST_PATH, SCHEMA_PATH, POLICY_PATH
    MANIFEST_PATH, SCHEMA_PATH, POLICY_PATH = old


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    tmp = Path(str(path) + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def current_commit_sha():
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=REPO_ROOT
    )
    if result.returncode != 0:
        raise RuntimeError("Unable to determine current Git commit SHA")
    return result.stdout.strip()


def calculate_evidence_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def calculate_verification_hash(item_id, commit_sha, evidence_hash, timestamp, verifier_id):
    payload = f"{item_id}:{commit_sha}:{evidence_hash}:{timestamp}:{verifier_id}".encode()
    return hashlib.sha256(payload).hexdigest()


def calculate_merkle_root(items):
    leaves = sorted(i["verification_hash"] for i in items if i.get("status") == "VERIFIED")
    if not leaves:
        return None
    level = leaves[:]
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [
            hashlib.sha256((level[i] + level[i + 1]).encode()).hexdigest()
            for i in range(0, len(level), 2)
        ]
    return level[0]


def _secret():
    secret = os.environ.get("SLAB_VERIFIER_KEY")
    if not secret:
        raise RuntimeError("SLAB_VERIFIER_KEY is required; refusing to verify")
    return secret.encode()


def validate_provenance_identity(
    proof,
    expected_repository,
    expected_commit,
    expected_workflow_ref,
    expected_run_id=None,
):
    """Validate the identity bindings carried by a CI provenance proof.

    This is deliberately deterministic and fail-closed. Cryptographic
    signature verification is performed by the CI signing/verifying tool;
    this function validates that the verified identity refers to the exact
    repository, workflow, commit, issuer, and (when supplied) run.
    """
    required = {
        "artifact_sha256",
        "commit_sha",
        "repository",
        "workflow_ref",
        "oidc_issuer",
        "certificate_identity",
        "rekor_log_index",
    }
    missing = required - set(proof)
    if missing:
        return False, f"Missing provenance fields: {sorted(missing)}"
    if proof["repository"] != expected_repository:
        return False, "Provenance repository identity mismatch"
    if proof["commit_sha"] != expected_commit:
        return False, "Provenance commit SHA mismatch"
    if proof["workflow_ref"] != expected_workflow_ref:
        return False, "Provenance workflow reference mismatch"
    expected_identity = f"https://github.com/{expected_workflow_ref}"
    if proof["certificate_identity"] != expected_identity:
        return False, "Provenance certificate identity mismatch"
    if proof["oidc_issuer"] != "https://token.actions.githubusercontent.com":
        return False, "Unexpected OIDC issuer"
    if not str(proof["rekor_log_index"]).strip():
        return False, "Missing transparency-log reference"
    if expected_run_id is not None and str(proof.get("run_id")) != str(expected_run_id):
        return False, "Provenance run identity mismatch (possible replay)"
    return True, "Provenance identity is exactly bound"


def verify_evidence_bundle(path, expected_commit, expected_claim=None):
    try:
        evidence = load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        return False, f"Invalid evidence bundle: {exc}"

    required = {"commit_sha", "source_link", "evidence_locator", "test_result", "claim", "signature"}
    missing = required - set(evidence)
    if missing:
        return False, f"Missing evidence fields: {sorted(missing)}"
    if evidence["commit_sha"] != expected_commit:
        return False, "Evidence commit SHA does not match current repository state"
    if evidence["test_result"] != "PASS":
        return False, "Evidence test_result is not PASS"
    if not evidence["source_link"] or not evidence["evidence_locator"]:
        return False, "Evidence locator/source link is empty"
    if expected_claim is not None and evidence["claim"] != expected_claim:
        return False, "Evidence claim does not match requested claim"

    supplied_signature = evidence["signature"]
    unsigned = {k: v for k, v in evidence.items() if k != "signature"}
    expected_signature = hmac.new(_secret(), canonical_json(unsigned).encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(supplied_signature, expected_signature):
        return False, "Evidence signature/MAC is invalid"
    return True, evidence


def update_completion(manifest):
    items = manifest.get("verified_items", [])
    verified = sum(1 for i in items if i.get("status") == "VERIFIED")
    manifest["completion_percentage"] = round((verified / len(items)) * 100, 2) if items else 0.0
    manifest["merkle_root"] = calculate_merkle_root(items)
    return manifest


def verify_item(item_id, evidence_path=None, claim=None, verifier_id="local-dev"):
    manifest = load_json(MANIFEST_PATH)
    policy = load_json(POLICY_PATH)
    if not policy["verification_rules"].get("fail_closed", True):
        raise RuntimeError("Policy must be fail-closed")
    if policy["verification_rules"].get("allow_ai_only_promotion", False):
        raise RuntimeError("AI-only promotion is forbidden by Slab-Zero law")
    if not evidence_path:
        print("[FAIL] No evidence supplied; rejecting.")
        return False
    path = Path(evidence_path)
    if not path.exists() or not path.is_file():
        print(f"[FAIL] Evidence file {path} not found; rejecting.")
        return False

    try:
        commit_sha = current_commit_sha()
        ok, evidence_or_error = verify_evidence_bundle(path, commit_sha, claim)
    except RuntimeError as exc:
        print(f"[FAIL] {exc}")
        return False
    if not ok:
        print(f"[FAIL] {evidence_or_error}")
        return False

    evidence = evidence_or_error
    timestamp = int(time.time())
    evidence_hash = calculate_evidence_hash(path)
    verification_hash = calculate_verification_hash(item_id, commit_sha, evidence_hash, timestamp, verifier_id)
    item = next((i for i in manifest["verified_items"] if i["item_id"] == item_id), None)
    if item is None:
        item = {"item_id": item_id}
        manifest["verified_items"].append(item)

    item.update({
        "claim": evidence["claim"],
        "status": "VERIFIED",
        "evidence": {
            "commit_sha": commit_sha,
            "evidence_hash": evidence_hash,
            "source_link": evidence["source_link"],
            "evidence_locator": evidence["evidence_locator"],
            "test_result": evidence["test_result"],
            "verifier_id": verifier_id,
        },
        "verification_hash": verification_hash,
        "last_verified_at": timestamp,
    })
    manifest["last_verified_at"] = timestamp
    manifest["audit"] = {
        "last_drift_check": manifest.get("audit", {}).get("last_drift_check"),
        "drift_detected": False,
    }
    update_completion(manifest)
    save_json(MANIFEST_PATH, manifest)
    print(f"[OK] {item_id} VERIFIED at commit {commit_sha}. Completion: {manifest['completion_percentage']}%")
    return True


def detect_git_drift(item):
    sha = item.get("evidence", {}).get("commit_sha")
    if not sha:
        return True, "Missing verified commit SHA"
    try:
        current = current_commit_sha()
    except RuntimeError as exc:
        return True, str(exc)
    if current != sha:
        return True, f"Repository HEAD changed from verified commit {sha} to {current}"
    return False, "Repository HEAD matches verified commit"


def detect_deps_drift(item):
    expected = item.get("evidence", {}).get("dependency_lock_hashes", {})
    for relative, expected_hash in expected.items():
        path = REPO_ROOT / relative
        if not path.exists():
            return True, f"Tracked dependency lockfile missing: {relative}"
        current = hashlib.sha256(path.read_bytes()).hexdigest()
        if current != expected_hash:
            return True, f"Dependency lockfile changed: {relative}"
    return False, "No tracked dependency drift"


def run_drift_check():
    manifest = load_json(MANIFEST_PATH)
    policy = load_json(POLICY_PATH)
    stale = False
    details = []
    for item in manifest.get("verified_items", []):
        if item.get("status") != "VERIFIED":
            continue
        for probe in policy["drift_watch"]["probe_types"]:
            if probe == "git":
                changed, detail = detect_git_drift(item)
            elif probe == "deps":
                changed, detail = detect_deps_drift(item)
            else:
                changed, detail = True, f"Unsupported configured probe: {probe}"
            details.append((item["item_id"], probe, changed, detail))
            if changed:
                item["status"] = "STALE"
                stale = True
                break

    now = int(time.time())
    manifest["audit"] = {"last_drift_check": now, "drift_detected": stale, "details": details}
    update_completion(manifest)
    save_json(MANIFEST_PATH, manifest)
    for item_id, probe, changed, detail in details:
        print(f"Probe {probe} / {item_id}: {'DRIFT' if changed else 'OK'} - {detail}")
    print(f"[DRIFT] {'STALE state detected' if stale else 'No drift detected'}. Completion: {manifest['completion_percentage']}%")
    return not stale


def print_status():
    manifest = load_json(MANIFEST_PATH)
    items = manifest.get("verified_items", [])
    print(f"Project: {manifest['project_id']}")
    print(f"Completion: {manifest['completion_percentage']}%")
    print(f"Verified: {sum(i.get('status') == 'VERIFIED' for i in items)}")
    print(f"Stale: {sum(i.get('status') == 'STALE' for i in items)}")
    print(f"Unverified: {sum(i.get('status') == 'UNVERIFIED' for i in items)}")
    print(f"Merkle root: {manifest.get('merkle_root')}")
    for item in items:
        print(f"  {item['item_id']}: {item.get('status')} ({item.get('verification_hash', '')[:12]}...)")


def main():
    parser = argparse.ArgumentParser(description="APEX Slab-Zero Gatekeeper")
    sub = parser.add_subparsers(dest="command", required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("item_id")
    verify.add_argument("--evidence", required=True)
    verify.add_argument("--claim", required=False)
    verify.add_argument("--verifier-id", default="local-dev")
    sub.add_parser("drift")
    sub.add_parser("status")
    args = parser.parse_args()
    if args.command == "verify":
        sys.exit(0 if verify_item(args.item_id, args.evidence, args.claim, args.verifier_id) else 1)
    if args.command == "drift":
        sys.exit(0 if run_drift_check() else 2)
    print_status()


if __name__ == "__main__":
    main()
