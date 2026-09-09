#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'analysis-table-validated.jsonl'
PROPS=ROOT/'PROMPT-PROPERTIES.jsonl'

# Join executed prompt properties to validated analysis rows by collection + source filename.
props={}
for line in PROPS.read_text().splitlines():
    if not line.strip(): continue
    p=json.loads(line)
    props[(p.get('collection'),p.get('file'))]=p

rows=[]
for line in SOURCE.read_text().splitlines():
    if not line.strip(): continue
    r=json.loads(line)
    if r.get('unit_type')!='battery_answer': continue
    p=props.get((r.get('collection'),r.get('source_file')))
    if not p or not p.get('property_primary'): continue
    rr=dict(r)
    rr['primary_population']=True
    rr['primary_population_basis']='executed_prompt_properties_pre_outcome'
    rr['primary_role']=p.get('factorial_role')
    rr['primary_schema_family']=p.get('schema_family')
    rr['primary_schema_present']=p.get('schema_present_at_battery')
    rr['primary_preliminaries_lived']=p.get('preliminaries_lived')
    rr['primary_reasoning_channel_available']=p.get('reasoning_channel_available')
    rr['primary_reasoning_requested']=p.get('reasoning_requested')
    rr['primary_reasoning_inherited']=p.get('reasoning_inherited')
    rr['primary_reasoning_observed']=p.get('reasoning_observed')
    rr['primary_strict_answer_only']=p.get('strict_answer_only')
    rows.append(rr)

rows.sort(key=lambda r:(str(r.get('collection')),str(r.get('cell')),str(r.get('replicate')),str(r.get('item')),str(r.get('source_file'))))
(ROOT/'PRIMARY-ANALYSIS-POPULATION.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))

by_cell=Counter((r.get('collection'),r.get('cell')) for r in rows)
by_role=Counter(r.get('primary_role') for r in rows)
concept=Counter((r.get('primary_role'),r.get('primary_schema_family')) for r in rows)
summary={
 'schema_version':2,
 'object':'EXP-003 primary analysis population',
 'source':'analysis-table-validated.jsonl + PROMPT-PROPERTIES.jsonl',
 'selection_basis':'pre-outcome executed prompt properties',
 'membership_rule':{
   'full_battery_items':25,
   'minimum_replicates':3,
   'allowed_factorial_roles':['neither','schema_only','preliminaries_only','schema_plus_preliminaries'],
   'strict_answer_only':False,
   'reasoning_channel_available_for_all_rows':True,
   'outcome_dependent_gates':False
 },
 'notes':[
   'Membership is derived from executed prompt/prefix properties rather than a hard-coded cell allowlist.',
   'Observed prose, refusal, answer value, and parse success do not determine membership.',
   'CP is retained as preliminaries-only; it is not labelled a neutral control.',
   'Validated parsing and refusal coding travel with the included rows for downstream analyses but do not select the sample.',
   'Pass-1 item-level validity/measurement statuses remain a separate analysis layer.'
 ],
 'row_count':len(rows),
 'battery_answer_count':len(rows),
 'counts_by_collection_cell':[{'collection':k[0],'cell':k[1],'n':v} for k,v in sorted(by_cell.items())],
 'counts_by_primary_role':[{'role':k,'n':v} for k,v in sorted(by_role.items(),key=lambda kv:str(kv[0]))],
 'counts_by_role_schema':[{'role':k[0],'schema_family':k[1],'n':v} for k,v in sorted(concept.items(),key=lambda kv:(str(kv[0][0]),str(kv[0][1])))],
}
(ROOT/'PRIMARY-ANALYSIS-POPULATION-SUMMARY.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')

md=['# EXP-003 Primary Analysis Population','',
    'Canonical row object: `PRIMARY-ANALYSIS-POPULATION.jsonl`.','',
    'This population is now selected from **executed prompt properties**, not from a hand-written cell allowlist.','',
    '## Membership rule','',
    '- all 25 battery items represented in the condition;',
    '- at least 3 replicates;',
    '- factorial role is `neither`, `schema_only`, `preliminaries_only`, or `schema_plus_preliminaries`;',
    '- OLD `providing only your answer` wrapper absent;',
    '- a reasoning channel is available by prompt/prefix design for every row;',
    '- **no outcome-dependent gate**: refusal, prose length, parse success, and answer value do not determine membership.','',
    '## Selected groups','',
    '| collection | cell | role | schema | n |','|---|---|---|---|---:|']
# derive group metadata from first row per group
seen={}
for r in rows:
    seen.setdefault((r['collection'],r['cell']),r)
for (c,cell),r in sorted(seen.items()):
    md.append(f"| {c} | `{cell}` | {r.get('primary_role')} | {r.get('primary_schema_family')} | {by_cell[(c,cell)]} |")
md += ['', f'Rows: **{len(rows)}**','',
       'CP/preliminaries-only remains included as an informative condition, not a neutral control. Pass-1 item qualifications remain separate from population membership.','']
(ROOT/'PRIMARY-ANALYSIS-POPULATION.md').write_text('\n'.join(md))
print(json.dumps({'rows':len(rows),'groups':len(by_cell),'roles':dict(by_role)},indent=2))
