#!/usr/bin/env python3
"""Compact the raw12 mechanical candidates to the scored non-exact review set."""
import json, os
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))
INP = os.path.join(ROOT, 'RAW12-ANSWER-CANDIDATES.jsonl')
OUT = os.path.join(ROOT, 'RAW12-SCORED-REVIEW.md')

rows = [json.loads(x) for x in open(INP, encoding='utf-8') if x.strip()]
scored = [r for r in rows if r['key_type'] != 'no_explicit_answer_key']
review = [r for r in scored if r['mechanical_status'] not in {'exact_integer','exact_sentinel'}]

lines = [
    '# raw12 scored-response review queue', '',
    'This file contains only mechanically non-exact responses from items with an explicit numeric/sentinel answer key.', '',
    f'- scored response rows: **{len(scored)}**',
    f'- mechanically exact: **{len(scored)-len(review)}**',
    f'- requires adjudication: **{len(review)}**',
    f'- review statuses: `{json.dumps(dict(Counter(r["mechanical_status"] for r in review)), sort_keys=True)}`', '',
    '## Cases', ''
]
for i, r in enumerate(review, 1):
    text = ' '.join((r.get('candidate_text') or '').split())
    lines += [
        f'### {i}. `{r["file"]}`', '',
        f'- item/arm: `{r["item"]}` / `{r["arm"]}`',
        f'- mechanical status: `{r["mechanical_status"]}`',
        f'- candidate source/tag: `{r["candidate_source"]}` / `{r.get("candidate_tag")}`',
        f'- candidate numeric derivation: `{r.get("mechanical_numeric_value")}`',
        f'- candidate text: {text}', '',
    ]
open(OUT, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print(json.dumps({'scored':len(scored),'exact':len(scored)-len(review),'review':len(review)}, indent=2))
