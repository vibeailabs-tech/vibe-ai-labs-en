import math, sys
sys.path.insert(0,"/tmp/brandbuild")
import logo
def glows(W,H,dark=True,uid="x"):
    if dark:
        return ('<defs><radialGradient id="%sg1" cx="0.78" cy="0.22" r="0.65"><stop offset="0" stop-color="#2563FF" stop-opacity=".55"/><stop offset="1" stop-color="#2563FF" stop-opacity="0"/></radialGradient>'
                '<radialGradient id="%sg2" cx="0.1" cy="0.95" r="0.6"><stop offset="0" stop-color="#14D8C4" stop-opacity=".28"/><stop offset="1" stop-color="#14D8C4" stop-opacity="0"/></radialGradient>'
                '<radialGradient id="%sg3" cx="0.95" cy="0.9" r="0.5"><stop offset="0" stop-color="#8B5CF6" stop-opacity=".3"/><stop offset="1" stop-color="#8B5CF6" stop-opacity="0"/></radialGradient></defs>'
                '<rect width="%d" height="%d" fill="#0B1026"/><rect width="%d" height="%d" fill="url(#%sg1)"/><rect width="%d" height="%d" fill="url(#%sg2)"/><rect width="%d" height="%d" fill="url(#%sg3)"/>'%(uid,uid,uid,W,H,W,H,uid,W,H,uid,W,H,uid))
    return ('<defs><radialGradient id="%sg1" cx="0.85" cy="0.1" r="0.7"><stop offset="0" stop-color="#2563FF" stop-opacity=".16"/><stop offset="1" stop-color="#2563FF" stop-opacity="0"/></radialGradient>'
            '<radialGradient id="%sg2" cx="0.05" cy="1" r="0.6"><stop offset="0" stop-color="#14D8C4" stop-opacity=".18"/><stop offset="1" stop-color="#14D8C4" stop-opacity="0"/></radialGradient></defs>'
            '<rect width="%d" height="%d" fill="#F8FAFC"/><rect width="%d" height="%d" fill="url(#%sg1)"/><rect width="%d" height="%d" fill="url(#%sg2)"/>'%(uid,uid,W,H,W,H,uid,W,H,uid))
def ribbon(W,H,dark=True,cx=0.74,cy=0.6,wr=1.25,opacity=None,uid="rb"):
    md,mb=logo.mark_color(uid)
    s=wr*W/logo.MARK_W
    tx=cx*W-(logo.MARK_X0+logo.MARK_W/2)*s; ty=cy*H-(logo.MARK_H/2)*s
    op=opacity if opacity is not None else (0.92 if dark else 0.16)
    return md, glows(W,H,dark,uid)+'<g opacity="%s" transform="translate(%.1f,%.1f) scale(%.4f)">%s</g>'%(op,tx,ty,s,mb)
def waves(W,H,dark=True,n=44,amp=0.16,y0=0.62,uid="wv",glow=True):
    b=glows(W,H,dark,uid) if glow else ""
    defs='<linearGradient id="%swl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2563FF"/><stop offset=".55" stop-color="#14D8C4"/><stop offset="1" stop-color="#8B5CF6"/></linearGradient>'%uid
    for i in range(n):
        t=i/(n-1); pts=[]
        for k in range(0,121):
            x=W*k/120.0; u=k/120.0
            y=H*y0+H*amp*math.sin(u*math.pi*2.0+t*1.9)*(0.55+0.45*math.sin(u*math.pi*0.9+0.4))+(t-0.5)*H*0.30*(1-0.35*math.cos(u*math.pi*2))
            pts.append((x,y))
        op=0.10+0.55*(1-abs(t-0.5)*2)
        b+='<path d="M%s" fill="none" stroke="url(#%swl)" stroke-width="1.6" opacity="%.2f"/>'%(" L".join("%.1f %.1f"%p for p in pts),uid,op if dark else op*0.8)
    return defs,b
