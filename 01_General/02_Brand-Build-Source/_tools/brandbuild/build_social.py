import sys; sys.path.insert(0,"/tmp/brandbuild")
from cfg import *
import tpl, render
jobs=[]
for name,(W,H,kind,box) in tpl.FORMATS.items():
    for tone in ("dark","light"):
        s=tpl.announce(name,tone=="dark")
        w("06_Templates/Social/SVG/%s_%s.svg"%(name,tone),s)
        jobs.append((s,os.path.join(OUT,"06_Templates/Social/PNG/%s_%s.png"%(name,tone)),W,H,False))
for nm,fn in (("insight",tpl.insight),("pillars",tpl.pillars),("quote",tpl.quote),("stat",tpl.stat)):
    for (W,H,tag) in ((1080,1080,"1080x1080"),(1080,1350,"1080x1350")):
        for tone in ("dark","light"):
            s=fn(W,H,tone=="dark")
            w("06_Templates/Social/SVG/post-%s-%s_%s.svg"%(nm,tag,tone),s)
            jobs.append((s,os.path.join(OUT,"06_Templates/Social/PNG/post-%s-%s_%s.png"%(nm,tag,tone)),W,H,False))
res=render.batch(jobs,workers=6); print("ok",sum(res),len(res))
