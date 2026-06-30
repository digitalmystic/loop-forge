#!/bin/bash
# loop-forge/scripts/loop-audit.sh
# Score loop readiness (0-100). Reads loop.yaml or loop.resolved.json from target dir.
# Usage: loop-audit.sh <target-dir> [--suggest] [--badge]

set -euo pipefail

TARGET="${1:-.}"
SUGGEST=false
BADGE=false

shift 2>/dev/null || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --suggest) SUGGEST=true ;;
    --badge) BADGE=true ;;
  esac
  shift
done

SCORE=0
MAX=100
DETAILS=()

# Find loop spec
LOOP_FILE=""
if [[ -f "$TARGET/loop.yaml" ]]; then
  LOOP_FILE="$TARGET/loop.yaml"
elif [[ -f "$TARGET/loop.resolved.json" ]]; then
  LOOP_FILE="$TARGET/loop.resolved.json"
fi

if [[ -z "$LOOP_FILE" ]]; then
  echo "ERROR: No loop.yaml or loop.resolved.json found in $TARGET"
  echo "Run 'loop-init.sh $TARGET --pattern daily-triage' first."
  exit 1
fi

echo "=== Loop Forge Audit ==="
echo "  Target: $TARGET"
echo "  Spec:   $(basename $LOOP_FILE)"
echo ""

# Dimension 1: Goal clarity (0-10)
if grep -q "definition_of_done" "$LOOP_FILE" 2>/dev/null || grep -q '"definition_of_done"' "$LOOP_FILE" 2>/dev/null; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] Goal clarity: definition of done present")
else
  DETAILS+=("[FAIL] Goal clarity: no definition_of_done found")
  if $SUGGEST; then DETAILS+=("  → Add definition_of_done to loop.yaml goal section"); fi
fi

# Dimension 2: Verification (0-10)
VERIFY_COUNT=$(grep -c '"type"' "$LOOP_FILE" 2>/dev/null || echo 0)
if [[ $VERIFY_COUNT -ge 2 ]]; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] Verification: $VERIFY_COUNT checks found (programmatic/judge/human)")
elif [[ $VERIFY_COUNT -ge 1 ]]; then
  SCORE=$((SCORE + 5))
  DETAILS+=("[WARN] Verification: only 1 check, recommend 2+ (programmatic + judge)")
else
  DETAILS+=("[FAIL] Verification: no verification checks defined")
  if $SUGGEST; then DETAILS+=("  → Add verification array to goal section"); fi
fi

# Dimension 3: Council (0-10)
if grep -q "council" "$LOOP_FILE" 2>/dev/null; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] Council: cross-model reviewer defined")
else
  DETAILS+=("[FAIL] Council: no cross-model reviewer")
  if $SUGGEST; then DETAILS+=("  → Add council section with different model for review"); fi
fi

# Dimension 4: Gates (0-10)
GATE_COUNT=0
grep -q "plan_gate" "$LOOP_FILE" 2>/dev/null && GATE_COUNT=$((GATE_COUNT + 1))
grep -q "delivery_gate" "$LOOP_FILE" 2>/dev/null && GATE_COUNT=$((GATE_COUNT + 1))
if [[ $GATE_COUNT -eq 2 ]]; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] Gates: plan_gate + delivery_gate defined")
elif [[ $GATE_COUNT -eq 1 ]]; then
  SCORE=$((SCORE + 5))
  DETAILS+=("[WARN] Gates: only 1 gate defined (need plan + delivery)")
else
  DETAILS+=("[FAIL] Gates: no gates defined")
  if $SUGGEST; then DETAILS+=("  → Add gates section with plan_gate and delivery_gate"); fi
fi

# Dimension 5: Stop guards (0-10)
if grep -q "stop_conditions\|max_iterations\|no_progress" "$LOOP_FILE" 2>/dev/null; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] Stop guards: max_iterations + no_progress + budget caps")
else
  DETAILS+=("[FAIL] Stop guards: no max_iterations or stop conditions")
  if $SUGGEST; then DETAILS+=("  → Add loop_control section with max_iterations and stop_conditions"); fi
fi

# Dimension 6: State (0-10)
if [[ -f "$TARGET/loop-workspace/STATE.md" ]] || [[ -f "$TARGET/STATE.md" ]]; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] State: STATE.md present")
else
  DETAILS+=("[FAIL] State: no STATE.md found")
  if $SUGGEST; then DETAILS+=("  → Run loop-init to scaffold STATE.md"); fi
fi

# Dimension 7: Constraints (0-10)
if [[ -f "$TARGET/loop-workspace/constraints.md" ]] || grep -q "budget\|isolation\|worktree" "$LOOP_FILE" 2>/dev/null; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] Constraints: budget/isolation defined")
else
  SCORE=$((SCORE + 3))
  DETAILS+=("[WARN] Constraints: minimal constraint definition")
fi

# Dimension 8: Observability (0-10)
HAS_STATE_JSON=false
HAS_RUN_LOG=false
grep -q "state.json" "$LOOP_FILE" 2>/dev/null && HAS_STATE_JSON=true
[[ -f "$TARGET/loop-workspace/run-log.md" ]] && HAS_RUN_LOG=true
if $HAS_STATE_JSON && $HAS_RUN_LOG; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] Observability: state.json + run-log.md configured")
elif $HAS_STATE_JSON || $HAS_RUN_LOG; then
  SCORE=$((SCORE + 5))
  DETAILS+=("[WARN] Observability: only 1 of 2 (state.json + run-log.md)")
else
  DETAILS+=("[FAIL] Observability: no state.json or run-log.md")
  if $SUGGEST; then DETAILS+=("  → Add observability section to loop.yaml"); fi
fi

# Dimension 9: Schema valid (0-10) — basic check
if grep -q '"version": 1\|version: 1' "$LOOP_FILE" 2>/dev/null; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] Schema: version field present")
else
  SCORE=$((SCORE + 3))
  DETAILS+=("[WARN] Schema: version field missing or unclear")
fi

# Dimension 10: Resolved ready (0-10)
if [[ -f "$TARGET/loop.resolved.json" ]]; then
  SCORE=$((SCORE + 10))
  DETAILS+=("[PASS] Resolved: loop.resolved.json generated")
else
  DETAILS+=("[FAIL] Resolved: no loop.resolved.json")
  if $SUGGEST; then DETAILS+=("  → Run loop-design to generate loop.resolved.json"); fi
fi

# Print results
echo "--- Dimension Scores ---"
for detail in "${DETAILS[@]}"; do
  echo "  $detail"
done
echo ""
echo "========================="
echo "  LOOP READY SCORE: $SCORE / $MAX"

# Color-code interpretation
if [[ $SCORE -ge 86 ]]; then
  echo "  RATING: 🟢 Production-Ready"
elif [[ $SCORE -ge 61 ]]; then
  echo "  RATING: 🟡 Well-Designed (minor gaps)"
elif [[ $SCORE -ge 31 ]]; then
  echo "  RATING: 🟠 Basic Loop Shape"
else
  echo "  RATING: 🔴 Raw Prompt — design a loop first"
fi

# Badge output
if $BADGE; then
  COLOR="red"
  [[ $SCORE -ge 61 ]] && COLOR="yellow"
  [[ $SCORE -ge 86 ]] && COLOR="green"
  echo ""
  echo "README badge:"
  echo "![Loop Ready](https://img.shields.io/badge/Loop_Ready-${SCORE}%2F100-${COLOR})"
fi

exit 0
