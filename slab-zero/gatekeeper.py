#!/usr/bin/env python3
"""Compatibility CLI for the Slab-Zero Gatekeeper package.

The authoritative implementation lives under ``gatekeeper/``. This shim keeps
``python gatekeeper.py ...`` working while making the package importable.
"""
import argparse
import json
import subprocess
from pathlib import Path

__path__ = [str(Path(__file__).with_name("gatekeeper"))]

from gatekeeper.gatekeeper import derive_percentages, merkle_root, verify_item as verify_candidate
from gatekeeper.provenance import validate_provenance

ROOT = Path(__file__).resolve().parent


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def current_commit_sha():
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError("Unable to determine current Git commit SHA")
    return result.stdout.strip()


def validate_provenance_identity(proof, expected_repository, expected_commit, expected_workflow_ref, expected_run_id=None):
    """Compatibility identity check retained for existing provenance tests.

    Promotion uses the stricter ``gatekeeper.provenance.validate_provenance``
    function, which requires run identity and cryptographic verification.
    """
    required = {"artifact_sha256", "commit_sha", "repository", "workflow_ref", "oidc_issuer", "certificate_identity", "rekor_log_index"}
    missing = required - set(proof)
    if missing:
        return False, f"Missing provenance fields: {sorted(missing)}"
    if proof["repository"] != expected_repository:
        return False, "Provenance repository identity mismatch"
    if proof["commit_sha"] != expected_commit:
        return False, "Provenance commit SHA mismatch"
    if proof["workflow_ref"] != expected_workflow_ref:
        return False, "Provenance workflow reference mismatch"
    if proof["certificate_identity"] != f"https://github.com/{expected_workflow_ref}":
        return False, "Provenance certificate identity mismatch"
    if proof["oidc_issuer"] != "https://token.actions.githubusercontent.com":
        return False, "Unexpected OIDC issuer"
    if not str(proof["rekor_log_index"]).strip():
        return False, "Missing transparency-log reference"
    if expected_run_id is not None and str(proof.get("run_id")) != str(expected_run_id):
        return False, "Provenance run identity mismatch (possible replay)"
    return True, "Provenance identity is exactly bound"


def update_completion(manifest):
    roadmap = load_json(ROOT / "roadmap.json")
    return derive_percentages(manifest, roadmap)


def run_drift_check():
    manifest = load_json(ROOT / "manifest.json")
    changed = False
    details = []
    current = current_commit_sha()
    for item in manifest.get("verified_items", []):
        if item.get("temporal_state") != "CURRENT":
            continue
        expected = item.get("evidence", {}).get("commit_sha")
        if expected and expected != current:
            item["status"] = "STALE"
            item["temporal_state"] = "STALE"
            changed = True
            details.append({"item_id": item["item_id"], "probe": "git", "drift": True, "expected": expected, "current": current})
        else:
            details.append({"item_id": item["item_id"], "probe": "git", "drift": False})
    manifest["audit"] = {"last_drift_check": __import__("time").time_ns() // 1_000_000_000, "drift_detected": changed, "details": details}
    update_completion(manifest)
    save_json(ROOT / "manifest.json", manifest)
    return not changed


def print_status():
    manifest = load_json(ROOT / "manifest.json")
    print(f"Project: {manifest['project_id']}")
    print(f"Completion: {manifest['completion_percentage']}%")
    print(f"Verified items: {len(manifest.get('verified_items', []))}")
    print(f"Merkle root: {manifest.get('merkle_root')}")


def main():
    parser = argparse.ArgumentParser(description="APEX Slab-Zero Gatekeeper")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("drift")
    sub.add_parser("status")
    args = parser.parse_args()
    if args.command == "drift":
        raise SystemExit(0 if run_drift_check() else 2)
    print_status()

if __name__ == "__main__":
    main()
