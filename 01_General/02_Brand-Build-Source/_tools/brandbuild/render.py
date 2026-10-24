import subprocess, os, tempfile, pathlib
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FONT_CSS = """
@font-face{font-family:'Plus Jakarta Sans';src:url('file:///tmp/fonts/PlusJakartaSans.ttf');font-weight:200 800;}
@font-face{font-family:'Inter';src:url('file:///tmp/fonts/Inter.ttf');font-weight:100 900;}
"""
import shutil
def _run(args):
    ud=tempfile.mkdtemp(prefix="chr_")
    try:
        return subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars","--force-device-scale-factor=1","--user-data-dir="+ud,"--no-first-run","--disable-extensions","--allow-file-access-from-files"]+args,
                          stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=180)
    finally:
        shutil.rmtree(ud,ignore_errors=True)
def html_to_png(html, out, w, h, transparent=True, wait=800):
    os.makedirs(os.path.dirname(out),exist_ok=True)
    d=tempfile.mkdtemp(prefix="rend_")
    p=os.path.join(d,"p.html"); open(p,"w",encoding="utf8").write(html)
    ww,hh=max(w,520),h+170          # headless window includes browser chrome; render bigger and crop
    tmp=os.path.join(d,"shot.png")
    args=["--screenshot="+tmp,"--window-size=%d,%d"%(ww,hh),"--virtual-time-budget=%d"%wait]
    if transparent: args.append("--default-background-color=00000000")
    _run(args+["file://"+p])
    if not os.path.exists(tmp): return False
    from PIL import Image
    im=Image.open(tmp); im=im.crop((0,0,w,h)); im.save(out)
    shutil.rmtree(d,ignore_errors=True)
    return True
def svg_to_png(svg_text, out, w, h, transparent=True, inline=True):
    html=("<!doctype html><meta charset=utf-8><style>%s html,body{margin:0;padding:0;background:transparent}svg{display:block;width:%dpx;height:%dpx}</style>%s"
          %(FONT_CSS,w,h,svg_text))
    return html_to_png(html,out,w,h,transparent)
def html_to_pdf(html_path, out, landscape=False):
    _run(["--print-to-pdf="+out,"--no-pdf-header-footer","--virtual-time-budget=4000","file://"+html_path])
    return os.path.exists(out)

from concurrent.futures import ThreadPoolExecutor
def batch(jobs, workers=6):
    """jobs: list of (svg_text, out, w, h, transparent)"""
    def f(j):
        ok=svg_to_png(j[0],j[1],j[2],j[3],j[4])
        if not ok: print("FAILED",j[1])
        return ok
    with ThreadPoolExecutor(workers) as ex: return list(ex.map(f,jobs))
