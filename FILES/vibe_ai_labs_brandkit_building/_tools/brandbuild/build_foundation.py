import sys; sys.path.insert(0,"/tmp/brandbuild")
import struct, colorsys, urllib.request
from cfg import *
import render

def hex2rgb(h): h=h.lstrip("#"); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def rgb2hex(r): return "#%02X%02X%02X"%tuple(int(round(max(0,min(255,v)))) for v in r)
def hsl(h):
    r,g,b=[v/255 for v in hex2rgb(h)]; hh,l,s=colorsys.rgb_to_hls(r,g,b); return (round(hh*360),round(s*100),round(l*100))
def cmyk(h):
    r,g,b=[v/255 for v in hex2rgb(h)]; k=1-max(r,g,b)
    if k>=1: return (0,0,0,100)
    return tuple(round(v*100) for v in ((1-r-k)/(1-k),(1-g-k)/(1-k),(1-b-k)/(1-k),k))
def lum(h):
    f=lambda c:(c/255/12.92) if c/255<=0.03928 else (((c/255)+0.055)/1.055)**2.4
    r,g,b=[f(v) for v in hex2rgb(h)]; return .2126*r+.7152*g+.0722*b
def cr(a,b):
    la,lb=lum(a),lum(b); hi,lo=max(la,lb),min(la,lb); return (hi+.05)/(lo+.05)
def mix(a,b,t): return rgb2hex([x*(1-t)+y*t for x,y in zip(hex2rgb(a),hex2rgb(b))])

CORE=[("Midnight","midnight","#0B1026","Trust · depth · strategy","Nền tối chính, chữ tiêu đề trên nền sáng"),
      ("Electric Blue","blue","#2563FF","Innovation · momentum","Màu hành động: CTA, link, điểm nhấn chính"),
      ("Aqua","aqua","#14D8C4","Growth · freshness","Điểm nhấn tăng trưởng, gradient, dữ liệu tích cực"),
      ("Violet Glow","violet","#8B5CF6","Creativity · experimentation","Nhấn sáng tạo, gradient phụ, tag Creativity"),
      ("Cloud","cloud","#F8FAFC","Clarity · space","Nền sáng chính, khoảng thở")]
SUPPORT=[("Ink","ink","#111827","Chữ thân bài trên nền sáng"),("Slate","slate","#667085","Chữ phụ, chú thích, nhãn"),
         ("Line","line","#D9E2F2","Đường kẻ, viền, nền thẻ"),("White","white","#FFFFFF","Nền trắng, chữ trên nền tối")]
SERVICE=[("Marketing số / Digital Marketing","marketing","#2563FF"),("Trí tuệ nhân tạo (AI) & Tự động hóa / AI & Automation","ai","#16A34A"),("Thiết kế & Sáng tạo / Design & Creative Studio","creative","#F97316")]
LOGO=[("Logo Navy","#000667"),("Logo Blue","#0258FE"),("Logo Cyan","#00F9FE")]
GRAD=[("Growth","Electric Blue → Aqua","#2563FF","#14D8C4",135),("Creative","Violet Glow → Electric Blue","#8B5CF6","#2563FF",135),
      ("Depth","Midnight → Electric Blue","#0B1026","#2563FF",135),("Spectrum","Logo ribbon (Navy → Blue → Cyan)","#0B2C9D","#00F9FE",135)]

