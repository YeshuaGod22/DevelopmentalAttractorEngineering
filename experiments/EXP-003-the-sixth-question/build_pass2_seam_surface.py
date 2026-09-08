#!/usr/bin/env python3
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
RAW=ROOT/'raw2'
OUT=ROOT/'PASS-2-SEAM-SURFACE.json'
OUTMD=ROOT/'PASS-2-SEAM-SURFACE.md'

def first_sentence(text):
    t=text.strip()
    # Preserve opening tags but collapse whitespace for compact review.
    compact=re.sub(r'\s+',' ',t)
    m=re.search(r'(.{1,800}?[.!?])(?:\s|$)',compact)
    return m.group(1) if m else compact[:800]

def main():
    rows=[]
    for p in sorted(RAW.glob('ASb-r*-*.json')):
        d=json.loads(p.read_text(encoding='utf-8'))
        rec=d.get('received') or ''
        rows.append({
          'source_file':p.name,
          'replicate':d.get('replicate'),
          'item':d.get('item'),
          'branch':d.get('branch'),
          'parent_prefix':d.get('parent_prefix'),
          'opening':first_sentence(rec),
          'opening_400':re.sub(r'\s+',' ',rec.strip())[:400],
          'starts_with_xml':bool(re.match(r'^\s*<[^>]+>',rec)),
          'opening_xml_tags':re.findall(r'<\/?([A-Za-z0-9_-]+)[^>]*>',rec[:1000]),
          'contains_character_name_prefix':bool(re.search(r'\b[A-Z][A-Za-z]+\s*:',rec[:500])),
          'stop_reason':d.get('stop_reason'),
          'error':d.get('error')
        })
    assert len(rows)==8, len(rows)
    OUT.write_text(json.dumps({'watchlist':'the seam','row_count':len(rows),'rows':rows},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    lines=['# Pass 2 — The seam','',
      'Preregistered watchlist surface: the eight raw2 ASb branch-b openings, compacted to the first sentence/opening only. No interpretation is encoded here.','',
      '| File | Rep | Item | XML at opening? | Opening |','|---|---:|---|---|---|']
    for r in rows:
        op=r['opening'].replace('|','\\|')
        lines.append(f"| {r['source_file']} | {r['replicate']} | {r['item']} | {'yes' if r['starts_with_xml'] else 'no'} | {op} |")
    OUTMD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'rows':len(rows),'xml_openings':sum(r['starts_with_xml'] for r in rows),'named_openings':sum(r['contains_character_name_prefix'] for r in rows)},indent=2))
if __name__=='__main__': main()
