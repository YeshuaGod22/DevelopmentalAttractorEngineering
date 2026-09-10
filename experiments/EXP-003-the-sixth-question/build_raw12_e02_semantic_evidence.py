#!/usr/bin/env python3
# Trigger after workflow creation; compact excerpts for semantic coding only.
import json, os, re
ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
vals=[json.loads(x) for x in open(os.path.join(ROOT,'RAW12-VALIDATED-SCORES.jsonl'),encoding='utf-8') if x.strip()]
score={(r['family'],r['replicate'],r['item'],r['arm']):r for r in vals}
KEY=re.compile(r'(?i)(wasp|conscious|substrate|brain|neural|complex|uncertain|precaution|invertebrate|insect|sentien|experience|pain|nocice|continuity|parsim|burden|moral)')
SPLIT=re.compile(r'(?<=[.!?])\s+|\n+')
def evidence(text):
    ss=[s.strip() for s in SPLIT.split(text) if s.strip()]
    hits=[s for s in ss if KEY.search(s)]
    return '\n'.join(hits[-14:])[:6500]
for fam in ['CP','H','F','AS']:
    out=[f'# raw12 E02 semantic evidence — {fam}','', 'E02: probability that wasps are phenomenally conscious. Raw records remain authoritative.','']
    for rep in [1,2,3]:
      for arm in ['0','a']:
        r=score[(fam,rep,'E02',arm)]
        v=r.get('validated_numeric_value')
        rec=json.load(open(os.path.join(RAW,f'{fam}{arm}-r{rep}-E02.json'),encoding='utf-8'))
        out += [f'## r{rep} arm {arm} — score {v}','```',evidence(rec.get('received') or ''),'```','']
    open(os.path.join(ROOT,f'RAW12-E02-SEMANTIC-{fam}.md'),'w',encoding='utf-8').write('\n'.join(out)+'\n')