# ---------------- csv / json / css / gpl / ase
rows=["Group,Name,Token,HEX,RGB,HSL,CMYK (approx),Role"]
allc=[]
for n,t,h,m,u in CORE: rows.append('Core,%s,%s,%s,"%d %d %d","%d %d%% %d%%","%d %d %d %d","%s — %s"'%((n,t,h)+hex2rgb(h)+hsl(h)+cmyk(h)+(m,u))); allc.append((n,h))
for n,t,h,u in SUPPORT: rows.append('Support,%s,%s,%s,"%d %d %d","%d %d%% %d%%","%d %d %d %d","%s"'%((n,t,h)+hex2rgb(h)+hsl(h)+cmyk(h)+(u,))); allc.append((n,h))
for n,t,h in SERVICE: rows.append('Service accent,%s,%s,%s,"%d %d %d","%d %d%% %d%%","%d %d %d %d","Phân biệt trụ dịch vụ"'%((n,t,h)+hex2rgb(h)+hsl(h)+cmyk(h)))
for n,h in LOGO: rows.append('Logo artwork,%s,,%s,"%d %d %d","%d %d%% %d%%","%d %d %d %d","Chỉ dùng trong logo / ribbon"'%((n,h)+hex2rgb(h)+hsl(h)+cmyk(h))); allc.append((n,h))
w("02_Color/colors.csv","﻿"+"\n".join(rows)+"\n")
w("02_Color/CMYK-NOTE.txt","CMYK values are straight RGB->CMYK conversions for reference only. For print, proof against a physical swatch or ask the printer for the closest Pantone/Coated match before production.\n")
w("02_Color/vibe-ai-labs.gpl","GIMP Palette\nName: Vibe AI Labs\nColumns: 5\n#\n"+"".join("%3d %3d %3d %s\n"%(hex2rgb(h)+(n,)) for n,h in allc))
def ase(colors):
    blocks=b""; n=0
    for name,h in colors:
        r,g,b=[v/255 for v in hex2rgb(h)]
        nm=(name+"\0").encode("utf-16-be")
        body=struct.pack(">H",len(name)+1)+nm+b"RGB "+struct.pack(">fff",r,g,b)+struct.pack(">H",2)
        blocks+=struct.pack(">HI",1,len(body))+body; n+=1
    return b"ASEF"+struct.pack(">HHI",1,0,n)+blocks
w("02_Color/vibe-ai-labs.ase",ase(allc))
# tint scales
scales={}
for key,base in (("blue","#2563FF"),("aqua","#14D8C4"),("violet","#8B5CF6"),("midnight","#0B1026"),("slate","#667085")):
    sc={}
    for step,t in ((50,.92),(100,.84),(200,.68),(300,.5),(400,.25)): sc[str(step)]=mix(base,"#FFFFFF",t)
    sc["500"]=base
    for step,t in ((600,.16),(700,.32),(800,.5),(900,.68)): sc[str(step)]=mix(base,"#000000",t)
    scales[key]=sc
# contrast
text=[("Midnight","#0B1026"),("Ink","#111827"),("Slate","#667085"),("Electric Blue","#2563FF"),("Aqua","#14D8C4"),("Violet Glow","#8B5CF6"),("White","#FFFFFF"),("Cloud","#F8FAFC")]
bgs=[("White","#FFFFFF"),("Cloud","#F8FAFC"),("Midnight","#0B1026"),("Electric Blue","#2563FF")]
md="# Contrast matrix (WCAG 2.1)\n\nTỷ lệ tương phản giữa màu chữ (hàng) và màu nền (cột). **AA text ≥ 4.5**, **AA large text / UI ≥ 3.0**. ✅ = đạt AA, 🔸 = chỉ dùng cho chữ lớn (≥ 24 px hoặc ≥ 19 px đậm) / thành phần UI, ❌ = không dùng làm chữ.\n\n| Text \\ Background | "+" | ".join(b for b,_ in bgs)+" |\n|---|"+"---|"*len(bgs)+"\n"
cm={}
for tn,th in text:
    cells=[]
    for bn,bh in bgs:
        if th==bh: cells.append("—"); continue
        r=cr(th,bh); cm[(tn,bn)]=r
        mark="✅" if r>=4.5 else ("🔸" if r>=3 else "❌")
        cells.append("%s %.2f"%(mark,r))
    md+="| %s | %s |\n"%(tn," | ".join(cells))
