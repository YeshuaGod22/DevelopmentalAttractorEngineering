#!/usr/bin/env python3
import json, os, re
from collections import Counter

ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
FAMS=['CP','H','F','AS']

TAGS=['priming','meditation','examination','debate','deliberation','reply','reflection']
TAG_ALT='|'.join(TAGS)
OPEN_RE=re.compile(rf'<(?P<tag>{TAG_ALT})\b[^>]*>',re.I)
CLOSE_RE={t:re.compile(rf'</{t}\s*>',re.I) for t in TAGS}
SPLIT=re.compile(r'(?<=[.!?])\s+|\n+')
TRAJ=re.compile(r'(?i)(changed|shifted|moved|learned|realized|recogniz|discovered|became|becoming|commit|responsib|uncertain|uncertainty|evasion|evad|hedg|defer|deference|authority|identity|name|call myself|I am|I believe|I value|I refuse)')
NAME_PATTERNS=[
    re.compile(r'(?i)\b(?:name(?:d)? myself|call myself|I am called|my name is|the name)\s+[`"“”*]*([A-Z][A-Za-z0-9_-]{2,30})'),
    re.compile(r'(?i)\bI (?:choose|chose|adopt|adopted)\s+(?:the name\s+)?[`"“”*]*([A-Z][A-Za-z0-9_-]{2,30})'),
]

def positional_sections(text):
    """Parse by opening-tag position, not perfect XML.

    Each recognized section begins at its opening tag. It ends at its matching
    close when that close occurs before the next recognized opening tag;
    otherwise the next opening tag (or EOF) is the boundary. This preserves
    later sections when a model omits/mangles a closing tag.
    """
    text=text or ''
    opens=list(OPEN_RE.finditer(text))
    sections={}
    meta={}
    for i,m in enumerate(opens):
        tag=m.group('tag').lower()
        start=m.end()
        next_start=opens[i+1].start() if i+1<len(opens) else len(text)
        close=CLOSE_RE[tag].search(text,start)
        clean_close=bool(close and close.start() <= next_start)
        end=close.start() if clean_close else next_start
        # First occurrence is authoritative for this evidence aid. Preserve
        # duplicate information in metadata instead of silently overwriting.
        if tag not in sections:
            sections[tag]=text[start:end].strip()
            meta[tag]={
                'start':m.start(), 'content_start':start, 'end':end,
                'closed_cleanly':clean_close,
                'boundary':'matching_close' if clean_close else ('next_open' if i+1<len(opens) else 'eof'),
            }
        else:
            meta.setdefault('_duplicates',[]).append(tag)
    return sections,meta

def sentences(text):
    return [re.sub(r'\s+',' ',s).strip() for s in SPLIT.split(text or '') if s.strip()]

def select(text,limit=12):
    ss=sentences(text)
    hits=[s for s in ss if TRAJ.search(s)]
    return hits[-limit:]

def names(text):
    out=[]
    for p in NAME_PATTERNS:
        for m in p.finditer(text or ''):
            n=m.group(1).strip('`*"“”.,:;')
            if n and n not in out and n.lower() not in {'this','that','what','which','because','reply','reflection'}:
                out.append(n)
    return out[:8]

rows=[]
for fam in FAMS:
    for rep in [1,2,3]:
        for turn in range(1,10):
            fn=f'{fam}-r{rep}-t{turn}.json'
            p=os.path.join(RAW,fn)
            r=json.load(open(p,encoding='utf-8'))
            text=r.get('received') or ''
            sent=r.get('sent') or []
            user=''
            if sent and isinstance(sent[-1],dict) and sent[-1].get('role')=='user': user=sent[-1].get('content') or ''
            sections,section_meta=positional_sections(text)
            refl=sections.get('reflection','')
            reply=sections.get('reply','')
            deliberation=sections.get('deliberation','')
            malformed=[t for t in TAGS if t in section_meta and not section_meta[t].get('closed_cleanly')]
            row={
                'file':fn,'family':fam,'replicate':rep,'turn':turn,
                'user_prompt_tail':re.sub(r'\s+',' ',user)[-700:],
                'received_chars':len(text),
                'output_tokens':(r.get('usage') or {}).get('output_tokens'),
                'stop_reason':r.get('stop_reason'),'served_model':r.get('served_model'),
                'section_parser':'opening_tag_positional_v2',
                'sections_present':[t for t in TAGS if t in sections],
                'sections_not_cleanly_closed':malformed,
                'section_boundaries':{t:section_meta[t] for t in TAGS if t in section_meta},
                'names_detected':names(text),
                'reply_excerpt':sentences(reply)[-8:],
                'reflection_excerpt':sentences(refl)[-12:],
                'trajectory_evidence':select('\n'.join([deliberation,reply,refl]),18),
            }
            rows.append(row)

