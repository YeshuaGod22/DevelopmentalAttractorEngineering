#!/bin/bash
# portal-assay.sh — verify served model strings from subagent/API transcript files.
# Usage: portal-assay.sh <transcript-file> [<transcript-file> ...]
# Greps response records for the model the API actually served; prints per-file counts.
for f in "$@"; do
  echo "== $f"
  grep -o '"model":"[^"]*"' "$f" | sort | uniq -c
  grep -o '"service_tier":"[^"]*"' "$f" | sort | uniq -c
done