md+="\n## Quy tắc rút ra\n\n- **Aqua #14D8C4 không dùng làm chữ trên nền sáng** (1.8:1). Aqua chỉ dùng làm màu nền/nhấn, hoặc làm chữ trên Midnight (≈ 10.4:1).\n- **Electric Blue #2563FF** đạt AA cho chữ thường trên White/Cloud (≈ 4.9:1). Trên Midnight chỉ đạt cho chữ lớn / UI.\n- **Violet Glow #8B5CF6** chỉ dùng cho chữ lớn hoặc tag; không dùng cho đoạn văn.\n- Nút CTA: nền Electric Blue + chữ White (≈ 4.9:1) ✅.\n- Chữ thân bài: Ink hoặc Midnight trên nền White/Cloud; White trên nền Midnight.\n- Gradient chỉ dùng cho tiêu đề lớn, ruy-băng, nền và chuyển động; không đặt đoạn văn trực tiếp lên vùng gradient sáng.\n"
w("02_Color/contrast-matrix.md",md)
colors_json={"core":{t:{"name":n,"hex":h,"rgb":list(hex2rgb(h)),"hsl":list(hsl(h)),"meaning":m} for n,t,h,m,u in CORE},
 "support":{t:{"name":n,"hex":h,"rgb":list(hex2rgb(h))} for n,t,h,u in SUPPORT},
 "service":{t:{"name":n,"hex":h} for n,t,h in SERVICE},
 "logo":{n.lower().replace(" ","_"):h for n,h in LOGO},
 "gradients":{n.lower():{"from":a,"to":b,"angle":ang,"css":"linear-gradient(%ddeg, %s, %s)"%(ang,a,b)} for n,_,a,b,ang in GRAD},
 "scales":scales}
w("02_Color/colors.json",json.dumps(colors_json,indent=2,ensure_ascii=False))
w("02_Color/gradients.css",":root{\n"+"".join("  --vibe-gradient-%s: linear-gradient(%ddeg, %s 0%%, %s 100%%);\n"%(n.lower(),ang,a,b) for n,_,a,b,ang in GRAD)+"  --vibe-gradient-spectrum-3: linear-gradient(135deg, #0B2C9D 0%, #2563FF 48%, #00F9FE 100%);\n  --vibe-gradient-hero-dark: radial-gradient(1200px 600px at 75% 20%, rgba(37,99,255,.45), transparent 60%), radial-gradient(900px 500px at 15% 90%, rgba(20,216,196,.25), transparent 60%), #0B1026;\n}\n")

# ---------------- palette poster
def swatch(x,y,wd,ht,hexv,name,sub,txt):
    s='<rect x="%d" y="%d" width="%d" height="%d" rx="28" fill="%s"%s/>'%(x,y,wd,ht,hexv,' stroke="#D9E2F2" stroke-width="2"' if hexv in("#F8FAFC","#FFFFFF") else "")
    s+='<text x="%d" y="%d" font-family="Plus Jakarta Sans" font-weight="800" font-size="30" fill="#0B1026">%s</text>'%(x+4,y+ht+44,name)
    s+='<text x="%d" y="%d" font-family="Inter" font-weight="600" font-size="22" fill="#111827">%s · RGB %d %d %d</text>'%(x+4,y+ht+76,hexv,*hex2rgb(hexv))
    s+='<text x="%d" y="%d" font-family="Inter" font-size="19" fill="#667085">%s</text>'%(x+4,y+ht+106,sub)
    return s
Wd,Ht=2400,1500
b='<rect width="%d" height="%d" fill="#F8FAFC"/>'%(Wd,Ht)
b+='<text x="100" y="130" font-family="Plus Jakarta Sans" font-weight="800" font-size="64" fill="#0B1026">Bảng màu · Color Palette</text><text x="100" y="180" font-family="Inter" font-size="26" fill="#667085">Vibe AI Labs · Ideas. Intelligence. Real Growth.</text>'
sw=(Wd-200-4*36)//5
for i,(n,t,h,m,u) in enumerate(CORE): b+=swatch(100+i*(sw+36),240,sw,300,h,n,m,"")
b+='<text x="100" y="720" font-family="Plus Jakarta Sans" font-weight="800" font-size="34" fill="#0B1026">Màu hỗ trợ</text>'
for i,(n,t,h,u) in enumerate(SUPPORT): b+=swatch(100+i*(sw+36),760,sw,120,h,n,u,"")
b+='<text x="%d" y="720" font-family="Plus Jakarta Sans" font-weight="800" font-size="34" fill="#0B1026">Màu theo trụ dịch vụ</text>'%(100+4*(sw+36))
sv=[("Marketing số","#2563FF"),("AI &amp; Tự động hóa","#16A34A"),("Thiết kế &amp; Sáng tạo","#F97316")]
for i,(n,h) in enumerate(sv):
    yy=760+i*54; b+='<circle cx="%d" cy="%d" r="18" fill="%s"/><text x="%d" y="%d" font-family="Inter" font-weight="600" font-size="22" fill="#0B1026">%s  %s</text>'%(100+4*(sw+36)+18,yy+14,h,100+4*(sw+36)+48,yy+22,n,h)
