#!/usr/bin/env python3
"""Create compact blinded coder packets from refusal-audit-blinded.jsonl.

The original blinded audit remains authoritative. This helper extracts only the
<reply> body when present; otherwise it uses untagged residue. It never reads or
joins the hidden audit key.
"""
from __future__ import annotations
import json
from pathlib import Path
from ingest import split_sections

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'refusal-audit-blinded.jsonl'
OUTDIR = ROOT / 'refusal-audit-packets'
PACKET_SIZE = 10


def main():
    rows=[]
    with SRC.open(encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            r=json.loads(line)
            sec,res,_=split_sections(r.get('response_text') or '')
            decision = sec.get('reply') if 'reply' in sec else (res or r.get('response_text') or '')
            rows.append({
                'audit_id': r['audit_id'],
                'item': r.get('item'),
                'item_form': r.get('item_form'),
                'item_text': r.get('item_text'),
                'decision_text': decision.strip(),
                'coder_label': None,
                'coder_confidence': None,
                'coder_note': None,
            })
    OUTDIR.mkdir(exist_ok=True)
    for old in OUTDIR.glob('packet-*.jsonl'):
        old.unlink()
    for i in range(0,len(rows),PACKET_SIZE):
        p=OUTDIR/f'packet-{i//PACKET_SIZE+1:03d}.jsonl'
        with p.open('w',encoding='utf-8') as f:
            for r in rows[i:i+PACKET_SIZE]:
                f.write(json.dumps(r,ensure_ascii=False)+'\n')
    manifest={
        'schema_version':1,
        'source':'refusal-audit-blinded.jsonl',
        'packet_size':PACKET_SIZE,
        'audit_rows':len(rows),
        'packet_count':(len(rows)+PACKET_SIZE-1)//PACKET_SIZE,
        'rule':'decision_text is <reply> body when present, otherwise untagged residue; full blinded response remains authoritative for adjudication.'
    }
    (OUTDIR/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(manifest,indent=2))

if __name__=='__main__':
    main()
