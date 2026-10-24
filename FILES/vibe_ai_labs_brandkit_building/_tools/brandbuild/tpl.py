import sys, re, math; sys.path.insert(0,"/tmp/brandbuild")
from xml.sax.saxutils import escape
import logo, gfx
exec(open("/tmp/brandbuild/icons_def.py").read())
C=dict(midnight="#0B1026",blue="#2563FF",aqua="#14D8C4",violet="#8B5CF6",cloud="#F8FAFC",ink="#111827",slate="#667085",line="#D9E2F2",white="#FFFFFF",green="#16A34A",orange="#F97316")
HF="Plus Jakarta Sans"; BF="Inter"
_uid=[0]
def uid(p="u"): _uid[0]+=1; return "%s%d"%(p,_uid[0])
def T(x,y,s,size,weight=800,fill="#0B1026",font=HF,anchor="start",ls=0,op=1,extra=""):
    return '<text x="%.1f" y="%.1f" font-family="%s" font-weight="%d" font-size="%.1f" fill="%s" text-anchor="%s" letter-spacing="%s" opacity="%s"%s>%s</text>'%(x,y,font,weight,size,fill,anchor,ls,op,extra,escape(s))
def grad_def(id_,x1,y1,x2,y2,a="#2563FF",b="#14D8C4"):
    return '<linearGradient id="%s" gradientUnits="userSpaceOnUse" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'%(id_,x1,y1,x2,y2,a,b)
def pill(x,y,label,size,bg="#2563FF",fg="#FFFFFF",arrow=True,padx=None):
    padx=padx or size*1.15; h=size*2.5
    txt=label+("  →" if arrow else "")
    wd=len(txt)*size*0.56+2*padx
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s"/>'%(x,y,wd,h,h/2,bg)+T(x+padx,y+h/2+size*0.35,txt,size,600,fg,BF)),wd,h
def icon_g(name,x,y,size,color,sw=1.75):
    s=size/24.0
    return '<g transform="translate(%.1f,%.1f) scale(%.4f)" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</g>'%(x,y,s,color,sw,ICONS[name])
def fit(lines,boxw,boxh,maxsize,lh=1.06,cw=0.585):
    mx=max(len(l) for l in lines)
    return min(maxsize,boxw/(mx*cw),boxh/(len(lines)*lh))
def wrap_svg(W,H,defs,body):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d"><defs>%s</defs>%s</svg>'%(W,H,defs,body)