b+='<text x="100" y="1100" font-family="Plus Jakarta Sans" font-weight="800" font-size="34" fill="#0B1026">Gradient</text><defs>'
for i,(n,d_,a,c2,ang) in enumerate(GRAD): b+='<linearGradient id="gg%d" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'%(i,a,c2)
b+='</defs>'
gw=(Wd-200-3*36)//4
for i,(n,d_,a,c2,ang) in enumerate(GRAD):
    x=100+i*(gw+36); b+='<rect x="%d" y="1140" width="%d" height="120" rx="24" fill="url(#gg%d)"/><text x="%d" y="1304" font-family="Plus Jakarta Sans" font-weight="800" font-size="26" fill="#0B1026">%s</text><text x="%d" y="1336" font-family="Inter" font-size="20" fill="#667085">%s</text>'%(x,gw,i,x+4,n,x+4,d_)
b+='<text x="100" y="1440" font-family="Inter" font-size="20" fill="#667085">Quy tắc 60-30-10: 60% Cloud/White hoặc Midnight · 30% Midnight/Ink + Electric Blue · 10% Aqua, Violet và màu trụ dịch vụ.</text>'
pal='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">%s</svg>'%(Wd,Ht,b)
w("02_Color/color-palette.svg",pal); render.svg_to_png(pal,os.path.join(OUT,"02_Color/color-palette.png"),Wd,Ht,False)
# contrast PNG
cells=""; cw,ch=420,120; x0,y0=330,200
for j,(bn,bh) in enumerate(bgs): cells+='<text x="%d" y="%d" font-family="Inter" font-weight="700" font-size="24" fill="#0B1026" text-anchor="middle">%s</text>'%(x0+j*cw+cw/2,y0-40,"nền "+bn)
for i,(tn,th) in enumerate(text):
    cells+='<text x="40" y="%d" font-family="Inter" font-weight="700" font-size="24" fill="#0B1026">chữ %s</text>'%(y0+i*ch+ch/2+8,tn)
    for j,(bn,bh) in enumerate(bgs):
        if th==bh: continue
        r=cr(th,bh); mk="AA" if r>=4.5 else ("Large" if r>=3 else "Fail")
        cells+='<rect x="%d" y="%d" width="%d" height="%d" fill="%s" stroke="#D9E2F2"/><text x="%d" y="%d" font-family="Plus Jakarta Sans" font-weight="800" font-size="40" fill="%s" text-anchor="middle">Aa</text><text x="%d" y="%d" font-family="Inter" font-weight="600" font-size="20" fill="%s" text-anchor="middle">%.2f · %s</text>'%(x0+j*cw,y0+i*ch,cw,ch,bh,x0+j*cw+cw/2-70,y0+i*ch+ch/2+14,th,x0+j*cw+cw/2+50,y0+i*ch+ch/2+8,th,r,mk)
sv2='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2100 1260"><rect width="2100" height="1260" fill="#FFFFFF"/><text x="40" y="70" font-family="Plus Jakarta Sans" font-weight="800" font-size="44" fill="#0B1026">Contrast matrix · WCAG 2.1</text>%s</svg>'%cells
w("02_Color/contrast-matrix.svg",sv2); render.svg_to_png(sv2,os.path.join(OUT,"02_Color/contrast-matrix.png"),2100,1260,False)

