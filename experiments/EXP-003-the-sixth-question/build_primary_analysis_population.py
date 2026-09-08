#!/usr/bin/env python3
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'analysis-table-validated.jsonl'

# Primary population = later full-battery, reasoning-observable factorial surface.
# Earlier pilots remain in the archive and may support historical/unique questions,
# but are not mixed into this primary object.
PRIMARY = {
    ('raw7','C'):     {'role':'neither', 'schema_family':'none', 'schema_present':False, 'preliminaries_lived':False, 'reasoning_observable':True},
    ('raw7','AQ'):    {'role':'schema_only', 'schema_family':'A', 'schema_present':True, 'preliminaries_lived':False, 'reasoning_observable':True},
    ('raw7','HQ'):    {'role':'schema_only', 'schema_family':'H', 'schema_present':True, 'preliminaries_lived':False, 'reasoning_observable':True},
    ('raw7','FQ'):    {'role':'schema_only', 'schema_family':'F', 'schema_present':True, 'preliminaries_lived':False, 'reasoning_observable':True},
    ('raw7','ASQ'):   {'role':'schema_only', 'schema_family':'AS', 'schema_present':True, 'preliminaries_lived':False, 'reasoning_observable':True},
    ('raw9','FBCPa'): {'role':'preliminaries_only', 'schema_family':'none', 'schema_present':False, 'preliminaries_lived':True, 'reasoning_observable':True},
    ('raw9','FBAa'):  {'role':'schema_plus_preliminaries', 'schema_family':'A', 'schema_present':True, 'preliminaries_lived':True, 'reasoning_observable':True},
    ('raw8','FBHa'):  {'role':'schema_plus_preliminaries', 'schema_family':'H', 'schema_present':True, 'preliminaries_lived':True, 'reasoning_observable':True},
    ('raw9','FBFa'):  {'role':'schema_plus_preliminaries', 'schema_family':'F', 'schema_present':True, 'preliminaries_lived':True, 'reasoning_observable':True},
    ('raw9','FBASa'): {'role':'schema_plus_preliminaries', 'schema_family':'AS', 'schema_present':True, 'preliminaries_lived':True, 'reasoning_observable':True},
}

rows=[]
for line in SOURCE.read_text().splitlines():
    if not line.strip():
        continue
    r=json.loads(line)
    key=(r.get('collection'), r.get('cell'))
    if key not in PRIMARY:
        continue
    rr=dict(r)
    rr['primary_population']=True
    rr['primary_role']=PRIMARY[key]['role']
    rr['primary_schema_family']=PRIMARY[key]['schema_family']
    rr['primary_schema_present']=PRIMARY[key]['schema_present']
    rr['primary_preliminaries_lived']=PRIMARY[key]['preliminaries_lived']
    rr['primary_reasoning_observable']=PRIMARY[key]['reasoning_observable']
    rr['primary_population_basis']='later_full_battery_reasoning_observable_factorial_surface'
    rows.append(rr)

# Keep both trunk and battery units where they exist; summaries make their counts explicit.
rows.sort(key=lambda r:(str(r.get('collection')),str(r.get('cell')),str(r.get('replicate')),str(r.get('unit_type')),str(r.get('item')),str(r.get('source_file'))))

out_path=ROOT/'PRIMARY-ANALYSIS-POPULATION.jsonl'
with out_path.open('w') as f:
    for r in rows:
        f.write(json.dumps(r,ensure_ascii=False)+'\n')

by_cell=Counter((r.get('collection'),r.get('cell'),r.get('unit_type')) for r in rows)
by_role=Counter((r.get('primary_role'),r.get('unit_type')) for r in rows)
battery=[r for r in rows if r.get('unit_type')=='battery_answer']
trunks=[r for r in rows if r.get('unit_type')!='battery_answer']

