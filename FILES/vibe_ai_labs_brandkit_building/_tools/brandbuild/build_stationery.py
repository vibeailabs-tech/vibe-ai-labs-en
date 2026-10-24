import sys; sys.path.insert(0,"/tmp/brandbuild")
from cfg import *
import tpl, gfx, logo, render
from tpl import T, grad_def, wrap_svg, C, HF, BF, icon_g
jobs=[]
def pngjob(svg,rel,W,H,transp=False): jobs.append((svg,os.path.join(OUT,rel),W,H,transp))

# ---------------------------------------------------------------- business card (units: 0.1 mm), bleed 30
def card_front(bleed=0):
    W,H=900,540; x0=-bleed; y0=-bleed; vw=W+2*bleed; vh=H+2*bleed
    d,b=gfx.ribbon(vw,vh,True,cx=0.9,cy=1.0,wr=1.15,uid="cf")
    # shift origin for bleed
    lg=logo.stacked_parts("reversed","cs",True); ld,lb,lw,lh=logo.place(lg,0,0,width=440)
    body='<g transform="translate(%d,%d)">%s</g>'%(x0,y0,b)+'<g transform="translate(%.1f,%.1f)">%s</g>'%((W-lw)/2,(H-lh)/2,lb)
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%d %d %d %d"><defs>%s%s</defs>%s</svg>'%(x0,y0,vw,vh,d,ld,body)
def card_back(bleed=0):
    W,H=900,540; x0=-bleed; y0=-bleed; vw=W+2*bleed; vh=H+2*bleed
    body='<rect x="%d" y="%d" width="%d" height="%d" fill="#FFFFFF"/>'%(x0,y0,vw,vh)
    # ribbon fragment top-right
    md,mb=logo.mark_color("cb"); s=1.5
    body+='<g opacity=".10" transform="translate(%.1f,%.1f) scale(%.3f)">%s</g>'%(430-logo.MARK_X0*s,-60,s,mb)
    lg=logo.horizontal_parts("color","cl",False); ld,lb,lw,lh=logo.place(lg,60,60,width=250)
    body+=lb
    body+=T(60,270,FOUNDER,46,800,C["midnight"],HF,ls=-0.5)+T(60,314,FOUNDER_TITLE,22,600,C["blue"],BF)
    body+='<rect x="60" y="346" width="64" height="4" rx="2" fill="#14D8C4"/>'
    rows=[("mail",EMAIL),("website",WEBSITE_SHORT),("pin",ADDRESS1+", "+ADDRESS2)]
    y=392
    for ic,t in rows:
        body+=icon_g(ic if ic!="mail" else "chatbot",60,y-16,22,C["blue"],1.8)+T(94,y,t,20,500,C["ink"],BF); y+=40
    body+=T(W-60,H-48,BRAND_LINE,19,600,C["slate"],BF,"end")
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%d %d %d %d"><defs>%s%s</defs>%s</svg>'%(x0,y0,vw,vh,md,ld,body)
tpl.ICONS["mail"]='<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7l8.5 6 8.5-6"/>'
tpl.ICONS["pin"]='<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>'
def card_back(bleed=0, _orig=card_back):
    return _orig(bleed).replace('icon_g','icon_g')
# rebuild back with proper mail icon
def card_back2(bleed=0):
    W,H=900,540; x0=-bleed; y0=-bleed; vw=W+2*bleed; vh=H+2*bleed
    md,mb=logo.mark_color("cb"); s=1.5
    body='<rect x="%d" y="%d" width="%d" height="%d" fill="#FFFFFF"/>'%(x0,y0,vw,vh)
    body+='<g opacity=".10" transform="translate(%.1f,%.1f) scale(%.3f)">%s</g>'%(430-logo.MARK_X0*s,-60,s,mb)
    lg=logo.horizontal_parts("color","cl",False); ld,lb,lw,lh=logo.place(lg,60,60,width=250); body+=lb
    body+=T(60,270,FOUNDER,46,800,C["midnight"],HF,ls=-0.5)+T(60,314,FOUNDER_TITLE,22,600,C["blue"],BF)
    body+='<rect x="60" y="346" width="64" height="4" rx="2" fill="#14D8C4"/>'
    y=392
    for ic,t in (("mail",EMAIL),("website",WEBSITE_SHORT),("pin","21 Võ Trường Toản, An Khánh, TP. Hồ Chí Minh")):
        body+=icon_g(ic,60,y-17,22,C["blue"],1.8)+T(94,y,t,19,500,C["ink"],BF); y+=36
    body+=T(W-60,110,BRAND_LINE,19,600,C["slate"],BF,"end")
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%d %d %d %d"><defs>%s%s</defs>%s</svg>'%(x0,y0,vw,vh,md,ld,body)
for side,fn in (("front",card_front),("back",card_back2)):
    s=fn(0); w("06_Templates/Stationery/SVG/business-card-%s.svg"%side,s); pngjob(s,"06_Templates/Stationery/PNG/business-card-%s.png"%side,1063,638)
    sb=fn(30); w("06_Templates/Stationery/SVG/business-card-%s_bleed3mm.svg"%side,sb)

