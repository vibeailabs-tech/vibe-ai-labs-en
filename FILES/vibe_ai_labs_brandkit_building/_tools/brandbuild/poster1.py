import sys; sys.path.insert(0,"/tmp/brandbuild")
from cfg import *
import tpl, gfx, logo, render
from tpl import T, grad_def, wrap_svg, C, HF, BF, icon_g, pill
W=H=1080; m=86
def poster(dark):
    fg="#FFFFFF" if dark else C["midnight"]; sub="#D9E2F2" if dark else C["slate"]
    if dark: d,b=gfx.ribbon(W,H,True,cx=0.80,cy=0.95,wr=1.25,opacity=0.7,uid="pr")
    else: d,b=gfx.ribbon(W,H,False,cx=0.80,cy=0.95,wr=1.25,opacity=0.20,uid="pr")
    defs=d; body=b
    lg=logo.horizontal_parts("reversed" if dark else "color","lg",False); ld,lb,lw,lh=logo.place(lg,m,m,width=360); defs+=ld; body+=lb
    gid="gh"; defs+=grad_def(gid,m,0,m+800,0,"#5B8CFF" if dark else "#2563FF","#14D8C4")
    body+=T(m,372,"Ba năng lực.",124,800,fg,HF,ls=-3.5)+T(m,500,"Một hệ thống.",124,800,"url(#gh)",HF,ls=-3.5)
    cw=273; gap=44; y=612; ch=200
    cards=[("growth","Marketing",C["blue"]),("ai","AI",C["green"]),("design","Creative",C["orange"])]
    for i,(ic,t,col) in enumerate(cards):
        x=m+i*(cw+gap)
        if dark: body+='<rect x="%d" y="%d" width="%d" height="%d" rx="32" fill="#0B1026" fill-opacity=".72" stroke="#FFFFFF" stroke-opacity=".22"/>'%(x,y,cw,ch)
        else: body+='<rect x="%d" y="%d" width="%d" height="%d" rx="32" fill="#FFFFFF" stroke="#D9E2F2"/>'%(x,y,cw,ch)
        body+='<rect x="%d" y="%d" width="76" height="76" rx="22" fill="%s" fill-opacity="%s"/>'%(x+28,y+28,col,".22" if dark else ".14")
        body+=icon_g(ic,x+28+16,y+28+16,44,col if not dark else {"#2563FF":"#7DA2FF","#16A34A":"#4ADE80","#F97316":"#FDBA74"}[col],1.8)
        body+=T(x+28,y+158,t,36,800,fg,HF)
        body+='<rect x="%d" y="%d" width="46" height="5" rx="2.5" fill="%s"/>'%(x+28,y+ch-24,col)
        if i<2: body+=T(x+cw+gap/2,y+ch/2+14,"×",36,700,C["aqua"] if dark else C["blue"],HF,"middle")
    pb,pw,ph=pill(m,892,"Nhắn tin cho chúng tôi",28); body+=pb
    return wrap_svg(W,H,defs,body)
os.makedirs("/Users/henryle/Desktop/vibe_ai_labs/posts",exist_ok=True)
for tone in ("dark","light"):
    s=poster(tone=="dark")
    base="/Users/henryle/Desktop/vibe_ai_labs/posts/facebook-poster_marketing-ai-creative_1080x1080_%s"%tone
    open(base+".svg","w",encoding="utf8").write(s)
    print(render.svg_to_png(s,base+".png",1080,1080,False))