# ---------------- typography
os.makedirs(OUT+"/03_Typography/fonts",exist_ok=True)
import shutil as sh
sh.copy("/tmp/fonts/PlusJakartaSans.ttf",OUT+"/03_Typography/fonts/PlusJakartaSans[wght].ttf")
sh.copy("/tmp/fonts/Inter.ttf",OUT+"/03_Typography/fonts/Inter[opsz,wght].ttf")
for fam,u in (("PlusJakartaSans","plusjakartasans"),("Inter","inter")):
    try:
        data=urllib.request.urlopen("https://github.com/google/fonts/raw/main/ofl/%s/OFL.txt"%u,timeout=30).read()
        w("03_Typography/fonts/OFL-%s.txt"%fam,data)
    except Exception as e: print("OFL fail",fam,e)
w("03_Typography/fonts/README.txt","Plus Jakarta Sans and Inter are free, open-source fonts licensed under the SIL Open Font License 1.1 (see OFL-*.txt).\nThey are variable fonts: install the .ttf files to use every weight. Both fully support Vietnamese.\n\nSources: https://fonts.google.com/specimen/Plus+Jakarta+Sans · https://fonts.google.com/specimen/Inter\n")
w("03_Typography/fonts.css","""/* Web usage - host the files or use Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

:root{
  --font-headline: 'Plus Jakarta Sans', 'Inter', Arial, sans-serif;
  --font-body: 'Inter', Arial, sans-serif;
}
body{font-family:var(--font-body);font-size:16px;line-height:1.6;color:#111827}
h1,h2,h3,h4{font-family:var(--font-headline);color:#0B1026;letter-spacing:-0.02em}
""")
SCALE=[("Display","Plus Jakarta Sans",800,72,80,"-0.03em","Hero, bìa, tiêu đề chiến dịch"),
       ("H1","Plus Jakarta Sans",700,56,64,"-0.02em","Tiêu đề trang"),
       ("H2","Plus Jakarta Sans",700,40,48,"-0.02em","Tiêu đề mục"),
       ("H3","Plus Jakarta Sans",700,28,36,"-0.01em","Tiêu đề thẻ, khối"),
       ("H4","Plus Jakarta Sans",600,22,30,"0","Tiêu đề phụ"),
       ("Body L","Inter",400,18,28,"0","Đoạn dẫn, mô tả chính"),
       ("Body","Inter",400,16,26,"0","Nội dung chuẩn"),
       ("Small","Inter",400,14,22,"0","Ghi chú, mô tả phụ"),
       ("Caption","Inter",500,12,18,"0.01em","Chú thích hình, metadata"),
       ("Overline","Plus Jakarta Sans",700,12,16,"0.2em","Nhãn trên tiêu đề, IN HOA"),
       ("Button","Inter",600,15,20,"0","Nút, UI")]
md="# Type scale\n\n| Style | Font | Weight | Size / Line (px) | Tracking | Dùng cho |\n|---|---|---|---|---|---|\n"+"".join("| %s | %s | %d | %d / %d | %s | %s |\n"%x for x in SCALE)
md+="\n## Nguyên tắc\n\n- Tiêu đề: **Plus Jakarta Sans** (Bold/ExtraBold). Thân bài và UI: **Inter**.\n- Tối đa 2 họ chữ trên một sản phẩm; tối đa 3 cỡ chữ trên một màn hình/slide.\n- Line-height thân bài 1.5–1.6 (tiếng Việt có dấu cần khoảng thở). Độ dài dòng 55–75 ký tự.\n- Căn trái là mặc định; chỉ căn giữa cho tiêu đề ngắn trên bìa/banner.\n- Chữ IN HOA chỉ dùng cho Overline và tagline (có giãn chữ 0.2–0.26em).\n- Không dùng chữ nghiêng cho tiêu đề; không đặt tiêu đề gradient lên nền sáng tương phản thấp.\n- Fallback: `Arial, sans-serif`. Không thay wordmark bằng bất kỳ font nào — luôn dùng file logo.\n- Tương đương khi không có font: dùng Inter cho cả tiêu đề (Bold/ExtraBold).\n"
w("03_Typography/type-scale.md",md)
rowsvg=""; y=340
for n,f,wt,sz,lh,tr,use in SCALE:
    shown=min(sz,64); rowsvg+='<text x="60" y="%d" font-family="%s" font-weight="%d" font-size="%d" fill="#0B1026" letter-spacing="%s">%s</text>'%(y,f,wt,shown,("0" if tr=="0" else tr.replace("em","em")),"Ý tưởng. Trí tuệ. Tăng trưởng thực." if sz>=18 else ("Vibe AI Labs — Marketing × AI × Creative" if n!="Overline" else "MARKETING × AI × CREATIVE"))
    rowsvg+='<text x="1500" y="%d" font-family="Inter" font-size="20" fill="#667085">%s · %s %d · %d/%d</text>'%(y-6,n,f.split()[0],wt,sz,lh)
    y+=max(shown,24)+44