# ------------------------------------------------------------------ social announcement
FORMATS={ # name: (W,H,kind,box(x,y,w,h))
 "facebook-post-1080x1080":(1080,1080,"square",(86,86,908,908)),
 "instagram-post-1080x1350":(1080,1350,"portrait",(86,100,908,1150)),
 "instagram-story-1080x1920":(1080,1920,"story",(86,260,908,1300)),
 "linkedin-post-1200x1200":(1200,1200,"square",(96,96,1008,1008)),
 "x-post-1600x900":(1600,900,"wide16",(110,100,880,700)),
 "youtube-thumbnail-1280x720":(1280,720,"wide16",(90,80,700,560)),
 "x-header-1500x500":(1500,500,"banner",(250,50,1200,400)),
 "facebook-cover-1640x624":(1640,624,"banner",(260,60,1280,360)),
 "linkedin-banner-1584x396":(1584,396,"banner",(360,40,1200,316)),
 "youtube-banner-2560x1440":(2560,1440,"banner",(507,508,1546,423)),
 "email-banner-1200x400":(1200,400,"banner",(70,40,1060,320)),
}
def announce(name,dark):
    W,H,kind,(bx,by,bw,bh)=FORMATS[name]
    fg="#FFFFFF" if dark else C["midnight"]; sub="#D9E2F2" if dark else C["slate"]
    defs=""; body=""
    if kind=="banner":
        d,b=gfx.waves(W,H,dark,n=40,amp=0.2 if H<600 else 0.14,y0=0.55,uid="bw")
        defs+=d; body+=b
        md,mb=logo.mark_color("bm"); defs+=md
        ms=(bh*0.86)/logo.MARK_H; mw=logo.MARK_W*ms; mh=logo.MARK_H*ms
        mx=bx+bw-mw; my=by+(bh-mh)/2
        body+='<g transform="translate(%.1f,%.1f) scale(%.4f)">%s</g>'%(mx-logo.MARK_X0*ms,my,ms,mb)
        bw_eff=mx-bx-0.05*bw
        lines=["Ideas. Intelligence.","Real Growth."]
        size=fit(lines,bw_eff,bh*0.62,170,cw=0.60)
        lh_target=max(24,min(size*0.60,64))
        lg=logo.horizontal_parts("reversed" if dark else "color","l"+uid(),False); ld,lb,lw,lh_=logo.place(lg,bx,by,height=lh_target)
        defs+=ld; body+=lb
        y1=by+lh_+size*1.15
        gid=uid("tg"); defs+=grad_def(gid,bx,0,bx+size*7,0,"#2563FF" if not dark else "#5B8CFF","#14D8C4")
        body+=T(bx,y1,lines[0],size,800,fg,HF,ls=-size*0.02)+T(bx,y1+size*1.04,lines[1],size,800,"url(#%s)"%gid,HF,ls=-size*0.02)
        if bh>330:
            body+=T(bx,y1+size*1.04+size*0.55,"Marketing × AI × Creative",size*0.30,600,sub,BF,ls=size*0.012)
        return wrap_svg(W,H,defs,body)
    # square/portrait/story/wide16
    if kind=="wide16":
        d,b=gfx.ribbon(W,H,dark,cx=0.9,cy=0.5,wr=0.85,uid="rw")
    elif kind=="story":
        d,b=gfx.ribbon(W,H,dark,cx=0.62,cy=0.86,wr=1.9,uid="rs")
    elif kind=="portrait":
        d,b=gfx.ribbon(W,H,dark,cx=0.72,cy=0.88,wr=1.25,uid="rp")
    else:
        d,b=gfx.ribbon(W,H,dark,cx=0.72,cy=0.86,wr=1.2,uid="rq")
    defs+=d; body+=b
    lg=logo.horizontal_parts("reversed" if dark else "color","l"+uid(),False); ld,lb,lw,lh_=logo.place(lg,bx,by,width=bw*0.40 if kind!="wide16" else bw*0.46)
    defs+=ld; body+=lb
    lines=["Ideas.","Intelligence.","Real Growth."]
    top=by+lh_+bh*0.07
    size=fit(lines,bw,bh*(0.40 if kind!="wide16" else 0.52),W*0.115 if kind!="wide16" else H*0.17,cw=0.60)
    gid=uid("tg"); defs+=grad_def(gid,bx,0,bx+size*7.5,0,"#2563FF" if not dark else "#5B8CFF","#14D8C4")
    y=top+size
    body+=T(bx,y,lines[0],size,800,fg,HF,ls=-size*0.025)+T(bx,y+size*1.04,lines[1],size,800,fg,HF,ls=-size*0.025)+T(bx,y+size*2.08,lines[2],size,800,"url(#%s)"%gid,HF,ls=-size*0.025)
    yy=y+size*2.08+size*0.42
    subsz=size*0.26
    body+=T(bx,yy+subsz,"Agency tăng trưởng & sáng tạo ứng dụng AI",subsz,500,sub,BF)
    if kind!="wide16":
        pb,pw,ph=pill(bx,by+bh-size*0.34*2.5-(0 if kind!="story" else 0),"Tìm hiểu thêm",size*0.27)
        # place pill at bottom of box on square/portrait
        body+=pb
    else:
        pb,pw,ph=pill(bx,yy+subsz*2.2,"Tìm hiểu thêm",size*0.2)
        body+=pb
    return wrap_svg(W,H,defs,body)

# variants for square + portrait feed
def card_base(W,H,dark,variant="ribbon"):
    if variant=="waves": return gfx.waves(W,H,dark,n=36,amp=0.12,y0=0.78,uid="cw"+uid())
    return gfx.ribbon(W,H,dark,cx=0.86,cy=0.92,wr=0.95,uid="cr"+uid())
def insight(W,H,dark):
    m=W*0.08; fg="#FFFFFF" if dark else C["midnight"]; sub="#D9E2F2" if dark else C["slate"]
    d,b=card_base(W,H,dark,"waves"); defs=d; body=b
    body+=T(W-m,H*0.52,"05",W*0.95,800,"#FFFFFF" if dark else C["blue"],HF,"end",ls=-W*0.03,op=0.06 if dark else 0.07)
    lg=logo.horizontal_parts("reversed" if dark else "color","l"+uid()); ld,lb,lw,lh_=logo.place(lg,m,m,width=W*0.34); defs+=ld; body+=lb
    body+=T(m,H*0.30,"INSIGHT",W*0.026,700,C["aqua"] if dark else C["blue"],HF,ls=W*0.006)
    lines=["5 cách AI giúp","thương hiệu tăng","trưởng nhanh hơn"]
    size=fit(lines,W-2*m,H*0.36,W*0.092,cw=0.585)
    for i,l in enumerate(lines): body+=T(m,H*0.30+W*0.05+size*(i+0.9)*1.05,l,size,800,fg,HF,ls=-size*0.02)
    pb,pw,ph=pill(m,H-m-W*0.075,"Đọc thêm",W*0.026); body+=pb
    return wrap_svg(W,H,defs,body)
