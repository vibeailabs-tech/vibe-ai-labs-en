import sys, os, re; sys.path.insert(0,"/tmp/brandbuild")
from cfg import *
import logo, render
K="file:///tmp/kit_out"
CSS="""
@font-face{font-family:'Plus Jakarta Sans';src:url('file:///tmp/fonts/PlusJakartaSans.ttf');font-weight:200 800}
@font-face{font-family:'Inter';src:url('file:///tmp/fonts/Inter.ttf');font-weight:100 900}
*{box-sizing:border-box;margin:0;padding:0}
:root{--mid:#0B1026;--blue:#2563FF;--aqua:#14D8C4;--vio:#8B5CF6;--cloud:#F8FAFC;--ink:#111827;--slate:#667085;--line:#D9E2F2;--green:#16A34A;--orange:#F97316}
html,body{background:#fff}
body{font-family:'Inter',Arial,sans-serif;color:var(--ink);font-size:10.5pt;line-height:1.5;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1,h2,h3,h4,.hf{font-family:'Plus Jakarta Sans','Inter',Arial,sans-serif;color:var(--mid);letter-spacing:-.02em}
.page{position:relative;overflow:hidden;page-break-after:always;break-after:page;background:#fff}
.land{width:297mm;height:210mm}.port{width:210mm;height:297mm}
.pad{position:absolute;left:18mm;right:18mm;top:28mm;bottom:18mm;zoom:1.14}
.pad-p{position:absolute;left:16mm;right:16mm;top:30mm;bottom:20mm}
.hdr{position:absolute;left:18mm;right:18mm;top:10mm;display:flex;justify-content:space-between;align-items:center}
.hdr img{height:6.4mm}
.eyebrow{font-family:'Plus Jakarta Sans';font-weight:700;font-size:8pt;letter-spacing:.2em;text-transform:uppercase;color:var(--blue)}
.ftr{position:absolute;left:18mm;right:18mm;bottom:8mm;display:flex;justify-content:space-between;font-size:7.5pt;color:var(--slate)}
.dark{background:var(--mid);color:#fff}.dark h1,.dark h2,.dark h3,.dark h4{color:#fff}.dark .ftr{color:#9FB0D6}.dark .eyebrow{color:var(--aqua)}
h1{font-size:30pt;line-height:1.08;font-weight:800}h2{font-size:21pt;line-height:1.12;font-weight:800}h3{font-size:12.5pt;font-weight:800;line-height:1.2}h4{font-size:10pt;font-weight:700}
.lead{font-size:11.5pt;color:var(--slate);max-width:170mm;margin-top:3mm}
.dark .lead{color:#C9D5F2}
.grid{display:grid;gap:5mm}.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}.g5{grid-template-columns:repeat(5,1fr)}.g6{grid-template-columns:repeat(6,1fr)}
.card{background:#fff;border:1px solid var(--line);border-radius:5mm;padding:5mm}
.card.soft{background:var(--cloud)}
.card.d{background:var(--mid);color:#fff;border-color:var(--mid)}.card.d h2,.card.d h3,.card.d h4{color:#fff}
.small{font-size:8.6pt;color:var(--slate)}.tiny{font-size:7.4pt;color:var(--slate)}
.tag{display:inline-block;padding:.6mm 3mm;border-radius:99px;background:rgba(37,99,255,.1);color:var(--blue);font-weight:600;font-size:7.6pt}
ul.b{list-style:none}ul.b li{position:relative;padding-left:4.5mm;margin:1.2mm 0}ul.b li:before{content:"";position:absolute;left:0;top:2.2mm;width:1.8mm;height:1.8mm;border-radius:50%;background:var(--blue)}
ul.x li:before{background:#E11D48}ul.ok li:before{background:var(--green)}
table{border-collapse:collapse;width:100%;font-size:8.8pt}th{text-align:left;font-family:'Plus Jakarta Sans';font-size:7.6pt;letter-spacing:.12em;text-transform:uppercase;color:var(--slate);padding:2mm 3mm;border-bottom:2px solid var(--line)}td{padding:2.2mm 3mm;border-bottom:1px solid var(--line);vertical-align:top}
.sw{border-radius:4mm;height:26mm;border:1px solid rgba(0,0,0,.05)}
.chip{display:inline-flex;align-items:center;gap:2mm;font-size:8pt}.dot{width:3mm;height:3mm;border-radius:50%}
.stage{border-radius:5mm;display:flex;align-items:center;justify-content:center;border:1px solid var(--line);overflow:hidden;position:relative}
.stage img{max-width:80%;max-height:80%}
.num{font-family:'Plus Jakarta Sans';font-weight:800;font-size:30pt;color:var(--blue);line-height:1}
.kv{display:grid;grid-template-columns:34mm 1fr;gap:2mm 4mm;font-size:9pt}.kv b{font-family:'Plus Jakarta Sans';color:var(--mid)}
.rule{height:1.2mm;width:16mm;border-radius:1mm;background:var(--aqua);margin:3mm 0}
.badge-ok{color:var(--green);font-weight:700}.badge-x{color:#E11D48;font-weight:700}
.btn{display:inline-block;padding:2.6mm 6mm;border-radius:99px;background:var(--blue);color:#fff;font-weight:600;font-size:9pt}
.btn.g{background:transparent;color:var(--blue);box-shadow:inset 0 0 0 .6mm var(--blue)}.btn.s{background:#fff;color:var(--mid);border:1px solid var(--line)}
img.fit{width:100%;display:block;border-radius:3mm}
"""
def html_doc(pages, css_extra="", pagesize="297mm 210mm"):
    return '<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>@page{size:%s;margin:0}%s%s</style></head><body>%s</body></html>'%(pagesize,CSS,css_extra,"".join(pages))
def L(name): return K+"/01_Logos/PNG/vibe-ai-labs_"+name+".png"
def logoimg(kind="horizontal_color",h=None,w=None,extra=""):
    st=("height:%smm;"%h if h else "")+("width:%smm;"%w if w else "")
    return '<img src="%s" style="%s%s">'%(L(kind+"_1000px" if kind.startswith("horizontal") else kind+"_800px" if kind.startswith("stacked") else kind+"_1024px"),st,extra)
class Doc:
    def __init__(self,title,total=None,ver="v2.0",land=True):
        self.pages=[];self.title=title;self.n=0;self.ver=ver;self.land=land
    def page(self,body,section="",dark=False,header=True,footer=True,bg="",cls=""):
        self.n+=1
        hdr=""
        if header:
            hdr='<div class="hdr"><span class="eyebrow" style="color:var(--slate)">%s</span><img src="%s"></div>'%(self.title,L("horizontal_reversed_1000px" if dark else "horizontal_color_1000px"))
        ftr='<div class="ftr"><span>Vibe AI Labs · %s · %s</span><span>%02d</span></div>'%(self.title,self.ver,self.n) if footer else ""
        self.pages.append('<section class="page %s %s %s">%s%s%s%s</section>'%("land" if self.land else "port","dark" if dark else "",cls,bg,hdr,body,ftr))
    def save(self,rel_pdf,html_path=None,pagesize=None):
        html=html_doc(self.pages,pagesize=pagesize or ("297mm 210mm" if self.land else "210mm 297mm"))
        hp=html_path or "/tmp/brandbuild/_doc_%s.html"%re.sub(r"\W+","_",self.title)
        open(hp,"w",encoding="utf8").write(html)
        out=os.path.join(globals().get("PDF_OUT",OUT),rel_pdf); os.makedirs(os.path.dirname(out),exist_ok=True)
        ok=render.html_to_pdf(hp,out); return ok,hp
