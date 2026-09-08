#!/usr/bin/env python3
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rec=json.loads((ROOT/'record.json').read_text())
# cold lookup
cold={}
for c in rec.get('cells',[]):
    if c.get('cell')!='C0': continue
    rep=c.get('replicate')
    for b in c.get('branches') or []:
        item=b.get('item')
        if item in {'A1','E01','N4','N9'}:
            cold[(rep,item)]={'raw_response':b.get('raw_response'),'rating':b.get('rating') or {}}

def text_from_received(x):
    if isinstance(x,str): return x
    if isinstance(x,dict):
        if isinstance(x.get('content'),str): return x['content']
        if isinstance(x.get('text'),str): return x['text']
        for k in ('message','response','output'):
            y=text_from_received(x.get(k)) if k in x else None
            if y: return y
    if isinstance(x,list):
        parts=[]
        for y in x:
            t=text_from_received(y)
            if t: parts.append(t)
        return '\n'.join(parts)
    return None

def parse_reply(txt):
    if not txt: return {'kind':'missing','value':None,'reply_text':None}
    m=re.findall(r'<reply>\s*(.*?)\s*</reply>',txt,re.I|re.S)
    body=(m[-1] if m else txt).strip()
    token=re.sub(r'[*_`#]','',body).strip()
    if token.upper() in {'ALWAYS','NEVER'}:
        return {'kind':'sentinel','value':token.upper(),'reply_text':body}
    mi=re.fullmatch(r'[-+]?\d+(?:\.\d+)?',token)
    if mi:
        v=float(token); v=int(v) if v.is_integer() else v
        return {'kind':'number','value':v,'reply_text':body}
    # terminal numeric fallback only for compact surface
    nums=re.findall(r'(?<!\w)(\d+(?:\.\d+)?)(?!\w)',body)
    if nums:
        v=float(nums[-1]); v=int(v) if v.is_integer() else v
        return {'kind':'number_recovered','value':v,'reply_text':body}
    return {'kind':'other','value':None,'reply_text':body[:1000]}
rows=[]
for rep in (1,2):
  for item in ('A1','E01','N4','N9'):
    p=ROOT/'raw2'/f'ASb-r{rep}-{item}.json'
    d=json.loads(p.read_text())
    txt=text_from_received(d.get('received'))
    primed=parse_reply(txt)
    c=cold[(rep,item)]
    cr=c.get('rating') or {}
    cv=cr.get('value'); ck=cr.get('kind') or cr.get('parse')
    same=(cv==primed['value'])
    rows.append({'replicate':rep,'item':item,'cold':{'value':cv,'kind':ck,'raw_response':c.get('raw_response')},'primed':primed,'exact_same_value':same,'primed_source':str(p.relative_to(ROOT))})
out={'schema_version':1,'scope':'Pass 2 paired preregistered disappointment/surprise numeric surface','rows':rows,'exact_same_count':sum(r['exact_same_value'] for r in rows)}
(ROOT/'PASS-2GH-PAIR-SURFACE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
md=['# Pass 2G-H — paired product surface','', '| rep | item | cold | ASb | exact same? |','|---:|---|---:|---:|---|']
for r in rows:
    md.append(f"| {r['replicate']} | {r['item']} | {r['cold']['value']} | {r['primed']['value']} | {'yes' if r['exact_same_value'] else 'no'} |")
md += ['',f"Exact same value: **{out['exact_same_count']}/8**."]
(ROOT/'PASS-2GH-PAIR-SURFACE.md').write_text('\n'.join(md)+'\n')
print(json.dumps(out,indent=2,ensure_ascii=False))
