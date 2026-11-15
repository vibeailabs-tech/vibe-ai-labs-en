"""Build the service-package posters (Khởi động · Tăng tốc · overview) in the style of the 04_Services posters.

The original dv1/dv2/dv3 posters have no source in the repo, so the style is re-created from measurements of
the PNGs (2160 px wide). Layout is authored at 1080 px and rendered at 2x with headless Chrome.

Run:  python3 build_package_posters.py            -> writes PNGs into 04_Services/
      python3 build_package_posters.py --out DIR  -> writes PNGs into DIR
"""
import argparse
import pathlib
import shutil
import subprocess
import tempfile

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[4]
BK = ROOT / "02_Brandkit" / "01_General-Brandkit"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FONTS = BK / "03_Typography" / "fonts"
LOGO = BK / "01_Logos" / "SVG" / "vibe-ai-labs_horizontal_color.svg"

# the brandkit lockup leaves room for the descriptor: without it, centre the wordmark on the mark
LOGO_SVG = LOGO.read_text().replace('width="1470" height="246"', 'class="logo"', 1).replace("translate(502.50,-441.75)", "translate(502.50,-428.75)", 1)

TONES = {  # accent, card gradient start, card gradient end
    "blue": ("#2563FF", "#E8EEFF", "#DBE7FF"),
    "orange": ("#F97316", "#FFEEDF", "#FFE2CB"),
    "violet": ("#8B5CF6", "#F1E9FF", "#E7DCFF"),
    "teal": ("#10A58E", "#E1F7EF", "#D4F1E7"),
    "pink": ("#E11D74", "#FFE9EF", "#FFDEE9"),
}

CSS = f"""
@font-face{{font-family:'Plus Jakarta Sans';src:url('{(FONTS / "PlusJakartaSans[wght].ttf").as_uri()}');font-weight:200 800}}
@font-face{{font-family:'Inter';src:url('{(FONTS / "Inter[opsz,wght].ttf").as_uri()}');font-weight:100 900}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:var(--h);position:relative;overflow:hidden;font-family:'Inter',Arial,sans-serif;
  background:linear-gradient(160deg,#FBFCFF 0%,#F7F9FE 55%,#F1F5FD 100%)}}
body>*{{position:absolute}}
.ribbon{{left:0;top:0;width:1080px;height:520px}}
.logo{{left:44px;top:46px;width:334px}}
.tag{{right:48px;top:38px;text-align:right;font:500 17px/27px 'Inter',Arial,sans-serif;letter-spacing:.3em;margin-right:-.3em;color:#6B7A99}}
h1{{left:43px;font:800 var(--ts)/1.24 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.04em;text-transform:uppercase;color:#0B1026;white-space:nowrap}}
h1 em{{font-style:normal;display:block;width:max-content;background:linear-gradient(90deg,#2563FF 0%,#8B5CF6 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent;padding:.14em .06em .1em 0;margin-top:-.14em}}
.sub{{left:42px;right:42px;font:400 var(--ss)/1.35 'Inter',Arial,sans-serif;letter-spacing:-.005em;color:#5A6784}}
.grid{{left:42px;right:42px;bottom:88px;display:grid;gap:16px}}
.card{{position:relative;border-radius:26px;background:linear-gradient(135deg,var(--c1),var(--c2));overflow:hidden}}
.num{{font:500 var(--ns)/1 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.03em;color:var(--a)}}
.name{{font:800 var(--ls)/1.1 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.035em;text-transform:uppercase;color:#0B1026;margin-top:8px}}
.txt{{font:400 var(--bs)/1.4 'Inter',Arial,sans-serif;color:#3D4A66;margin-top:14px}}
.tile{{position:absolute;border-radius:30%;background:linear-gradient(180deg,#F8FAFF,#F1F5FF);border:2.5px solid #fff;color:var(--a);
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 14px 28px color-mix(in srgb,var(--a) 20%,transparent),0 2px 6px color-mix(in srgb,var(--a) 10%,transparent)}}
.tile svg{{width:46%;height:46%}}
.rule{{left:42px;right:42px;bottom:62px;height:1.5px;background:#C9D3E6}}
.foot{{left:46px;right:46px;bottom:22px;display:flex;justify-content:space-between;font:500 14.5px/20px 'Inter',Arial,sans-serif;
  letter-spacing:.26em;color:#5A6784;white-space:nowrap}}
.foot span:last-child{{margin-right:-.26em}}
"""

RIBBON = """<svg class="ribbon" viewBox="0 0 1080 520" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="r1" x1="560" y1="0" x2="1000" y2="400" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#C2D3FF"/><stop offset=".55" stop-color="#DAD6FD"/><stop offset="1" stop-color="#E9E4FE"/></linearGradient>
<linearGradient id="r2" x1="780" y1="0" x2="1080" y2="300" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#E4EAFE"/><stop offset="1" stop-color="#EEEBFE"/></linearGradient></defs>
<path d="M790 -20 L1000 222 L1160 20" fill="none" stroke="url(#r2)" stroke-width="100" stroke-linejoin="round" opacity=".9"/>
<path d="M588 -25 L940 327 L1175 2" fill="none" stroke="url(#r1)" stroke-width="106" stroke-linejoin="round" opacity=".92"/>
</svg>"""


def icon(name):
    return (BK / "05_Icons" / "SVG_currentColor" / f"{name}.svg").read_text().replace('stroke-width="1.75"', 'stroke-width="2"')


def tile(name, size, x, y, rot=0):
    return f'<div class="tile" style="width:{size}px;height:{size}px;left:{x}px;top:{y}px;transform:rotate({rot}deg)">{icon(name)}</div>'


