import sys; sys.path.insert(0,"/tmp/brandbuild")
import os, shutil
from cfg import *
import logo, render
from PIL import Image
jobs=[]
def add(name, svg, widths, folder="01_Logos"):
    w_(folder+"/SVG/"+name+".svg", svg)
    x,y,vw,vh=vb(svg)
    for W in widths:
        H=round(W*vh/vw)
        jobs.append((svg, os.path.join(OUT,folder,"PNG",name+("_%dpx"%W)+".png"), W, H, True))
def w_(p,t): w(p,t)
os.makedirs(OUT,exist_ok=True)
PAD=6
for kind in ("color","reversed","white","black"):
    for tg in (False,True):
        suf="_tagline" if tg else ""
        add("vibe-ai-labs_stacked_%s%s"%(kind,suf), logo.stacked(kind,pad=PAD,tagline=tg,p="a"), [2000,800])
        add("vibe-ai-labs_horizontal_%s%s"%(kind,suf), logo.horizontal(kind,pad=PAD,tagline=tg,p="b"), [2400,1000])
    add("vibe-ai-labs_icon_%s"%kind, logo.icon(kind,pad=PAD,p="c"), [1024,256])
# app icons / avatars
def sq(name, svg, sizes, folder="01_Logos/App_Icons_Avatars"):
    w(folder+"/SVG/"+name+".svg", svg)
    for S in sizes: jobs.append((svg, os.path.join(OUT,folder,"PNG",name+"_%d.png"%S), S, S, True))
sq("app-icon_midnight", logo.icon_square("color",1024,0.64,C["midnight"],radius=230,p="d"), [1024,512,180])
sq("app-icon_cloud",   logo.icon_square("color",1024,0.64,C["cloud"],radius=230,p="e"), [1024,512])
sq("app-icon_blue",    logo.icon_square("mono-white",1024,0.64,C["blue"],radius=230,p="f"), [1024,512])
sq("avatar_circle_midnight", logo.icon_square("color",1080,0.62,C["midnight"],circle=True,p="g"), [1080,400])
sq("avatar_square_midnight", logo.icon_square("color",1080,0.62,C["midnight"],radius=0,p="h"), [1080,400])
sq("avatar_square_cloud",    logo.icon_square("color",1080,0.62,C["cloud"],radius=0,p="i"), [1080,400])
# favicons
fav="01_Logos/Favicon"
fsvg=logo.icon_square("color",512,0.70,C["midnight"],radius=112,p="j")
w(fav+"/favicon.svg",fsvg)
for S in (16,32,48,64,96,128,180,192,256,512):
    jobs.append((fsvg,os.path.join(OUT,fav,"PNG","favicon-%d.png"%S),S,S,True))
w(fav+"/safari-pinned-tab.svg", logo.icon("black",pad=10,p="k"))
w(fav+"/site.webmanifest", json.dumps({"name":BRAND,"short_name":BRAND,"icons":[{"src":"favicon-192.png","sizes":"192x192","type":"image/png"},{"src":"favicon-512.png","sizes":"512x512","type":"image/png"}],"theme_color":C["midnight"],"background_color":C["midnight"],"display":"standalone"},indent=2))
w(fav+"/head-snippet.html", '''<!-- Paste into <head>. Copy files from 01_Logos/Favicon to your site root. -->
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/favicon-180.png">
<link rel="mask-icon" href="/safari-pinned-tab.svg" color="#0B1026">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0B1026">
''')
print("rendering",len(jobs))
res=render.batch(jobs,workers=6)
print("ok",sum(res),"of",len(res))
# ico
ims=[Image.open(os.path.join(OUT,fav,"PNG","favicon-%d.png"%s)).convert("RGBA") for s in (16,32,48,64)]
ims[3].save(os.path.join(OUT,fav,"favicon.ico"),sizes=[(16,16),(32,32),(48,48),(64,64)],append_images=ims[:3])
# official master
om="01_Logos/Official_Master"
src="/Users/henryle/Desktop/vibe_ai_labs/brandkit"
shutil.copy(src+"/01_Logos/Official/PNG/vibe-ai-labs-official-primary-no-tagline.png",os.path.join(OUT,om)+"/" if os.path.isdir(os.path.join(OUT,om)) else (os.makedirs(os.path.join(OUT,om),exist_ok=True) or os.path.join(OUT,om)+"/"))
shutil.copy(src+"/99_Reference/vibe-ai-labs-official-logo-source-with-tagline.png",os.path.join(OUT,om)+"/")
w(om+"/README.txt","""OFFICIAL MASTER ARTWORK (raster, supplied by the brand owner, 1254 x 1254, dark background)

- vibe-ai-labs-official-primary-no-tagline.png  -> primary master (no descriptor)
- vibe-ai-labs-official-logo-source-with-tagline.png -> same artwork with descriptor line

The vector files in ../SVG were rebuilt (traced) from this master so the logo can be used on any background
and at any size. If a designer later supplies the original vector (AI/SVG/PDF), replace the files in
../SVG and ../PNG and keep the same file names.
""")
