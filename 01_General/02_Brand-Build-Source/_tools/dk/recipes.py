import sys; sys.path.insert(0,"/tmp/brandbuild")
from cfg import *
import tpl, gfx, logo
from tpl import T, grad_def, wrap_svg, C, HF, BF, icon_g, pill, fit, uid
from xml.sax.saxutils import escape

RATIOS={"1x1":(1080,1080,"sq"),"4x5":(1080,1350,"p45"),"9x16":(1080,1920,"story"),"16x9":(1280,720,"land"),"A3":(1080,1527,"p45")}
def fr(W,H,kind):
    if kind=="land": m=70; return dict(m=m,x=m,cw=W*0.56-m,top=205,bottom=H-m,logo_y=m,logo_w=300)
    if kind=="story": m=86; return dict(m=m,x=m,cw=W-2*m,top=430,bottom=H-340,logo_y=270,logo_w=380)
    if kind=="p45": m=86; return dict(m=m,x=m,cw=W-2*m,top=270,bottom=H-m,logo_y=m,logo_w=360)
    m=86; return dict(m=m,x=m,cw=W-2*m,top=260,bottom=H-m,logo_y=m,logo_w=360)
def base(W,H,dark,kind,variant="ribbon",rb=None):
    pos={"sq":dict(cx=0.78,cy=0.97,wr=1.3),"p45":dict(cx=0.76,cy=0.96,wr=1.3),"story":dict(cx=0.62,cy=0.9,wr=2.0),"land":dict(cx=0.93,cy=0.6,wr=0.66)}[kind]
    if rb: pos.update(rb)
    if variant=="waves": d,b=gfx.waves(W,H,dark,n=36,amp=0.12,y0=0.78 if kind!="land" else 0.7,uid="w"+uid())
    else:
        pos["opacity"]=0.75 if dark else 0.22
        d,b=gfx.ribbon(W,H,dark,uid="r"+uid(),**pos)
    return d,b
def head_logo(W,H,dark,kind,f):
    lg=logo.horizontal_parts("reversed" if dark else "color","l"+uid(),False)
    return logo.place(lg,f["x"],f["logo_y"],width=f["logo_w"])
def col(dark): return dict(fg="#FFFFFF" if dark else C["midnight"],sub="#D9E2F2" if dark else C["slate"],acc=C["aqua"] if dark else C["blue"],g1="#5B8CFF" if dark else "#2563FF")
def gradient(defs,x,w_,dark):
    gid=uid("g"); return gid,defs+grad_def(gid,x,0,x+w_,0,col(dark)["g1"],"#14D8C4")
def scaffold(W,H,dark,kind,variant="ribbon",rb=None):
    f=fr(W,H,kind); c=col(dark); d,b=base(W,H,dark,kind,variant,rb)
    ld,lb,lw,lh=head_logo(W,H,dark,kind,f)
    return f,c,d+ld,b+lb,lh

# ---------------------------------------------------------------- R1 announcement
def r1(W,H,dark,kind):
    f,c,defs,body,lh=scaffold(W,H,dark,kind); x=f["x"]; cw=f["cw"]
    lines=["Ba năng lực.","Một hệ thống."]
    size=fit(lines,cw,(f["bottom"]-f["top"])*0.42,W*0.125 if kind!="land" else H*0.2,cw=0.60)
    gid,defs=gradient(defs,x,cw,dark)
    y=f["top"]+(40 if kind in("story",) else 40)+size
    if kind=="land": y=f["top"]+size*0.6+60
    body+=T(x,y,lines[0],size,800,c["fg"],HF,ls=-size*0.03)+T(x,y+size*1.04,lines[1],size,800,"url(#%s)"%gid,HF,ls=-size*0.03)
    ys=y+size*1.04+size*0.62
    s2=size*0.27
    body+=T(x,ys,"Marketing × AI × Creative cùng vận hành.",s2,500,c["sub"],BF)
    pb,pw,ph=pill(x,max(ys+s2*2.2,f["bottom"]-size*0.5-30) if kind in("sq",) else ys+s2*1.8,"Nhắn tin cho chúng tôi",size*0.30); body+=pb
    return wrap_svg(W,H,defs,body)
