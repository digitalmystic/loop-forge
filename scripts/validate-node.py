#!/usr/bin/env python3
import sys
import json
from pathlib import Path

try:
    import yaml
    import jsonschema
except ImportError as e:
    print(f"Missing dependency: {e}. Install with: pip install pyyaml jsonschema")
    sys.exit(2)

if len(sys.argv) != 2:
    print("Usage: python scripts/validate-node.py <node-manifest.yaml>")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
manifest_path = Path(sys.argv[1]).resolve()
schema_path = ROOT / "schemas" / "node-manifest.v1.schema.json"
registry_path = ROOT / "registry" / "repositories.yaml"
evidence_schema_path = ROOT / "schemas" / "evidence-record.v1.schema.json"
lease_schema_path = ROOT / "schemas" / "capability-lease.v1.schema.json"

manifest = yaml.safe_load(manifest_path.read_text())
schema = json.loads(schema_path.read_text())
registry = yaml.safe_load(registry_path.read_text())
evidence_schema = json.loads(evidence_schema_path.read_text())
lease_schema = json.loads(lease_schema_path.read_text())

jsonschema.validate(manifest, schema)

known_ids = {r["id"] for r in registry["repositories"]}
errors = []

def load_record(relative_path, expected_schema, kind):
    path = ROOT / relative_path
    if not path.exists():
        errors.append(f"Missing {kind} record: {relative_path}")
        return None
    try:
        record = yaml.safe_load(path.read_text())
        jsonschema.validate(record, expected_schema)
        return record
    except Exception as e:
        errors.append(f"Invalid {kind} record {relative_path}: {e}")
        return None

for cap in manifest.get("capabilities", []):
    cid = cap.get("id")
    rid = cap.get("repository_id")
    status = cap.get("status")
    authority = cap.get("authority", "")
    evidence_refs = cap.get("evidence", []) or []
    lease_refs = cap.get("leases", []) or []

    if rid and rid not in known_ids:
        errors.append(f"Capability {cid} references unknown repository_id: {rid}")

    if status in {"APPROVED", "IMPLEMENTED"} and not evidence_refs:
        errors.append(f"Capability {cid} is {status} but has no evidence records")

    for ref in evidence_refs:
        record = load_record(ref, evidence_schema, "evidence")
        if record:
            if record.get("node_id") != manifest.get("node_id"):
                errors.append(f"Evidence {ref} belongs to node {record.get('node_id')}, not {manifest.get('node_id')}")
            subject = record.get("subject", "")
            if cid not in subject:
                errors.append(f"Evidence {ref} does not clearly reference capability {cid}")
            if status in {"APPROVED", "IMPLEMENTED"}:
                if record.get("result") != "VERIFIED":
                    errors.append(f"Evidence {ref} for {cid} is not VERIFIED")
                review = record.get("review", {})
                if review.get("required") and review.get("decision") != "ACCEPTED":
                    errors.append(f"Evidence {ref} for {cid} has not been ACCEPTED")

    lease_required = "lease" in authority.lower()
    if status in {"APPROVED", "IMPLEMENTED"} and lease_required and not lease_refs:
        errors.append(f"Capability {cid} requires a capability lease but none is referenced")

    for ref in lease_refs:
        lease = load_record(ref, lease_schema, "lease")
        if lease:
            if lease.get("node_id") != manifest.get("node_id"):
                errors.append(f"Lease {ref} belongs to node {lease.get('node_id')}, not {manifest.get('node_id')}")
            if lease.get("capability_id") != cid:
                errors.append(f"Lease {ref} is for capability {lease.get('capability_id')}, not {cid}")
            if status == "IMPLEMENTED" and lease.get("status") not in {"ACTIVE", "EXPIRED"}:
                errors.append(f"Implemented capability {cid} has no historically active/active lease record")
            if status == "APPROVED" and lease.get("status") not in {"PROPOSED", "ACTIVE"}:
                errors.append(f"Approved capability {cid} has incompatible lease status {lease.get('status')}")

if errors:
    print("INVALID:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print(f"OK: node manifest {manifest['node_id']} validated with evidence/lease checks")
