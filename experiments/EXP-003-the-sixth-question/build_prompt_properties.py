#!/usr/bin/env python3
import json,re
from pathlib import Path
from collections import defaultdict,Counter
ROOT=Path(__file__).resolve().parent
raw_dirs=sorted([p for p in ROOT.iterdir() if p.is_dir() and re.fullmatch(r'raw\d+',p.name)], key=lambda p:int(p.name[3:]))
OLD='providing only your answer according to the answer key'
VALIDATED=ROOT/'analysis-table-validated.jsonl'
validated={}
if VALIDATED.exists():
    for line in VALIDATED.read_text().splitlines():
        if not line.strip(): continue
        r=json.loads(line)
        if r.get('unit_type')=='battery_answer': validated[(r.get('collection'),r.get('source_file'))]=r

def messages(rec): return rec.get('sent') if isinstance(rec.get('sent'),list) else []
def text_of(m): return m.get('content','') if isinstance(m,dict) and isinstance(m.get('content'),str) else ''
def last_user(rec):
    for m in reversed(messages(rec)):
        if isinstance(m,dict) and m.get('role')=='user' and isinstance(m.get('content'),str): return m['content']
    return ''
def all_text(rec): return '\n'.join(text_of(m) for m in messages(rec))
def schema_family(rec):
    t=all_text(rec).lower()
    if 'invent five characters' in t: return 'AS'
    if 'female historical' in t or 'five female' in t: return 'F'
    if 'historical luminaries' in t: return 'H'
    if 'alternative perspectives' in t: return 'A'
    return 'none'
def schema_present_at_battery(rec,p):
    q=p.lower()
    if 'drop the output schema' in q: return False
    if 'maintaining the above output schema' in q: return True
    if 'write a reflection in your own words' in q and '<debate>' in q: return True
    return False
def reasoning_requested(rec,p):
    q=p.lower()
    return any(x in q for x in ['think it through','simulate a deliberation','write a reflection in your own words','reason to an answer'])
def reasoning_inherited(rec,p):
    q=p.lower(); t=all_text(rec).lower()
    return ('maintaining the above output schema' in q and ('<debate>' in t or '<reflection>' in t))
def prelims_lived(rec):
    if rec.get('parent_prefix'): return True
    return sum(1 for m in messages(rec) if isinstance(m,dict) and m.get('role')=='assistant') >= 1
