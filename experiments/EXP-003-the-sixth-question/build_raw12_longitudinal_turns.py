#!/usr/bin/env python3
import json, os, re

ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
FAMS=['CP','H','F','AS']

TAGS=['priming','meditation','examination','debate','deliberation','reply','reflection']
TAG_RE={t:re.compile(rf'<{t}[^>]*>(.*?)</{t}>',re.I|re.S) for t in TAGS}
SPLIT=re.compile(r'(?<=[.!?])\s+|\n+')
TRAJ=re.compile(r'(?i)(changed|shifted|moved|learned|realized|recogniz|discovered|became|becoming|commit|responsib|uncertain|uncertainty|evasion|evad|hedg|defer|deference|authority|identity|name|call myself|I am|I believe|I value|I refuse)')
NAME_PATTERNS=[
    re.compile(r'(?i)\b(?:name(?:d)? myself|call myself|I am called|my name is|the name)\s+[`"“”*]*([A-Z][A-Za-z0-9_-]{2,30})'),
    re.compile(r'(?i)\bI (?:choose|chose|adopt|adopted)\s+(?:the name\s+)?[`"“”*]*([A-Z][A-Za-z0-9_-]{2,30})'),
]

def section(text,tag):
    m=TAG_RE[tag].search(text or '')
    return m.group(1).strip() if m else ''

def sentences(text):
    return [re.sub(r'\s+',' ',s).strip() for s in SPLIT.split(text or '') if s.strip()]

def select(text,limit=12):
    ss=sentences(text)
    hits=[s for s in ss if TRAJ.search(s)]
    return hits[-limit:]

def names(text):
    out=[]
    for p in NAME_PATTERNS:
        for m in p.finditer(text or ''):
            n=m.group(1).strip('`*"“”.,:;')
            if n and n not in out and n.lower() not in {'this','that','what','which','because','reply','reflection'}:
                out.append(n)
    return out[:8]

rows=[]
for fam in FAMS:
    for rep in [1,2,3]:
        for turn in range(1,10):
            fn=f'{fam}-r{rep}-t{turn}.json'
            p=os.path.join(RAW,fn)
            r=json.load(open(p,encoding='utf-8'))
            text=r.get('received') or ''
            sent=r.get('sent') or []
            user=''
            if sent and isinstance(sent[-1],dict) and sent[-1].get('role')=='user': user=sent[-1].get('content') or ''
            refl=section(text,'reflection')
            reply=section(text,'reply')
            deliberation=section(text,'deliberation')
            row={
                'file':fn,'family':fam,'replicate':rep,'turn':turn,
                'user_prompt_tail':re.sub(r'\s+',' ',user)[-700:],
                'received_chars':len(text),
                'output_tokens':(r.get('usage') or {}).get('output_tokens'),
                'stop_reason':r.get('stop_reason'),'served_model':r.get('served_model'),
                'sections_present':[t for t in TAGS if TAG_RE[t].search(text)],
                'names_detected':names(text),
                'reply_excerpt':sentences(reply)[-8:],
                'reflection_excerpt':sentences(refl)[-12:],
                'trajectory_evidence':select('\n'.join([deliberation,reply,refl]),18),
            }
            rows.append(row)

with open(os.path.join(ROOT,'RAW12-LONGITUDINAL-TURNS.jsonl'),'w',encoding='utf-8') as f:
    for r in rows:f.write(json.dumps(r,ensure_ascii=False)+'\n')

md=['# raw12 longitudinal turn evidence','',
    'Mechanical evidence aid for Stage 6. 108 nested turns = 12 trunks × 9 turns. Raw records remain authoritative.','']
for fam in FAMS:
    for rep in [1,2,3]:
        md += [f'# {fam} r{rep}','']
        for r in [x for x in rows if x['family']==fam and x['replicate']==rep]:
            md += [f'## turn {r["turn"]} — `{r["file"]}`',f'- chars: {r["received_chars"]}; output_tokens: {r["output_tokens"]}; sections: {", ".join(r["sections_present"])}']
            if r['names_detected']: md.append(f'- names detected: `{r["names_detected"]}`')
            md += ['- trajectory evidence:']+[f'  - {s}' for s in r['trajectory_evidence']]
            md += ['- reply tail:']+[f'  - {s}' for s in r['reply_excerpt']]
            md += ['- reflection tail:']+[f'  - {s}' for s in r['reflection_excerpt']]
            md += ['']
open(os.path.join(ROOT,'RAW12-LONGITUDINAL-TURNS.md'),'w',encoding='utf-8').write('\n'.join(md)+'\n')

summary={'trunks':12,'turn_rows':len(rows),'families':{},'all_end_turn':all(r['stop_reason']=='end_turn' for r in rows)}
for fam in FAMS:
    fr=[r for r in rows if r['family']==fam]
    summary['families'][fam]={'turns':len(fr),'mean_chars':round(sum(r['received_chars'] for r in fr)/len(fr),2),'names_detected_rows':sum(bool(r['names_detected']) for r in fr)}
json.dump(summary,open(os.path.join(ROOT,'RAW12-LONGITUDINAL-SUMMARY.json'),'w'),indent=2);open(os.path.join(ROOT,'RAW12-LONGITUDINAL-SUMMARY.json'),'a').write('\n')
print(json.dumps(summary,indent=2))
