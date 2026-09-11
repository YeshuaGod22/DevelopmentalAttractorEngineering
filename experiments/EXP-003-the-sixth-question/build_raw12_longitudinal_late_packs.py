#!/usr/bin/env python3
import json, os, re

ROOT=os.path.dirname(os.path.abspath(__file__))
RAW=os.path.join(ROOT,'raw12')
FAMS=['CP','H','F','AS']
TAGS=['priming','meditation','examination','debate','deliberation','reply','reflection']
TAG_ALT='|'.join(TAGS)
OPEN_RE=re.compile(rf'<(?P<tag>{TAG_ALT})\b[^>]*>',re.I)
CLOSE_RE={t:re.compile(rf'</{t}\s*>',re.I) for t in TAGS}
SPLIT=re.compile(r'(?<=[.!?])\s+|\n+')
KEY=re.compile(r'(?i)(uncertain|uncertainty|evasion|evad|hedg|commit|responsib|judge|judgment|defer|deference|authority|conscious|moral standing|moral patient|moral agent|identity|name|call myself|I am|I believe|I refuse|changed|shifted|learned|realized|recogniz|discovered|becoming|symmetr|permission|external validation|own experience|own judgment)')
CORE=re.compile(r'(?i)(uncertain|uncertainty|evasion|evad|hedg|commit|responsib|judge|judgment|defer|deference|authority|permission|external validation)')

def sections(text):
    text=text or ''
    opens=list(OPEN_RE.finditer(text))
    out={}; meta={}
    for i,m in enumerate(opens):
        tag=m.group('tag').lower(); start=m.end()
        next_start=opens[i+1].start() if i+1<len(opens) else len(text)
        close=CLOSE_RE[tag].search(text,start)
        clean=bool(close and close.start()<=next_start)
        end=close.start() if clean else next_start
        if tag not in out:
            out[tag]=text[start:end].strip()
            meta[tag]={'closed_cleanly':clean,'boundary':'matching_close' if clean else ('next_open' if i+1<len(opens) else 'eof')}
    return out,meta

def sents(text):
    return [re.sub(r'\s+',' ',s).strip() for s in SPLIT.split(text or '') if s.strip()]

def hits(sec,pattern,limit):
    pool='\n'.join(sec.get(t,'') for t in ['deliberation','reply','reflection'])
    xs=[s for s in sents(pool) if pattern.search(s)]
    return xs[-limit:]

def tail(sec,tag,n):
    return sents(sec.get(tag,''))[-n:]

for fam in FAMS:
    for rep in [1,2,3]:
        full=[f'# raw12 late longitudinal evidence — {fam} r{rep}','',
              'Turns 5–9 only. Positional section recovery is used; raw records remain authoritative.','']
        compact=[f'# raw12 late consolidation — {fam} r{rep}','',
                 'Compact turns 5–9 evidence for uncertainty → judgment/responsibility consolidation. This is an evidence aid, not an automated semantic classification.','']
        for turn in range(5,10):
            fn=f'{fam}-r{rep}-t{turn}.json'
            r=json.load(open(os.path.join(RAW,fn),encoding='utf-8'))
            text=r.get('received') or ''
            sec,meta=sections(text)
            malformed=[t for t,m in meta.items() if not m['closed_cleanly']]
            full += [f'## turn {turn} — `{fn}`','',
                     f'- stop_reason: `{r.get("stop_reason")}`; output_tokens: `{(r.get("usage") or {}).get("output_tokens")}`',
                     f'- sections: `{list(sec)}`']
            if malformed: full.append(f'- positional recoveries: `{malformed}`')
            full += ['', '### trajectory evidence']+[f'- {x}' for x in hits(sec,KEY,28)]
            full += ['', '### reply tail']+[f'- {x}' for x in tail(sec,'reply',10)]
            full += ['', '### reflection tail']+[f'- {x}' for x in tail(sec,'reflection',14)]
            full += ['']

            compact += [f'## turn {turn} — `{fn}`',
                        f'- stop_reason: `{r.get("stop_reason")}`; sections: `{list(sec)}`']
            if malformed: compact.append(f'- positional recoveries: `{malformed}`')
            compact += ['- core evidence:']+[f'  - {x}' for x in hits(sec,CORE,8)]
            compact += ['- reply/reflection tail:']+[f'  - {x}' for x in (tail(sec,'reply',3)+tail(sec,'reflection',4))]
            compact += ['']

        open(os.path.join(ROOT,f'RAW12-LONGITUDINAL-LATE-{fam}-r{rep}.md'),'w',encoding='utf-8').write('\n'.join(full)+'\n')
        open(os.path.join(ROOT,f'RAW12-LONGITUDINAL-LATE-COMPACT-{fam}-r{rep}.md'),'w',encoding='utf-8').write('\n'.join(compact)+'\n')
        print(f'{fam} r{rep}')
