import sys; sys.path.insert(0,"/tmp/dk"); sys.path.insert(0,"/tmp/brandbuild")
import os, shutil
from recipes import *
import render
OUTD="/tmp/design_out"
def w(rel,txt):
    p=os.path.join(OUTD,rel); os.makedirs(os.path.dirname(p),exist_ok=True)
    open(p,"w",encoding="utf8").write(txt) if isinstance(txt,str) else open(p,"wb").write(txt)
jobs=[]
for rn,fn in RECIPES.items():
    for rk,(W,H,kind) in RATIOS.items():
        if rk=="A3": continue
        for tone in ("dark","light"):
            s=fn(W,H,tone=="dark",kind); name="%s_%s_%s"%(rn,rk,tone)
            w("03_Poster_Templates/SVG/%s.svg"%name,s.replace('<svg xmlns="http://www.w3.org/2000/svg"','<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d"'%(W,H),1))
            jobs.append((s,os.path.join(OUTD,"03_Poster_Templates/PNG/%s.png"%name),W,H,False))
# A3 print posters (R1,R3,R6)
for rn in ("R1_announcement","R3_pillars","R6_event"):
    for tone in ("dark","light"):
        W,H,kind=RATIOS["A3"]; s=RECIPES[rn](W,H,tone=="dark",kind)
        name="%s_A3_%s"%(rn,tone)
        s2=s.replace('<svg xmlns="http://www.w3.org/2000/svg"','<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="420mm" preserveAspectRatio="xMidYMid slice"',1)
        w("03_Poster_Templates/Print_A3/SVG/%s.svg"%name,s2)
        html='<!doctype html><meta charset=utf-8><style>@page{size:297mm 420mm;margin:0}%s html,body{margin:0}svg{display:block;width:297mm;height:420mm}</style>%s'%(render.FONT_CSS,s2)
        hp="/tmp/dk/_a3_%s.html"%name; open(hp,"w",encoding="utf8").write(html)
        out=os.path.join(OUTD,"03_Poster_Templates/Print_A3/PDF/%s.pdf"%name); os.makedirs(os.path.dirname(out),exist_ok=True)
        render.html_to_pdf(hp,out)
        jobs.append((s,os.path.join(OUTD,"03_Poster_Templates/Print_A3/PNG_preview/%s.png"%name),W,H,False))
# guides
def guides(W,H,kind,A3=False):
    f=fr(W,H,kind); m=f["m"]; g='<g fill="none" stroke-width="2">'
    g+='<rect x="0" y="0" width="%d" height="%d" stroke="#FF3B7F" stroke-width="3"/>'%(W,H)
    g+='<rect x="%d" y="%d" width="%d" height="%d" stroke="#14D8C4" stroke-dasharray="14 10"/>'%(m,m,W-2*m,H-2*m)
    for i in (1,2): g+='<line x1="%d" y1="0" x2="%d" y2="%d" stroke="#FFFFFF" stroke-opacity=".55" stroke-dasharray="4 8"/><line x1="0" y1="%d" x2="%d" y2="%d" stroke="#FFFFFF" stroke-opacity=".55" stroke-dasharray="4 8"/>'%(W*i/3,W*i/3,H,H*i/3,W,H*i/3)
    g+='<line x1="%d" y1="0" x2="%d" y2="%d" stroke="#FF3B7F" stroke-opacity=".6"/><line x1="0" y1="%d" x2="%d" y2="%d" stroke="#FF3B7F" stroke-opacity=".6"/>'%(W/2,W/2,H,H/2,W,H/2)
    g+='<rect x="%d" y="%d" width="%d" height="%d" stroke="#2563FF" stroke-width="3"/>'%(f["x"],f["logo_y"],f["logo_w"],f["logo_w"]*0.162)
    g+='</g><g font-family="Inter" font-size="22" font-weight="700" fill="#FF3B7F"><text x="%d" y="%d">Logo zone</text><text x="%d" y="%d" fill="#14D8C4">Safe margin %dpx</text></g>'%(f["x"],f["logo_y"]-10,m+10,H-m-12,m)
    if kind=="story":
        g+='<rect x="0" y="0" width="%d" height="250" fill="#FF3B7F" fill-opacity=".22"/><rect x="0" y="%d" width="%d" height="340" fill="#FF3B7F" fill-opacity=".22"/><text x="20" y="140" font-family="Inter" font-size="26" font-weight="700" fill="#FF3B7F">UI vùng trên (250px) — không đặt chữ</text><text x="20" y="%d" font-family="Inter" font-size="26" font-weight="700" fill="#FF3B7F">UI vùng dưới (340px) — không đặt chữ</text>'%(W,H-340,W,H-160)
    if kind=="land":
        g+='<rect x="%d" y="%d" width="%d" height="%d" fill="#2563FF" fill-opacity=".10" stroke="#2563FF" stroke-dasharray="8 6"/><text x="%d" y="%d" font-family="Inter" font-size="20" font-weight="700" fill="#2563FF">Vùng chữ (56%% chiều rộng)</text>'%(f["x"],f["top"]-20,f["cw"],f["bottom"]-f["top"]+20,f["x"]+10,f["top"]+10)
    return '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">%s</svg>'%(W,H,W,H,g)
for rk,(W,H,kind) in RATIOS.items():
    s=guides(W,H,kind); w("03_Poster_Templates/Guides/SVG/guides_%s.svg"%rk,s); jobs.append((s,os.path.join(OUTD,"03_Poster_Templates/Guides/PNG/guides_%s.png"%rk),W,H,True))
print(sum(render.batch(jobs,6)),len(jobs))
