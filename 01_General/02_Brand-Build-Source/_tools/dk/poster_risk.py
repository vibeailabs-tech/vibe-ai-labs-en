import sys; sys.path.insert(0,"/tmp/dk"); sys.path.insert(0,"/tmp/brandbuild")
from recipes import *
import render
W=H=1080; m=86
def poster(dark):
    c=col(dark)
    d,b=gfx.ribbon(W,H,dark,cx=0.86,cy=1.02,wr=1.15,opacity=0.7 if dark else 0.2,uid="rk")
    lg=logo.horizontal_parts("reversed" if dark else "color","lk",False); ld,lb,lw,lh=logo.place(lg,m,m,width=360)
    defs=d+ld; body=b+lb
    body+=T(m,236,"LƯU Ý KHI DÙNG AI",24,700,c["acc"],HF,ls=6)
    gid,defs=gradient(defs,m,700,dark)
    body+=T(m,356,"4 rủi ro khi dùng AI",110,800,c["fg"],HF,ls=-3.5)+T(m,472,"thiếu kiểm soát.",110,800,"url(#%s)"%gid,HF,ls=-3.5)
    items=["Thông tin sai","Lộ dữ liệu","Nội dung na ná","Mất kiểm soát"]
    cw=439; ch=124; gx=30; gy=22; y0=548
    for i,t in enumerate(items):
        x=m+(i%2)*(cw+gx); y=y0+(i//2)*(ch+gy)
        if dark: body+='<rect x="%d" y="%d" width="%d" height="%d" rx="30" fill="#0B1026" fill-opacity=".72" stroke="#FFFFFF" stroke-opacity=".22"/>'%(x,y,cw,ch)
        else: body+='<rect x="%d" y="%d" width="%d" height="%d" rx="30" fill="#FFFFFF" stroke="#D9E2F2"/>'%(x,y,cw,ch)
        body+=T(x+30,y+ch/2+16,"%02d"%(i+1),48,800,c["acc"] if dark else C["blue"],HF)+T(x+118,y+ch/2+12,t,34,800,c["fg"],HF)
    body+=T(m,880,"AI hỗ trợ. Con người quyết định.",32,600,c["sub"],BF)
    pb,pw,ph=pill(m,916,"Nhắn tin cho chúng tôi",28); body+=pb
    return wrap_svg(W,H,defs,body)
os.makedirs("/Users/henryle/Desktop/vibe_ai_labs/posts",exist_ok=True)
for tone in ("dark","light"):
    s=poster(tone=="dark"); base="/Users/henryle/Desktop/vibe_ai_labs/posts/facebook-poster_rui-ro-khi-dung-ai_1080x1080_%s"%tone
    open(base+".svg","w",encoding="utf8").write(s.replace('<svg xmlns="http://www.w3.org/2000/svg"','<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080"',1))
    print(render.svg_to_png(s,base+".png",1080,1080,False))
