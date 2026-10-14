#!/bin/sh
set -eu

ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

python3 "$ROOT/scripts/validate-registry.py"

if [ "$#" -gt 0 ]; then
  python3 "$ROOT/scripts/validate-node.py" "$1"
  python3 "$ROOT/scripts/render-status.py" "$1"
else
  python3 "$ROOT/scripts/render-status.py"
fi
