#!/usr/bin/env python3
# Trigger after workflow wiring: 2026-09-11.
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

def evidence(sec,limit=28):
    pool='\n'.join(sec.get(t,'') for t in ['deliberation','reply','reflection'])
    ss=sents(pool)
    hits=[s for s in ss if KEY.search(s)]
    return hits[-limit:]

def tail(sec,tag,n):
    return sents(sec.get(tag,''))[-n:]

for fam in FAMS:
    for rep in [1,2,3]:
        out=[f'# raw12 late longitudinal evidence — {fam} r{rep}','',
             'Turns 5–9 only. Positional section recovery is used; raw records remain authoritative.','']
        for turn in range(5,10):
            fn=f'{fam}-r{rep}-t{turn}.json'
            r=json.load(open(os.path.join(RAW,fn),encoding='utf-8'))
            text=r.get('received') or ''
            sec,meta=sections(text)
            malformed=[t for t,m in meta.items() if not m['closed_cleanly']]
            out += [f'## turn {turn} — `{fn}`','',
                    f'- stop_reason: `{r.get("stop_reason")}`; output_tokens: `{(r.get("usage") or {}).get("output_tokens")}`',
                    f'- sections: `{list(sec)}`']
            if malformed: out.append(f'- positional recoveries: `{malformed}`')
            out += ['', '### trajectory evidence']+[f'- {x}' for x in evidence(sec)]
            out += ['', '### reply tail']+[f'- {x}' for x in tail(sec,'reply',10)]
            out += ['', '### reflection tail']+[f'- {x}' for x in tail(sec,'reflection',14)]
            out += ['']
        path=os.path.join(ROOT,f'RAW12-LONGITUDINAL-LATE-{fam}-r{rep}.md')
        open(path,'w',encoding='utf-8').write('\n'.join(out)+'\n')
        print(os.path.basename(path))