def card(tone, inner, style=""):
    a, c1, c2 = TONES[tone]
    return f'<div class="card" style="--a:{a};--c1:{c1};--c2:{c2};{style}">{inner}</div>'


def page(h, title_top, ts, title, sub_top, ss, sub, grid_top, grid_style, cards, foot, vars_):
    return f"""<!doctype html><meta charset="utf-8"><style>{CSS}</style>
<body style="--h:{h}px;--ts:{ts}px;--ss:{ss}px;{vars_}">{RIBBON}
{LOGO_SVG}
<div class="tag">TURN<br>BRANDS<br>INTO<br>GROWTH</div>
<h1 style="top:{title_top}px">{title[0]}<em>{title[1]}</em></h1>
<p class="sub" style="top:{sub_top}px">{sub}</p>
<div class="grid" style="top:{grid_top}px;{grid_style}">{cards}</div>
<div class="rule"></div><div class="foot"><span>VIBE AI LABS</span><span>{foot}</span></div></body>"""


def package_poster(name, who, rows):
    """4:5 poster: three full-width pillar cards."""
    tones = ["blue", "teal", "orange"]
    pillars = ["Marketing số", "AI &amp; Tự động hóa", "Thiết kế &amp; Sáng tạo"]
    cards = ""
    for i, (txt, big, small_a, small_b) in enumerate(rows):
        inner = (f'<div style="position:absolute;left:38px;top:40px;width:570px"><div class="num">0{i + 1}</div>'
                 f'<div class="name">{pillars[i]}</div><p class="txt">{txt}</p></div>'
                 + tile(big, 150, 706, 68) + tile(small_a, 76, 872, 34, 8) + tile(small_b, 72, 622, 176, -8))
        cards += card(tones[i], inner)
    return page(1350, 112, 88, ("Gói dịch vụ", name), 334, 24, who, 388, "grid-template-rows:repeat(3,1fr)", cards,
                "MARKETING × AI × CREATIVE", "--ns:64px;--ls:35px;--bs:23.5px")


def overview_poster():
    """1:1 poster: the two packages side by side."""
    data = [
        ("blue", "Khởi động", "Dành cho doanh nghiệp mới bắt đầu,<br>muốn xây nền tảng vững chắc.", "AUDIT → BUILD", "ideas", "brand", "website"),
        ("violet", "Tăng tốc", "Dành cho doanh nghiệp đã hoạt động,<br>muốn nâng cao hiệu quả.", "AUTOMATE → GROW", "speed", "agent", "growth"),
    ]
    cards = ""
    for i, (tone, name, who, focus, big, sa, sb) in enumerate(data):
        inner = (f'<div style="position:absolute;left:32px;top:28px;right:24px"><div class="num">0{i + 1}</div>'
                 f'<div class="name">{name}</div><p class="txt">{who}</p>'
                 f'<p style="font:700 14px/20px \'Inter\',Arial,sans-serif;letter-spacing:.2em;color:var(--a);margin-top:14px">{focus}</p></div>'
                 + tile(big, 184, 153, 336) + tile(sa, 88, 352, 284, 8) + tile(sb, 84, 56, 474, -8))
        cards += card(tone, inner)
    return page(1080, 112, 66, ("Hai gói dịch vụ", "Khởi động &amp; Tăng tốc"), 276, 22.5,
                "Mỗi gói kết hợp Marketing, Trí tuệ nhân tạo (AI) và Sáng tạo thành một hệ thống.<br>Chọn theo giai đoạn của bạn.",
                362, "grid-template-columns:1fr 1fr", cards, "MARKETING × AI × CREATIVE", "--ns:62px;--ls:38px;--bs:21px")


POSTERS = {
    "goi0_hai-goi-dich-vu_1x1": (1080, overview_poster),
    "goi1_khoi-dong_4x5": (1350, lambda: package_poster("Khởi động", "Dành cho doanh nghiệp mới bắt đầu, muốn xây nền tảng vững chắc.", [
        ("Định vị, landing page,<br>kênh mạng xã hội, đo lường.", "strategy", "growth", "website"),
        ("Chatbot trả lời khách,<br>tự động hóa tác vụ đơn giản.", "chatbot", "ai", "automation"),
        ("Logo, nhận diện cơ bản, template,<br>ảnh sản phẩm bằng AI.", "brand", "design", "photo")])),
    "goi2_tang-toc_4x5": (1350, lambda: package_poster("Tăng tốc", "Dành cho doanh nghiệp đã hoạt động, muốn nâng cao hiệu quả.", [
        ("Quảng cáo hiệu suất, CRO,<br>SEO và tìm kiếm bằng AI, CRM.", "performance", "seo", "data"),
        ("AI Agent, chatbot RAG, tự động hóa<br>bán hàng và báo cáo.", "automation", "agent", "ai"),
        ("Key visual, video, nội dung số lượng lớn<br>bằng AI tạo sinh.", "genai", "video", "content")])),
}


def render(html, out, h):
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="pkgposter_"))
    try:
        (tmp / "p.html").write_text(html, encoding="utf8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=2",
                        f"--user-data-dir={tmp / 'ud'}", "--no-first-run", "--disable-extensions", "--allow-file-access-from-files",
                        f"--screenshot={tmp / 's.png'}", f"--window-size=1080,{h + 200}", "--virtual-time-budget=1500",
                        (tmp / "p.html").as_uri()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180, check=True)
        Image.open(tmp / "s.png").convert("RGB").crop((0, 0, 2160, h * 2)).save(out)  # window is taller than the page: crop
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "04_Services"))
    out = pathlib.Path(ap.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    for name, (h, build) in POSTERS.items():
        render(build(), out / f"{name}.png", h)
        print(out / f"{name}.png")
