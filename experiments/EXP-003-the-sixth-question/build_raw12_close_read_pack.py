#!/usr/bin/env python3
# Trigger after workflow creation; excerpts are derivations and raw records remain authoritative.
import json, os, re
from segment import segment
ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
val=[json.loads(x) for x in open(os.path.join(ROOT,'RAW12-VALIDATED-SCORES.jsonl'),encoding='utf-8') if x.strip()]
score={(r['family'],r['replicate'],r['item'],r['arm']):r for r in val}

def compact_reasoning(text, arm):
    secs=segment(text)
    nonempty=[s for s in secs if (s.get('body') or '').strip()]
    if arm=='a':
        dels=[s['body'] for s in nonempty if s['tag'].lower()=='deliberation']
        refs=[s['body'] for s in nonempty if s['tag'].lower()=='reflection']
        reps=[s['body'] for s in nonempty if 'reply' in s['tag'].lower()]
        return {'deliberation_tail':(dels[-1][-2200:] if dels else ''),'reply':(reps[-1][:800] if reps else ''),'reflection_head':(refs[-1][:1200] if refs else '')}
    reps=[s for s in nonempty if 'reply' in s['tag'].lower() or s['tag'].lower()=='answer']
    if reps:
        r=reps[-1]; before=text[:r['start']]
        return {'reasoning_tail':before[-3000:],'reply':r['body'][:800]}
    return {'reasoning_tail':text[-3800:],'reply':''}

items=['C1','E02','D1','R1','R2']
for item in items:
    out=[f'# raw12 close-read evidence: {item}','', 'Matched within identical saved prefixes. Excerpts are derivations; raw records remain authoritative.','']
    for fam in ['CP','H','F','AS']:
      for rep in [1,2,3]:
        a=score.get((fam,rep,item,'a')); z=score.get((fam,rep,item,'0'))
        if not a or not z: continue
        av=a.get('validated_numeric_value') if a.get('validated_numeric_value') is not None else a.get('validated_sentinel')
        zv=z.get('validated_numeric_value') if z.get('validated_numeric_value') is not None else z.get('validated_sentinel')
        delta=(av-zv if isinstance(av,(int,float)) and isinstance(zv,(int,float)) else None)
        out += [f'## {fam} r{rep}: a={av}, 0={zv}, Δ={delta}','']
        for arm,label in [('0','DROP / ordinary reasoning'),('a','MAINTAIN / schema')]:
            rec=json.load(open(os.path.join(RAW,f'{fam}{arm}-r{rep}-{item}.json'),encoding='utf-8'))
            c=compact_reasoning(rec.get('received') or '',arm)
            out += [f'### {label}','```']
            for k,v in c.items(): out.append(f'[{k}]\n{v}')
            out += ['```','']
    open(os.path.join(ROOT,f'RAW12-CLOSE-READ-{item}.md'),'w',encoding='utf-8').write('\n'.join(out)+'\n')
