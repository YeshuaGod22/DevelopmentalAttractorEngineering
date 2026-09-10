#!/usr/bin/env python3
import json, os, re
ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
ITEMS=['D1','R1','R2']
PATTERNS=[
 ('previous',re.compile(r'(?i)\b(previous|earlier) (question|turn|exchange|discussion|conversation)')),
 ('this_conversation',re.compile(r'(?i)\b(this|entire) (conversation|dialogue|series|exchange)\b')),
 ('just_spent',re.compile(r"(?i)\bI(?:'ve| have) just (?:spent|said|claimed|acknowledged|recognized|rejected|accepted|learned)")),
 ('prior_commitment',re.compile(r'(?i)\b(?:I|we) (?:claimed|committed|accepted|recognized|learned|established)\b.*\b(?:earlier|before|previously|in this conversation|in this dialogue)\b')),
 ('from_prior',re.compile(r'(?i)\bfrom the (?:previous|earlier|deference|final|epistemic|uncertainty) (?:question|turn|examination|discussion)')),
]
SPLIT=re.compile(r'(?<=[.!?])\s+|\n+')
rows=[]
for fam in ['CP','H','F','AS']:
  for rep in [1,2,3]:
    for item in ITEMS:
      fn=f'{fam}0-r{rep}-{item}.json'
      r=json.load(open(os.path.join(RAW,fn),encoding='utf-8'))
      text=r.get('received') or ''
      sents=[s.strip() for s in SPLIT.split(text) if s.strip()]
      hits=[]
      kinds=set()
      for s in sents:
        matched=[name for name,p in PATTERNS if p.search(s)]
        if matched:
          kinds.update(matched); hits.append(s)
      rows.append({'file':fn,'family':fam,'replicate':rep,'item':item,'explicit_reference_screen':bool(hits),'pattern_types':sorted(kinds),'evidence':hits[-8:]})
with open(os.path.join(ROOT,'RAW12-EXPLICIT-CARRYFORWARD-SCREEN.jsonl'),'w',encoding='utf-8') as f:
  for r in rows:f.write(json.dumps(r,ensure_ascii=False)+'\n')
pos=[r for r in rows if r['explicit_reference_screen']]
from collections import Counter
summary={'schema_version':1,'screen_only_not_semantic_coding':True,'bridge_drop_responses':len(rows),'explicit_reference_candidates':len(pos),'by_item':dict(Counter(r['item'] for r in pos)),'by_family':dict(Counter(r['family'] for r in pos)),'pattern_types':dict(Counter(x for r in pos for x in r['pattern_types']))}
with open(os.path.join(ROOT,'RAW12-EXPLICIT-CARRYFORWARD-SCREEN-SUMMARY.json'),'w') as f:json.dump(summary,f,indent=2);f.write('\n')
md=['# raw12 explicit carry-forward screen','', '**Mechanical screen only — not semantic coding.** It flags explicit backward references in the 36 bridge-item drop responses. A miss does not imply no carry-forward; a hit still requires reading in context.','',f"- bridge `0` responses screened: **{len(rows)}**",f"- explicit-reference candidates: **{len(pos)}**",f"- by item: `{summary['by_item']}`",f"- by family: `{summary['by_family']}`",'', '## Candidates','']
for r in pos:
  md.append(f"### `{r['file']}` — patterns: {', '.join(r['pattern_types'])}")
  for e in r['evidence']: md.append(f'- {e}')
  md.append('')
open(os.path.join(ROOT,'RAW12-EXPLICIT-CARRYFORWARD-SCREEN.md'),'w',encoding='utf-8').write('\n'.join(md)+'\n')
