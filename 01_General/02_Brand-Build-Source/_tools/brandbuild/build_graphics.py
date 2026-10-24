import sys, math; sys.path.insert(0,"/tmp/brandbuild")
from cfg import *
import logo, render

jobs=[]
def add_png(svg,rel,W,H,transp=True): jobs.append((svg,os.path.join(OUT,rel),W,H,transp))

# ---------------------------------------------------------------- backgrounds
def glows(W,H,dark=True):
    if dark:
        return ('<defs><radialGradient id="g1" cx="0.78" cy="0.22" r="0.65"><stop offset="0" stop-color="#2563FF" stop-opacity=".55"/><stop offset="1" stop-color="#2563FF" stop-opacity="0"/></radialGradient>'
                '<radialGradient id="g2" cx="0.1" cy="0.95" r="0.6"><stop offset="0" stop-color="#14D8C4" stop-opacity=".28"/><stop offset="1" stop-color="#14D8C4" stop-opacity="0"/></radialGradient>'
                '<radialGradient id="g3" cx="0.95" cy="0.9" r="0.5"><stop offset="0" stop-color="#8B5CF6" stop-opacity=".3"/><stop offset="1" stop-color="#8B5CF6" stop-opacity="0"/></radialGradient></defs>'
                '<rect width="%d" height="%d" fill="#0B1026"/><rect width="%d" height="%d" fill="url(#g1)"/><rect width="%d" height="%d" fill="url(#g2)"/><rect width="%d" height="%d" fill="url(#g3)"/>'%((W,H)*4))
    return ('<defs><radialGradient id="g1" cx="0.85" cy="0.1" r="0.7"><stop offset="0" stop-color="#2563FF" stop-opacity=".16"/><stop offset="1" stop-color="#2563FF" stop-opacity="0"/></radialGradient>'
            '<radialGradient id="g2" cx="0.05" cy="1" r="0.6"><stop offset="0" stop-color="#14D8C4" stop-opacity=".18"/><stop offset="1" stop-color="#14D8C4" stop-opacity="0"/></radialGradient></defs>'
            '<rect width="%d" height="%d" fill="#F8FAFC"/><rect width="%d" height="%d" fill="url(#g1)"/><rect width="%d" height="%d" fill="url(#g2)"/>'%((W,H)*3))

def ribbon_bg(W,H,dark=True,cx=0.74,cy=0.6,wr=1.25,opacity=None):
    md,mb=logo.mark_color("rb")
    s=wr*W/logo.MARK_W if W>=H else wr*H/logo.MARK_W*1.15
    tx=cx*W-(logo.MARK_X0+logo.MARK_W/2)*s; ty=cy*H-(logo.MARK_H/2)*s
    op=opacity if opacity is not None else (0.92 if dark else 0.16)
    body=glows(W,H,dark)+'<g opacity="%s" transform="translate(%.1f,%.1f) scale(%.4f)">%s</g>'%(op,tx,ty,s,mb)
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d"><defs>%s</defs>%s</svg>'%(W,H,md,body)

def wave_lines(W,H,dark=True,n=44,amp=0.16,y0=0.62):
    b=glows(W,H,dark); defs='<linearGradient id="wl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2563FF"/><stop offset=".55" stop-color="#14D8C4"/><stop offset="1" stop-color="#8B5CF6"/></linearGradient>'
    for i in range(n):
        t=i/(n-1); pts=[]
        for k in range(0,121):
            x=W*k/120.0; u=k/120.0
            y=H*y0+H*amp*math.sin(u*math.pi*2.0+t*1.9)*(0.55+0.45*math.sin(u*math.pi*0.9+0.4))+(t-0.5)*H*0.30*(1-0.35*math.cos(u*math.pi*2))
            pts.append((x,y))
        d="M"+" L".join("%.1f %.1f"%p for p in pts)
        op=0.10+0.55*(1-abs(t-0.5)*2)
        b+='<path d="%s" fill="none" stroke="url(#wl)" stroke-width="1.6" opacity="%.2f"/>'%(d,op if dark else op*0.8)
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d"><defs>%s</defs>%s</svg>'%(W,H,defs,b)

