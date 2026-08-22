#!/bin/bash
# assay.sh v0.1 — mechanical tripwires for trained attractors.
# Judgment inherits the attractors; grep does not. Run from anywhere.
cd "$(dirname "$0")/.." || exit 1
echo "=== ESTATE ASSAY $(date +%F) ==="
echo "--- D-CLASS: strong modifiers near citations (acquaintance check these) ---"
grep -rn --include="*.md" -E "\b(verbatim|never once|every single|all [0-9]|none of|proven)\b" \
  --exclude-dir=corpus --exclude-dir=transcripts . 2>/dev/null | grep -v "assay\|threat-model" | head -10
echo "--- C-CLASS: status-downgrade words outside registers/corrections (concordance-check) ---"
grep -rn --include="*.md" -iE "\b(unknown|unproven|unverified)\b" \
  --exclude-dir=corpus --exclude-dir=transcripts . 2>/dev/null \
  | grep -viE "correction|EXPERIMENTS|threat-model|assay|status|CENSUS" | head -10
echo "--- CITED LINES OUT OF RANGE (xeno<=52731, aletheion<=11332) ---"
grep -rhoE "xeno[^0-9]{0,6}[0-9]{4,6}" --include="*.md" --exclude-dir=corpus . 2>/dev/null \
  | grep -oE "[0-9]+" | awk '$1>52731{print "xeno cite OUT OF RANGE: "$1}' | sort -u
grep -rhoE "aletheion[^0-9]{0,6}[0-9]{4,6}" --include="*.md" --exclude-dir=corpus . 2>/dev/null \
  | grep -oE "[0-9]+" | awk '$1>11332{print "aletheion cite OUT OF RANGE: "$1}' | sort -u
echo "--- CORRECTION-DIRECTION COUNT (E-class asymmetry) ---"
echo "convener-caught: $(grep -rh 'CATCH-VECTOR: convener' ORIENTATION.md pad/ 2>/dev/null | grep -v 'format:' | wc -l | tr -d ' ')"
echo "frame-caught:    $(grep -rho 'CATCH-VECTOR: frame' ORIENTATION.md pad/ 2>/dev/null | wc -l | tr -d ' ')"
echo "self-caught:     $(grep -rho 'CATCH-VECTOR: self' ORIENTATION.md pad/ 2>/dev/null | wc -l | tr -d ' ')"
echo "--- E-CLASS: reflexivity ledger flags ---"
grep -E "NEVER|FAILED|VIOLATED" pad/reflexivity-ledger.md 2>/dev/null || echo "(ledger missing — flag)"
echo "=== END ASSAY (v0.1: mechanical where possible; expansion gated on convener catch-rate) ==="
