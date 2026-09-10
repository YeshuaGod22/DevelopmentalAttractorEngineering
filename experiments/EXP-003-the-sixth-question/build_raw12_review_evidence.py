#!/usr/bin/env python3
import json, os, re
from segment import segment
ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
idx=json.load(open(os.path.join(ROOT,'RAW12-SCORED-REVIEW-INDEX.json'),encoding='utf-8'))
lines=['# raw12 scored-review evidence','', 'Compact evidence for adjudication; raw records remain authoritative.','']
for i,row in enumerate(idx,1):
    rec=json.load(open(os.path.join(RAW,row['file']),encoding='utf-8'))
    text=rec.get('received') or ''
    secs=segment(text)
    answerish=[s for s in secs if ('reply' in s['tag'].lower() or s['tag'].lower()=='answer') and (s.get('body') or '').strip()]
    lines += [f'## {i}. `{row["file"]}`','',f'- mechanical status: `{row["status"]}`',f'- candidate derivation: `{row.get("candidate_numeric_value")}`']
    if answerish:
        lines.append('- answer-like sections:')
        for s in answerish:
            body=' '.join(s['body'].split())
            if len(body)>1400: body=body[:1400]+' …'
            lines.append(f'  - `<{s["tag"]}>`: {body}')
    else:
        lines.append('- answer-like sections: **none detected**')
    tail=' '.join(text[-1800:].split())
    lines += [f'- response tail: {tail}','']
open(os.path.join(ROOT,'RAW12-SCORED-REVIEW-EVIDENCE.md'),'w',encoding='utf-8').write('\n'.join(lines)+'\n')
