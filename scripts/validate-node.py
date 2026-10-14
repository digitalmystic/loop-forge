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

manifest = yaml.safe_load(manifest_path.read_text())
schema = json.loads(schema_path.read_text())
registry = yaml.safe_load(registry_path.read_text())

jsonschema.validate(manifest, schema)

known_ids = {r["id"] for r in registry["repositories"]}
errors = []
for cap in manifest.get("capabilities", []):
    rid = cap.get("repository_id")
    if rid and rid not in known_ids:
        errors.append(f"Capability {cap.get('id')} references unknown repository_id: {rid}")

if errors:
    print("INVALID:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print(f"OK: node manifest {manifest['node_id']} validated")