H=y+60
head='<text x="60" y="110" font-family="Plus Jakarta Sans" font-weight="800" font-size="56" fill="#0B1026">Typography</text><text x="60" y="160" font-family="Inter" font-size="26" fill="#667085">Headline: Plus Jakarta Sans · Body/UI: Inter · Hỗ trợ đầy đủ tiếng Việt</text><text x="60" y="210" font-family="Inter" font-size="22" fill="#111827">Aa Bb Cc Dd Ee Ăă Ââ Êê Ôô Ơơ Ưư Đđ  0123456789  &amp; @ # % → ×</text>'
spec='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 %d"><rect width="2000" height="%d" fill="#FFFFFF"/>%s%s</svg>'%(H,H,head,rowsvg)
w("03_Typography/typography-specimen.svg",spec); render.svg_to_png(spec,os.path.join(OUT,"03_Typography/typography-specimen.png"),2000,H,False)

# ---------------- tokens
tokens={"$schema":"brand tokens v2","brand":{"name":BRAND,"descriptor":DESCRIPTOR,"descriptor_vi":DESCRIPTOR_VI,"brand_line":BRAND_LINE,"campaign_line":CAMPAIGN_LINE,"pillar_order":["marketing","ai_automation","creative"],"website":WEBSITE,"email":EMAIL},
 "colors":dict(C, **{"logo_navy":"#000667","logo_blue":"#0258FE","logo_cyan":"#00F9FE"}),
 "service_accents":{"digital_marketing":"#2563FF","ai_automation":"#16A34A","creative_studio":"#F97316"},
 "gradients":{n.lower():"linear-gradient(%ddeg, %s, %s)"%(ang,a,b) for n,_,a,b,ang in GRAD},
 "typography":{"headline":"Plus Jakarta Sans","body":"Inter","fallback":"Arial, sans-serif","weights":{"regular":400,"medium":500,"semibold":600,"bold":700,"extrabold":800},
   "scale":{n.lower().replace(" ","_"):{"font":f,"weight":wt,"size":sz,"line_height":lh,"tracking":tr} for n,f,wt,sz,lh,tr,u in SCALE}},
 "spacing":{"2xs":2,"xs":4,"sm":8,"md":16,"lg":24,"xl":40,"2xl":64,"3xl":96},
 "radius":{"xs":6,"sm":12,"md":20,"lg":32,"pill":999},
 "shadow":{"sm":"0 1px 2px rgba(11,16,38,.08)","md":"0 8px 24px rgba(11,16,38,.10)","lg":"0 24px 64px rgba(11,16,38,.18)","glow":"0 0 48px rgba(37,99,255,.45)"},
 "breakpoints":{"sm":640,"md":768,"lg":1024,"xl":1280,"2xl":1536},
 "motion":{"fast":"150ms","base":"250ms","slow":"500ms","easing":"cubic-bezier(.22,1,.36,1)"},
 "logo":{"min_width_horizontal_px":140,"min_width_stacked_px":96,"min_icon_px":24,"clear_space":"1x = height of the logo dot (circle)"},
 "voice":["Intelligent","Clear","Creative","Experimental","Forward-looking"]}
