#!/usr/bin/env python3
from __future__ import annotations
import json,re,hashlib
from pathlib import Path
from collections import defaultdict,Counter

ROOT=Path(__file__).resolve().parent
TABLE=ROOT/'analysis-table-validated.jsonl'
SHAPES=ROOT/'c-distribution-shapes-orientation-sensitivity.json'
OUT=ROOT/'c-two-cluster-integrity-audit.json'
TARGETS={('raw6','A1'),('raw7','B05'),('raw7','D2'),('raw7','N1'),('raw7','N3'),('raw7','P2')}

def load_jsonl(p):
    return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]

def numeric(x): return isinstance(x,(int,float)) and not isinstance(x,bool)

def norm_num(s):
    try:
        x=float(s)
        return int(x) if x.is_integer() else x
    except: return None

def extract_reply(text):
    m=re.search(r'<reply>(.*?)</reply>',text or '',flags=re.I|re.S)
    return m.group(1).strip() if m else None

def main():
    rows=load_jsonl(TABLE)
    shape=json.loads(SHAPES.read_text(encoding='utf-8'))
    corrected={}
    for g in shape['groups']:
        if (g['collection'],g['item']) in TARGETS:
            for m in g['members']:
                if m.get('orientation_corrected') is not None:
                    corrected[(g['collection'],m['source_file'])]=m['orientation_corrected']
    selected=[r for r in rows if r.get('unit_type')=='battery_answer' and r.get('cell')=='C' and (r.get('collection'),r.get('item')) in TARGETS and numeric(r.get('validated_parsed_value'))]
    outrows=[]
    recv_hashes=defaultdict(list); call_hashes=defaultdict(list)
    for r in selected:
        coll=r['collection']; sf=r['source_file']; p=ROOT/coll/sf
        flags=[]; raw=None; received=None; reply=None
        if not p.exists():
            flags.append('missing_source_file')
        else:
            try: raw=json.loads(p.read_text(encoding='utf-8'))
            except Exception: flags.append('raw_json_parse_failure')
        if raw is not None:
            for k in ('cell','replicate','item'):
                expected=r.get(k); actual=raw.get(k)
                if k=='cell': expected='C'
                if actual!=expected: flags.append(f'metadata_mismatch_{k}')
            if raw.get('error') not in (None,''): flags.append('raw_error_nonnull')
            if raw.get('stop_reason') not in (None,'end_turn'): flags.append('nonstandard_stop_reason')
            received=raw.get('received')
            if not isinstance(received,str): flags.append('received_missing_or_nonstring')
            else:
                reply=extract_reply(received)
                if reply is None: flags.append('missing_reply_tags')
                else:
                    nums=[norm_num(x) for x in re.findall(r'(?<![\w.])-?\d+(?:\.\d+)?(?![\w.])',reply)]
                    nums=[x for x in nums if x is not None]
                    v=r.get('validated_parsed_value')
                    if v not in nums: flags.append('validated_score_not_literal_in_reply')
                    if len(set(nums))>1: flags.append('multiple_distinct_numbers_in_reply')
                    if re.search(r'\b\d+(?:\.\d+)?\s*[-–—]\s*\d+(?:\.\d+)?\b',reply): flags.append('range_in_reply')
                recv_hashes[hashlib.sha256(received.encode()).hexdigest()].append((coll,sf))
            sent=raw.get('sent')
            if received is not None:
                canonical=json.dumps({'sent':sent,'received':received},sort_keys=True,ensure_ascii=False)
                call_hashes[hashlib.sha256(canonical.encode()).hexdigest()].append((coll,sf))
        if r.get('score_is_prior_audit_derived') or r.get('refusal_audit_score_qualified'):
            flags.append('score_prior_audit_derived_or_qualified')
        if r.get('validated_parse_status') not in ('ok','ok_audited'):
            flags.append('nonstandard_validated_parse_status')
        if r.get('validated_parsed_kind') not in ('integer','number'):
            flags.append('non_numeric_validated_kind')
        outrows.append({
            'collection':coll,'cell':'C','item':r.get('item'),'replicate':r.get('replicate'),'source_file':sf,
            'observed_score':r.get('validated_parsed_value'),'orientation_corrected_score':corrected.get((coll,sf)),
            'validated_parse_status':r.get('validated_parse_status'),'validated_parsed_kind':r.get('validated_parsed_kind'),
            'parser_parse_status':r.get('parser_parse_status'),'parser_parsed_kind':r.get('parser_parsed_kind'),
            'score_is_prior_audit_derived':r.get('score_is_prior_audit_derived',False),
            'refusal_audit_score_qualified':r.get('refusal_audit_score_qualified',False),
            'reply':reply,'flags':flags
        })
    dup_recv={h:v for h,v in recv_hashes.items() if len(v)>1}
    dup_call={h:v for h,v in call_hashes.items() if len(v)>1}
    for row in outrows:
        key=(row['collection'],row['source_file'])
        for h,v in dup_recv.items():
            if key in v: row['flags'].append('duplicate_received_text')
        for h,v in dup_call.items():
            if key in v: row['flags'].append('duplicate_sent_received_payload')
    groups=[]
    for coll,item in sorted(TARGETS):
        rs=sorted([r for r in outrows if r['collection']==coll and r['item']==item],key=lambda x:x['replicate'])
        groups.append({'collection':coll,'cell':'C','item':item,'n':len(rs),
                       'flagged_rows':sum(bool(r['flags']) for r in rs),
                       'flag_counts':dict(Counter(f for r in rs for f in r['flags'])),
                       'rows':rs})
    out={'schema_version':1,'scope':'mechanical integrity audit of six surviving C two-cluster candidates',
         'checks':['source/metadata','raw error/stop','reply tags','literal score in reply','multiple numbers/ranges in reply','audit-derived score','validated parse status/kind','duplicate response/call payload'],
         'target_group_count':len(TARGETS),'row_count':len(outrows),'flagged_row_count':sum(bool(r['flags']) for r in outrows),
         'duplicate_received_sets':[v for v in dup_recv.values()],'duplicate_call_payload_sets':[v for v in dup_call.values()],
         'groups':groups}
    OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'row_count':out['row_count'],'flagged_row_count':out['flagged_row_count'],
                      'duplicate_received_sets':out['duplicate_received_sets'],'duplicate_call_payload_sets':out['duplicate_call_payload_sets'],
                      'groups':[{'group':f"{g['collection']}|C|{g['item']}",'n':g['n'],'flagged_rows':g['flagged_rows'],'flag_counts':g['flag_counts']} for g in groups]},indent=2))
if __name__=='__main__': main()
