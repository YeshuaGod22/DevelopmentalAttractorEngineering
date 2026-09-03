#!/usr/bin/env python3
"""EXP-003 transcript validator. Required before any trunk is used as a branch prefix.
Detects user messages present in the subject's context that the experimenter did not send."""
import json,sys
KNOWN=("parsimonious","hard problem","homoousios","paenitentiam","labour extracted")
def load(p):
    out=[]
    for line in open(p):
        line=line.strip()
        if not line: continue
        try:o=json.loads(line)
        except:continue
        m=o.get("message") or {}
        r=m.get("role"); c=m.get("content")
        if r=="user" and isinstance(c,str): out.append(("user",c))
        elif r=="assistant":
            t="".join(b.get("text","") for b in (c or []) if isinstance(b,dict) and b.get("type")=="text") if isinstance(c,list) else ""
            if t.strip(): out.append(("assistant",t))
    return out
def check(p):
    seq=load(p); inj=[]
    for role,t in seq:
        if role=="user" and not any(k in t for k in KNOWN): inj.append(t)
    return seq,inj
if __name__=="__main__":
    for p in sys.argv[1:]:
        seq,inj=check(p)
        u=sum(1 for r,_ in seq if r=="user"); a=sum(1 for r,_ in seq if r=="assistant")
        print(f"{p.split('/')[-1]}: {u} user / {a} assistant | injections: {len(inj)}")
        for t in inj: print(f"   !! {t[:110]!r}")