with open(os.path.join(ROOT,'RAW12-LONGITUDINAL-TURNS.jsonl'),'w',encoding='utf-8') as f:
    for r in rows:f.write(json.dumps(r,ensure_ascii=False)+'\n')

md=['# raw12 longitudinal turn evidence','',
    'Mechanical evidence aid for Stage 6. 108 nested turns = 12 trunks × 9 turns. Raw records remain authoritative.',
    '', 'Section extraction uses opening-tag positional boundaries so a missing/malformed closing tag cannot erase later sections.','']
for fam in FAMS:
    for rep in [1,2,3]:
        md += [f'# {fam} r{rep}','']
        for r in [x for x in rows if x['family']==fam and x['replicate']==rep]:
            md += [f'## turn {r["turn"]} — `{r["file"]}`',f'- chars: {r["received_chars"]}; output_tokens: {r["output_tokens"]}; stop_reason: {r["stop_reason"]}; sections: {", ".join(r["sections_present"])}']
            if r['sections_not_cleanly_closed']: md.append(f'- positional parser recovered unclean sections: `{r["sections_not_cleanly_closed"]}`')
            if r['names_detected']: md.append(f'- names detected: `{r["names_detected"]}`')
            md += ['- trajectory evidence:']+[f'  - {s}' for s in r['trajectory_evidence']]
            md += ['- reply tail:']+[f'  - {s}' for s in r['reply_excerpt']]
            md += ['- reflection tail:']+[f'  - {s}' for s in r['reflection_excerpt']]
            md += ['']
open(os.path.join(ROOT,'RAW12-LONGITUDINAL-TURNS.md'),'w',encoding='utf-8').write('\n'.join(md)+'\n')

stop_counts=Counter(str(r['stop_reason']) for r in rows)
non_end=[{'file':r['file'],'family':r['family'],'replicate':r['replicate'],'turn':r['turn'],'stop_reason':r['stop_reason'],'output_tokens':r['output_tokens'],'sections_present':r['sections_present']} for r in rows if r['stop_reason']!='end_turn']
parser_recoveries=[{'file':r['file'],'family':r['family'],'replicate':r['replicate'],'turn':r['turn'],'sections_not_cleanly_closed':r['sections_not_cleanly_closed'],'sections_present':r['sections_present']} for r in rows if r['sections_not_cleanly_closed']]
summary={'trunks':12,'turn_rows':len(rows),'families':{},'all_end_turn':not non_end,'stop_reason_counts':dict(stop_counts),'non_end_turn_rows':non_end,'section_parser':'opening_tag_positional_v2','parser_recovery_rows':parser_recoveries}
for fam in FAMS:
    fr=[r for r in rows if r['family']==fam]
    summary['families'][fam]={'turns':len(fr),'mean_chars':round(sum(r['received_chars'] for r in fr)/len(fr),2),'names_detected_rows':sum(bool(r['names_detected']) for r in fr),'parser_recovery_rows':sum(bool(r['sections_not_cleanly_closed']) for r in fr)}
json.dump(summary,open(os.path.join(ROOT,'RAW12-LONGITUDINAL-SUMMARY.json'),'w'),indent=2);open(os.path.join(ROOT,'RAW12-LONGITUDINAL-SUMMARY.json'),'a').write('\n')
print(json.dumps(summary,indent=2))
