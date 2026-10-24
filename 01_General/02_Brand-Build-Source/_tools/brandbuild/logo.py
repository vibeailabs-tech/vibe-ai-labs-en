"""Vibe AI Labs - vector logo builder (traced from the official master PNG)."""
import json

D = json.load(open("/tmp/brandbuild/logo_paths.json"))
OX, OY = D["origin"]
MARK_W, MARK_H = 849.0, 467.0     # mark bbox in lockup-local coords (starts x=62,y=0)
MARK_X0 = 62.0                    # left of mark bbox
WORD_Y0 = 494.0                   # top of wordmark in stacked lockup
STACK_W, STACK_H = 958.0, 625.0

import sys
sys.path.insert(0, "/tmp/brandbuild")
import tagline as _tg
TAGLINE = "AI-POWERED GROWTH & CREATIVE AGENCY"
_TG_D, _TG_W, _TG_CAP = _tg.fit_text(TAGLINE, 956.0, wght=600, tracking=0.26, x=0, y=0)
TAG_GAP = 46.0
TAG_COLORS = {"color": "#667085", "reversed": "#D9E2F2", "white": "#FFFFFF", "black": "#0B1026", "blue": "#2563FF"}

def tagline_group(kind, tx=0.0, ty=0.0):
    return '<path fill="%s" transform="translate(%.2f,%.2f)" d="%s"/>' % (TAG_COLORS[kind], tx, ty, _TG_D)

MIDNIGHT = "#0B1026"
WHITE = "#FFFFFF"


def _grad(gid, g):
    stops = "".join('<stop offset="%.3f" stop-color="%s"/>' % (o, c) for o, c in g["stops"])
    return ('<linearGradient id="%s" gradientUnits="userSpaceOnUse" x1="%s" y1="%s" x2="%s" y2="%s">%s</linearGradient>'
            % (gid, g["x1"], g["y1"], g["x2"], g["y2"], stops))


def mark_color(p="m"):
    """Full-colour ribbon mark, local coords of the stacked lockup."""
    defs = ""
    body = ""
    for r in D["regions"]:
        gid = "%s-%s" % (p, r["name"])
        defs += _grad(gid, r["grad"])
        body += '<path fill="url(#%s)" d="%s"/>' % (gid, r["d"])
    dot = D["dot"]
    defs += _grad(p + "-dot", dot["grad"])
    body += '<circle cx="%s" cy="%s" r="%s" fill="url(#%s-dot)"/>' % (dot["cx"], dot["cy"], dot["r"], p)
    return defs, body


# luminance levels used by the one-colour mark (white = full ink)
MONO_LEVELS = {"back": 0.52, "front": 0.80, "core": 1.0, "under": 0.70}


def mark_mono(color, p="mm"):
    """One-colour mark: faces carried by tonal steps through a luminance mask."""
    gray = lambda v: "#%02X%02X%02X" % ((int(255 * v),) * 3)
    shapes = ""
    for r in D["regions"]:
        shapes += '<path fill="%s" d="%s"/>' % (gray(MONO_LEVELS[r["name"]]), r["d"])
    dot = D["dot"]
    shapes += '<circle cx="%s" cy="%s" r="%s" fill="#FFFFFF"/>' % (dot["cx"], dot["cy"], dot["r"])
    defs = ('<mask id="%s-mask" maskUnits="userSpaceOnUse" x="%d" y="-4" width="%d" height="%d" '
            'style="mask-type:luminance">%s</mask>' % (p, MARK_X0 - 4, MARK_W + 8, MARK_H + 8, shapes))
    body = ('<rect x="%d" y="-4" width="%d" height="%d" fill="%s" mask="url(#%s-mask)"/>'
            % (MARK_X0 - 4, MARK_W + 8, MARK_H + 8, color, p))
    return defs, body


def word(text_color, ai="gradient", p="w", ai_color=None):
    """Wordmark paths in stacked-lockup coords. ai: 'gradient' | 'solid'"""
    defs = ""
    if ai == "gradient":
        defs = _grad(p + "-ai", D["ai_grad"])
        ai_fill = "url(#%s-ai)" % p
    else:
        ai_fill = ai_color or text_color
    body = ('<g fill-rule="evenodd"><path fill="%s" d="%s"/><path fill="%s" d="%s"/><path fill="%s" d="%s"/></g>'
            % (text_color, D["word"]["vibe"], ai_fill, D["word"]["ai"], text_color, D["word"]["labs"]))
    return defs, body


def svg(vb, defs, body, title="Vibe AI Labs", bg=None, w=None, h=None):
    x, y, vw, vh = vb
    size = ""
    if w and h:
        size = ' width="%s" height="%s"' % (w, h)
    bgrect = '<rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>' % (x, y, vw, vh, bg) if bg else ""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s %s %s %s"%s role="img" aria-label="%s">'
            '<title>%s</title><defs>%s</defs>%s%s</svg>' % (x, y, vw, vh, size, title, title, defs, bgrect, body))


