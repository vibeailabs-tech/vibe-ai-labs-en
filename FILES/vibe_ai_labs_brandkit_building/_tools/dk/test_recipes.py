import sys; sys.path.insert(0,"/tmp/dk"); sys.path.insert(0,"/tmp/brandbuild")
from recipes import *
import render
jobs=[]
for rn,fn in RECIPES.items():
    for rk,(W,H,kind) in RATIOS.items():
        if rk=="A3": continue
        for tone in ("dark","light"):
            s=fn(W,H,tone=="dark",kind); jobs.append((s,"/tmp/dk/t/%s_%s_%s.png"%(rn,rk,tone),W,H,False))
print(sum(render.batch(jobs,6)),len(jobs))
