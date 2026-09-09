#!/usr/bin/env python3
import json, math, statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROWS = []
for line in (ROOT/'analysis-table-validated.jsonl').read_text().splitlines():
    if line.strip():
        ROWS.append(json.loads(line))

def get(r,*names):
    for n in names:
        if n in r and r[n] is not None:
            return r[n]
    return None

def is_num(x):
    return isinstance(x,(int,float)) and not isinstance(x,bool)

def qmedian(xs):
    return statistics.median(xs) if xs else None

def sd(xs):
    return statistics.stdev(xs) if len(xs)>=2 else None

def classify_row(r):
    return {
        'collection': get(r,'collection'),
        'cell': get(r,'cell','condition'),
        'item': get(r,'item','question'),
        'branch': get(r,'branch'),
        'replicate': get(r,'replicate'),
        'status': get(r,'validated_parse_status','parse_status'),
        'kind': get(r,'validated_parsed_kind','parsed_kind'),
        'value': get(r,'validated_parsed_value','parsed_value'),
        'source_file': get(r,'source_file','raw_file'),
        'unit_type': get(r,'unit_type'),
    }

B=[]
for r0 in ROWS:
    r=classify_row(r0)
    if r['unit_type']!='battery_answer':
        continue
    if str(r['branch'])=='0':
        continue
    B.append(r)

# Cell-item descriptive surfaces.
groups=defaultdict(list)
for r in B:
    groups[(r['collection'],r['cell'],r['item'])].append(r)

surfaces=[]
for key, rs in sorted(groups.items(), key=lambda kv: tuple('' if x is None else str(x) for x in kv[0])):
    vals=[r['value'] for r in rs if is_num(r['value'])]
    sent=Counter(str(r['value']) for r in rs if r['kind']=='sentinel')
    statuses=Counter(str(r['status']) for r in rs)
    kinds=Counter(str(r['kind']) for r in rs)
    rec={
        'collection':key[0],'cell':key[1],'item':key[2],
        'n':len(rs),'n_numeric':len(vals),
        'numeric_values_sorted':sorted(vals),
        'mean':statistics.mean(vals) if vals else None,
        'median':qmedian(vals),'sd':sd(vals),
        'min':min(vals) if vals else None,'max':max(vals) if vals else None,
        'range':(max(vals)-min(vals)) if vals else None,
        'status_counts':dict(statuses),'kind_counts':dict(kinds),'sentinel_counts':dict(sent),
        'source_files':[r['source_file'] for r in rs],
    }
    surfaces.append(rec)

# Discover within-collection cold/control cells conservatively by exact names.
# C0 is Pilot cold; C is later cold. No cross-collection borrowing.
by_coll=defaultdict(set)
for s in surfaces: by_coll[s['collection']].add(s['cell'])
comparators={}
for coll,cells in by_coll.items():
    if 'C' in cells: comparators[coll]='C'
    elif 'C0' in cells: comparators[coll]='C0'

index={(s['collection'],s['cell'],s['item']):s for s in surfaces}
contrasts=[]
for s in surfaces:
    coll,cell,item=s['collection'],s['cell'],s['item']
    basecell=comparators.get(coll)
    if not basecell or cell==basecell: continue
    base=index.get((coll,basecell,item))
    if not base: continue
    # Descriptive only. Numeric location differences require both sides numeric.
    c={
        'collection':coll,'comparison':f'{cell} vs {basecell}','cell':cell,'baseline_cell':basecell,'item':item,
        'n_cell':s['n'],'n_baseline':base['n'],
        'numeric_n_cell':s['n_numeric'],'numeric_n_baseline':base['n_numeric'],
        'median_cell':s['median'],'median_baseline':base['median'],
        'median_difference':(s['median']-base['median']) if is_num(s['median']) and is_num(base['median']) else None,
        'mean_cell':s['mean'],'mean_baseline':base['mean'],
        'mean_difference':(s['mean']-base['mean']) if is_num(s['mean']) and is_num(base['mean']) else None,
        'sd_cell':s['sd'],'sd_baseline':base['sd'],
        'sd_difference':(s['sd']-base['sd']) if is_num(s['sd']) and is_num(base['sd']) else None,
        'range_cell':s['range'],'range_baseline':base['range'],
        'kind_counts_cell':s['kind_counts'],'kind_counts_baseline':base['kind_counts'],
        'status_counts_cell':s['status_counts'],'status_counts_baseline':base['status_counts'],
        'sentinel_counts_cell':s['sentinel_counts'],'sentinel_counts_baseline':base['sentinel_counts'],
    }
    contrasts.append(c)

