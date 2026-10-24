"""Render 00_Folder-Map.png (level-1 folder map of VIBE AI LABS) with headless Chrome.

Run:  python3 folder_map.py
"""
import pathlib
import shutil
import subprocess
import tempfile

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[3]
BK = ROOT / "02_Brandkit" / "01_General-Brandkit"
OUT = ROOT / "00_Folder-Map.png"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1920, 1080
SKIP = {"node_modules", ".git", ".venv", "__pycache__"}

FOLDERS = [
    ("01_General", "#2563FF", "Company Profile, One Pager, mẫu đề xuất (VI · EN · ZH) · hồ sơ thương hiệu .docx · script build brandkit"),
    ("02_Brandkit", "#8B5CF6", "Brand Kit v2.0 (logo, màu, font, icon, template, guidelines) · Designer Kit cho team làm poster"),
    ("03_Decks", "#14D8C4", "Deck Community & Events (EN) · Outreach Kit: mẫu tin nhắn email, LinkedIn, X, Telegram, Zalo…"),
    ("04_Services", "#16A34A", "Infographic 3 nhóm dịch vụ: Marketing số · AI & Tự động hóa · Thiết kế & Sáng tạo"),
    ("05_Social-Covers", "#F97316", "Logo và ảnh bìa các group Facebook, banner tăng trưởng"),
    ("06_AI-Tools", "#2563FF", "AI agent & skill: brand voice, content agent Facebook/LinkedIn, design prompter, SEO/Ads stack"),
    ("07_Website", "#8B5CF6", "Mã nguồn website Vibe AI Labs (Next.js · Cloudflare Workers · 3 ngôn ngữ)"),
]


def count_files(d):
    n = 0
    for p in d.rglob("*"):
        if p.is_file() and p.name != ".DS_Store" and not SKIP.intersection(p.parts):
            n += 1
    return n


def main():
    fonts = BK / "03_Typography" / "fonts"
    logo = (BK / "01_Logos" / "SVG" / "vibe-ai-labs_horizontal_reversed.svg").as_uri()
    rows = ""
    for name, color, desc in FOLDERS:
        n = count_files(ROOT / name)
        num, label = name.split("_", 1)
        rows += f"""
<div class="row">
  <div class="branch"></div>
  <div class="card" style="border-left:6px solid {color}">
    <div class="num" style="color:{color}">{num}</div>
    <div class="name">{label}</div>
    <div class="desc">{desc}</div>
    <div class="count">{n:,} file</div>
  </div>
</div>"""
    html = f"""<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:'PJS';src:url('{(fonts / "PlusJakartaSans[wght].ttf").as_uri()}');font-weight:200 800}}
@font-face{{font-family:'Inter';src:url('{(fonts / "Inter[opsz,wght].ttf").as_uri()}');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#0B1026;color:#fff;font-family:'Inter';position:relative;overflow:hidden}}
body::before{{content:'';position:absolute;inset:0;background:
 radial-gradient(1200px 600px at 75% 20%,rgba(37,99,255,.40),transparent 60%),
 radial-gradient(900px 500px at 15% 90%,rgba(20,216,196,.20),transparent 60%)}}
.wrap{{position:absolute;inset:0;padding:64px 96px}}
.logo{{height:46px}}
.over{{font:700 18px 'PJS';letter-spacing:.2em;text-transform:uppercase;color:#14D8C4;margin-top:44px}}
h1{{font:800 60px/1.1 'PJS';letter-spacing:-.03em;margin-top:12px}}
.root{{display:inline-block;margin-top:34px;padding:12px 26px;border-radius:14px;background:#2563FF;font:700 24px 'PJS'}}
.tree{{position:relative;margin-left:40px;margin-top:6px}}
.tree::before{{content:'';position:absolute;left:0;top:0;bottom:44px;width:3px;background:rgba(217,226,242,.25)}}
.row{{display:flex;align-items:center;margin-top:14px}}
.branch{{width:44px;height:3px;background:rgba(217,226,242,.25);flex:none}}
.card{{flex:1;display:grid;grid-template-columns:70px 300px 1fr 130px;align-items:center;gap:18px;
 background:rgba(255,255,255,.05);border:1px solid rgba(217,226,242,.14);border-radius:18px;padding:16px 26px}}
.num{{font:800 32px 'PJS'}}
.name{{font:700 28px 'PJS';letter-spacing:-.01em}}
.desc{{font:400 20px/1.4 'Inter';color:#D9E2F2}}
.count{{font:600 18px 'Inter';color:#14D8C4;text-align:right}}
.foot{{position:absolute;left:96px;right:96px;bottom:40px;display:flex;justify-content:space-between;font:400 17px 'Inter';color:rgba(217,226,242,.7)}}
</style><body><div class="wrap">
<img class="logo" src="{logo}">
<div class="over">Folder map · cấp 1</div>
<h1>Bên trong VIBE AI LABS có gì</h1>
<div class="root">VIBE AI LABS /</div>
<div class="tree">{rows}</div>
</div>
<div class="foot"><span>Vibe AI Labs · Ideas. Intelligence. Real Growth.</span><span>github.com/vibeailabs-tech/vibe-ai-labs</span></div>
</body>"""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="map_"))
    page, shot = tmp / "map.html", tmp / "shot.png"
    page.write_text(html, encoding="utf-8")
    ud = tempfile.mkdtemp(prefix="chr_")
    try:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                        "--user-data-dir=" + ud, "--allow-file-access-from-files", f"--window-size={W},{H + 170}",
                        "--virtual-time-budget=3000", "--screenshot=" + str(shot), page.as_uri()],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120, check=True)
        Image.open(shot).crop((0, 0, W, H)).save(OUT)
    finally:
        shutil.rmtree(ud, ignore_errors=True)
        shutil.rmtree(tmp, ignore_errors=True)
    print(OUT)


if __name__ == "__main__":
    main()