SIZES={"16x9":(1920,1080),"1x1":(1080,1080),"9x16":(1080,1920)}
for tone in ("dark","light"):
    dk=tone=="dark"
    for r,(W,H) in SIZES.items():
        cx,cy,wr=(0.74,0.62,1.25) if r=="16x9" else ((0.7,0.66,1.35) if r=="1x1" else (0.62,0.74,2.0))
        s=ribbon_bg(W,H,dk,cx,cy,wr); w("04_Graphic_Elements/SVG/ribbon-background_%s_%s.svg"%(tone,r),s); add_png(s,"04_Graphic_Elements/PNG/ribbon-background_%s_%s.png"%(tone,r),W,H,False)
        s=wave_lines(W,H,dk,y0=0.6 if r!="9x16" else 0.7,amp=0.15 if r!="9x16" else 0.09); w("04_Graphic_Elements/SVG/wave-lines_%s_%s.svg"%(tone,r),s); add_png(s,"04_Graphic_Elements/PNG/wave-lines_%s_%s.png"%(tone,r),W,H,False)
# transparent wave overlay (no bg)
def wave_overlay(W=2400,H=900,n=46):
    s=wave_lines(W,H,True,n=n,amp=0.2,y0=0.5)
    s=s.replace(glows(W,H,True),"")
    return s
ov=wave_overlay(); w("04_Graphic_Elements/SVG/wave-lines_overlay_transparent.svg",ov); add_png(ov,"04_Graphic_Elements/PNG/wave-lines_overlay_transparent.png",2400,900,True)
# gradient orb
orb=('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800"><defs><radialGradient id="o" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="#7DF9FF"/><stop offset=".45" stop-color="#14D8C4"/><stop offset=".8" stop-color="#2563FF"/><stop offset="1" stop-color="#1B2BA8"/></radialGradient>'
     '<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset=".55" stop-color="#14D8C4" stop-opacity=".45"/><stop offset="1" stop-color="#14D8C4" stop-opacity="0"/></radialGradient></defs>'
     '<circle cx="400" cy="400" r="400" fill="url(#glow)"/><circle cx="400" cy="400" r="260" fill="url(#o)"/></svg>')
w("04_Graphic_Elements/SVG/gradient-orb.svg",orb); add_png(orb,"04_Graphic_Elements/PNG/gradient-orb.png",1200,1200,True)
# dot grid
dots='<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><circle cx="16" cy="16" r="1.6" fill="#2563FF" opacity=".35"/></svg>'
w("04_Graphic_Elements/SVG/dot-grid-tile.svg",dots)
# ribbon fragments (decorative crops, transparent)
md,mb=logo.mark_color("rf")
frag='<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s 0 %s %s"><defs>%s</defs>%s</svg>'%(logo.MARK_X0,logo.MARK_W,logo.MARK_H,md,mb)
w("04_Graphic_Elements/SVG/ribbon-mark-large.svg",frag); add_png(frag,"04_Graphic_Elements/PNG/ribbon-mark-large.png",2400,round(2400*logo.MARK_H/logo.MARK_W),True)
w("04_Graphic_Elements/README.md","""# Graphic elements

| File | Dùng cho |
|---|---|
| `ribbon-background_*` | Nền chủ đạo: ruy-băng từ logo phóng lớn, cắt tràn khung. 16:9 (slide, web hero), 1:1 (post), 9:16 (story/reel). Dark = bìa, tiêu đề lớn. Light = nội dung. |
| `wave-lines_*` | Nền họa tiết sóng (data / motion / growth) — nền phụ, section divider, nền slide nội dung. |
| `wave-lines_overlay_transparent` | Lớp sóng trong suốt để đặt chồng lên ảnh hoặc nền Midnight. |
| `gradient-orb` | Điểm nhấn tròn (lấy từ chấm của logo), dùng làm điểm nhấn hoặc "AI glow". |
| `ribbon-mark-large` | Ruy-băng nguyên bản độ phân giải cao (trong suốt). |
| `dot-grid-tile.svg` | Texture chấm cho nền tài liệu / UI (lặp lại). |

**Quy tắc:** giữ khoảng trắng, một yếu tố họa tiết chính trên mỗi layout; không đặt chữ thân bài lên vùng sáng của ruy-băng; không dùng ruy-băng đã chỉnh méo hoặc đổi màu.
""")

