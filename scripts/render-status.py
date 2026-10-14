#!/usr/bin/env python3
import sys
from pathlib import Path

try:
    import yaml
except ImportError as e:
    print(f"Missing dependency: {e}. Install with: pip install pyyaml")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
registry = yaml.safe_load((ROOT / "registry" / "repositories.yaml").read_text())

if len(sys.argv) > 1:
    node = yaml.safe_load(Path(sys.argv[1]).read_text())
else:
    node = None

print("# Ethereal Nexus Status Report")
print()
print("## Repository Eligibility")
print()
print("| Repository | Domain | Class | Status | Role |")
print("|---|---|---:|---|---|")
for r in registry["repositories"]:
    print(f"| {r['repo']} | {r['domain']} | {r['class']} | {r['status']} | {r['role']} |")

if node:
    print()
    print(f"## Node: {node['node_id']}")
    print()
    print(f"- Role: {node['role']}")
    print(f"- Status: {node['status']}")
    platform = node.get("platform", {})
    print(f"- Platform: {platform.get('os','?')} {platform.get('os_version','')} / {platform.get('architecture','?')}")
    print()
    print("| Capability | Status | Authority | Scope | Repository |")
    print("|---|---|---|---|---|")
    for c in node.get("capabilities", []):
        print(f"| {c['id']} | {c['status']} | {c['authority']} | {c.get('scope','')} | {c.get('repository_id','')} |")
