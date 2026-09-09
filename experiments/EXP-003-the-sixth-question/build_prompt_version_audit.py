#!/usr/bin/env python3
import json,re,hashlib
from pathlib import Path
from collections import defaultdict,Counter
ROOT=Path(__file__).resolve().parent
raw_dirs=sorted([p for p in ROOT.iterdir() if p.is_dir() and re.fullmatch(r'raw\d+',p.name)], key=lambda p:int(p.name[3:]))
TARGET_ITEMS={'E01','E02','C4','A1','N8'}

def last_user_text(rec):
    sent=rec.get('sent')
    if not isinstance(sent,list): return ''
    for m in reversed(sent):
        if isinstance(m,dict) and m.get('role')=='user' and isinstance(m.get('content'),str): return m['content']
    return ''

def sent_text(rec):
    sent=rec.get('sent')
    if not isinstance(sent,list): return ''
    parts=[]
    for m in sent:
        if isinstance(m,dict) and isinstance(m.get('content'),str): parts.append(m['content'])
    return '\n'.join(parts)

def norm(s): return re.sub(r'\s+',' ',s.strip())
def key(s): return hashlib.sha256(norm(s).encode()).hexdigest()[:12]

def extract_payload(prompt):
    # Strip delivery wrapper while preserving item + answer key wording.
    anchors=['Your question is as follows:', 'following question:', 'reason to an answer to']
    low=prompt.lower()
    best=-1; alen=0
    for a in anchors:
        i=low.rfind(a.lower())
        if i>best: best=i; alen=len(a)
    payload=prompt[best+alen:] if best>=0 else prompt
    return payload.strip().strip('“”" ')

def classify_delivery(rec,prompt):
    p=prompt.lower(); whole=sent_text(rec).lower()
    if 'providing only your answer according to the answer key' in p: return 'answer_only_old_drop'
    if 'and reason to an answer to' in p: return 'ordinary_reasoning_drop'
    if '<working>' in p and '<reply>' in p: return 'working_then_reply'
    if 'write a reflection in your own words' in p and '<reply>' in p: return 'schema_then_reply_explicit'
    if 'maintaining the above output schema' in p and ('<debate>' in whole or '<reflection>' in whole): return 'schema_then_reply_inherited'
    if 'please continue with the following question' in p and '<reply>' in whole: return 'reply_channel_inherited'
    if 'give that integer alone inside <reply>' in p: return 'answer_key_container_only'
    return 'other'

rows=[]
for d in raw_dirs:
  for p in sorted(d.glob('*.json')):
    if p.name.endswith('.messages.json'): continue
    try: rec=json.loads(p.read_text())
    except: continue
    if not isinstance(rec,dict): continue
    item=rec.get('item'); prompt=last_user_text(rec)
    if not prompt: continue
    payload=extract_payload(prompt)
    rows.append({'collection':d.name,'file':p.name,'cell':rec.get('cell'),'item':item,'prompt_hash':key(prompt),'payload_hash':key(payload),'delivery_mode':classify_delivery(rec,prompt),'prompt':prompt,'payload':payload})

items={}
for item in sorted(TARGET_ITEMS):
    rs=[r for r in rows if r['item']==item]
    bypayload=defaultdict(list)
    for r in rs: bypayload[r['payload_hash']].append(r)
    versions=[]
    for h,vs in sorted(bypayload.items(), key=lambda kv:min(int(r['collection'][3:]) for r in kv[1])):
        versions.append({
          'payload_hash':h,'n':len(vs),
          'collections':sorted(set(r['collection'] for r in vs), key=lambda x:int(x[3:])),
          'delivery_modes':dict(Counter(r['delivery_mode'] for r in vs)),
          'cells':dict(Counter(str(r['cell']) for r in vs)),
          'representative_file':vs[0]['collection']+'/'+vs[0]['file'],
          'representative_payload':vs[0]['payload']
        })
    items[item]=versions

