"""Re-set the text of the three original service posters (I. / II. / III.) in the brand typefaces.

The posters are flat PNGs with no source: the text was drawn in a Montserrat-like face and the logo is the
legacy wave mark. This script erases every text block (black-hat mask + inpainting), then draws the same copy
in Plus Jakarta Sans / Inter and the official logo on top. The 3D illustrations are left untouched.

Each new block is fitted to the ink box of the block it replaces: Chrome passes measure the ink of every block
at a trial size, then the overlay is rendered at the fitted size and position.

Run:  python3 retype_legacy_posters.py [--out DIR] [--debug]
Sources are read from git (commit SRC_REV) so the script can be re-run on its own output.
"""
import argparse
import html
import io
import pathlib
import shutil
import statistics
import subprocess
import tempfile

import cv2
import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[4]
BK = ROOT / "02_Brandkit" / "01_General-Brandkit"
FONTS = BK / "03_Typography" / "fonts"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SRC_REV = "9d30642"
REF = 40  # first trial font size (px) of the measuring passes
CELL = 420
LABEL_LH = 1.3  # line height of the service names in the final render

LOGO_SVG = ((BK / "01_Logos" / "SVG" / "vibe-ai-labs_horizontal_color.svg").read_text()
            .replace('width="1470" height="246"', "", 1).replace("translate(502.50,-441.75)", "translate(502.50,-428.75)", 1))

CSS = f"""
@font-face{{font-family:'Plus Jakarta Sans';src:url('{(FONTS / "PlusJakartaSans[wght].ttf").as_uri()}');font-weight:200 800}}
@font-face{{font-family:'Inter';src:url('{(FONTS / "Inter[opsz,wght].ttf").as_uri()}');font-weight:100 900}}
*{{margin:0;padding:0}} body{{position:relative}}
.e{{position:absolute;white-space:nowrap}}
.title{{font:800 1em/1.1 'Plus Jakarta Sans';letter-spacing:-.03em;word-spacing:.1em}}
.sub{{font:400 1em/1.38 'Inter'}}
.tag{{font:500 1em/1.55 'Inter';letter-spacing:.38em;text-align:right}}
.foot{{font:500 1em/1.2 'Inter';letter-spacing:.26em}}
.num{{font:500 1em/1 'Plus Jakarta Sans';letter-spacing:-.03em}}
.label{{font:800 1em/var(--lh,1.1) 'Plus Jakarta Sans';letter-spacing:-.025em;word-spacing:.12em}}
.grad{{-webkit-background-clip:text;background-clip:text;color:transparent;padding:.3em .1em;margin:-.3em -.1em}}
"""


def E(kind, text, *rects, pick="any", align="left", group=None):
    return dict(kind=kind, text=text, rects=rects, pick=pick, align=align, group=group or kind)


def cards(spec):
    out = []
    for n, num_rect, label_rects, text in spec:
        out.append(E("num", n, num_rect))
        out.append(E("label", text, *label_rects))
    return out


