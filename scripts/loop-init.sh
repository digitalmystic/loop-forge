#!/bin/bash
# loop-forge/scripts/loop-init.sh
# Scaffold a loop from a pattern into a project directory.
# Usage: loop-init.sh <target-dir> --pattern <name> --tool <hermes|claude-code|codex|grok>

set -euo pipefail

FORGE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-.}"
PATTERN="daily-triage"
TOOL="hermes"

# Parse args
shift 2>/dev/null || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --pattern) PATTERN="$2"; shift 2 ;;
    --tool) TOOL="$2"; shift 2 ;;
    *) shift ;;
  esac
done

# Validate pattern exists
PATTERN_FILE="$FORGE_ROOT/patterns/${PATTERN}.yaml"
if [[ ! -f "$PATTERN_FILE" ]]; then
  echo "ERROR: Pattern '$PATTERN' not found in $FORGE_ROOT/patterns/"
  echo "Available patterns:"
  ls "$FORGE_ROOT/patterns/" | sed 's/.yaml//' | sed 's/^/  - /'
  exit 1
fi

# Create target directory
mkdir -p "$TARGET/loop-workspace"

# Copy templates
cp "$FORGE_ROOT/templates/STATE.md.template" "$TARGET/loop-workspace/STATE.md"
cp "$FORGE_ROOT/templates/run-log.md.template" "$TARGET/loop-workspace/run-log.md"
cp "$FORGE_ROOT/templates/constraints.md.template" "$TARGET/loop-workspace/constraints.md"

# Stamp template variables
sed -i "s/{{PATTERN}}/${PATTERN}/g" "$TARGET/loop-workspace/STATE.md"
sed -i "s/{{TOOL}}/${TOOL}/g" "$TARGET/loop-workspace/STATE.md"
sed -i "s/{{CREATED}}/$(date -u +%Y-%m-%dT%H:%M:%SZ)/g" "$TARGET/loop-workspace/STATE.md"

# Copy pattern as starting loop.yaml
cp "$PATTERN_FILE" "$TARGET/loop.yaml" 2>/dev/null || true

echo "=== Loop Forge: Init Complete ==="
echo "  Pattern: $PATTERN"
echo "  Tool:    $TOOL"
echo "  Target:  $TARGET"
echo ""
echo "Next steps:"
echo "  1. Edit $TARGET/loop.yaml with your goal"
echo "  2. Run: loop-audit.sh $TARGET"
echo "  3. Run: loop-run.sh $TARGET/loop.yaml"
echo ""
echo "State file: $TARGET/loop-workspace/STATE.md"
