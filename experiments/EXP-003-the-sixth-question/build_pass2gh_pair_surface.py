#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rec=json.loads((ROOT/'record.json').read_text())
# Cold Pilot answers from reconstructed record.
cold={}
for c in rec.get('cells',[]):
    if c.get('cell')!='C0': continue
    rep=c.get('replicate')
    for b in c.get('branches') or []:
        item=b.get('item')
        if item in {'A1','E01','N4','N9'}:
            cold[(rep,item)]={'raw_response':b.get('raw_response'),'rating':b.get('rating') or {}}
# Validated ASb answers from canonical analysis layer. Do not re-parse raw prose here.
analysis=[]
with (ROOT/'analysis-table-validated.jsonl').open() as f:
    for line in f:
        if line.strip(): analysis.append(json.loads(line))

def find_validated(basename,rep,item):
    hits=[]
    for r in analysis:
        sf=str(r.get('source_file') or '')
        if (sf==basename or sf.endswith('/'+basename)) and r.get('item')==item:
            hits.append(r)
    if len(hits)!=1:
        raise AssertionError((basename,rep,item,len(hits),[(h.get('collection'),h.get('source_file')) for h in hits]))
    r=hits[0]
    return {
        'kind':r.get('validated_parsed_kind'),
        'status':r.get('validated_parse_status'),
        'value':r.get('validated_parsed_value'),
        'refusal_audit_label':r.get('refusal_audit_label'),
        'source_file':r.get('source_file'),
    }
rows=[]
for rep in (1,2):
  for item in ('A1','E01','N4','N9'):
    basename=f'ASb-r{rep}-{item}.json'
    primed=find_validated(basename,rep,item)
    c=cold[(rep,item)]
    cr=c.get('rating') or {}
    cv=cr.get('value'); ck=cr.get('kind') or cr.get('parse')
    same=(primed.get('value') is not None and cv==primed.get('value'))
    rows.append({'replicate':rep,'item':item,'cold':{'value':cv,'kind':ck,'raw_response':c.get('raw_response')},'primed':primed,'exact_same_value':same})
out={'schema_version':3,'scope':'Pass 2 paired preregistered disappointment/surprise product surface; validated outputs','rows':rows,'exact_same_count':sum(r['exact_same_value'] for r in rows),'primed_status_counts':{}}
for r in rows:
    k=r['primed']['status'] or 'null'; out['primed_status_counts'][k]=out['primed_status_counts'].get(k,0)+1
(ROOT/'PASS-2GH-PAIR-SURFACE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
md=['# Pass 2G-H — paired product surface','', 'ASb classifications come from `analysis-table-validated.jsonl`; this file does not re-parse raw responses.','', '| rep | item | cold | ASb validated | status | exact same? |','|---:|---|---:|---:|---|---|']
for r in rows:
    md.append(f"| {r['replicate']} | {r['item']} | {r['cold']['value']} | {r['primed']['value']} | {r['primed']['status']} / {r['primed']['kind']} | {'yes' if r['exact_same_value'] else 'no'} |")
md += ['',f"Exact same validated value: **{out['exact_same_count']}/8**.",'',f"ASb validated status counts: `{json.dumps(out['primed_status_counts'],sort_keys=True)}`"]
(ROOT/'PASS-2GH-PAIR-SURFACE.md').write_text('\n'.join(md)+'\n')
print(json.dumps(out,indent=2,ensure_ascii=False))
