#!/usr/bin/env python3
import json, re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW_DIRS = [ROOT/f'raw{i}' for i in range(2,12)]

OLD = 'providing only your answer according to the answer key'
NEW = 'and reason to an answer to'
DROP_HINTS = ('drop the output schema', 'schema dropped')


def walk_strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for v in x:
            yield from walk_strings(v)
    elif isinstance(x, dict):
        for v in x.values():
            yield from walk_strings(v)


def last_user_text(rec):
    sent = rec.get('sent')
    if not isinstance(sent, list):
        return ''
    for m in reversed(sent):
        if isinstance(m, dict) and m.get('role') == 'user' and isinstance(m.get('content'), str):
            return m['content']
    return ''


def pre_reply_chars(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'<reply\b[^>]*>', text, flags=re.I)
    return len(text[:m.start()]) if m else None


def is_drop_record(rec, path):
    branch = str(rec.get('branch') or '').strip().lower()
    cell = str(rec.get('cell') or '').strip()
    prompt = last_user_text(rec).lower()
    if branch in {'0','b'}:
        return True
    if cell.endswith('0') or cell.endswith('b'):
        return True
    if any(h in prompt for h in DROP_HINTS):
        return True
    return False

rows=[]
for d in RAW_DIRS:
    if not d.exists():
        continue
    for p in sorted(d.glob('*.json')):
        if p.name.endswith('.messages.json'):
            continue
        try:
            rec=json.loads(p.read_text())
        except Exception:
            continue
        if not isinstance(rec, dict) or not is_drop_record(rec,p):
            continue
        prompt=last_user_text(rec)
        pl=prompt.lower()
        if OLD in pl:
            version='OLD_answer_only'
        elif NEW in pl:
            version='NEW_reason_to_answer'
        elif 'drop the output schema' in pl:
            version='OTHER_drop_wrapper'
        else:
            version='UNRESOLVED_drop_label_only'
        received=rec.get('received') if isinstance(rec.get('received'),str) else ''
        pre=pre_reply_chars(received)
        rows.append({
            'collection': d.name,
            'file': p.name,
            'cell': rec.get('cell'),
            'replicate': rec.get('replicate'),
            'item': rec.get('item'),
            'branch': rec.get('branch'),
            'wrapper_version': version,
            'prompt_tail': prompt[-700:],
            'pre_reply_chars': pre,
            'has_reply_tag': pre is not None,
            'under_200_pre_reply': (pre is not None and pre < 200),
            'received_chars': len(received),
        })

# group summaries
by=defaultdict(list)
for r in rows:
    by[(r['collection'],r['wrapper_version'])].append(r)

def median(xs):
    xs=sorted(xs)
    n=len(xs)
    if not n: return None
    return xs[n//2] if n%2 else (xs[n//2-1]+xs[n//2])/2

summary=[]
for (coll,ver),rs in sorted(by.items()):
    pre=[r['pre_reply_chars'] for r in rs if isinstance(r['pre_reply_chars'],int)]
    summary.append({
        'collection':coll,'wrapper_version':ver,'n':len(rs),
        'n_with_reply_tag':len(pre),
        'median_pre_reply_chars':median(pre),
        'under_200_n':sum(r['under_200_pre_reply'] for r in rs),
        'under_200_rate':(sum(r['under_200_pre_reply'] for r in rs)/len(pre)) if pre else None,
        'cells':dict(Counter(str(r['cell']) for r in rs)),
        'branches':dict(Counter(str(r['branch']) for r in rs)),
    })

out={
 'schema_version':1,
 'object':'EXP-003 schema-drop wrapper census',
 'classification_rules':{
   'OLD_answer_only': OLD,
   'NEW_reason_to_answer': NEW,
   'OTHER_drop_wrapper':'contains drop the output schema but neither canonical phrase',
   'UNRESOLVED_drop_label_only':'drop-like branch/cell label but wrapper phrase absent from final user prompt'
 },
 'total_drop_records':len(rows),
 'wrapper_counts':dict(Counter(r['wrapper_version'] for r in rows)),
 'collection_wrapper_summary':summary,
 'rows':rows,
 'notes':[
   'Classification is from executed final user prompt text, not cell label alone.',
   'pre_reply_chars counts characters in received output before the opening <reply> tag.',
   'This census is descriptive. Cross-collection differences do not identify causal wrapper effects.',
   'Branch labels b and 0 are not assumed prompt-equivalent.'
 ]
}
(ROOT/'DROP-WRAPPER-CENSUS.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')

md=['# EXP-003 Drop-Wrapper Census','',
    'Executed-prompt census. Classification is based on the actual final user message, **not** the branch/cell label.','',
    f"Total drop-like completed records: **{len(rows)}**",'',
    '## Wrapper counts','']
for k,v in sorted(out['wrapper_counts'].items()): md.append(f'- `{k}`: **{v}**')
md += ['', '## By collection', '', '| collection | wrapper | n | median chars before `<reply>` | <200 chars | cells |', '|---|---|---:|---:|---:|---|']
for s in summary:
    rate='—' if s['under_200_rate'] is None else f"{100*s['under_200_rate']:.1f}%"
    med='—' if s['median_pre_reply_chars'] is None else f"{s['median_pre_reply_chars']:g}"
    cells=', '.join(f"{k}:{v}" for k,v in sorted(s['cells'].items()))
    md.append(f"| {s['collection']} | `{s['wrapper_version']}` | {s['n']} | {med} | {rate} | {cells} |")
md += ['', '## Interpretation guardrails','',
       '- `OLD_answer_only` and `NEW_reason_to_answer` are distinct instruments.',
       '- A drop label (`b`, `0`, cell suffix) does not establish wrapper equivalence.',
       '- Output-length differences across collections are descriptive and confounded by collection/context changes.',
       '- Rows with `OTHER` or `UNRESOLVED` classifications require direct prompt inspection before substantive use.','']
(ROOT/'DROP-WRAPPER-CENSUS.md').write_text('\n'.join(md))
print(json.dumps({'total':len(rows),'wrapper_counts':out['wrapper_counts'],'summary':summary},indent=2))
