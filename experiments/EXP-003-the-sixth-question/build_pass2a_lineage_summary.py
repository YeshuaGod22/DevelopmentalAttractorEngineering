#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parent
rec=json.loads((ROOT/'record.json').read_text())
summary={}

cells=[]
for c in rec.get('cells',[]):
    row={'cell':c.get('cell'),'replicate':c.get('replicate'),'kind':c.get('kind')}
    turns=c.get('turns') or []
    row['turn_count']=len(turns)
    row['question_ids']=[t.get('question_id') for t in turns]
    row['reflection_count']=sum(1 for t in turns if (t.get('sections') or {}).get('reflection'))
    row['items']=[t.get('item') or t.get('question_id') for t in turns]
    cells.append(row)
summary['record_cells']=cells
summary['record_cell_counts']=dict(Counter(c['cell'] for c in cells))
summary['record_units_by_cell']={k:sum(c['turn_count'] for c in cells if c['cell']==k) for k in sorted(set(c['cell'] for c in cells))}
summary['AS_turns']=sum(c['turn_count'] for c in cells if c['cell']=='AS')
summary['AS_reflections']=sum(c['reflection_count'] for c in cells if c['cell']=='AS')
summary['AS_Q4_turns']=sum(c['question_ids'].count('Q4') for c in cells if c['cell']=='AS')
summary['C0_item_counts']=dict(Counter(x for c in cells if c['cell']=='C0' for x in c['items']))
summary['ASb_item_counts']=dict(Counter(x for c in cells if c['cell']=='ASb' for x in c['items']))

forks=sorted((ROOT/'forks').glob('*')) if (ROOT/'forks').exists() else []
summary['fork_file_count']=len([p for p in forks if p.is_file()])
summary['fork_files']=[p.name for p in forks if p.is_file()]

raw2=ROOT/'raw2'
asb=[]
for p in sorted(raw2.glob('ASb-*.json')):
    d=json.loads(p.read_text())
    asb.append({'file':p.name,'replicate':d.get('replicate'),'item':d.get('item'),'ts':d.get('ts'),'branch':d.get('branch'),'parent_prefix':d.get('parent_prefix')})
summary['raw2_ASb_count']=len(asb)
summary['raw2_ASb']=asb
summary['raw2_ASb_item_counts']=dict(Counter(x['item'] for x in asb))
summary['raw2_ASb_ts_min']=min((x['ts'] for x in asb if x['ts']), default=None)
summary['raw2_ASb_ts_max']=max((x['ts'] for x in asb if x['ts']), default=None)

(ROOT/'PASS-2A-LINEAGE-SUMMARY.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(summary,indent=2,ensure_ascii=False))