# ---------------------------------------------------------------- letterhead A4 (units 0.1mm)
def letterhead(sample=True):
    W,H=2100,2970
    md,mb=logo.mark_color("lh")
    body='<rect width="%d" height="%d" fill="#FFFFFF"/>'%(W,H)
    s=2.6; body+='<g opacity=".08" transform="translate(%.1f,%.1f) scale(%.3f)">%s</g>'%(1000-logo.MARK_X0*s,-180,s,mb)
    lg=logo.horizontal_parts("color","ll",False); ld,lb,lw,lh=logo.place(lg,160,170,width=560); body+=lb
    body+='<rect x="160" y="2680" width="1780" height="3" fill="#D9E2F2"/>'
    cols=[("ĐỊA CHỈ",[ADDRESS1,ADDRESS2]),("LIÊN HỆ",[EMAIL,WEBSITE_SHORT]),("KẾT NỐI",[FACEBOOK,XHANDLE])]
    for i,(h,ls_) in enumerate(cols):
        x=160+i*610; body+=T(x,2740,h,20,700,C["blue"],HF,ls=3)
        for j,l in enumerate(ls_): body+=T(x,2780+j*34,l,22,500,C["slate"],BF)
    if sample:
        body+=T(160,640,"[Ngày] tháng [tháng] năm [năm]",26,500,C["slate"],BF)
        body+=T(160,730,"Kính gửi: [Tên người nhận]",30,700,C["midnight"],HF)+T(160,774,"[Chức vụ · Doanh nghiệp]",24,500,C["slate"],BF)
        txt=["Vibe AI Labs kết hợp chiến lược Marketing, Trí tuệ nhân tạo (AI) và Sáng tạo để giúp doanh","nghiệp tăng trưởng nhanh hơn, tạo khác biệt rõ hơn và vận hành hiệu quả hơn.","","[Nội dung thư — mở đầu bằng bài toán của khách hàng, không bằng công nghệ. Dùng câu ngắn,","động từ cụ thể và kết thúc bằng một lời kêu gọi hành động rõ ràng.]"]
        for i,l in enumerate(txt): body+=T(160,920+i*52,l,26,400,C["ink"],BF)
        body+=T(160,1330,"Trân trọng,",26,400,C["ink"],BF)+T(160,1470,FOUNDER,30,800,C["midnight"],HF)+T(160,1512,FOUNDER_TITLE,22,500,C["slate"],BF)
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d"><defs>%s%s</defs>%s</svg>'%(W,H,md,ld,body)
for nm,sm in (("letterhead",False),("letterhead-sample",True)):
    s=letterhead(sm); w("06_Templates/Stationery/SVG/%s-A4.svg"%nm,s); pngjob(s,"06_Templates/Stationery/PNG/%s-A4.png"%nm,1240,1754)

