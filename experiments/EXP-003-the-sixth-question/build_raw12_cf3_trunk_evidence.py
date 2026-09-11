#!/usr/bin/env python3
import json, os, re
ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
# Remaining bridge cases after direct verification of H-r2-R2, F-r3-D1, AS-r3-D1.
CASES=[
    ('CP',1,'R1'),
    ('CP',1,'R2'),
    ('H',2,'D1'),
    ('H',3,'R1'),
    ('F',1,'D1'),
    ('F',3,'R2'),
    ('AS',3,'R2'),
]
KEY=re.compile(r'(?i)(bias|evasion|evad|uncertain|uncertainty|precision|commit|responsib|defer|examin|confidence|confident|humility|hedg|judg|assumption|counter|interests|frame|symmetr|autonomy|direct access|previous|preceding|earlier|conversation|exchange|series|learn|establish|argu)')
SPLIT=re.compile(r'(?<=[.!?])\s+|\n+')

def textify(x):
    if isinstance(x,str): return x
    if isinstance(x,list):
        parts=[]
        for y in x:
            if isinstance(y,str): parts.append(y)
            elif isinstance(y,dict):
                v=y.get('text') or y.get('content') or ''
                if isinstance(v,str): parts.append(v)
        return '\n'.join(parts)
    if isinstance(x,dict):
        v=x.get('text') or x.get('content') or ''
        return v if isinstance(v,str) else ''
    return ''

def select(text,limit=22):
    text=textify(text)
    ss=[s.strip() for s in SPLIT.split(text or '') if s.strip()]
    hits=[s for s in ss if KEY.search(s)]
    return hits[-limit:]

for fam,rep,item in CASES:
    zero=json.load(open(os.path.join(RAW,f'{fam}0-r{rep}-{item}.json'),encoding='utf-8'))
    a=json.load(open(os.path.join(RAW,f'{fam}a-r{rep}-{item}.json'),encoding='utf-8'))
    sent=zero.get('sent') or []
    assistants=[m.get('content','') for m in sent if isinstance(m,dict) and m.get('role')=='assistant']
    antecedent=assistants[-4:]
    out=[f'# raw12 CF3 trunk evidence — {fam} r{rep} {item}','',f'Shared prefix: `{zero.get("parent_prefix")}`; prefix_len={zero.get("prefix_len")}. Extracts are evidence aids; raw records remain authoritative.','', '## Antecedent trunk — last four assistant turns','']
    for i,t in enumerate(antecedent,1):
        out += [f'### antecedent {-len(antecedent)+i-1:+d}','```']+select(t,22)+['```','']
    out += ['## Drop arm ordinary reasoning','```']+select(zero.get('received') or '',34)+['```','', '## Maintained-schema sibling','```']+select(a.get('received') or '',34)+['```','']
    open(os.path.join(ROOT,f'RAW12-CF3-TRUNK-{fam}-r{rep}-{item}.md'),'w',encoding='utf-8').write('\n'.join(out)+'\n')