def pillars(W,H,dark):
    m=W*0.08; fg="#FFFFFF" if dark else C["midnight"]; sub="#D9E2F2" if dark else C["slate"]
    d,b=card_base(W,H,dark,"waves"); defs=d; body=b
    lg=logo.horizontal_parts("reversed" if dark else "color","l"+uid()); ld,lb,lw,lh_=logo.place(lg,m,m,width=W*0.34); defs+=ld; body+=lb
    body+=T(m,H*0.27,"Một hệ thống.",W*0.082,800,fg,HF,ls=-W*0.002)+T(m,H*0.27+W*0.09,"Ba năng lực.",W*0.082,800,C["aqua"] if dark else C["blue"],HF,ls=-W*0.002)
    rows=[("growth","Marketing số","Chiến lược · Thương hiệu · Nội dung · Performance",C["blue"]),
          ("ai","AI & Tự động hóa","AI Agent · Chatbot · Quy trình tự động",C["green"]),
          ("design","Thiết kế & Sáng tạo","Nhận diện · Hình ảnh · Video · AI tạo sinh",C["orange"])]
    y=H*0.45; rh=(H*0.95-y-m*0.4)/3
    for i,(ic,t,s_,col) in enumerate(rows):
        yy=y+i*rh
        body+='<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" fill-opacity="%s" stroke="%s" stroke-opacity=".5"/>'%(m,yy,W-2*m,rh-W*0.025,W*0.03,"#FFFFFF" if dark else "#FFFFFF","0.07" if dark else "1","#FFFFFF" if dark else C["line"])
        body+='<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" fill-opacity=".18"/>'%(m+W*0.03,yy+(rh-W*0.025-W*0.11)/2,W*0.11,W*0.11,W*0.03,col)
        body+=icon_g(ic,m+W*0.03+W*0.11*0.2,yy+(rh-W*0.025-W*0.11)/2+W*0.11*0.2,W*0.11*0.6,col if not dark else "#FFFFFF" if False else col,1.75)
        body+=T(m+W*0.19,yy+rh*0.40,t,W*0.04,800,fg,HF)+T(m+W*0.19,yy+rh*0.40+W*0.04,s_,W*0.023,500,sub,BF)
    return wrap_svg(W,H,defs,body)
def quote(W,H,dark):
    m=W*0.09; fg="#FFFFFF" if dark else C["midnight"]; sub="#D9E2F2" if dark else C["slate"]
    d,b=card_base(W,H,dark,"ribbon"); defs=d; body=b
    lg=logo.horizontal_parts("reversed" if dark else "color","l"+uid()); ld,lb,lw,lh_=logo.place(lg,m,m,width=W*0.34); defs+=ld; body+=lb
    gid=uid("q"); defs+=grad_def(gid,m,0,m+W*0.3,0,"#2563FF" if not dark else "#5B8CFF","#14D8C4")
    body+=T(m,H*0.43,"“",W*0.30,800,"url(#%s)"%gid,HF)
    lines=["Nội dung nhận xét của khách","hàng đặt tại đây — ngắn gọn,","cụ thể và có kết quả."]
    size=fit(lines,W-2*m,H*0.28,W*0.056,cw=0.56)
    for i,l in enumerate(lines): body+=T(m,H*0.50+size*(i+1)*1.22,l,size,700,fg,HF)
    body+=T(m,H*0.50+size*4.9,"Tên khách hàng",W*0.03,700,fg,BF)+T(m,H*0.50+size*4.9+W*0.045,"Chức vụ · Doanh nghiệp",W*0.024,500,sub,BF)
    return wrap_svg(W,H,defs,body)
def stat(W,H,dark):
    m=W*0.08; fg="#FFFFFF" if dark else C["midnight"]; sub="#D9E2F2" if dark else C["slate"]
    d,b=card_base(W,H,dark,"waves"); defs=d; body=b
    lg=logo.horizontal_parts("reversed" if dark else "color","l"+uid()); ld,lb,lw,lh_=logo.place(lg,m,m,width=W*0.34); defs+=ld; body+=lb
    gid=uid("s"); defs+=grad_def(gid,m,0,m+W*0.8,0,"#2563FF" if not dark else "#5B8CFF","#14D8C4")
    body+=T(m,H*0.30,"DATA INSIGHT",W*0.026,700,C["aqua"] if dark else C["blue"],HF,ls=W*0.006)
    body+=T(m,H*0.30+W*0.30,"+00%",W*0.30,800,"url(#%s)"%gid,HF,ls=-W*0.012)
    body+=T(m,H*0.30+W*0.30+W*0.085,"Mô tả chỉ số ở đây — chỉ dùng số liệu",W*0.04,700,fg,HF)+T(m,H*0.30+W*0.30+W*0.14,"có thể xác minh, kèm nguồn và kỳ đo.",W*0.04,700,fg,HF)
    body+=T(m,H-m,"Nguồn: [Dự án / khách hàng · thời gian đo]",W*0.022,500,sub,BF)
    return wrap_svg(W,H,defs,body)
