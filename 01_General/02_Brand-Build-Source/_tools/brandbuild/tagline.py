import io
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
_cache={}
def _font(path,wght):
    k=(path,wght)
    if k not in _cache:
        f=TTFont(path)
        f=instancer.instantiateVariableFont(f,{"wght":wght,**({"opsz":14} if "opsz" in [a.axisTag for a in f["fvar"].axes] else {})},inplace=False)
        _cache[k]=f
    return _cache[k]
JAK="/tmp/fonts/PlusJakartaSans.ttf"
INTER="/tmp/fonts/Inter.ttf"
def text_outline(text, font=JAK, wght=600, size=100.0, tracking=0.0, x=0.0, y=0.0):
    """returns (path_d, width, cap_height). y = baseline."""
    f=_font(font,wght); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f["head"].unitsPerEm
    sc=size/upm; pen_d=""; cx=0.0
    for i,ch in enumerate(text):
        gn=cmap.get(ord(ch))
        if gn is None: continue
        sp=SVGPathPen(gs, ntos=lambda v:("%.2f"%v).rstrip("0").rstrip("."))
        tp=TransformPen(sp,(sc,0,0,-sc,x+cx,y))
        gs[gn].draw(tp)
        pen_d+=sp.getCommands()
        cx+=gs[gn].width*sc+tracking*size
    cap=f["OS/2"].sCapHeight*sc
    return pen_d, cx-tracking*size, cap
def fit_text(text, target_w, font=JAK, wght=600, tracking=0.24, x=0.0, y=0.0):
    d,w,cap=text_outline(text,font,wght,100.0,tracking,0,0)
    s=100.0*target_w/w
    return text_outline(text,font,wght,s,tracking,x,y)
