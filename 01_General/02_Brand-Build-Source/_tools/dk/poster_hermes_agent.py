import sys,math; sys.path.insert(0,"/tmp/dk"); sys.path.insert(0,"/tmp/brandbuild")
from recipes import *
import render,base64
LOGO="data:image/png;base64,"+base64.b64encode(open("/Users/henryle/Desktop/vibe_ai_labs/_tools/assets/hermes-agent-logo.png","rb").read()).decode()
W=H=1080; m=64
def tile(x,y,label,ic,col):
    w,h=224,76
    s='<rect x="%d" y="%d" width="%d" height="%d" rx="24" fill="url(#glass)" stroke="url(#edge)" stroke-width="1.5"/>'%(x,y,w,h)
    s+='<circle cx="%d" cy="%d" r="24" fill="%s" fill-opacity=".16"/>'%(x+14+24+2,y+h/2,col)
    s+=icon_g(ic,x+16+2+8,y+h/2-14+0,28,col,1.8)
    s+=T(x+82,y+h/2+8,label,23,700,"#FFFFFF",HF)
    return s
def poster():
    defs=('<radialGradient id="bg1" cx="50%" cy="58%" r="55%"><stop offset="0" stop-color="#2563FF" stop-opacity=".40"/><stop offset="1" stop-color="#2563FF" stop-opacity="0"/></radialGradient>'
          '<radialGradient id="bg2" cx="90%" cy="6%" r="50%"><stop offset="0" stop-color="#8B5CF6" stop-opacity=".30"/><stop offset="1" stop-color="#8B5CF6" stop-opacity="0"/></radialGradient>'
          '<radialGradient id="core"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".3" stop-color="#14D8C4"/><stop offset=".75" stop-color="#2563FF"/><stop offset="1" stop-color="#8B5CF6"/></radialGradient>'
          '<radialGradient id="halo"><stop offset="0" stop-color="#14D8C4" stop-opacity=".7"/><stop offset=".45" stop-color="#2563FF" stop-opacity=".30"/><stop offset="1" stop-color="#2563FF" stop-opacity="0"/></radialGradient>'
          '<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".14"/><stop offset="1" stop-color="#8B5CF6" stop-opacity=".10"/></linearGradient>'
          '<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#14D8C4" stop-opacity=".8"/><stop offset="1" stop-color="#8B5CF6" stop-opacity=".5"/></linearGradient>'
          '<linearGradient id="hl" gradientUnits="userSpaceOnUse" x1="64" y1="0" x2="1016" y2="0"><stop offset="0" stop-color="#5B8CFF"/><stop offset=".55" stop-color="#14D8C4"/><stop offset="1" stop-color="#8B5CF6"/></linearGradient>'
          '<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>')
    body='<rect width="1080" height="1080" fill="#0B1026"/><rect width="1080" height="1080" fill="url(#bg1)"/><rect width="1080" height="1080" fill="url(#bg2)"/>'
    body+='<g fill="#FFFFFF" fill-opacity=".07">'+''.join('<circle cx="%d" cy="%d r="1.6"/>'%(x,y) if False else '<circle cx="%d" cy="%d" r="1.6"/>'%(x,y) for x in range(64,1030,48) for y in range(440,820,48))+'</g>'
    lg=logo.horizontal_parts("reversed","lc",False); ld,lb,lw,lh=logo.place(lg,m,m,width=300); defs+=ld; body+=lb
    body+=T(W-m,m+34,"MARKETING × AI × CREATIVE",18,600,"#D9E2F2",BF,anchor="end",ls=2.5,op=.85)
    body+=T(540,196,"Dịch vụ thiết kế",46,800,C["aqua"],HF,anchor="middle",ls=1)
    body+=T(540+2,304,"Hermes Agent",112,800,"#FFFFFF",HF,anchor="middle",ls=-3.5)
    body+=T(540,364,"Trợ lý AI cá nhân, thiết kế theo cách bạn làm việc.",38,600,"#D9E2F2",HF,anchor="middle")
    cx,cy=540,626
    lines="";rings=""
    rings+='<circle cx="%d" cy="%d" r="126" fill="none" stroke="#14D8C4" stroke-opacity=".55" stroke-width="1.5"/>'%(cx,cy)
    rings+='<circle cx="%d" cy="%d" r="172" fill="none" stroke="#2563FF" stroke-opacity=".75" stroke-width="1.5" stroke-dasharray="3 9"/>'%(cx,cy)
    rings+='<circle cx="%d" cy="%d" r="218" fill="none" stroke="#8B5CF6" stroke-opacity=".45" stroke-width="1.2"/>'%(cx,cy)
    for a in (35,150,255,320):
        r=172 if a%2 else 218; rings+='<circle cx="%.1f" cy="%.1f" r="6" fill="url(#core)"/>'%(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)))
    tiles=[(64,458,"Nghiên cứu","audit",C["aqua"]),(792,458,"Nội dung","content","#8FB0FF"),(64,704,"Công việc","strategy","#8FB0FF"),(792,704,"Tự động hóa","automation",C["aqua"])]
    tb=""
    for (x,y,l,ic,col) in tiles:
        ex=x+224 if x<cx else x; ey=y+38
        lines+='<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="#14D8C4" stroke-opacity=".85" stroke-width="2.2"/>'%(ex,ey,(ex+cx)/2,ey,(ex+cx)/2,cy,cx,cy)
        tb+=tile(x,y,l,ic,col)
    body+='<g filter="url(#glow)" opacity=".7">'+lines+'</g>'+lines+rings
    body+='<circle cx="%d" cy="%d" r="210" fill="url(#halo)"/><circle cx="%d" cy="%d" r="110" fill="none" stroke="#14D8C4" stroke-width="3.5"/><circle cx="%d" cy="%d" r="104" fill="#FFFFFF"/>'%(cx,cy,cx,cy,cx,cy)
    defs+='<clipPath id="cc"><circle cx="%d" cy="%d" r="104"/></clipPath>'%(cx,cy)
    body+='<image href="%s" x="%d" y="%d" width="208" height="208" clip-path="url(#cc)" preserveAspectRatio="xMidYMid slice"/>'%(LOGO,cx-104,cy-104)+tb
    body+=T(540,892,"Từ câu lệnh đến hệ thống AI của riêng bạn.",42,800,"url(#hl)",HF,anchor="middle",ls=-1)
    body+='<rect x="%d" y="940" width="952" height="1" fill="#FFFFFF" fill-opacity=".16"/>'%m
    body+=T(m,992,"VIBE AI LABS",22,700,"#FFFFFF",BF,ls=3)+T(W-m,992,"Marketing × AI × Creative",22,500,"#D9E2F2",BF,anchor="end")
    return wrap_svg(W,H,defs,body)
s=poster(); base="/Users/henryle/Desktop/vibe_ai_labs/posts/facebook-poster_hermes-agent_1080x1080_dark"
open(base+".svg","w",encoding="utf8").write(s.replace('<svg xmlns="http://www.w3.org/2000/svg"','<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080"',1))
print(render.svg_to_png(s,base+".png",1080,1080,False))
