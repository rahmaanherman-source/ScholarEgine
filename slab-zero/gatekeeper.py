#!/usr/bin/env python3
"""Compatibility CLI for the Slab-Zero Gatekeeper package.

The authoritative implementation lives under ``gatekeeper/``. This shim keeps
``python gatekeeper.py ...`` working while making the package importable.
"""
import argparse
import json
import subprocess
from pathlib import Path

# Allow ``import gatekeeper.lib`` even though this compatibility entrypoint
# retains the historical gatekeeper.py path.
__path__ = [str(Path(__file__).with_name("gatekeeper"))]

from gatekeeper.gatekeeper import derive_percentages, merkle_root, verify_item as verify_candidate

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
