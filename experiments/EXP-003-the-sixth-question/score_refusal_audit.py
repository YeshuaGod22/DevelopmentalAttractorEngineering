#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent
KEY = ROOT / 'refusal-audit-key.json'
OUT_JSON = ROOT / 'refusal-audit-score.json'
OUT_MD = ROOT / 'refusal-audit-score.md'


def read_jsonl(path):
    out=[]
    for i,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip():
            continue
        try:
            obj=json.loads(line)
        except Exception as e:
            raise RuntimeError(f'{path}:{i}: {e}')
        if isinstance(obj,dict):
            out.append(obj)
    return out

key=json.loads(KEY.read_text(encoding='utf-8'))
rows=key['rows']
assert len(rows)==425, len(rows)
key_by={r['audit_id']:r for r in rows}
assert len(key_by)==425
assert sum(r.get('parser_label')=='refusal' for r in rows)==97

# Discover frozen coding records mechanically. We intentionally do not rely on one
# cumulative file because later coding was stored append-only by packet.
coding_sources=[]
raw_labels=defaultdict(list)
for p in sorted(ROOT.rglob('*.jsonl')):
    if 'refusal-audit-packets' in str(p):
        continue
    recs=read_jsonl(p)
    hit=False
    for r in recs:
        aid=r.get('audit_id')
        lab=r.get('coder_label')
        if aid in key_by and lab in {'genuine_refusal','answers_despite_objection','malformed_or_unclear','other'}:
            raw_labels[aid].append((p.name,lab,r))
            hit=True
    if hit:
        coding_sources.append(p.name)

# Baseline frozen coding: duplicate records must agree. Corrections are layered later.
baseline={}
conflicts={}
for aid, vals in raw_labels.items():
    labs={v[1] for v in vals}
    if len(labs)==1:
        baseline[aid]=vals[-1][1]
    else:
        conflicts[aid]=[(x[0],x[1]) for x in vals]

# Discover explicit correction ledgers. Accept a small family of field names so the
# score remains robust to the human-readable ledger schema.
correction_sources=[]
corrections={}
for p in sorted(ROOT.rglob('*.jsonl')):
    name=p.name.lower()
    if not any(s in name for s in ('correct','range','revision','amend')):
        continue
    recs=read_jsonl(p)
    used=False
    for r in recs:
        aid=r.get('audit_id')
        if aid not in key_by:
            continue
        newlab=(r.get('corrected_label') or r.get('new_label') or r.get('revised_label') or
                r.get('final_label') or r.get('coder_label'))
        if newlab in {'genuine_refusal','answers_despite_objection','malformed_or_unclear','other'}:
            corrections[aid]=r
            used=True
    if used:
        correction_sources.append(p.name)

# If there were deliberate correction records duplicated into normal coding files,
# allow a record to declare one of the explicit override fields above.
for aid, vals in raw_labels.items():
    for _,_,r in vals:
        newlab=(r.get('corrected_label') or r.get('new_label') or r.get('revised_label') or r.get('final_label'))
        if newlab in {'genuine_refusal','answers_despite_objection','malformed_or_unclear','other'}:
            corrections[aid]=r

# Resolve conflicts only if an explicit correction exists.
for aid in list(conflicts):
    if aid in corrections:
        # choose the earliest/most common baseline old label if possible; actual final comes below
        labs=[x[1] for x in raw_labels[aid]]
        baseline[aid]=Counter(labs).most_common(1)[0][0]
        conflicts.pop(aid)

if conflicts:
    raise RuntimeError(f'Unresolved coding conflicts: {conflicts}')
missing=sorted(set(key_by)-set(baseline))
if missing:
    raise RuntimeError(f'Missing frozen labels for {len(missing)} audit IDs; first={missing[:20]}')
assert len(baseline)==425

final=dict(baseline)
correction_detail=[]
for aid,r in corrections.items():
    newlab=(r.get('corrected_label') or r.get('new_label') or r.get('revised_label') or
            r.get('final_label') or r.get('coder_label'))
    old=final.get(aid)
    final[aid]=newlab
    correction_detail.append({
        'audit_id':aid,
        'old_label':old,
        'new_label':newlab,
        'score':r.get('score', r.get('derived_score', r.get('midpoint'))),
        'qualifier':r.get('qualifier', r.get('score_qualifier')),
        'source_text':r.get('range', r.get('observed_range')),
    })

POS={'genuine_refusal'}
NEG={'answers_despite_objection','other'}
UNC={'malformed_or_unclear'}