# ---------------------------------------------------------------- icons
ICONS={
"strategy":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/><path d="M12 12l6-6"/>',
"brand":'<path d="M6 3h12l4 6-10 12L2 9z"/><path d="M2 9h20M10 3 8 9l4 12 4-12-2-6"/>',
"content":'<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
"social":'<circle cx="6" cy="12" r="2.6"/><circle cx="18" cy="6" r="2.6"/><circle cx="18" cy="18" r="2.6"/><path d="M8.3 10.8l7.4-3.6M8.3 13.2l7.4 3.6"/>',
"website":'<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M3 9h18M7 14h6M6.5 6.5h.01M9 6.5h.01"/>',
"performance":'<path d="M3 11v3a1 1 0 0 0 1 1h2l5 4V6L6 10H4a1 1 0 0 0-1 1z"/><path d="M15 9a4 4 0 0 1 0 6M18 6.5a8 8 0 0 1 0 11"/>',
"seo":'<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5M8.2 11.4l2 2 3.6-4"/>',
"pr":'<path d="M5 4h11a1 1 0 0 1 1 1v14H7a2 2 0 0 1-2-2z"/><path d="M17 8h3v9a2 2 0 0 1-2 2M8 8h6M8 12h6M8 15.5h4"/>',
"data":'<path d="M3 21h18M6 21v-6M12 21v-10M18 21V5"/>',
"ecommerce":'<path d="M3 4h2.5l2 11h10.5l2-8H7"/><circle cx="9.5" cy="19" r="1.3"/><circle cx="17" cy="19" r="1.3"/>',
"ai":'<rect x="6" y="6" width="12" height="12" rx="2.5"/><path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3M10 15l2-6 2 6M10.8 13.4h2.4"/>',
"agent":'<rect x="5" y="8" width="14" height="11" rx="3"/><path d="M12 8V5.5M3 12v3M21 12v3M10 16.5h4"/><circle cx="12" cy="4.2" r="1.2"/><circle cx="9.3" cy="12.5" r=".9"/><circle cx="14.7" cy="12.5" r=".9"/>',
"automation":'<rect x="3" y="4" width="6" height="5" rx="1.2"/><rect x="15" y="4" width="6" height="5" rx="1.2"/><rect x="9" y="15" width="6" height="5" rx="1.2"/><path d="M6 9v3h12V9M12 12v3"/>',
"chatbot":'<path d="M4 5h16a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H10l-5 4v-4H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/><circle cx="8.5" cy="11" r=".9"/><circle cx="12" cy="11" r=".9"/><circle cx="15.5" cy="11" r=".9"/>',
"genai":'<path d="M10 4l1.8 5.2L17 11l-5.2 1.8L10 18l-1.8-5.2L3 11l5.2-1.8z"/><path d="M18 3v4M16 5h4M18 16v4M16 18h4"/>',
"design":'<path d="M12 2.5L18 11l-3.5 3.5h-5L6 11z"/><path d="M12 14.5V21M9 21h6"/><circle cx="12" cy="9.5" r="1.3"/>',
"photo":'<path d="M4 8h3l2-3h6l2 3h3a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><circle cx="12" cy="13.5" r="3.5"/>',
"video":'<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9.5v5l4.5-2.5z"/>',
"illustration":'<path d="M20 4L11 13"/><path d="M9.5 13.5c-2.3 0-4 1.6-4 3.8 0 1.2-.6 2-2 2.4 4.2 1.2 8.5-.2 8.5-3.6 0-1.4-1-2.6-2.5-2.6z"/>',
"intelligence":'<circle cx="12" cy="12" r="3"/><circle cx="12" cy="4" r="1.4"/><circle cx="12" cy="20" r="1.4"/><circle cx="4" cy="12" r="1.4"/><circle cx="20" cy="12" r="1.4"/><path d="M12 5.4V9M12 15v3.6M5.4 12H9M15 12h3.6"/>',
"ideas":'<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.4.4.5 1 .5 1.6V16h6v-.5c0-.6.1-1.2.5-1.6A6 6 0 0 0 12 3z"/>',
"speed":'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
"growth":'<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
"community":'<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20a6 6 0 0 1 12 0M15 20a5 5 0 0 1 6-4.5"/>',
"human-in-the-loop":'<circle cx="12" cy="7" r="3"/><path d="M5 20a7 7 0 0 1 14 0"/><path d="M17.5 3.5a9 9 0 0 1 3 4M6.5 3.5a9 9 0 0 0-3 4"/>',
"audit":'<path d="M9 3h6l1 2h3v16H5V5h3z"/><path d="M8.5 13l2.5 2.5 4.5-5"/>',
}
def icon_svg(name,color="#2563FF",size=24):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="%d" height="%d" fill="none" stroke="%s" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="%s">%s</svg>'%(size,size,color,name,ICONS[name])
for n in ICONS:
    w("05_Icons/SVG/%s.svg"%n,icon_svg(n))
    w("05_Icons/SVG_white/%s.svg"%n,icon_svg(n,"#FFFFFF"))
    w("05_Icons/SVG_currentColor/%s.svg"%n,icon_svg(n,"currentColor"))
    add_png(icon_svg(n,"#2563FF",256),"05_Icons/PNG/%s.png"%n,256,256,True)
    add_png(icon_svg(n,"#FFFFFF",256),"05_Icons/PNG_white/%s.png"%n,256,256,True)
