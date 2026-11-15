"""Open up the line spacing of the multi-line service names on the dv1 / dv2 / dv3 posters.

The posters are flat PNGs with no source and the names were set so tight that Vietnamese accents touch the
line above. This script finds every name (Midnight ink inside the card grid), splits it into lines and moves
each line down by a fraction of the cap height. Nothing else on the poster changes.

The footer is also redrawn so that every poster ends with the same line: VIBE AI LABS · MARKETING × AI × CREATIVE
(same type as build_package_posters.py).

Run:  python3 loosen_label_lines.py [--out DIR]
Sources are read from git (commit SRC_REV) so the script can be re-run on its own output.
"""
import argparse
import io
import pathlib
import shutil
import subprocess
import tempfile

import cv2
import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[4]
SRC_REV = "9d30642"
POSTERS = {  # file: (top of the card grid, footer rule in px, added line gap as a fraction of the cap height)
    "dv1_marketing-so_4x5.png": (772, 2560, 0.34),
    "dv2_ai-tu-dong-hoa_4x5.png": (852, 2560, 0.34),
    "dv3_thiet-ke-sang-tao_1x1.png": (720, 2020, 0.24),  # less: the four-line name sits right above its icon tile
}


FONT = ROOT / "02_Brandkit" / "01_General-Brandkit" / "03_Typography" / "fonts" / "Inter[opsz,wght].ttf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FOOT_H = 120


def footer_overlay(width):
    page = f"""<!doctype html><meta charset=utf-8><style>@font-face{{font-family:'Inter';src:url('{FONT.as_uri()}');font-weight:100 900}}
*{{margin:0;padding:0}}div{{position:absolute;left:92px;right:92px;bottom:44px;display:flex;justify-content:space-between;
font:500 29px/40px 'Inter';letter-spacing:.26em;color:#5A6784;white-space:nowrap;font-variation-settings:'opsz' 14.5}}span:last-child{{margin-right:-.26em}}
body{{width:{width}px;height:{FOOT_H}px;position:relative}}</style><body><div><span>VIBE AI LABS</span><span>MARKETING × AI × CREATIVE</span></div>"""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="foot_"))
    try:
        (tmp / "p.html").write_text(page, encoding="utf8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=1",
                        f"--user-data-dir={tmp / 'ud'}", "--no-first-run", "--disable-extensions", "--allow-file-access-from-files",
                        "--default-background-color=00000000", f"--screenshot={tmp / 's.png'}", f"--window-size={width},{FOOT_H + 300}",
                        "--virtual-time-budget=1500", (tmp / "p.html").as_uri()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180, check=True)
        return Image.open(tmp / "s.png").convert("RGBA").crop((0, 0, width, FOOT_H))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def replace_footer(result):
    h, w = result.shape[:2]
    band = result[h - FOOT_H + 12:h - 8].astype(float)  # below the rule: wipe the old text with the background gradient
    t = np.linspace(0, 1, w - 80)[None, :, None]
    band[:, 40:w - 40] = band[:, 39:40] * (1 - t) + band[:, w - 40:w - 39] * t
    result[h - FOOT_H + 12:h - 8] = band.round().astype(np.uint8)
    strip = Image.fromarray(result[h - FOOT_H:]).convert("RGBA")
    result[h - FOOT_H:] = np.array(Image.alpha_composite(strip, footer_overlay(w)).convert("RGB"))


