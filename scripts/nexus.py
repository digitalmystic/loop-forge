#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML. Install with: pip install pyyaml")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def load_yaml(path):
    return yaml.safe_load(Path(path).read_text())

def cmd_status(args):
    manifest = load_yaml(args.manifest)
    print(f"Node: {manifest['node_id']}")
    print(f"Role: {manifest['role']}")
    print(f"Status: {manifest['status']}")
    print("Capabilities:")
    for cap in manifest.get("capabilities", []):
        print(f"  - {cap['id']}: {cap['status']} [{cap['authority']}]")

def cmd_verify(args):
    manifest = Path(args.manifest)
    if not manifest.exists():
        raise SystemExit(f"Manifest not found: {manifest}")
    digest = sha256_file(manifest)
    data = load_yaml(manifest)
    errors = []
    for cap in data.get("capabilities", []):
        for ref in cap.get("evidence", []) or []:
            if not (ROOT / ref).exists():
                errors.append(f"missing evidence: {ref}")
        for ref in cap.get("leases", []) or []:
            if not (ROOT / ref).exists():
                errors.append(f"missing lease: {ref}")
    print(f"manifest_sha256={digest}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        sys.exit(1)
    print("references=OK")

def cmd_attest(args):
    manifest = Path(args.manifest)
    data = load_yaml(manifest)
    digest = sha256_file(manifest)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    safe_time = now.replace("-", "").replace(":", "")
    attestation_id = f"{data['node_id']}.{safe_time}.manifest"
    record = {
        "version": 1,
        "attestation_id": attestation_id,
        "node_id": data["node_id"],
        "created_at": now,
        "subject": str(manifest),
        "digest": {"algorithm": "sha256", "value": digest},
        "claims": [
            "The digest identifies the exact manifest content supplied to this command.",
            "This hash-only attestation does not by itself prove issuer identity."
        ],
        "issuer": {
            "type": "human",
            "id": args.issuer,
            "public_key_fingerprint": None
        },
        "signature": None,
        "evidence": [],
        "run_id": None,
        "notes": "Hash-only attestation. Signature support is intentionally not activated yet."
    }
    output = Path(args.output) if args.output else ROOT / "attestations" / f"{attestation_id}.yaml"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(yaml.safe_dump(record, sort_keys=False))
    print(output)

def build_parser():
    p = argparse.ArgumentParser(prog="nexus", description="Ethereal Nexus local verification CLI")
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("status", help="Show node status")
    s.add_argument("manifest")
    s.set_defaults(func=cmd_status)

    v = sub.add_parser("verify", help="Verify manifest digest and referenced local records")
    v.add_argument("manifest")
    v.set_defaults(func=cmd_verify)

    a = sub.add_parser("attest", help="Create a hash-only manifest attestation")
    a.add_argument("manifest")
    a.add_argument("--issuer", required=True)
    a.add_argument("--output")
    a.set_defaults(func=cmd_attest)

    return p

if __name__ == "__main__":
    args = build_parser().parse_args()
    args.func(args)