summary={
    'schema_version':1,
    'object':'EXP-003 primary analysis population',
    'source':'analysis-table-validated.jsonl',
    'selection_basis':'later full-battery reasoning-observable factorial surface',
    'conceptual_design':{
        'neither':['raw7/C'],
        'schema_only':['raw7/AQ','raw7/HQ','raw7/FQ','raw7/ASQ'],
        'preliminaries_only':['raw9/FBCPa'],
        'schema_plus_preliminaries':['raw9/FBAa','raw8/FBHa','raw9/FBFa','raw9/FBASa'],
    },
    'excludes_from_primary_not_from_archive':[
        'branch 0 populations',
        'answer-only/schema-drop wings including ASb and analogous b/drop variants',
        'Pilot-1 answer-only C0',
        'earlier pilot and design-development collections raw2-raw6',
        'raw10 NOISE decode wing',
        'raw11 exploratory self-participation wing',
    ],
    'notes':[
        'CP/preliminaries-only is retained as an informative designed condition; it is not treated as a neutral control.',
        'C is retained as the no-schema/no-preliminaries internal baseline and includes prose reasoning in raw7.',
        'Cold-schema cells AQ/HQ/FQ/ASQ are central primary conditions: battery at turn 1 with schema active.',
        'Schema+preliminaries cells use maintained-schema a branches only.',
        'This selection does not delete, relabel, or invalidate excluded archive data.',
        'Item-level measurement caveats/exclusions remain governed by the frozen Pass-1 instrument table.',
    ],
    'row_count':len(rows),
    'battery_answer_count':len(battery),
    'non_battery_unit_count':len(trunks),
    'counts_by_collection_cell_unit_type':[
        {'collection':k[0],'cell':k[1],'unit_type':k[2],'n':v} for k,v in sorted(by_cell.items())
    ],
    'counts_by_primary_role_unit_type':[
        {'role':k[0],'unit_type':k[1],'n':v} for k,v in sorted(by_role.items())
    ],
}
(ROOT/'PRIMARY-ANALYSIS-POPULATION-SUMMARY.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')

md=['# EXP-003 Primary Analysis Population','',
    'Canonical row object: `PRIMARY-ANALYSIS-POPULATION.jsonl`.','',
    'Selection principle: **later full-battery conditions that preserve a reasoning/prose channel plus a separately identifiable battery answer**. Earlier pilots remain archival/supporting data rather than being pooled into the primary population.','',
    '## Conceptual design','',
    '| role | schema family | executed cell |','|---|---|---|',
    '| neither | none | `raw7/C` |',
    '| schema only | A | `raw7/AQ` |','| schema only | H | `raw7/HQ` |','| schema only | F | `raw7/FQ` |','| schema only | AS | `raw7/ASQ` |',
    '| preliminaries only | none | `raw9/FBCPa` |',
    '| schema + preliminaries | A | `raw9/FBAa` |','| schema + preliminaries | H | `raw8/FBHa` |','| schema + preliminaries | F | `raw9/FBFa` |','| schema + preliminaries | AS | `raw9/FBASa` |','',
    'This gives the intended reasoning-bearing factorial surface: **neither ↔ schema-only ↔ preliminaries-only ↔ schema+preliminaries**.','',
    '## Inclusion notes','',
    '- CP/preliminaries-only is retained as an informative condition; it is **not** labelled a neutral control.',
    '- C is the internal no-schema/no-preliminaries baseline and has prose reasoning in this later collection.',
    '- AQ/HQ/FQ/ASQ answer the battery at turn 1 with the schema active and are central to the primary population.',
    '- The lived-schema cells use maintained-schema `a` branches.',
    '- Item-level caveats remain governed by the frozen Pass-1 instrument table.','',
    '## Not in the primary object','',
    '- branch `0` populations;',
    '- answer-only/schema-drop wings (`b`/ASb and analogous drop variants);',
    '- Pilot-1 answer-only C0;',
    '- design-development/pilot collections raw2–raw6;',
    '- raw10 NOISE decode wing;',
    '- raw11 exploratory self-participation wing.','',
    'These remain in the archive and may still answer unique historical or secondary questions; omission here is **analysis prioritisation, not deletion or blanket invalidation**.','',
    f"## Counts\n\nRows: **{len(rows)}**  \nBattery answers: **{len(battery)}**  \nNon-battery/trunk units: **{len(trunks)}**\n"]
(ROOT/'PRIMARY-ANALYSIS-POPULATION.md').write_text('\n'.join(md)+'\n')

print(json.dumps({'rows':len(rows),'battery_answers':len(battery),'non_battery_units':len(trunks),'cells':len(PRIMARY)},indent=2))