# ---------------------------------------------------------------- lockups
def _variant(kind, p):
    """returns (mark_defs, mark_body, word_defs, word_body) for a colour variant"""
    if kind == "color":      # for light backgrounds
        md, mb = mark_color(p + "m")
        wd, wb = word(MIDNIGHT, "gradient", p + "w")
    elif kind == "reversed":  # for dark backgrounds
        md, mb = mark_color(p + "m")
        wd, wb = word(WHITE, "gradient", p + "w")
    elif kind == "white":
        md, mb = mark_mono(WHITE, p + "m")
        wd, wb = word(WHITE, "solid", p + "w")
    elif kind == "black":
        md, mb = mark_mono(MIDNIGHT, p + "m")
        wd, wb = word(MIDNIGHT, "solid", p + "w")
    elif kind == "blue":
        md, mb = mark_mono("#2563FF", p + "m")
        wd, wb = word("#2563FF", "solid", p + "w")
    else:
        raise ValueError(kind)
    return md, mb, wd, wb


def stacked(kind="color", bg=None, pad=0, p="s", tagline=False):
    md, mb, wd, wb = _variant(kind, p)
    body = mb + '<g transform="translate(0,0)">' + wb + "</g>"
    h = STACK_H
    if tagline:
        ty = 623.0 + TAG_GAP + _TG_CAP
        body += tagline_group(kind, 0.0, ty)
        h = ty + 3.0
    return svg((-pad, -pad, STACK_W + 2 * pad, h + 2 * pad), md + wd, body, bg=bg)


H_MARK_SCALE = 0.50
H_GAP = 78.0


def horizontal_parts(kind="color", p="h", tagline=False):
    md, mb, wd, wb = _variant(kind, p)
    s = H_MARK_SCALE
    mark_w, mark_h = MARK_W * s, MARK_H * s
    word_h = 129.0
    block_h = word_h + ((TAG_GAP * 0.85 + _TG_CAP) if tagline else 0.0)
    total_h = max(mark_h, block_h)
    mark_ty = (total_h - mark_h) / 2.0
    block_ty = (total_h - block_h) / 2.0
    mark_tx = -MARK_X0 * s
    word_tx = mark_w + H_GAP
    body = ('<g transform="translate(%.2f,%.2f) scale(%.4f)">%s</g>' % (mark_tx, mark_ty, s, mb)
            + '<g transform="translate(%.2f,%.2f)">%s</g>' % (word_tx, block_ty - WORD_Y0, wb))
    if tagline:
        body += tagline_group(kind, word_tx, block_ty + word_h + TAG_GAP * 0.85 + _TG_CAP)
    return md + wd, body, word_tx + 956.0, total_h


def horizontal(kind="color", bg=None, pad=0, p="h", tagline=False):
    defs, body, W, H = horizontal_parts(kind, p, tagline)
    return svg((-pad, -pad, W + 2 * pad, H + 2 * pad), defs, body, bg=bg)


def stacked_parts(kind="color", p="s", tagline=False):
    md, mb, wd, wb = _variant(kind, p)
    body = mb + wb
    h = STACK_H
    if tagline:
        ty = 623.0 + TAG_GAP + _TG_CAP
        body += tagline_group(kind, 0.0, ty)
        h = ty + 3.0
    return md + wd, body, STACK_W, h


def place(parts, x, y, width=None, height=None):
    """returns (defs, group) placing a *_parts() result at x,y scaled to width or height"""
    defs, body, W, H = parts
    s = (width / W) if width else (height / H)
    return defs, '<g transform="translate(%.2f,%.2f) scale(%.5f)">%s</g>' % (x, y, s, body), W * s, H * s


def icon(kind="color", pad=0, bg=None, p="i"):
    """Mark only, tight crop."""
    if kind in ("color", "reversed"):
        md, mb = mark_color(p)
    elif kind == "white":
        md, mb = mark_mono(WHITE, p)
    elif kind == "black":
        md, mb = mark_mono(MIDNIGHT, p)
    else:
        md, mb = mark_mono("#2563FF", p)
    return svg((MARK_X0 - pad, -pad, MARK_W + 2 * pad, MARK_H + 2 * pad), md, mb, bg=bg)


def icon_square(kind="color", size=1024, scale=0.62, bg=None, radius=0, p="q", circle=False):
    """Square (or rounded / circular) app-icon with mark centred."""
    if kind == "mono-white":
        md, mb = mark_mono(WHITE, p)
    else:
        md, mb = mark_color(p)
    s = size * scale / MARK_W
    tx = (size - MARK_W * s) / 2 - MARK_X0 * s
    ty = (size - MARK_H * s) / 2
    shape = ""
    if bg:
        if circle:
            shape = '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (size / 2, size / 2, size / 2, bg)
        else:
            shape = '<rect width="%s" height="%s" rx="%s" fill="%s"/>' % (size, size, radius, bg)
    body = shape + '<g transform="translate(%.2f,%.2f) scale(%.5f)">%s</g>' % (tx, ty, s, mb)
    return svg((0, 0, size, size), md, body, w=size, h=size)
