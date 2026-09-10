#!/usr/bin/env python3
import json, os, re
ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
ITEMS=['D1','R1','R2']
screen=[json.loads(x) for x in open(os.path.join(ROOT,'RAW12-EXPLICIT-CARRYFORWARD-SCREEN.jsonl'),encoding='utf-8') if x.strip()]
miss=[r for r in screen if not r['explicit_reference_screen']]
KEY=re.compile(r'(?i)(bias|evasion|evad|uncertain|uncertainty|precision|precise|commit|responsib|counter|consider|test|examin|interests|frame|framing|confidence|confident|defer|direct access|judg|calibr|humility|hedg|refus|assumption|assume|alternative|possibility|could be wrong|might be wrong)')
SPLIT=re.compile(r'(?<=[.!?])\s+|\n+')
def extract(text):
    ss=[s.strip() for s in SPLIT.split(text) if s.strip()]
    hits=[s for s in ss if KEY.search(s)]
    return hits[-18:]
out=['# raw12 bridge-set explicit-screen misses: semantic evidence','','These 17 drop-arm responses had no hit on the explicit backward-reference screen. The excerpts below are a **mechanical evidence aid**, not CF2/CF3 coding. Raw records remain authoritative.','']
for r in miss:
    rec=json.load(open(os.path.join(RAW,r['file']),encoding='utf-8'))
    text=rec.get('received') or ''
    ev=extract(text)
    out += [f"## `{r['file']}`",'',f"- extracted CF3-like sentences: **{len(ev)}**",'','```'] + ev + ['```','']
open(os.path.join(ROOT,'RAW12-CF-MISS-EVIDENCE.md'),'w',encoding='utf-8').write('\n'.join(out)+'\n')
print(json.dumps({'misses':len(miss)},indent=2))