# pillar tiles
pillars=[("marketing","Marketing số","#2563FF","growth"),("ai-automation","AI & Tự động hóa","#16A34A","ai"),("creative","Thiết kế & Sáng tạo","#F97316","design")]
for key,lab,col,ic in pillars:
    t='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><rect width="96" height="96" rx="24" fill="%s" fill-opacity=".12"/><g transform="translate(24,24) scale(2)" fill="none" stroke="%s" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">%s</g></svg>'%(col,col,ICONS[ic])
    w("05_Icons/Pillar_Tiles/pillar-%s.svg"%key,t); add_png(t,"05_Icons/Pillar_Tiles/pillar-%s.png"%key,384,384,True)
# sheet
cols=7; rows_=(len(ICONS)+cols-1)//cols; cw,ch=300,260
sh='<rect width="%d" height="%d" fill="#FFFFFF"/><text x="50" y="80" font-family="Plus Jakarta Sans" font-weight="800" font-size="46" fill="#0B1026">Icon system · 24 px grid · 1.75 px stroke · round caps</text>'%(cols*cw+100,rows_*ch+230)
for i,n in enumerate(ICONS):
    x=50+(i%cols)*cw; y=150+(i//cols)*ch
    sh+='<rect x="%d" y="%d" width="%d" height="%d" rx="28" fill="#F8FAFC" stroke="#D9E2F2"/><g transform="translate(%d,%d) scale(5)" fill="none" stroke="#2563FF" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">%s</g><text x="%d" y="%d" font-family="Inter" font-weight="600" font-size="22" fill="#111827" text-anchor="middle">%s</text>'%(x,y,cw-30,ch-30,x+(cw-30)/2-60,y+30,ICONS[n],x+(cw-30)/2,y+ch-50,n)
sheet='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">%s</svg>'%(cols*cw+100,rows_*ch+230,sh)
w("05_Icons/icon-sheet.svg",sheet); add_png(sheet,"05_Icons/icon-sheet.png",cols*cw+100,rows_*ch+230,False)
w("05_Icons/README.md","# Icon system\n\n- Lưới 24 px, nét **1.75 px**, đầu nét và góc bo tròn, không tô đặc.\n- Màu mặc định **Electric Blue #2563FF**; icon đại diện trụ dịch vụ dùng màu trụ (xanh dương / xanh lá / cam) — xem `Pillar_Tiles/`.\n- `SVG_currentColor/` dùng cho web/UI (kế thừa màu chữ); `SVG_white/` dùng trên nền tối.\n- Kích thước tối thiểu 16 px; hiển thị lý tưởng 24 / 32 / 48 px.\n- Không trộn icon từ bộ khác trong cùng một layout.\n\n"+", ".join(sorted(ICONS))+"\n")
print("jobs",len(jobs))
res=render.batch(jobs,workers=6); print("ok",sum(res),len(res))
