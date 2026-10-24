import sys; sys.path.insert(0,"/tmp/dk"); sys.path.insert(0,"/tmp/brandbuild")
from recipes import *
import render, os
OUTD="/tmp/design_out"; jobs=[]
def save(name,svg,W,H,transp=True):
    p=os.path.join(OUTD,"04_Components/SVG/%s.svg"%name); os.makedirs(os.path.dirname(p),exist_ok=True)
    open(p,"w",encoding="utf8").write(svg.replace('<svg xmlns="http://www.w3.org/2000/svg"','<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d"'%(W,H),1))
    jobs.append((svg,os.path.join(OUTD,"04_Components/PNG/%s.png"%name),W,H,transp))
def S(W,H,body,defs=""): return wrap_svg(W,H,defs,body)
# buttons
for nm,bg,fg,stroke in (("button-primary","#2563FF","#FFFFFF",None),("button-secondary-light","#FFFFFF","#0B1026","#D9E2F2"),("button-ghost-dark",None,"#FFFFFF","#FFFFFF"),("button-ghost-light",None,"#2563FF","#2563FF")):
    lab="Nhắn tin cho chúng tôi  →"; sz=28; wd=int(len(lab)*sz*0.56+2*32); h=72
    b='<rect x="2" y="2" width="%d" height="%d" rx="%d" fill="%s"%s/>'%(wd-4,h-4,(h-4)//2,bg or "none",' stroke="%s" stroke-width="3" stroke-opacity="%s"'%(stroke,".7" if nm=="button-ghost-dark" else "1") if stroke else "")
    b+=T(32,h/2+10,lab,sz,600,fg,BF)
    save(nm,S(wd,h,b),wd,h)
# tags
for nm,bg,fg,lab in (("tag-ai","#2563FF22","#2563FF","AI"),("tag-automation","#16A34A22","#16A34A","Automation"),("tag-creative","#F9731622","#F97316","Creative"),("tag-insight","#8B5CF622","#8B5CF6","Insight"),("tag-new","#14D8C4","#0B1026","MỚI"),("tag-webinar","#2563FF","#FFFFFF","WEBINAR")):
    sz=22; wd=int(len(lab)*sz*0.66+40); h=44
    b='<rect width="%d" height="%d" rx="22" fill="%s"/>'%(wd,h,bg)+T(wd/2,h/2+8,lab,sz,700,fg,HF,"middle",ls=1)
    save(nm,S(wd,h,b),wd,h)
# pillar cards
cards=[("growth","Marketing số","Chiến lược · Nội dung · Dữ liệu",C["blue"]),("ai","AI & Tự động hóa","AI Agent · Chatbot · Quy trình",C["green"]),("design","Thiết kế & Sáng tạo","Nhận diện · Hình ảnh · Video",C["orange"])]
for tone in ("dark","light"):
    d=tone=="dark"; c=col(d)
    for i,(ic,t,s_,cc) in enumerate(cards):
        W,H=908,150; body='<rect width="%d" height="%d" fill="none"/>'%(W,H)+card(0,0,W,H,ic,t,s_,cc,d,c)
        save("pillar-card_%s_%s"%(["marketing","ai","creative"][i],tone),S(W,H,body),W,H)
# number badges
for i,n in enumerate(["01","02","03","04"]):
    b='<circle cx="48" cy="48" r="46" fill="none" stroke="#2563FF" stroke-width="4"/>'+T(48,62,n,40,800,"#2563FF",HF,"middle")
    save("number-badge_%s"%n,S(96,96,b),96,96)
# quote mark + divider + url pill + brand line strip
defs=grad_def("qg",0,0,160,0,"#5B8CFF","#14D8C4"); save("quote-mark",S(160,170,T(0,160,"“",220,800,"url(#qg)",HF),defs),160,170)
save("divider-aqua",S(64,8,'<rect width="64" height="8" rx="4" fill="#14D8C4"/>'),64,8)
b='<rect x="2" y="2" width="%d" height="52" rx="26" fill="none" stroke="#2563FF" stroke-width="3"/>'%(len(WEBSITE_SHORT)*13+56)+T(28,36,WEBSITE_SHORT,22,600,"#2563FF",BF)
save("url-pill",S(len(WEBSITE_SHORT)*13+60,58,b),len(WEBSITE_SHORT)*13+60,58)
lg=logo.horizontal_parts("reversed","fs",False); ld,lb,lw,lh=logo.place(lg,0,0,height=44)
save("footer-strip_dark",S(1080,64,'<rect width="1080" height="64" fill="#0B1026"/>'+'<g transform="translate(24,10)">%s</g>'%lb+T(1056,40,BRAND_LINE,20,500,"#D9E2F2",BF,"end"),ld),1080,64,False)
lg=logo.horizontal_parts("color","fl",False); ld,lb,lw,lh=logo.place(lg,0,0,height=44)
save("footer-strip_light",S(1080,64,'<rect width="1080" height="64" fill="#FFFFFF"/><rect y="63" width="1080" height="1" fill="#D9E2F2"/>'+'<g transform="translate(24,10)">%s</g>'%lb+T(1056,40,BRAND_LINE,20,500,"#667085",BF,"end"),ld),1080,64,False)
print(sum(render.batch(jobs,6)),len(jobs))
# sheet
from PIL import Image
import glob
fs=[f for f in sorted(glob.glob(OUTD+"/04_Components/PNG/*.png"))]
cols_=[["button-primary","button-secondary-light","button-ghost-light"],["tag-ai","tag-automation","tag-creative","tag-insight","tag-new","tag-webinar"]]
sheet=Image.new("RGB",(1800,1500),(240,244,252)); d=Image.new("RGB",(1800,520),(11,16,38)); sheet.paste(d,(0,980))
def put(n,x,y,bg=None):
    im=Image.open(OUTD+"/04_Components/PNG/%s.png"%n).convert("RGBA"); sheet.paste(im,(x,y),im); return im.size
y=40; x=40
for n in ("button-primary","button-secondary-light","button-ghost-light"): w_,h_=put(n,x,y); x+=w_+30
x=40; y=150
for n in ("tag-ai","tag-automation","tag-creative","tag-insight","tag-new","tag-webinar"): w_,h_=put(n,x,y); x+=w_+24
x=40; y=240
for n in ("number-badge_01","number-badge_02","number-badge_03","number-badge_04","quote-mark","divider-aqua"): w_,h_=put(n,x,y); x+=w_+40
y=400
for i,nm in enumerate(("marketing","ai","creative")): put("pillar-card_%s_light"%nm,40+(i%1)*0,y+i*170)
put("url-pill",900,260)
for i,nm in enumerate(("marketing","ai","creative")): put("pillar-card_%s_dark"%nm,40,1010+i*170)
put("button-ghost-dark",1100,1010)
sheet.save(OUTD+"/04_Components/components-sheet.png")