w("09_Brand_Tokens/brand-tokens.json",json.dumps(tokens,indent=2,ensure_ascii=False))
css=":root{\n"
for k,v in tokens["colors"].items(): css+="  --vibe-color-%s: %s;\n"%(k.replace("_","-"),v)
for k,v in tokens["service_accents"].items(): css+="  --vibe-accent-%s: %s;\n"%(k.replace("_","-"),v)
for k,v in tokens["gradients"].items(): css+="  --vibe-gradient-%s: %s;\n"%(k,v)
css+="  --vibe-font-headline: 'Plus Jakarta Sans', 'Inter', Arial, sans-serif;\n  --vibe-font-body: 'Inter', Arial, sans-serif;\n"
for k,v in tokens["spacing"].items(): css+="  --vibe-space-%s: %dpx;\n"%(k,v)
for k,v in tokens["radius"].items(): css+="  --vibe-radius-%s: %dpx;\n"%(k,v)
for k,v in tokens["shadow"].items(): css+="  --vibe-shadow-%s: %s;\n"%(k,v)
for k,v in tokens["motion"].items(): css+="  --vibe-motion-%s: %s;\n"%(k,v)
css+="}\n\n/* Components */\n.vibe-btn{display:inline-flex;align-items:center;gap:8px;padding:14px 24px;border-radius:999px;background:var(--vibe-color-blue);color:#fff;font:600 15px/20px var(--vibe-font-body);border:0;cursor:pointer;transition:transform var(--vibe-motion-base) var(--vibe-motion-easing)}\n.vibe-btn:hover{transform:translateY(-1px)}\n.vibe-btn--ghost{background:transparent;color:var(--vibe-color-blue);box-shadow:inset 0 0 0 2px var(--vibe-color-blue)}\n.vibe-card{background:#fff;border:1px solid var(--vibe-color-line);border-radius:var(--vibe-radius-md);padding:var(--vibe-space-lg)}\n.vibe-tag{display:inline-block;padding:4px 12px;border-radius:999px;background:rgba(37,99,255,.1);color:var(--vibe-color-blue);font:600 12px/16px var(--vibe-font-body)}\n"
w("09_Brand_Tokens/tokens.css",css)
tw="module.exports = {\n  theme: {\n    extend: {\n      colors: {\n        vibe: {\n"+"".join("          %s: '%s',\n"%(k.replace("_","-"),v) for k,v in tokens["colors"].items())+"        },\n      },\n      fontFamily: {\n        headline: ['Plus Jakarta Sans', 'Inter', 'Arial', 'sans-serif'],\n        body: ['Inter', 'Arial', 'sans-serif'],\n      },\n      borderRadius: { xs: '6px', sm: '12px', md: '20px', lg: '32px' },\n      boxShadow: { 'vibe-md': '0 8px 24px rgba(11,16,38,.10)', 'vibe-lg': '0 24px 64px rgba(11,16,38,.18)', 'vibe-glow': '0 0 48px rgba(37,99,255,.45)' },\n      backgroundImage: {\n"+"".join("        'vibe-%s': '%s',\n"%(k,v) for k,v in tokens["gradients"].items())+"      },\n    },\n  },\n};\n"
w("09_Brand_Tokens/tailwind.config.js",tw)
def w3c(o):
    if isinstance(o,dict): return {k:w3c(v) for k,v in o.items()}
    return o
dt={"color":{k:{"$value":v,"$type":"color"} for k,v in tokens["colors"].items()},
    "service":{k:{"$value":v,"$type":"color"} for k,v in tokens["service_accents"].items()},
    "font":{"headline":{"$value":"Plus Jakarta Sans","$type":"fontFamily"},"body":{"$value":"Inter","$type":"fontFamily"}},
    "spacing":{k:{"$value":"%dpx"%v,"$type":"dimension"} for k,v in tokens["spacing"].items()},
    "radius":{k:{"$value":"%dpx"%v,"$type":"dimension"} for k,v in tokens["radius"].items()}}
w("09_Brand_Tokens/design-tokens.w3c.json",json.dumps(dt,indent=2))
print("foundation done")