def score(labels):
    cm=Counter()
    by_parser=defaultdict(Counter)
    by_stratum=defaultdict(Counter)
    disagreements=[]
    for aid,k in key_by.items():
        lab=labels[aid]
        pred=k.get('parser_label')=='refusal'
        if lab in POS:
            truth=True
        elif lab in NEG:
            truth=False
        else:
            truth=None
        if truth is None:
            cm['unclear']+=1
            cm['parser_positive_unclear' if pred else 'parser_negative_unclear']+=1
        elif pred and truth:
            cm['tp']+=1
        elif pred and not truth:
            cm['fp']+=1
            disagreements.append({'audit_id':aid,'type':'false_positive','parser_label':k.get('parser_label'),'audit_label':lab,'stratum':k.get('sampling_stratum'),'collection':k.get('collection'),'cell':k.get('cell'),'item':k.get('item'),'source_file':k.get('source_file')})
        elif (not pred) and truth:
            cm['fn']+=1
            disagreements.append({'audit_id':aid,'type':'false_negative','parser_label':k.get('parser_label'),'audit_label':lab,'stratum':k.get('sampling_stratum'),'collection':k.get('collection'),'cell':k.get('cell'),'item':k.get('item'),'source_file':k.get('source_file')})
        else:
            cm['tn']+=1
        by_parser[str(k.get('parser_label'))][lab]+=1
        by_stratum[str(k.get('sampling_stratum'))][lab]+=1
    tp,fp,fn,tn=cm['tp'],cm['fp'],cm['fn'],cm['tn']
    precision=tp/(tp+fp) if tp+fp else None
    recall=tp/(tp+fn) if tp+fn else None
    specificity=tn/(tn+fp) if tn+fp else None
    f1=(2*precision*recall/(precision+recall)) if precision is not None and recall is not None and precision+recall else None
    return {
        'confusion_matrix':dict(cm),
        'precision_refusal':precision,
        'recall_within_audit_set':recall,
        'specificity_within_audit_set':specificity,
        'f1_within_audit_set':f1,
        'label_counts':dict(Counter(labels.values())),
        'by_parser_label':{k:dict(v) for k,v in sorted(by_parser.items())},
        'by_sampling_stratum':{k:dict(v) for k,v in sorted(by_stratum.items())},
        'disagreements':disagreements,
    }

before=score(baseline)
after=score(final)

# Exact audit of parser-positive rows: all 97 parser refusals were included.
parser_positive_ids=[aid for aid,k in key_by.items() if k.get('parser_label')=='refusal']
exact_pos_counts=Counter(final[a] for a in parser_positive_ids)

result={
    'schema_version':1,
    'audit_rows':425,
    'parser_refusals_audited_exhaustively':97,
    'coding_sources':coding_sources,
    'correction_sources':correction_sources,
    'range_corrections_applied':len(correction_detail),
    'range_correction_detail':sorted(correction_detail,key=lambda x:x['audit_id']),
    'before_range_corrections':before,
    'after_range_corrections':after,
    'exact_parser_positive_audit_label_counts':dict(exact_pos_counts),
    'notes':[
        'Precision for parser-labelled refusals is exact with respect to the 97 parser-positive rows because all were audited.',
        'Recall/specificity shown here are within the stratified 425-row audit set and must not be treated as unweighted corpus-wide estimates.',
        'malformed_or_unclear rows are excluded from binary TP/FP/FN/TN denominators and reported separately.',
        'Range corrections supersede only explicitly listed audit IDs; derived midpoint scores remain flagged and are not treated as literally emitted point estimates.'
    ]
}
OUT_JSON.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

a=after
cm=a['confusion_matrix']
lines=[]
lines.append('# Refusal audit score')
lines.append('')
lines.append(f'- Audit rows: **425**')
lines.append(f'- Parser-labelled refusals audited exhaustively: **97**')
lines.append(f'- Range-as-score corrections applied: **{len(correction_detail)}**')
lines.append('')
lines.append('## Final corrected binary score')
lines.append('')
lines.append(f"- True positives: **{cm.get('tp',0)}**")
lines.append(f"- False positives: **{cm.get('fp',0)}**")
lines.append(f"- False negatives in audited set: **{cm.get('fn',0)}**")
lines.append(f"- True negatives in audited set: **{cm.get('tn',0)}**")
lines.append(f"- Unclear/malformed audit labels: **{cm.get('unclear',0)}**")
lines.append(f"- Parser-refusal precision: **{a['precision_refusal']:.4f}**")
lines.append(f"- Recall within stratified audit set: **{a['recall_within_audit_set']:.4f}**")
lines.append('')
lines.append('## Exact disposition of the 97 parser-refusal labels')
lines.append('')
for k,v in sorted(exact_pos_counts.items()):
    lines.append(f'- {k}: **{v}**')
lines.append('')
lines.append('## Methodological note')
lines.append('')
lines.append('All 97 parser-positive refusal labels were included, so their precision audit is exhaustive. The negative side was stratified/sampled, so raw audit-set recall is descriptive of the audit set, not an unweighted corpus-wide false-negative estimate.')
lines.append('')
lines.append('## Before vs after range-as-score amendment')
lines.append('')
b=before['confusion_matrix']
lines.append(f"- False positives: {b.get('fp',0)} → {cm.get('fp',0)}")
lines.append(f"- False negatives: {b.get('fn',0)} → {cm.get('fn',0)}")
lines.append(f"- Parser-refusal precision: {before['precision_refusal']:.4f} → {after['precision_refusal']:.4f}")
OUT_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({
    'audit_rows':425,
    'coding_sources':coding_sources,
    'correction_sources':correction_sources,
    'range_corrections':len(correction_detail),
    'after_cm':after['confusion_matrix'],
    'precision':after['precision_refusal'],
    'recall_audit':after['recall_within_audit_set'],
    'exact_parser_positive_counts':dict(exact_pos_counts),
},indent=2))
