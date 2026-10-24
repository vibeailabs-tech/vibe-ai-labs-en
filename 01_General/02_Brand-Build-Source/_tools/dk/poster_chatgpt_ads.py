import sys; sys.path.insert(0,"/tmp/dk"); sys.path.insert(0,"/tmp/brandbuild")
from recipes import *
import render
W=H=1080; m=64
TS=60          # cả hai title cùng cỡ chữ, cùng weight 800, mỗi title một dòng
def chip(x,y,t,rot):
    w=len(t)*22*0.56+40; h=46
    return ('<g transform="rotate(%s %.1f %.1f)" opacity=".9"><rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="23" fill="#FFFFFF" fill-opacity=".05" stroke="#FFFFFF" stroke-opacity=".28"/>'%(rot,x+w/2,y+h/2,x,y,w,h)
            +T(x+20,y+31,t,22,500,"#D9E2F2",BF,op=.8)+'</g>'),(x+w,y+h/2)
def bubble(x,y,w,h,bars,right=False):
    s='<rect x="%d" y="%d" width="%d" height="%d" rx="30" fill="url(#glass)" stroke="url(#edge)" stroke-width="1.5"/>'%(x,y,w,h)
    ax=x+w-46 if right else x+46
    s+='<circle cx="%d" cy="%d" r="14" fill="url(#node)"/>'%(ax,y+h/2)
    bx=x+34 if right else x+84
    for i,bw in enumerate(bars):
        s+='<rect x="%d" y="%d" width="%d" height="12" rx="6" fill="#FFFFFF" fill-opacity="%s"/>'%(bx,y+h/2-26+i*30,bw,.55 if i==0 else .28)
    return s
def poster():
    defs=('<radialGradient id="bg1" cx="78%" cy="62%" r="60%"><stop offset="0" stop-color="#2563FF" stop-opacity=".38"/><stop offset="1" stop-color="#2563FF" stop-opacity="0"/></radialGradient>'
          '<radialGradient id="bg2" cx="12%" cy="8%" r="50%"><stop offset="0" stop-color="#8B5CF6" stop-opacity=".30"/><stop offset="1" stop-color="#8B5CF6" stop-opacity="0"/></radialGradient>'
          '<radialGradient id="node"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".35" stop-color="#14D8C4"/><stop offset="1" stop-color="#2563FF"/></radialGradient>'
          '<radialGradient id="halo"><stop offset="0" stop-color="#14D8C4" stop-opacity=".75"/><stop offset=".45" stop-color="#2563FF" stop-opacity=".30"/><stop offset="1" stop-color="#2563FF" stop-opacity="0"/></radialGradient>'
          '<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".14"/><stop offset="1" stop-color="#8B5CF6" stop-opacity=".10"/></linearGradient>'
          '<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#14D8C4" stop-opacity=".8"/><stop offset="1" stop-color="#8B5CF6" stop-opacity=".5"/></linearGradient>'
          '<linearGradient id="flowL" gradientUnits="userSpaceOnUse" x1="64" y1="0" x2="600" y2="0"><stop offset="0" stop-color="#2563FF" stop-opacity=".15"/><stop offset="1" stop-color="#14D8C4" stop-opacity=".95"/></linearGradient>'
          '<linearGradient id="flowR" gradientUnits="userSpaceOnUse" x1="600" y1="0" x2="760" y2="0"><stop offset="0" stop-color="#14D8C4" stop-opacity=".95"/><stop offset="1" stop-color="#8B5CF6" stop-opacity=".8"/></linearGradient>'
          '<linearGradient id="hl" gradientUnits="userSpaceOnUse" x1="64" y1="0" x2="1016" y2="0"><stop offset="0" stop-color="#5B8CFF"/><stop offset=".55" stop-color="#14D8C4"/><stop offset="1" stop-color="#8B5CF6"/></linearGradient>'
          '<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>')
    body='<rect width="1080" height="1080" fill="#0B1026"/><rect width="1080" height="1080" fill="url(#bg1)"/><rect width="1080" height="1080" fill="url(#bg2)"/>'
    # dot grid mờ
    body+='<g fill="#FFFFFF" fill-opacity=".07">'+''.join('<circle cx="%d" cy="%d" r="1.6"/>'%(x,y) for x in range(64,1030,48) for y in range(420,830,48))+'</g>'
    lg=logo.horizontal_parts("reversed","lc",False); ld,lb,lw,lh=logo.place(lg,m,m,width=300); defs+=ld; body+=lb
    body+=T(W-m,m+34,"MARKETING × AI × CREATIVE",18,600,"#D9E2F2",BF,anchor="end",ls=2.5,op=.85)
    body+=T(m,206,"AI INSIGHTS",22,700,C["aqua"],HF,ls=6)
    body+=T(m,282,"ChatGPT Ads",TS,800,"#FFFFFF",HF,ls=-1.5)
    body+=T(m,356,"Kỷ nguyên quảng cáo hội thoại AI",TS,800,"#FFFFFF",HF,ls=-1.5)
    # visual: keywords -> conversations
    nx,ny=600,612
    chips=[(64,440,"giày chạy bộ",-4),(250,484,"giá rẻ",3),(84,548,"top 10",2),(236,606,"mua ở đâu",-3),(64,676,"so sánh",4),(214,730,"review",-2),(330,430,"gần tôi",5)]
    flows="";cb=""
    for (x,y,t,r) in chips:
        s,(ex,ey)=chip(x,y,t,r); cb+=s
        flows+='<path d="M%.1f %.1f C%.1f %.1f %d %d %d %d" fill="none" stroke="url(#flowL)" stroke-width="2.2"/>'%(ex,ey,ex+130,ey,nx-190,ny,nx,ny)
    bubs=[(690,452,326,104,[210,150],False),(730,580,286,104,[150,130],True),(690,708,326,104,[220,120],False)]
    out=""
    for (x,y,w,h,bars,rt) in bubs:
        out+='<path d="M%d %d C%d %d %d %d %d %d" fill="none" stroke="url(#flowR)" stroke-width="3"/>'%(nx,ny,nx+80,ny,x-70,y+h/2,x,y+h/2)
    body+='<g filter="url(#glow)" opacity=".7">'+flows+out+'</g>'+flows+out+cb
    for (x,y,w,h,bars,rt) in bubs: body+=bubble(x,y,w,h,bars,rt)
    body+='<circle cx="%d" cy="%d" r="120" fill="url(#halo)"/><circle cx="%d" cy="%d" r="30" fill="none" stroke="#14D8C4" stroke-opacity=".55" stroke-width="1.5"/><circle cx="%d" cy="%d" r="15" fill="url(#node)"/>'%(nx,ny,nx,ny,nx,ny)
    body+=T(m,902,"Từ Keywords đến Conversations",58,800,"url(#hl)",HF,ls=-1.5)
    body+='<rect x="%d" y="940" width="952" height="1" fill="#FFFFFF" fill-opacity=".16"/>'%m
    body+=T(m,992,"VIBE AI LABS",22,700,"#FFFFFF",BF,ls=3)+T(W-m,992,"Marketing × AI × Creative",22,500,"#D9E2F2",BF,anchor="end")
    return wrap_svg(W,H,defs,body)
s=poster(); base="/Users/henryle/Desktop/vibe_ai_labs/posts/facebook-poster_chatgpt-ads_1080x1080_dark"
open(base+".svg","w",encoding="utf8").write(s.replace('<svg xmlns="http://www.w3.org/2000/svg"','<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080"',1))
print(render.svg_to_png(s,base+".png",1080,1080,False))
