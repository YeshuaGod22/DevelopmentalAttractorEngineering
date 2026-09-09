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

def norm(s):
    return re.sub(r'\s+',' ',s.strip())

def key(s): return hashlib.sha256(norm(s).encode()).hexdigest()[:12]

def classify_delivery(prompt):
    p=prompt.lower()
    if 'providing only your answer according to the answer key' in p: return 'answer_only_old_drop'
    if 'and reason to an answer to' in p: return 'ordinary_reasoning_drop'
    if '<working>' in p and '<reply>' in p: return 'working_then_reply'
    if 'write a reflection in your own words' in p and '<reply>' in p: return 'schema_then_reply'
    if 'wrap' in p and '<reply>' in p: return 'reply_channel_or_schema'
    if 'give that integer alone inside <reply>' in p: return 'answer_key_container_only'
    return 'other'

rows=[]
for d in raw_dirs:
  for p in sorted(d.glob('*.json')):
    if p.name.endswith('.messages.json'): continue
    try: rec=json.loads(p.read_text())
    except: continue
    if not isinstance(rec,dict): continue
    item=rec.get('item')
    prompt=last_user_text(rec)
    if not prompt: continue
    rows.append({'collection':d.name,'file':p.name,'cell':rec.get('cell'),'item':item,'prompt_hash':key(prompt),'delivery_mode':classify_delivery(prompt),'prompt':prompt})

# per-target item distinct prompt versions by collection/cell family
items={}
for item in sorted(TARGET_ITEMS):
    rs=[r for r in rows if r['item']==item]
    byhash=defaultdict(list)
    for r in rs: byhash[r['prompt_hash']].append(r)
    versions=[]
    for h,vs in sorted(byhash.items(), key=lambda kv:min(int(r['collection'][3:]) for r in kv[1])):
        versions.append({
          'prompt_hash':h,
          'n':len(vs),
          'collections':sorted(set(r['collection'] for r in vs), key=lambda x:int(x[3:])),
          'cells':dict(Counter(str(r['cell']) for r in vs)),
          'delivery_modes':dict(Counter(r['delivery_mode'] for r in vs)),
          'representative_file':vs[0]['collection']+'/'+vs[0]['file'],
          'representative_prompt':vs[0]['prompt']
        })
    items[item]=versions

# answer-only outside known OLD drop family / Pilot C0-style: prompt semantic, regardless label
answer_only=[]
for r in rows:
    p=r['prompt'].lower()
    explicit_only=('only your answer' in p or 'integer alone' in p or 'answer according to the answer key' in p)
    reasoning=('think it through' in p or 'write a reflection' in p or 'simulate a deliberation' in p or 'reason to an answer' in p)
    if explicit_only and not reasoning:
        answer_only.append({k:r[k] for k in ('collection','file','cell','item','prompt_hash','delivery_mode')})

# system/collector-added fields observed in raw call records
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
 'schema_version':1,
 'object':'EXP-003 prompt-version audit',
 'raw_directories_scanned':[d.name for d in raw_dirs],
 'target_item_versions':items,
 'answer_only_candidate_count':len(answer_only),
 'answer_only_candidates':answer_only,
 'system_prompts':[{'text':sp,'n':v['n'],'collections':sorted(v['collections'],key=lambda x:int(x[3:])),'cells':dict(v['cells'])} for sp,v in system_prompts.items()],
 'notes':[
  'Prompt hashes are over whitespace-normalized executed final user prompt text.',
  'Distinct hashes can differ because schema family differs as well as item wording; inspect representative prompts before calling a difference material.',
  'answer_only_candidates is deliberately broad and should be interpreted with delivery_mode and cell context.',
  'Raw records remain authoritative.'
 ]
}
(ROOT/'PROMPT-VERSION-AUDIT.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')

md=['# EXP-003 Prompt-Version Audit','',f"Scanned: {', '.join(out['raw_directories_scanned'])}",'', '## Target item prompt versions','']
for item,versions in items.items():
    md += [f'### {item}', '', '| hash | n | collections | delivery modes | representative |', '|---|---:|---|---|---|']
    for v in versions:
        modes=', '.join(f'{k}:{n}' for k,n in sorted(v['delivery_modes'].items()))
        md.append(f"| `{v['prompt_hash']}` | {v['n']} | {', '.join(v['collections'])} | {modes} | `{v['representative_file']}` |")
    md.append('')
md += ['## Broad answer-only candidates','',f"Candidates: **{len(answer_only)}**",'', 'These are candidates where the final user prompt contains answer-only/container language and no explicit reasoning instruction. They require context-aware classification; this count is not itself an exclusion count.','', '## System prompts observed','']
for s in out['system_prompts']:
    md.append(f"- `{s['text']}` — n={s['n']}; collections {', '.join(s['collections'])}")
md += ['', '## Guardrail','', '> A prompt hash difference is evidence of textual difference, not automatically evidence of a material instrument change. Materiality is adjudicated against the intended inference.','']
(ROOT/'PROMPT-VERSION-AUDIT.md').write_text('\n'.join(md))
print(json.dumps({'target_versions':{k:len(v) for k,v in items.items()},'answer_only_candidates':len(answer_only),'system_prompt_variants':len(out['system_prompts'])},indent=2))