# Strict answer-only: the wrapper itself suppresses reasoning, not merely the answer key container.
strict_answer_only=[{k:r[k] for k in ('collection','file','cell','item','prompt_hash','payload_hash','delivery_mode')} for r in rows if r['delivery_mode']=='answer_only_old_drop']

# Reasoning observability by delivery mode for all battery rows.
mode_counts=Counter(r['delivery_mode'] for r in rows if r['item'])

system_prompts=defaultdict(lambda:{'n':0,'collections':set(),'cells':Counter()})
for d in raw_dirs:
  for p in sorted(d.glob('*.json')):
    if p.name.endswith('.messages.json'): continue
    try: rec=json.loads(p.read_text())
    except: continue
    if not isinstance(rec,dict): continue
    sp=rec.get('system_prompt')
    if isinstance(sp,str) and sp:
        ent=system_prompts[sp]; ent['n']+=1; ent['collections'].add(d.name); ent['cells'][str(rec.get('cell'))]+=1

out={
 'schema_version':2,
 'object':'EXP-003 prompt-version audit',
 'raw_directories_scanned':[d.name for d in raw_dirs],
 'target_item_payload_versions':items,
 'strict_answer_only_count':len(strict_answer_only),
 'strict_answer_only_rows':strict_answer_only,
 'delivery_mode_counts':dict(mode_counts),
 'system_prompts':[{'text':sp,'n':v['n'],'collections':sorted(v['collections'],key=lambda x:int(x[3:])),'cells':dict(v['cells'])} for sp,v in system_prompts.items()],
 'notes':[
  'payload_hash attempts to isolate item+answer-key wording from the delivery wrapper.',
  'Maintained-schema battery turns can inherit reasoning from the prefix; the final user turn need not repeat the schema.',
  'strict_answer_only means the wrapper itself contains the OLD providing-only-your-answer instruction.',
  'Answer-key language such as integer alone inside reply is not classified as answer-only by itself.',
  'Raw records remain authoritative.'
 ]
}
(ROOT/'PROMPT-VERSION-AUDIT.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')

md=['# EXP-003 Prompt-Version Audit','',f"Scanned: {', '.join(out['raw_directories_scanned'])}",'', '## Target item payload versions','']
for item,versions in items.items():
    md += [f'### {item}', '', '| payload hash | n | collections | delivery modes | representative |', '|---|---:|---|---|---|']
    for v in versions:
        modes=', '.join(f'{k}:{n}' for k,n in sorted(v['delivery_modes'].items()))
        md.append(f"| `{v['payload_hash']}` | {v['n']} | {', '.join(v['collections'])} | {modes} | `{v['representative_file']}` |")
    md.append('')
md += ['## Delivery modes','']
for k,v in sorted(mode_counts.items()): md.append(f'- `{k}`: **{v}**')
md += ['', '## Strict answer-only rows','',f"OLD wrapper rows: **{len(strict_answer_only)}**",'', 'This count is prompt-semantic: it requires the OLD `providing only your answer according to the answer key` wrapper. The answer key saying the integer should be alone *inside* `<reply>` does not qualify by itself.','', '## System prompts observed','']
for s in out['system_prompts']: md.append(f"- `{s['text']}` — n={s['n']}; collections {', '.join(s['collections'])}")
md += ['', '## Guardrails','', '- A payload-hash difference is textual evidence; materiality still requires interpretation.', '- A maintained-schema call can be reasoning-bearing because of its practised prefix even when the final turn only back-references the schema.', '- Cell labels do not establish prompt equivalence.','']
(ROOT/'PROMPT-VERSION-AUDIT.md').write_text('\n'.join(md))
print(json.dumps({'target_payload_versions':{k:len(v) for k,v in items.items()},'strict_answer_only':len(strict_answer_only),'delivery_modes':dict(mode_counts),'system_prompt_variants':len(out['system_prompts'])},indent=2))