# ---------------------------------------------------------------- R2 insight list
def r2(W,H,dark,kind):
    f,c,defs,body,lh=scaffold(W,H,dark,kind,"waves"); x=f["x"]; cw=f["cw"]
    big=(f["bottom"]-f["top"])*(0.55 if kind!="land" else 0.9)
    body+=T(W-f["m"]*0.6,f["top"]+big*0.95,"05",min(W*0.95,big*1.55),800,"#FFFFFF" if dark else C["blue"],HF,"end",ls=-W*0.03,op=0.06 if dark else 0.07)
    body+=T(x,f["top"]+10,"INSIGHT",W*0.022 if kind!="land" else 22,700,c["acc"],HF,ls=6)
    lines=["5 cách AI giúp","thương hiệu tăng","trưởng nhanh hơn"]
    size=fit(lines,cw,(f["bottom"]-f["top"])*0.50,W*0.098 if kind!="land" else H*0.12,cw=0.585)
    y0=f["top"]+size*1.55
    for i,l in enumerate(lines): body+=T(x,y0+i*size*1.06,l,size,800,c["fg"],HF,ls=-size*0.02)
    pb,pw,ph=pill(x,y0+3*size*1.06+size*0.4 if kind in("land","story") else f["bottom"]-size*0.32*2.5,"Đọc thêm",size*0.32); body+=pb
    return wrap_svg(W,H,defs,body)
# ---------------------------------------------------------------- R3 pillars
def r3(W,H,dark,kind):
    f,c,defs,body,lh=scaffold(W,H,dark,kind,"waves"); x=f["x"]; cw=f["cw"]
    lines=["Một hệ thống.","Ba năng lực."]
    size=fit(lines,cw,(f["bottom"]-f["top"])*0.30,W*0.098 if kind!="land" else H*0.15,cw=0.6)
    y=f["top"]+size*0.9
    body+=T(x,y,lines[0],size,800,c["fg"],HF,ls=-size*0.02)+T(x,y+size*1.04,lines[1],size,800,c["acc"],HF,ls=-size*0.02)
    cards=[("growth","Marketing số","Chiến lược · Nội dung · Dữ liệu",C["blue"]),("ai","AI & Tự động hóa","AI Agent · Chatbot · Quy trình",C["green"]),("design","Thiết kế & Sáng tạo","Nhận diện · Hình ảnh · Video",C["orange"])]
    top=y+size*1.04+size*0.5; avail=f["bottom"]-top
    if kind=="land":
        top=f["top"]-20; x2=W*0.56+30; cw2=W-x2-f["m"]; h_=(f["bottom"]-top-2*16)/3
        for i,(ic,t,s_,col_) in enumerate(cards): body+=card(x2,top+i*(h_+16),cw2,h_,ic,t,s_,col_,dark,c)
    else:
        h_=(avail-2*18)/3
        for i,(ic,t,s_,col_) in enumerate(cards): body+=card(x,top+i*(h_+18),cw,h_,ic,t,s_,col_,dark,c)
    return wrap_svg(W,H,defs,body)
def card(x,y,w_,h_,ic,t,s_,col_,dark,c):
    r=min(h_*0.22,32)
    out='<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" fill-opacity="%s" stroke="%s" stroke-opacity="%s"/>'%(x,y,w_,h_,r,"#0B1026" if dark else "#FFFFFF",".72" if dark else "1","#FFFFFF" if dark else C["line"],".22" if dark else "1")
    ts=min(h_*0.62,92); ty=y+(h_-ts)/2
    out+='<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" fill-opacity="%s"/>'%(x+h_*0.16,ty,ts,ts,ts*0.28,col_,".22" if dark else ".14")
    icc={"#2563FF":"#7DA2FF","#16A34A":"#4ADE80","#F97316":"#FDBA74"}[col_] if dark else col_
    out+=icon_g(ic,x+h_*0.16+ts*0.2,ty+ts*0.2,ts*0.6,icc,1.8)
    tx=x+h_*0.16+ts+h_*0.18
    out+=T(tx,y+h_*0.46,t,min(h_*0.27,40),800,c["fg"],HF)+T(tx,y+h_*0.46+min(h_*0.21,32),s_,min(h_*0.15,25),500,c["sub"],BF)
    return out