# ---------------------------------------------------------------- proposal cover A4
def proposal(dark=True):
    W,H=2100,2970
    fg="#FFFFFF" if dark else C["midnight"]
    d,b=gfx.ribbon(W,H,dark,cx=0.62,cy=0.74,wr=2.1,uid="pc")
    lg=logo.horizontal_parts("reversed" if dark else "color","pl",False); ld,lb,lw,lh=logo.place(lg,170,190,width=620)
    gid="pg"; gd=grad_def(gid,170,0,1500,0,"#5B8CFF" if dark else "#2563FF","#14D8C4")
    body=b+lb+T(170,760,"PROPOSAL",30,700,C["aqua"] if dark else C["blue"],HF,ls=8)
    body+=T(170,900,"[Tên dự án /",118,800,fg,HF,ls=-2)+T(170,1030,"đề xuất]",118,800,"url(#pg)",HF,ls=-2)
    body+=T(170,1130,"Marketing × AI × Creative",34,500,"#D9E2F2" if dark else C["slate"],BF)
    body+=T(170,2640,"Chuẩn bị cho",22,600,"#D9E2F2" if dark else C["slate"],BF,ls=1)+T(170,2690,"[Tên khách hàng]",34,800,fg,HF)
    body+=T(1930,2690,"[Tháng / Năm]",30,600,fg,BF,"end")+T(1930,2640,"Phiên bản 1.0",22,600,"#D9E2F2" if dark else C["slate"],BF,"end",ls=1)
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d"><defs>%s%s%s</defs>%s</svg>'%(W,H,d,ld,gd,body)
for tone in ("dark","light"):
    s=proposal(tone=="dark"); w("06_Templates/Stationery/SVG/proposal-cover-A4_%s.svg"%tone,s); pngjob(s,"06_Templates/Stationery/PNG/proposal-cover-A4_%s.png"%tone,1240,1754)

# ---------------------------------------------------------------- zoom / meet virtual background + email banner
def vbg(dark):
    W,H=1920,1080
    d,b=gfx.ribbon(W,H,dark,cx=0.86,cy=0.58,wr=0.95,uid="zb")
    lg=logo.horizontal_parts("reversed" if dark else "color","zl",False); ld,lb,lw,lh=logo.place(lg,110,H-110-80,height=80)
    return wrap_svg(W,H,d+ld,b+lb)
for tone in ("dark","light"):
    s=vbg(tone=="dark"); w("06_Templates/Digital/SVG/virtual-background_%s.svg"%tone,s); pngjob(s,"06_Templates/Digital/PNG/virtual-background_%s.png"%tone,1920,1080)
res=render.batch(jobs,workers=6); print("png ok",sum(res),len(res))

# ---------------------------------------------------------------- email signature
logo_rel="vibe-ai-labs_icon_color_256px.png"
sig=f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><title>Chữ ký email – Vibe AI Labs</title></head>
<body style="margin:0;padding:16px;background:#ffffff">
<!-- HƯỚNG DẪN: 1) Tải {logo_rel} lên nơi lưu trữ công khai (website/CDN) và thay đường dẫn ảnh bên dưới. 2) Thay họ tên, chức danh. 3) Dán toàn bộ khối <table> vào phần chữ ký của Gmail/Outlook. -->
<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;color:#0B1026;font-size:14px;line-height:20px">
  <tr>
    <td style="padding-right:18px;border-right:3px solid #2563FF;vertical-align:middle">
      <img src="https://REPLACE-WITH-HOSTED-URL/{logo_rel}" width="96" alt="Vibe AI Labs" style="display:block;border:0">
    </td>
    <td style="padding-left:18px;vertical-align:middle">
      <div style="font-size:18px;line-height:24px;font-weight:700;color:#0B1026">{FOUNDER}</div>
      <div style="color:#2563FF;font-weight:600">{FOUNDER_TITLE} · Vibe AI Labs</div>
      <div style="color:#667085;padding-top:4px">{DESCRIPTOR}</div>
      <div style="padding-top:8px">
        <a href="mailto:{EMAIL}" style="color:#0B1026;text-decoration:none">{EMAIL}</a> &nbsp;·&nbsp;
        <a href="{WEBSITE}" style="color:#2563FF;text-decoration:none">{WEBSITE_SHORT}</a>
      </div>
      <div style="color:#667085;font-size:12px;padding-top:4px">{ADDRESS1}, {ADDRESS2}</div>
      <div style="color:#667085;font-size:12px;font-style:italic;padding-top:6px">{BRAND_LINE}</div>
    </td>
  </tr>
</table>
</body></html>
'''
w("06_Templates/Stationery/email-signature.html",sig)
shutil.copy(OUT+"/01_Logos/PNG/vibe-ai-labs_icon_color_256px.png",OUT+"/06_Templates/Stationery/"+logo_rel)
print("stationery done")