TAG = "TURN\nBRANDS\nINTO\nGROWTH"
POSTERS = {
    "I. DỊCH VỤ MARKETING SỐ.png": dict(
        logo=dict(rect=(55, 40, 425, 118), left=64.4, top=41.5, width=347),
        els=[
            E("title", "DỊCH VỤ", (55, 140, 470, 250), pick="dark"),
            E("title", "MARKETING SỐ", (55, 215, 760, 322), pick="color"),
            E("sub", "10 nhóm dịch vụ toàn diện cho tăng trưởng thương hiệu.", (55, 326, 820, 366)),
            E("tag", TAG, (940, 40, 1095, 152), align="right"),
            E("foot", "VIBE AI LABS", (40, 1358, 200, 1382)),
            E("foot", "MARKETING × AI × CREATIVE", (630, 1358, 1090, 1382), align="right"),
        ] + cards([
            ("01", (68, 405, 140, 462), [(68, 462, 275, 536)], "CHIẾN LƯỢC\nMARKETING"),
            ("02", (598, 405, 675, 462), [(598, 462, 825, 536)], "XÂY DỰNG\nTHƯƠNG HIỆU"),
            ("03", (68, 592, 145, 648), [(68, 648, 270, 722)], "SÁNG TẠO &\nNỘI DUNG"),
            ("04", (598, 592, 675, 648), [(598, 652, 809, 694)], "MẠNG XÃ HỘI"),
            ("05", (68, 780, 145, 834), [(68, 836, 280, 908)], "WEBSITE &\nNỀN TẢNG SỐ"),
            ("06", (598, 780, 675, 834), [(598, 840, 890, 908)], "TRUYỀN THÔNG &\nPERFORMANCE"),
            ("07", (68, 968, 145, 1022), [(68, 1022, 292, 1120)], "SEO & TÌM KIẾM\nBẰNG AI"),
            ("08", (598, 968, 675, 1022), [(598, 1026, 880, 1092)], "PR & KOL"),
            ("09", (68, 1163, 145, 1218), [(68, 1222, 278, 1290)], "DỮ LIỆU &\nTĂNG TRƯỞNG"),
            ("10", (598, 1163, 675, 1218), [(598, 1218, 905, 1308)], "ECOMMERCE &\nSOCIAL COMMERCE"),
        ])),
    "II. DỊCH VỤ TRÍ TUỆ NHÂN TẠO (AI) & TỰ ĐỘNG HÓA.png": dict(
        logo=dict(rect=(55, 40, 425, 118), left=64.4, top=41.5, width=347),
        els=[
            E("title", "DỊCH VỤ", (55, 150, 470, 262), pick="dark"),
            E("title", "AI & TỰ ĐỘNG HÓA", (55, 240, 895, 360), pick="color"),
            E("sub", "04 nhóm dịch vụ giúp doanh nghiệp ứng dụng AI hiệu quả.", (55, 362, 870, 400)),
            E("tag", TAG, (940, 40, 1095, 155), align="right"),
            E("foot", "VIBE AI LABS", (38, 1350, 200, 1372)),
            E("foot", "MARKETING × AI × CREATIVE", (610, 1350, 1090, 1372), align="right"),
        ] + cards([
            ("01", (65, 452, 150, 522), [(65, 528, 350, 618)], "CHIẾN LƯỢC &\nTƯ VẤN AI"),
            ("02", (595, 452, 700, 522), [(595, 528, 866, 618)], "TỰ ĐỘNG HÓA\nAI & AI AGENT"),
            ("03", (65, 902, 165, 972), [(65, 978, 295, 1068)], "CHATBOT &\nTRỢ LÝ AI"),
            ("04", (595, 902, 695, 972), [(595, 975, 1066, 1066)], "NỘI DUNG &\nSÁNG TẠO VỚI AI TẠO SINH"),
        ])),
    "III. THIẾT KẾ & SÁNG TẠO.png": dict(
        logo=dict(rect=(50, 28, 395, 97), left=57.3, top=27.9, width=388),
        els=[
            E("title", "DỊCH VỤ", (50, 125, 420, 215), pick="dark"),
            E("title", "THIẾT KẾ & SÁNG TẠO", (50, 195, 955, 302), pick="color"),
            E("sub", "Biến ý tưởng thành những hình ảnh và nội dung ấn tượng, giúp thương hiệu\nnổi bật và tạo khác biệt trên mọi điểm chạm.",
              (50, 303, 960, 366)),
            E("tag", TAG, (1065, 40, 1220, 150), align="right"),
            E("foot", "VIBE AI LABS", (50, 1192, 215, 1214)),
            E("foot", "MARKETING × AI × CREATIVE", (600, 1192, 1205, 1214), align="right"),
        ] + cards([
            ("01", (70, 410, 160, 468), [(72, 472, 301, 618)], "THIẾT KẾ\nNHẬN DIỆN\nTHƯƠNG HIỆU\n& LOGO"),
            ("02", (475, 410, 565, 468), [(478, 472, 780, 546), (478, 546, 640, 584)], "THIẾT KẾ ĐỒ HỌA\n& TRUYỀN THÔNG\nTHỊ GIÁC"),
            ("03", (855, 410, 945, 468), [(858, 478, 1078, 546), (858, 546, 1005, 584)], "MINH HOẠ &\nNGHỆ THUẬT\nTHỊ GIÁC"),
            ("04", (72, 845, 165, 905), [(78, 912, 333, 984)], "NHIẾP ẢNH &\nSẢN XUẤT VIDEO"),
            ("05", (660, 845, 750, 905), [(668, 912, 915, 1018)], "SÁNG TẠO &\nSẢN XUẤT BẰNG\nAI TẠO SINH"),
        ])),
}


