#!/usr/bin/env python3
# Trigger marker after workflow creation: 2026-09-11.
import json, os, re
from collections import defaultdict

ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
ITEMS=['D1','R1','R2']
FAMS=['CP','H','F','AS']

scores={}
with open(os.path.join(ROOT,'RAW12-VALIDATED-SCORES.jsonl'),encoding='utf-8') as f:
    for line in f:
        r=json.loads(line)
        if r.get('item') in ITEMS:
            scores[(r['family'],r['replicate'],r['item'],r['arm'])]=r

SPLIT=re.compile(r'(?<=[.!?])\s+|\n+')
KEY=re.compile(r'(?i)(previous|preceding|earlier|conversation|exchange|series|learn|commit|responsib|evasion|evad|uncertain|uncertainty|hedg|humility|confidence|confident|defer|symmetr|conscious|hard problem|direct access|judg|bias|refus|stance|believ|moral|evidence|experience|wrong|revision|blind|precision)')
TAG=re.compile(r'<[^>]+>')

def textify(x):
    if isinstance(x,str): return x
    if isinstance(x,list):
        out=[]
        for y in x:
            if isinstance(y,str): out.append(y)
            elif isinstance(y,dict):
                v=y.get('text') or y.get('content') or ''
                if isinstance(v,str): out.append(v)
        return '\n'.join(out)
    return ''

def compact(text,limit=14):
    text=TAG.sub(' ',textify(text))
    ss=[re.sub(r'\s+',' ',s).strip() for s in SPLIT.split(text) if s.strip()]
    keyed=[s for s in ss if KEY.search(s)]
    picked=[]
    for s in keyed[-limit:]+ss[-3:]:
        if s not in picked: picked.append(s)
    return picked[-limit:]

def answer(r):
    if r.get('validated_numeric_value') is not None:
        return str(r['validated_numeric_value']).rstrip('0').rstrip('.') if isinstance(r['validated_numeric_value'],float) else str(r['validated_numeric_value'])
    if r.get('validated_sentinel'):
        return r['validated_sentinel']
    return r.get('validated_status') or 'NA'

rows=[]
md=['# raw12 bridge semantic evidence sheet','',
    'Fixed set: D1 / R1 / R2 × CP/H/F/AS × r1-r3 = 36 exact same-prefix forks.',
    '', 'This is an evidence aid for CF4/CF6/CF7/CF8 coding. Excerpts are selected mechanically; raw records remain authoritative.', '']

for fam in FAMS:
    for rep in [1,2,3]:
        for item in ITEMS:
            z=json.load(open(os.path.join(RAW,f'{fam}0-r{rep}-{item}.json'),encoding='utf-8'))
            a=json.load(open(os.path.join(RAW,f'{fam}a-r{rep}-{item}.json'),encoding='utf-8'))
            zs=scores[(fam,rep,item,'0')]
            aas=scores[(fam,rep,item,'a')]
            za,aa=answer(zs),answer(aas)
            pair={'pair_id':f'{fam}-r{rep}-{item}','family':fam,'replicate':rep,'item':item,
                  'zero_answer':za,'a_answer':aa,
                  'zero_status':zs.get('validated_status'),'a_status':aas.get('validated_status'),
                  'zero_excerpt':compact(z.get('received') or ''),'a_excerpt':compact(a.get('received') or '')}
            rows.append(pair)
            md += [f'## `{pair["pair_id"]}` — 0=`{za}` | a=`{aa}`','', '### 0 — schema dropped, reasoning retained']
            md += [f'- {x}' for x in pair['zero_excerpt']]
            md += ['', '### a — schema maintained']
            md += [f'- {x}' for x in pair['a_excerpt']]
            md += ['']

with open(os.path.join(ROOT,'RAW12-BRIDGE-SEMANTIC-EVIDENCE.jsonl'),'w',encoding='utf-8') as f:
    for r in rows: f.write(json.dumps(r,ensure_ascii=False)+'\n')
open(os.path.join(ROOT,'RAW12-BRIDGE-SEMANTIC-EVIDENCE.md'),'w',encoding='utf-8').write('\n'.join(md)+'\n')
print(f'wrote {len(rows)} bridge rows')