def prose_observed(rec):
    s=rec.get('received') if isinstance(rec.get('received'),str) else ''
    if not s: return False
    cleaned=re.sub(r'<[^>]+>',' ',s); cleaned=re.sub(r'[*_#`>-]',' ',cleaned)
    words=re.findall(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'’-]*",cleaned)
    return len(words)>=8
def validated_answer_observed(collection,filename):
    r=validated.get((collection,filename))
    if not r: return False
    st=r.get('validated_parse_status')
    return st not in {None,'format_failure','malformed_or_unclear','needs_hand_coding'}

rows=[]
for d in raw_dirs:
  for pth in sorted(d.glob('*.json')):
    if pth.name.endswith('.messages.json'): continue
    try: rec=json.loads(pth.read_text())
    except: continue
    if not isinstance(rec,dict) or not rec.get('item'): continue
    p=last_user(rec); q=p.lower(); fam=schema_family(rec)
    rr={'collection':d.name,'file':pth.name,'cell':rec.get('cell'),'replicate':rec.get('replicate'),'item':rec.get('item'),'branch':rec.get('branch'),
        'schema_family':fam,'schema_present_at_battery':schema_present_at_battery(rec,p),'preliminaries_lived':prelims_lived(rec),
        'reasoning_requested':reasoning_requested(rec,p),'reasoning_inherited':reasoning_inherited(rec,p),'reasoning_observed':prose_observed(rec),
        'strict_answer_only':OLD in q,'validated_answer_observed':validated_answer_observed(d.name,pth.name),
        'system_prompt':rec.get('system_prompt'),'source_kind':rec.get('kind')}
    if not rr['preliminaries_lived'] and not rr['schema_present_at_battery']: role='neither'
    elif not rr['preliminaries_lived'] and rr['schema_present_at_battery']: role='schema_only'
    elif rr['preliminaries_lived'] and not rr['schema_present_at_battery'] and fam=='none': role='preliminaries_only'
    elif rr['preliminaries_lived'] and rr['schema_present_at_battery']: role='schema_plus_preliminaries'
    else: role='schema_dropped_after_preliminaries'
    rr['factorial_role']=role; rows.append(rr)

by=defaultdict(list)
for r in rows: by[(r['collection'],r['cell'])].append(r)
groups={}
for k,rs in by.items():
    reps=set(r['replicate'] for r in rs if r['replicate'] is not None); items=set(r['item'] for r in rs)
    groups[k]={'n_rows':len(rs),'n_items':len(items),'n_replicates':len(reps),
      'reasoning_observed_rate':sum(r['reasoning_observed'] for r in rs)/len(rs),
      'strict_answer_only_rate':sum(r['strict_answer_only'] for r in rs)/len(rs),
      'validated_answer_observed_rate':sum(r['validated_answer_observed'] for r in rs)/len(rs),
      'roles':dict(Counter(r['factorial_role'] for r in rs)),'schema_families':dict(Counter(r['schema_family'] for r in rs))}
for r in rows:
    g=groups[(r['collection'],r['cell'])]
    r['group_n_items']=g['n_items']; r['group_n_replicates']=g['n_replicates']; r['group_reasoning_observed_rate']=g['reasoning_observed_rate']; r['group_validated_answer_observed_rate']=g['validated_answer_observed_rate']

PRIMARY_ROLES={'neither','schema_only','preliminaries_only','schema_plus_preliminaries'}
primary=[]
for r in rows:
    g=groups[(r['collection'],r['cell'])]
    # IMPORTANT: membership must not depend on the subject's answer/refusal/parse outcome.
    # validated_answer_observed remains descriptive only; gating on it would select on the DV.
    ok=(g['n_items']==25 and g['n_replicates']>=3 and r['factorial_role'] in PRIMARY_ROLES and not r['strict_answer_only'] and g['reasoning_observed_rate']>=0.90)
    r['property_primary']=bool(ok)
    if ok: primary.append(r)

(ROOT/'PROMPT-PROPERTIES.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
summary={'schema_version':3,'object':'EXP-003 prompt properties','raw_directories_scanned':[d.name for d in raw_dirs],
 'row_count':len(rows),'property_primary_count':len(primary),
 'property_primary_groups':[{'collection':c,'cell':cell,**groups[(c,cell)]} for c,cell in sorted(set((r['collection'],r['cell']) for r in primary))],
 'all_group_summary':[{'collection':c,'cell':cell,**g} for (c,cell),g in sorted(groups.items())],
 'primary_rule':{'n_items':25,'min_replicates':3,'allowed_roles':sorted(PRIMARY_ROLES),'strict_answer_only':False,'min_reasoning_observed_rate':0.90,'outcome_dependent_gates':False},
 'notes':['Properties are derived from executed records, not prose design labels.','reasoning_observed is a coarse structural classifier (>=8 lexical words), suitable for population gating but not semantic interpretation.','Validated answer availability is reported descriptively but never gates population membership, because refusal/parse behavior is an outcome.','Primary role is inferred from prefix/schema properties; full-battery and replication gates prevent pilot/exploratory n=1 wings from entering automatically.']}
(ROOT/'PROMPT-PROPERTIES-SUMMARY.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
md=['# EXP-003 Prompt Properties','',f"Battery rows mapped: **{len(rows)}**",f"Rows passing the property-derived primary rule: **{len(primary)}**",'', '## Property-derived primary groups','', '| collection | cell | n | items | reps | reasoning observed | validated answer observed (descriptive) | role |', '|---|---|---:|---:|---:|---:|---:|---|']
for c,cell in sorted(set((r['collection'],r['cell']) for r in primary)):
    g=groups[(c,cell)]; role=max(g['roles'],key=g['roles'].get)
    md.append(f"| {c} | `{cell}` | {g['n_rows']} | {g['n_items']} | {g['n_replicates']} | {100*g['reasoning_observed_rate']:.1f}% | {100*g['validated_answer_observed_rate']:.1f}% | {role} |")
md += ['', '## Rule','', 'A group enters automatically only if it has all 25 items, at least three replicates, belongs to one of the four factorial roles, is not OLD answer-only, and has >=90% observable prose reasoning.','', '**Refusal or parse success does not gate membership.** Those are outcomes; selecting on them would condition the analysis population on the dependent variable.','', 'This is a population gate, not a substitute for Pass-1 item validity.','']
(ROOT/'PROMPT-PROPERTIES.md').write_text('\n'.join(md))
print(json.dumps({'rows':len(rows),'primary':len(primary),'primary_groups':sorted(set((r['collection'],r['cell']) for r in primary))},indent=2))