def chrome(page_html, w, h, transparent):
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="retype_"))
    try:
        (tmp / "p.html").write_text(page_html, encoding="utf8")
        args = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=1",
                f"--user-data-dir={tmp / 'ud'}", "--no-first-run", "--disable-extensions", "--allow-file-access-from-files",
                f"--screenshot={tmp / 's.png'}", f"--window-size={w},{h + 200}", "--virtual-time-budget=1500"]
        if transparent:
            args.append("--default-background-color=00000000")
        subprocess.run(args + [(tmp / "p.html").as_uri()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180, check=True)
        return Image.open(tmp / "s.png").convert("RGBA").crop((0, 0, w, h))  # window is taller than the page: crop
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def hx(c):
    return "#%02X%02X%02X" % tuple(int(round(v)) for v in c)


def el_html(el, left, top, size, measure=False):
    text = html.escape(el["text"]).replace("\n", "<br>")
    style = f"left:{left:.2f}px;top:{top:.2f}px;font-size:{size:.2f}px;"
    cls = f"e {el['kind']}"
    if measure:
        style += "color:#000"
    elif "grad" in el:
        cls += " grad"
        style += f"background-image:linear-gradient({el['grad'][0]},{hx(el['grad'][1])},{hx(el['grad'][2])})"
    else:
        style += f"color:{hx(el['color'])}"
    return f'<div class="{cls}" style="{style}">{text}</div>'


def analyse(img, els):
    """Find the ink of every block in the source: mask (for erasing), ink box and colours."""
    low = img.min(axis=2)
    sat = img.max(axis=2).astype(int) - low
    hats = {k: cv2.morphologyEx(low, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))).astype(int) - low for k in (31, 61)}
    erase = np.zeros(low.shape, np.uint8)
    for el in els:
        ink = np.zeros(low.shape, bool)
        hat = hats[61 if el["kind"] == "title" else 31]
        for x0, y0, x1, y1 in el["rects"]:
            ink[y0:y1, x0:x1] = hat[y0:y1, x0:x1] > 14
        if el["pick"] == "dark":
            ink &= (sat < 70) & (low < 150)
        elif el["pick"] == "color":
            ink &= sat > 70
        ink = cv2.morphologyEx(ink.astype(np.uint8), cv2.MORPH_OPEN, np.ones((2, 2), np.uint8)).astype(bool)
        if el["kind"] == "num":  # the box may reach the accents of the label below: keep the first band of ink only
            rows = np.nonzero(ink.any(axis=1))[0]
            gaps = np.nonzero(np.diff(rows) > 1)[0]
            if len(gaps):
                ink[rows[gaps[0]] + 1:] = False
        ys, xs = np.nonzero(ink)
        el["box"] = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
        erase |= cv2.dilate(ink.astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
        strong = ink & (hat > np.percentile(hat[ink], 55))  # stroke cores, away from the anti-aliased edge
        px, py, pxy = img[strong], np.nonzero(strong)[0], np.nonzero(strong)[1]
        if el["kind"] == "title" and el["pick"] == "color":
            q = np.percentile(pxy, [18, 82])
            el["grad"] = ("90deg", np.median(px[pxy <= q[0]], axis=0), np.median(px[pxy >= q[1]], axis=0))
        elif el["kind"] == "num":
            q = np.percentile(py, [30, 70])
            el["grad"] = ("180deg", np.median(px[py <= q[0]], axis=0), np.median(px[py >= q[1]], axis=0))
        else:
            el["color"] = np.percentile(px, 30, axis=0)
    return erase


def measure(els):
    """Ink box of every block at its current trial size, relative to the block origin."""
    w, h = 2400, CELL * len(els)
    body = "".join(el_html(el, 100, i * CELL + 90, el["size"], measure=True) for i, el in enumerate(els))
    shot = np.array(chrome(f"<!doctype html><meta charset=utf-8><style>{CSS}body{{background:#fff;width:{w}px;height:{h}px}}</style><body>{body}", w, h, False).convert("L"))
    for i, el in enumerate(els):
        ys, xs = np.nonzero(shot[i * CELL:(i + 1) * CELL] < 128)
        el["ref"] = (xs.min() - 100, ys.min() - 90, xs.max() + 1 - xs.min(), ys.max() + 1 - ys.min())


def fit(els):
    """Scale every block from its trial size to the source ink box: Inter blocks by width, Plus Jakarta Sans by height."""
    for el in els:
        by_width = el["kind"] in ("foot", "tag", "sub")
        el["k"] = (el["box"][2] - el["box"][0]) / el["ref"][2] if by_width else (el["box"][3] - el["box"][1]) / el["ref"][3]
    for group in ("title", "label", "num", "foot"):  # one size per kind of text on a poster
        members = [el for el in els if el["kind"] == group]
        sizes = [el["size"] * el["k"] for el in members]
        size = statistics.median(sizes) * 0.92 if group == "num" else min(sizes)  # a little air between number and label
        if group == "label":  # the longest label must stay clear of its illustration
            size = min([statistics.median(sizes)] + [el["size"] * (max(r[2] for r in el["rects"]) - 3 - el["box"][0]) / el["ref"][2] for el in members])
        for el in members:
            el["k"] = size / el["size"]
    for el in els:
        ox, oy, w, _ = el["ref"]
        k, (x0, y0, x1, _) = el["k"], el["box"]
        el["pos"] = ((x0 - k * ox) if el["align"] == "left" else (x1 - k * (ox + w)), y0 - k * oy, el["size"] * k)
        el["size"] *= k


def build(name, cfg, out, debug):
    raw = subprocess.run(["git", "-C", str(ROOT), "show", f"{SRC_REV}:04_Services/{name}"], capture_output=True, check=True).stdout
    img = np.array(Image.open(io.BytesIO(raw)).convert("RGB"))
    h, w = img.shape[:2]
    els = cfg["els"]
    erase = analyse(img, els)
    x0, y0, x1, y1 = cfg["logo"]["rect"]
    erase[y0:y1, x0:x1] = 1
    clean = cv2.inpaint(np.ascontiguousarray(img[:, :, ::-1]), erase, 5, cv2.INPAINT_TELEA)[:, :, ::-1]
    soft = cv2.GaussianBlur(clean, (0, 0), 7)  # smooth the inpainted patches so no ghost of the old text remains
    m = cv2.GaussianBlur(cv2.dilate(erase, np.ones((7, 7), np.uint8)).astype(np.float32), (0, 0), 3)[:, :, None]
    clean = (clean * (1 - m) + soft * m).round().astype(np.uint8)
    for el in els:
        el["size"] = REF
    for _ in range(3):  # glyph widths do not scale linearly (optical size, hinting): re-measure at the fitted size
        measure(els)
        fit(els)
    lg = cfg["logo"]
    body = f'<div class="e" style="left:{lg["left"]}px;top:{lg["top"]}px;width:{lg["width"]}px">{LOGO_SVG}</div>'
    feet = [el for el in els if el["kind"] == "foot"]  # same footer as the other posters: size, margins and colour by canvas width
    for el in feet:
        el["size"], el["color"] = 14.5 * w / 1080, (0x5A, 0x67, 0x84)
    measure(els)
    for el in feet:
        ox, oy, fw, fh = el["ref"]
        cy = (el["box"][1] + el["box"][3]) / 2
        el["pos"] = (46 * w / 1080 - ox if el["align"] == "left" else w - 46 * w / 1080 - ox - fw, cy - oy - fh / 2, el["size"])
    for el in els:  # blocks are fitted at line-height 1.1, then the names are opened up so accents clear the line above
        if el["kind"] == "label":
            left, top, size = el["pos"]
            el["pos"] = (left, top - (LABEL_LH - 1.1) / 2 * size, size)
    body += "".join(el_html(el, *el["pos"]) for el in els)
    overlay = chrome(f"<!doctype html><meta charset=utf-8><style>{CSS}body{{width:{w}px;height:{h}px;--lh:{LABEL_LH}}}svg{{display:block;width:100%}}</style><body>{body}", w, h, True)
    result = Image.alpha_composite(Image.fromarray(clean).convert("RGBA"), overlay).convert("RGB")
    result.save(out / name)
    if debug:
        Image.fromarray(clean).save(out / ("clean_" + name))
        for el in els:
            print(f'  {el["kind"]:6s}{el["text"][:22]!r:26s} box={tuple(int(v) for v in el["box"])} size={el["pos"][2]:.1f}')
    print(out / name)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "04_Services"))
    ap.add_argument("--debug", action="store_true")
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, cfg in POSTERS.items():
        build(name, cfg, out, a.debug)