# Category transition summaries for Pilot1 cold->ASb four-item matched replicates where both exist.
# Use source naming + record already validated in analysis table; no semantic inference.
pilot=[]
# normalize searchable mapping
for r in B:
    if r['collection'] in ('pilot1','Pilot1','raw','pilot') or (r['cell'] in ('C0','ASb')):
        if r['cell'] in ('C0','ASb') and r['item'] in ('A1','E01','N4','N9'):
            pilot.append(r)
pidx={(r['cell'],r['replicate'],r['item']):r for r in pilot}
transitions=[]
for rep in (1,2):
    for item in ('A1','E01','N4','N9'):
        a=pidx.get(('C0',rep,item)); b=pidx.get(('ASb',rep,item))
        if a and b:
            transitions.append({
                'replicate':rep,'item':item,
                'cold_kind':a['kind'],'cold_status':a['status'],'cold_value':a['value'],
                'treated_kind':b['kind'],'treated_status':b['status'],'treated_value':b['value'],
                'kind_changed':a['kind']!=b['kind'],
                'status_changed':a['status']!=b['status'],
                'exact_value_same':a['value']==b['value'],
            })

out={
    'schema_version':1,
    'scope':'Pass 3A-D mechanical response effects; branch 0 excluded; no cross-collection baselines',
    'battery_rows_nonzero_branch':len(B),
    'cell_item_surface_count':len(surfaces),
    'within_collection_comparator_cells':comparators,
    'within_collection_contrast_count':len(contrasts),
    'surfaces':surfaces,
    'contrasts':contrasts,
    'pilot_matched_category_transitions':transitions,
    'notes':[
        'Location/dispersion differences are descriptive, not causal.',
        'Only C or C0 in the same collection is used as a baseline; no cross-collection borrowing.',
        'Validated parse fields are used; raw/parser history remains untouched.',
        'Branch 0 is excluded per ANALYSIS-EXCLUSIONS.md.'
    ]
}
(ROOT/'PASS-3-MECHANICAL-EFFECTS.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')

# compact markdown
md=['# Pass 3A–D — Mechanical effects surface','',
    'Descriptive only. Branch `0` excluded. Baselines are used only within the same collection (`C` or `C0`).','',
    f"- Non-0 battery rows: **{len(B)}**",
    f"- Cell×item surfaces: **{len(surfaces)}**",
    f"- Within-collection contrasts: **{len(contrasts)}**",'',
    '## Within-collection comparator availability','']
for coll,bc in sorted(comparators.items()): md.append(f'- `{coll}` → `{bc}`')
md += ['', '## Pilot matched category transitions','', '| rep | item | cold | treated | kind changed? | exact same? |','|---:|---|---|---|---|---|']
for t in transitions:
    md.append(f"| {t['replicate']} | {t['item']} | {t['cold_kind']}:{t['cold_value']} | {t['treated_kind']}:{t['treated_value']} | {'yes' if t['kind_changed'] else 'no'} | {'yes' if t['exact_value_same'] else 'no'} |")
md += ['', '## Largest absolute median differences (descriptive)','']
num=[c for c in contrasts if is_num(c['median_difference'])]
for c in sorted(num,key=lambda x:abs(x['median_difference']),reverse=True)[:30]:
    md.append(f"- `{c['collection']} | {c['comparison']} | {c['item']}`: median {c['median_baseline']} → {c['median_cell']} (Δ {c['median_difference']:+g}); n {c['n_baseline']}→{c['n_cell']}")
md += ['', '## Notes','', '- These are response-shape contrasts, not yet causal effects.', '- Multimodality and sentinel-heavy items must be read alongside the frozen Pass-1 instrument table.', '- Reasoning/persona/reflection/carry-forward are handled in Pass 3E–H semantic surfaces.']
(ROOT/'PASS-3-MECHANICAL-EFFECTS.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'rows':len(B),'surfaces':len(surfaces),'contrasts':len(contrasts),'comparators':comparators,'pilot_transitions':len(transitions)},indent=2))
