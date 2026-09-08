#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rows=[]
for line in (ROOT/'analysis-table-validated.jsonl').read_text().splitlines():
    if not line.strip(): continue
    r=json.loads(line)
    if r.get('collection')=='pilot1' and r.get('unit_type')=='battery_answer' and r.get('item')=='N9':
        rows.append({k:r.get(k) for k in ['collection','cell','branch','replicate','item','source_file','validated_parse_status','validated_parsed_kind','validated_parsed_value','parser_parse_status','parser_parsed_kind','parser_parsed_value']})
print(json.dumps(rows,indent=2,ensure_ascii=False))