# ---------------------------------------------------------------- R4 stat
def r4(W,H,dark,kind):
    f,c,defs,body,lh=scaffold(W,H,dark,kind,"waves"); x=f["x"]; cw=f["cw"]
    gid,defs=gradient(defs,x,cw,dark)
    body+=T(x,f["top"]+10,"KẾT QUẢ",W*0.022 if kind!="land" else 22,700,c["acc"],HF,ls=6)
    size=fit(["+00%"],cw,(f["bottom"]-f["top"])*0.5,W*0.3 if kind!="land" else H*0.42,cw=0.66)
    y=f["top"]+size*1.05+30
    body+=T(x,y,"+00%",size,800,"url(#%s)"%gid,HF,ls=-size*0.03)
    cs=size*0.2
    for i,l in enumerate(["Mô tả chỉ số ở đây —","chỉ dùng số liệu xác minh được."]): body+=T(x,y+size*0.3+i*cs*1.3,l,cs,700,c["fg"],HF)
    body+=T(x,f["bottom"] if kind!="land" else y+size*0.3+cs*3.4,"Nguồn: [Dự án · thời gian đo]",max(cs*0.58,18),500,c["sub"],BF)
    return wrap_svg(W,H,defs,body)
# ---------------------------------------------------------------- R5 quote
def r5(W,H,dark,kind):
    f,c,defs,body,lh=scaffold(W,H,dark,kind); x=f["x"]; cw=f["cw"]
    gid,defs=gradient(defs,x,300,dark)
    qs=W*0.26 if kind!="land" else H*0.42
    body+=T(x,f["top"]+qs*0.62,"“",qs,800,"url(#%s)"%gid,HF)
    lines=["Nhận xét của khách hàng đặt","tại đây — ngắn gọn, cụ thể","và có kết quả."]
    size=fit(lines,cw,(f["bottom"]-f["top"])*0.4,W*0.056 if kind!="land" else H*0.075,cw=0.56)
    y0=f["top"]+qs*0.62+size*1.5
    for i,l in enumerate(lines): body+=T(x,y0+i*size*1.25,l,size,700,c["fg"],HF)
    yn=y0+3*size*1.25+size*0.6
    body+='<rect x="%.1f" y="%.1f" width="56" height="5" rx="2.5" fill="%s"/>'%(x,yn-size*0.5,C["aqua"])
    body+=T(x,yn+size*0.45,"Tên khách hàng",size*0.55,700,c["fg"],BF)+T(x,yn+size*0.45+size*0.55,"Chức vụ · Doanh nghiệp",size*0.45,500,c["sub"],BF)
    return wrap_svg(W,H,defs,body)
# ---------------------------------------------------------------- R6 event
def r6(W,H,dark,kind):
    f,c,defs,body,lh=scaffold(W,H,dark,kind); x=f["x"]; cw=f["cw"]
    ts=W*0.024 if kind!="land" else 22
    tw=len("WEBINAR")*ts*0.85+ts*2
    body+='<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s"/>'%(x,f["top"]-ts*0.2,tw,ts*2.4,ts*1.2,C["aqua"] if dark else C["blue"])
    body+=T(x+ts,f["top"]+ts*1.15,"WEBINAR",ts,800,C["midnight"] if dark else "#FFFFFF",HF,ls=ts*0.18)
    lines=["AI cho Marketing:","bắt đầu từ đâu?"]
    size=fit(lines,cw,(f["bottom"]-f["top"])*0.34,W*0.092 if kind!="land" else H*0.13,cw=0.6)
    y=f["top"]+ts*2.4+size*1.1
    gid,defs=gradient(defs,x,cw,dark)
    body+=T(x,y,lines[0],size,800,c["fg"],HF,ls=-size*0.02)+T(x,y+size*1.04,lines[1],size,800,"url(#%s)"%gid,HF,ls=-size*0.02)
    by=y+size*1.04+size*0.55; bh=size*1.3
    body+='<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" fill-opacity="%s" stroke="%s" stroke-opacity="%s"/>'%(x,by,cw,bh,bh*0.2,"#0B1026" if dark else "#FFFFFF",".72" if dark else "1","#FFFFFF" if dark else C["line"],".22" if dark else "1")
    body+=T(x+bh*0.25,by+bh*0.64,"[DD.MM]",bh*0.46,800,c["fg"],HF)+T(x+cw*0.40,by+bh*0.45,"[HH:MM] · [Thứ]",bh*0.27,700,c["fg"],BF)+T(x+cw*0.40,by+bh*0.77,"[Địa điểm / Online]",bh*0.22,500,c["sub"],BF)
    pb,pw,ph=pill(x,by+bh+size*0.45,"Đăng ký ngay",size*0.32); body+=pb
    return wrap_svg(W,H,defs,body)
RECIPES={"R1_announcement":r1,"R2_insight-list":r2,"R3_pillars":r3,"R4_stat":r4,"R5_quote":r5,"R6_event":r6}