def build(name, top, bottom, extra, out):
    raw = subprocess.run(["git", "-C", str(ROOT), "show", f"{SRC_REV}:04_Services/{name}"], capture_output=True, check=True).stdout
    img = np.array(Image.open(io.BytesIO(raw)).convert("RGB"))
    ink = np.zeros(img.shape[:2], np.uint8)
    ink[top:bottom] = img[top:bottom].max(axis=2) < 150  # Midnight text only: numbers and icons are coloured
    n_blocks, blocks = cv2.connectedComponents(cv2.dilate(ink, np.ones((50, 50), np.uint8)))
    moves, erase = [], np.zeros_like(ink)
    for b in range(1, n_blocks):
        block = ink & (blocks == b)
        ys, xs = np.nonzero(block)
        y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        local_ink = block[y0:y1, x0:x1].astype(np.uint8)
        for cut in (True, False):
            n, comps, stats, _ = cv2.connectedComponentsWithStats(local_ink, connectivity=8)
            tops, heights, widths = stats[1:, 1] + y0, stats[1:, 3], stats[1:, 2]
            fill = stats[1:, 4] / (widths * heights)
            cap = float(np.median(heights[heights > 0.5 * heights.max()]))
            letters = heights > 0.6 * cap
            baselines = []  # one per line: letters share a baseline, accents and dots do not reach it
            for base in sorted(tops[letters] + heights[letters]):
                if not baselines or base - baselines[-1][-1] > 0.5 * cap:
                    baselines.append([])
                baselines[-1].append(base)
            baselines = [float(np.median(g)) for g in baselines]
            if not cut:
                break
            # an accent that touches the letter above it is fused to that letter: cut it loose just under the baseline
            for c in range(n - 1):
                for base in baselines[:-1]:
                    if tops[c] < base - 0.3 * cap and tops[c] + heights[c] > base + 0.2 * cap:
                        row = int(base + round(0.06 * cap)) - y0
                        local_ink[row, stats[c + 1, 0]:stats[c + 1, 0] + widths[c]] &= comps[row, stats[c + 1, 0]:stats[c + 1, 0] + widths[c]] != c + 1
        if len(baselines) < 2:
            continue
        gap = round(extra * cap)
        def place(local, line):
            comp = np.zeros_like(ink)
            comp[y0:y1, x0:x1] = local
            others = cv2.dilate(block.astype(np.uint8) & ~comp, np.ones((3, 3), np.uint8))  # never drag a neighbour's pixels along
            grown = cv2.dilate(comp, np.ones((5, 5), np.uint8))
            erase[:] |= grown
            moves.append(((grown & ~others).astype(bool), line * gap))

        def line_above(a):  # dot below (dấu nặng): belongs to the line above it
            return max(i for i, base in enumerate(baselines) if base <= a + 3)

        def line_below(z):  # accent: belongs to the line whose letters start right below it
            return int(np.argmin([abs(base - cap - z) for base in baselines]))

        for c in range(n - 1):
            a, z = tops[c], tops[c] + heights[c]
            local = comps == c + 1
            if letters[c]:
                place(local, int(np.argmin([abs(z - base) for base in baselines])))
            elif fill[c] > 0.9 and max(widths[c], heights[c]) < 0.3 * cap:
                place(local, line_above(a))
            else:
                cols = np.nonzero(local[a - y0:a - y0 + 3].any(axis=0))[0]
                d = cols.max() - cols.min() + 1
                box = local[a - y0:a - y0 + d, cols.min():cols.max() + 1]
                if 0.17 * cap <= d < 0.3 * cap and box.mean() > 0.8 and d < 0.7 * widths[c] and heights[c] > 1.5 * d:
                    # a dot below that touches the accent of the next line: split them
                    dot = np.zeros_like(local)
                    dot[a - y0:a - y0 + d, cols.min():cols.max() + 1] = local[a - y0:a - y0 + d, cols.min():cols.max() + 1]
                    place(dot, line_above(a))
                    place(local & ~dot, line_below(z))
                else:
                    place(local, line_below(z))
        print(f"  {name}: block at ({x0},{y0}) {len(baselines)} lines, +{gap}px per line")
    clean = cv2.inpaint(np.ascontiguousarray(img[:, :, ::-1]), erase, 5, cv2.INPAINT_TELEA)[:, :, ::-1]
    soft = cv2.GaussianBlur(clean, (0, 0), 6)
    result = np.where(cv2.dilate(erase, np.ones((5, 5), np.uint8))[:, :, None].astype(bool), soft, clean)
    for mask, dy in moves:
        ys, xs = np.nonzero(mask)
        result[ys + dy, xs] = img[ys, xs]
    replace_footer(result)
    Image.fromarray(result).save(out / name)
    print(out / name)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "04_Services"))
    out = pathlib.Path(ap.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    for name, (top, bottom, extra) in POSTERS.items():
        build(name, top, bottom, extra, out)
