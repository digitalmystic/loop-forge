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

ROOT = Path(__file__).resolve().parents[1]
registry_path = ROOT / "registry" / "repositories.yaml"
schema_path = ROOT / "schemas" / "repository-registry.v1.schema.json"

registry = yaml.safe_load(registry_path.read_text())
schema = json.loads(schema_path.read_text())

jsonschema.validate(registry, schema)

ids = [r["id"] for r in registry["repositories"]]
if len(ids) != len(set(ids)):
    dupes = sorted({x for x in ids if ids.count(x) > 1})
    raise SystemExit(f"Duplicate repository ids: {', '.join(dupes)}")

print(f"OK: {len(ids)} repositories validated")
