"""Build the Vibe AI Community & Events deck (EN, 16:9): HTML -> PDF via headless Chrome.

Run:  python3 build_deck.py   ->  ../Vibe_AI_Labs_Community_Events_Deck_EN.pdf

Brand rules applied (Brandkit/1. General Brandkit):
- 03_Typography/type-scale.md: Plus Jakarta Sans for headings (Display 800, H1 700, H3 700, Overline 700),
  Inter for body (400), captions (500) and buttons (600). Static instances are generated from the brand's
  variable fonts so the PDF embeds correctly named weights.
- 02_Color/contrast-matrix.md: Aqua is never text on light backgrounds.
- Slide titles are always one line and one color (Midnight on light, White on dark), auto-fitted to the content width.
"""
import pathlib
import shutil
import subprocess
import tempfile

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BK = ROOT / "Brandkit" / "1. General Brandkit"
COVERS = ROOT / "FILES" / "Groups's Cover Photo"
OUT_PDF = HERE.parent / "Vibe_AI_Labs_Community_Events_Deck_EN.pdf"
OUT_HTML = HERE / "deck.html"
FONT_CACHE = pathlib.Path(tempfile.gettempdir()) / "vibe_deck_fonts"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

WEBSITE = "vibe-ai-labs.vibeailabs.workers.dev"
CONTACT_URL = "https://vibe-ai-labs.vibeailabs.workers.dev/en/lien-he"
FACEBOOK = "facebook.com/vibe.ai.labs"
X_HANDLE = "x.com/vibe_ai_labs"
EMAIL = "vibeailabs@gmail.com"
ADDRESS = "WORC@Q2 Building, 21 Võ Trường Toản, An Khánh, Ho Chi Minh City"

MIDNIGHT, INK, SLATE, LINE, WHITE = "#0B1026", "#111827", "#667085", "#D9E2F2", "#FFFFFF"
BLUE, AQUA, VIOLET = "#2563FF", "#14D8C4", "#8B5CF6"
GREEN, ORANGE = "#16A34A", "#F97316"

HERO, TITLE, SUB, BODY, META, NUMBER = 92, 76, 30, 22, 18, 56
CONTENT_W = 1728

FONTS = [
    ("PlusJakartaSans[wght].ttf", "Plus Jakarta Sans", "Bold", 700, {}),
    ("PlusJakartaSans[wght].ttf", "Plus Jakarta Sans", "ExtraBold", 800, {}),
    ("Inter[opsz,wght].ttf", "Inter", "Regular", 400, {"opsz": 22}),
    ("Inter[opsz,wght].ttf", "Inter", "Medium", 500, {"opsz": 22}),
    ("Inter[opsz,wght].ttf", "Inter", "SemiBold", 600, {"opsz": 22}),
]


def uri(p):
    return pathlib.Path(p).as_uri()


def static_font(src, family, style, weight, axes):
    out = FONT_CACHE / f"{family.replace(' ', '')}-{style}.ttf"
    if out.exists():
        return out
    FONT_CACHE.mkdir(parents=True, exist_ok=True)
    font = instancer.instantiateVariableFont(TTFont(BK / "03_Typography" / "fonts" / src), {"wght": weight, **axes})
    ribbi = style in ("Regular", "Bold")
    names = {1: family if ribbi else f"{family} {style}", 2: style if ribbi else "Regular",
             4: f"{family} {style}", 6: f"{family.replace(' ', '')}-{style}", 16: family, 17: style}
    table = font["name"]
    for nid in (1, 2, 4, 6, 16, 17, 25):
        table.removeNames(nameID=nid)
    for nid, val in names.items():
        table.setName(val, nid, 3, 1, 0x409)
        table.setName(val, nid, 1, 0, 0)
    font["OS/2"].usWeightClass = weight
    font.save(out)
    return out


def font_faces():
    return "".join(f"@font-face{{font-family:'{family}';src:url('{uri(static_font(src, family, style, weight, axes))}');"
                   f"font-weight:{weight};}}" for src, family, style, weight, axes in FONTS)


def light_img(path, width=900):
    """JPEG copy of a large PNG so the PDF stays small enough to email."""
    from PIL import Image
    out = FONT_CACHE / f"{pathlib.Path(path).stem[:40]}_{width}.jpg"
    if not out.exists():
        FONT_CACHE.mkdir(parents=True, exist_ok=True)
        im = Image.open(path).convert("RGB")
        im.thumbnail((width, width))
        im.save(out, "JPEG", quality=86, optimize=True)
    return uri(out)


def icon(name, size=40):
    svg = (BK / "05_Icons" / "SVG_currentColor" / f"{name}.svg").read_text()
    return svg.replace('width="24" height="24"', f'width="{size}" height="{size}"', 1)


LOGO_DARK = uri(BK / "01_Logos" / "SVG" / "vibe-ai-labs_horizontal_reversed.svg")
LOGO_LIGHT = uri(BK / "01_Logos" / "SVG" / "vibe-ai-labs_horizontal_color.svg")
RIBBON_MARK = uri(BK / "04_Graphic_Elements" / "SVG" / "ribbon-mark-large.svg")
WAVES = uri(BK / "04_Graphic_Elements" / "SVG" / "wave-lines_dark_16x9.svg")
OPENCLAW = uri(HERE / "assets" / "openclaw-mascot.png")
HERMES = uri(HERE / "assets" / "hermes-agent-logo.png")

CSS = f"""
@page{{size:1920px 1080px;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:{MIDNIGHT};-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:'Inter',Arial,sans-serif;color:{INK}}}
b{{font-weight:600}}
.slide{{width:1920px;height:1080px;position:relative;overflow:hidden;break-after:page}}
.light{{background:#F8FAFC}}
.light::before{{content:'';position:absolute;inset:0;background:
  radial-gradient(900px 600px at 100% 0%,rgba(37,99,255,.07),transparent 70%),
  radial-gradient(800px 600px at 0% 100%,rgba(20,216,196,.08),transparent 70%)}}
.dark{{background:{MIDNIGHT};color:{WHITE}}}
.dark::before{{content:'';position:absolute;inset:0;background:
  radial-gradient(1200px 600px at 75% 20%,rgba(37,99,255,.45),transparent 60%),
  radial-gradient(900px 500px at 15% 90%,rgba(20,216,196,.25),transparent 60%)}}
.bgimg{{position:absolute;inset:0;width:1920px;height:1080px;object-fit:cover}}
.z{{position:relative;z-index:2}}
.logo{{position:absolute;left:96px;top:64px;height:50px;z-index:3}}
.section,.over,.label{{font:700 {META}px/1.3 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;text-transform:uppercase}}
.section{{position:absolute;right:96px;top:80px;z-index:3;color:{SLATE}}}
.dark .section{{color:rgba(217,226,242,.75)}}
.foot{{position:absolute;left:96px;right:96px;bottom:52px;z-index:3;display:flex;justify-content:space-between;
  font:400 {META}px 'Inter',Arial,sans-serif;color:{SLATE}}}
.dark .foot{{color:rgba(217,226,242,.75)}}
.foot b{{color:{MIDNIGHT}}}.dark .foot b{{color:{WHITE}}}
.content{{position:absolute;left:96px;right:96px;top:170px;bottom:120px;z-index:2;display:flex;flex-direction:column}}
.hd{{flex:1 0 auto;padding-bottom:48px}}
.content::after{{content:'';flex:1.5 0 0}}
.over{{color:{BLUE};margin-bottom:22px}}
.dark .over{{color:{AQUA}}}
.label{{color:{SLATE}}}
.dark .label{{color:{AQUA}}}
.lead{{font:400 {SUB}px/1.45 'Inter',Arial,sans-serif;color:{SLATE};margin-top:26px;max-width:1300px}}
.dark .lead{{color:{LINE}}}
.card{{background:{WHITE};border:1px solid {LINE};border-radius:28px;padding:36px}}
.dark .card{{background:rgba(255,255,255,.05);border-color:rgba(217,226,242,.16)}}
.tile{{width:68px;height:68px;flex:none;border-radius:20px;background:#EEF3FF;color:{BLUE};display:flex;align-items:center;justify-content:center}}
.dark .tile{{background:rgba(37,99,255,.18);color:{AQUA}}}
.h3{{font:700 {SUB}px/1.2 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.01em;color:{MIDNIGHT}}}
.dark .h3{{color:{WHITE}}}
.p{{font:400 {BODY}px/1.5 'Inter',Arial,sans-serif;color:{SLATE}}}
.dark .p{{color:{LINE}}}
.ink{{color:{INK}!important}}
.statement{{font:400 {SUB}px/1.45 'Inter',Arial,sans-serif;color:{INK}}}
.num{{font:800 {NUMBER}px/1 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.03em}}
.chip{{display:inline-block;padding:10px 20px;border-radius:999px;background:#EEF3FF;color:{BLUE};font:600 {BODY}px 'Inter',Arial,sans-serif;margin:0 10px 12px 0}}
.src{{font:500 {META}px/1.4 'Inter',Arial,sans-serif;letter-spacing:.01em;color:{SLATE}}}
.grid{{display:grid;gap:28px}}
ul.clean{{list-style:none}}
ul.clean li{{position:relative;padding-left:26px;font:400 {BODY}px/1.5 'Inter',Arial,sans-serif;color:{INK};margin-bottom:8px}}
ul.clean li::before{{content:'';position:absolute;left:0;top:13px;width:9px;height:9px;border-radius:50%;background:{BLUE}}}
.dark ul.clean li{{color:{LINE}}}
.dark ul.clean li::before{{background:{AQUA}}}
.btn{{display:inline-block;padding:22px 46px;border-radius:999px;background:{BLUE};color:{WHITE};font:600 {SUB}px 'Inter',Arial,sans-serif;text-decoration:none}}
.nw{{white-space:nowrap}}
"""

FIT_JS = """
function fitHeadlines(){document.querySelectorAll('h1.hl').forEach(function(h){
  var size=+h.dataset.size;h.style.fontSize=size+'px';
  var w=h.scrollWidth,max=h.clientWidth;
  if(w>max){h.style.fontSize=Math.floor(size*max/w*10)/10+'px';}
});}
document.fonts.ready.then(fitHeadlines);window.addEventListener('load',fitHeadlines);
"""

PAGES = []


def slide(kind, section, body, bg=None, number=True):
    n = len(PAGES) + 1
    logo = LOGO_DARK if kind == "dark" else LOGO_LIGHT
    bgimg = f'<img class="bgimg" src="{bg}">' if bg else ""
    sec = f'<div class="section">{section}</div>' if section else ""
    num = f"<b>{n:02d}</b>" if number else ""
    PAGES.append(f'<section class="slide {kind}">{bgimg}<img class="logo" src="{logo}">{sec}'
                 f'<div class="foot"><span>Vibe AI Labs · Ideas. Intelligence. Real Growth.</span>{num}</div>{body}</section>')


def headline(l1, l2=None, size=TITLE, weight=700, track=-0.02, dark=False):
    """One-line, one-color title, auto-fitted to the content width."""
    text = f"{l1} {l2}" if l2 else l1
    return (f'<h1 class="hl" data-size="{size}" style="font:{weight} {size}px/1.08 \'Plus Jakarta Sans\',Arial,sans-serif;'
            f'letter-spacing:{track}em;color:{WHITE if dark else MIDNIGHT};white-space:nowrap;max-width:{CONTENT_W}px">{text}</h1>')


def head(over, l1, l2=None, lead=None, dark=False):
    h = f'<div class="over">{over}</div>{headline(l1, l2, dark=dark)}'
    if lead:
        h += f'<p class="lead">{lead}</p>'
    return f'<div class="hd">{h}</div>'


# 01 Cover -------------------------------------------------------------------
slide("dark", None, f"""
<img src="{RIBBON_MARK}" style="position:absolute;left:820px;top:480px;width:1300px;z-index:1">
<div class="z" style="position:absolute;left:96px;top:300px;width:{CONTENT_W}px">
  <div class="over">Community &amp; Events</div>
  {headline("Bring your AI project", "to Vietnam's builders.", HERO, 800, -0.03, dark=True)}
  <p class="lead" style="margin-top:34px">A ready community. Hands-on events.<br>Vietnamese content. Clear reporting.</p>
  <p class="src" style="margin-top:60px;color:rgba(217,226,242,.75)">Vibe AI Community &amp; Events · 2026</p>
</div>""", number=False)

# 02 Who we are --------------------------------------------------------------
pillars = [
    (BLUE, "Digital Marketing", "Strategy, brand, content, PR &amp; influencers, performance marketing."),
    (GREEN, "AI &amp; Automation", "AI agents, chatbots and workflow automation, including Hermes Agent setups for clients."),
    (ORANGE, "Design &amp; Creative Studio", "Identity, key visuals, photography, video and generative AI production."),
]
cards = "".join(f"""
<div class="card" style="border-top:6px solid {c}">
  <div class="h3" style="margin-bottom:14px">{t}</div><div class="p">{d}</div>
</div>""" for c, t, d in pillars)
facts = [("100,000+", "community members", BLUE), ("19", "service groups", VIOLET), ("3", "working languages: VI · EN · ZH", BLUE)]
frow = "".join(f"""
<div style="display:flex;align-items:baseline;gap:16px">
  <span class="num" style="color:{c}">{v}</span><span class="p">{t}</span>
</div>""" for v, t, c in facts)
slide("light", "About us", f"""
<div class="content">
  {head("About Vibe AI Labs", "Marketing × AI × Creative,", "under one roof.",
        "An AI-powered growth &amp; creative agency in Ho Chi Minh City. We build AI agents for our own clients, so we understand AI products from the inside, not just from the stage.")}
  <div class="grid" style="grid-template-columns:repeat(3,1fr)">{cards}</div>
  <div class="grid" style="grid-template-columns:repeat(3,1fr);margin-top:44px">{frow}</div>
</div>""")

# 03 Why Vietnam -------------------------------------------------------------
stats = [
    ("91%", "of Vietnamese workers want AI skills training.", "Public First, Vietnam AI Opportunity Report 2026"),
    ("~560,000", "people in Vietnam's tech &amp; digital workforce.", "TopDev, Vietnam IT Market Report 2024–2025 (estimate)"),
    ("Mar 1, 2026", "Vietnam's Law on Artificial Intelligence takes effect.", "Law No. 134/2025/QH15"),
    ("2030", "National AI Strategy approved, with a vision to 2045.", "Decision 1671/QD-TTg, Aug 28, 2026"),
]
cards = "".join(f"""
<div class="card" style="display:flex;flex-direction:column;min-height:330px">
  <div class="num" style="color:{BLUE if k % 2 == 0 else VIOLET}">{v}</div>
  <div class="p ink" style="margin-top:22px">{t}</div>
  <div class="src" style="margin-top:auto;padding-top:18px">{s}</div>
</div>""" for k, (v, t, s) in enumerate(stats))
slide("light", "Why Vietnam", f"""
<div class="content">
  {head("Why Vietnam, why now", "Vietnam is learning AI,", "fast.")}
  <div class="grid" style="grid-template-columns:repeat(4,1fr)">{cards}</div>
  <div style="margin-top:40px;display:flex;align-items:center;gap:24px">
    <div class="tile">{icon("growth")}</div>
    <p class="p ink">Global AI projects are already investing in Vietnam's builder community, with meetups, workshops and free credits in Ho Chi Minh City throughout 2026.</p>
  </div>
</div>""")

# 04 Challenge ---------------------------------------------------------------
pains = [
    ("audit", "Reaching the right people", "Getting past the hype to builders and users who will actually adopt."),
    ("content", "No Vietnamese docs yet", "Quickstarts, tutorials and videos are English-only."),
    ("social", "Different channels", "Vietnam's AI crowd lives on Facebook groups and Zalo, not Discord."),
    ("community", "No local team", "Nobody on the ground to run community and answer questions."),
    ("data", "Events with no follow-up", "The meetup ends, the momentum ends. No data, no next step."),
]
cards = "".join(f"""
<div class="card" style="padding:32px">
  <div class="tile" style="margin-bottom:26px">{icon(i)}</div>
  <div class="h3" style="margin-bottom:12px">{t}</div><div class="p">{d}</div>
</div>""" for i, t, d in pains)
slide("light", "The challenge", f"""
<div class="content">
  {head("The challenge", "A great product", "isn't enough to get users.")}
  <div class="grid" style="grid-template-columns:repeat(5,1fr)">{cards}</div>
  <div style="margin-top:36px;background:{MIDNIGHT};border-radius:28px;padding:30px 40px;display:flex;align-items:center;gap:26px">
    <div style="color:{AQUA}">{icon("ai", 44)}</div>
    <div class="h3" style="color:{WHITE}">Vibe AI Labs solves all five, as one local partner.</div>
  </div>
</div>""")

# 05 Community ---------------------------------------------------------------
groups = [
    ("AI Agent Việt Nam (OpenClaw, Hermes Agent, Muse, Dots, Grok Bot, Spark).png", "AI Agent Việt Nam",
     "OpenClaw, Hermes Agent, Muse, Dots, Grok Bot, Spark", "openclaw.vietnamcommunity"),
    ("AI Agent Marketing Việt Nam .png", "AI Agent Marketing Community",
     "Applying AI agents to digital marketing", "ai.agents.marketing"),
    ("Vibe Marketing Việt Nam (Branding - Content - AI Marketing).png", "Vibe Marketing Vietnam",
     "Brand · Content · AI Marketing", "vertical.ai.vietnam"),
    ("Chạy Quảng Cáo ChatGPT Ads Hiệu Quả.png", "Running ChatGPT Ads Effectively",
     "Advertising on ChatGPT", "chatgptads.vietnamgroup"),
]
cards = "".join(f"""
<div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column">
  <img src="{light_img(COVERS / f)}" style="width:100%;height:196px;object-fit:cover;display:block">
  <div style="padding:24px 30px 26px;display:flex;flex-direction:column;flex:1">
    <div class="h3" style="margin-bottom:10px">{n}</div>
    <div class="p">{t}</div>
    <div class="src" style="color:rgba(217,226,242,.7);margin-top:auto;padding-top:14px">facebook.com/groups/<br>{u}</div>
  </div>
</div>""" for f, n, t, u in groups)
slide("dark", "Our community", f"""
<div class="content">
  {head("Our community", "100,000+ members", "across 4 communities.",
        "Run by Vibe AI Labs. The daily home of Vietnamese builders, marketers and founders who use AI at work.", dark=True)}
  <div class="grid" style="grid-template-columns:repeat(4,1fr)">{cards}</div>
</div>""", bg=WAVES)


# 06 Track record ------------------------------------------------------------
def badge(inner, bg, border):
    return (f'<div style="width:150px;height:150px;border-radius:50%;background:{bg};border:4px solid {border};'
            f'display:flex;align-items:center;justify-content:center;overflow:hidden">{inner}</div>')


topics = [
    (badge(f'<div style="color:{BLUE}">{icon("agent", 76)}</div>', "#EEF3FF", BLUE), "AI Agents",
     "Meetups on building and using AI agents in real work."),
    (badge(f'<img src="{OPENCLAW}" style="width:150px;height:150px;object-fit:cover">', "#0B0B10", "#FF5A4E"), "OpenClaw",
     "Community meetups on the OpenClaw ecosystem."),
    (badge(f'<img src="{HERMES}" style="width:118px;height:118px;object-fit:contain">', WHITE, AQUA), "Hermes Agent",
     "Community meetups on Hermes Agent by Nous Research."),
]
cards = "".join(f"""
<div class="card" style="display:flex;flex-direction:column;align-items:center;text-align:center;padding:44px 40px 40px">
  {b}<div class="h3" style="margin:30px 0 12px">{t}</div><div class="p">{d}</div>
</div>""" for b, t, d in topics)
slide("light", "Track record", f"""
<div class="content">
  {head("Track record", "We've done this", "before.",
        "Vibe AI Labs has hosted community meetups on the tools Vietnam's builders care about most.")}
  <div class="grid" style="grid-template-columns:repeat(3,1fr)">{cards}</div>
  <p class="p" style="margin-top:28px">Our AI Agent Việt Nam community also covers <b class="ink">Muse, Dots, Grok Bot and Spark</b>.</p>
</div>""")

# 07 Audience ----------------------------------------------------------------
aud = [
    ("agent", "Developers &amp; AI engineers"),
    ("strategy", "Founders &amp; business owners"),
    ("content", "Marketers &amp; content creators"),
    ("ideas", "Freelancers &amp; consultants"),
    ("intelligence", "Tech students"),
]
cards = "".join(f"""
<div class="card" style="text-align:center;padding:44px 26px">
  <div class="tile" style="margin:0 auto 26px;width:84px;height:84px">{icon(i, 46)}</div>
  <div class="h3">{t}</div>
</div>""" for i, t in aud)
slide("light", "Audience", f"""
<div class="content">
  {head("Who's in the room", "Builders, users", "and decision-makers.")}
  <div class="grid" style="grid-template-columns:repeat(5,1fr)">{cards}</div>
  <div class="card" style="margin-top:36px;display:flex;align-items:center;gap:28px;background:#EEF3FF;border-color:#C9D8FF">
    <div style="color:{BLUE};flex:none">{icon("growth", 48)}</div>
    <p class="statement">Not only engineers. Our communities include the marketers and business owners who become paying users.</p>
  </div>
</div>""")

# 08 What we do --------------------------------------------------------------
layers = [
    ("community", "Community", ["Spotlight in our 4 communities", "AMAs &amp; livestreams", "Ambassador program", "A dedicated channel for your project"]),
    ("speed", "Events", ["Meetups", "Hands-on workshops", "Build Days &amp; hackathons", "Launch events &amp; webinars"]),
    ("design", "Content &amp; Creative", ["Vietnamese docs &amp; video tutorials", "Key visuals &amp; landing pages", "Recap photo &amp; video", "PR and KOL/KOC"]),
    ("data", "Data &amp; Reporting", ["Registration &amp; attendance", "Activation via unique links", "Feedback surveys", "A report after every activity"]),
]
cards = "".join(f"""
<div class="card" style="padding:40px 36px">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:28px">
    <div class="tile">{icon(i)}</div><div class="label">0{k}</div></div>
  <div class="h3" style="margin-bottom:22px">{t}</div>
  <ul class="clean">{"".join(f"<li>{x}</li>" for x in items)}</ul>
</div>""" for k, (i, t, items) in enumerate(layers, 1))
slide("light", "What we do", f"""
<div class="content">
  {head("What we do", "Four layers,", "one system.")}
  <div class="grid" style="grid-template-columns:repeat(4,1fr)">{cards}</div>
</div>""")

# 09 Event formats -----------------------------------------------------------
fmts = [
    ("Meetup", "50–150", "2.5 hours", "Introduce your project and build awareness."),
    ("Hands-on workshop", "20–50, laptops on", "2–3 hours", "Attendees install and run your product themselves."),
    ("Build Day / Hackathon", "30–100", "1–2 days", "Real use cases, sample projects, top builders."),
    ("Launch event", "80–200", "2–3 hours", "Launch a product or feature in Vietnam."),
    ("Webinar · Livestream · AMA", "Online", "60–90 min", "Nationwide reach at low cost."),
]
val = f"font:600 {BODY}px 'Inter',Arial,sans-serif;color:{INK};margin:6px 0 20px"
cards = "".join(f"""
<div class="card" style="display:flex;flex-direction:column;padding:36px 30px">
  <div class="h3" style="min-height:72px">{t}</div>
  <div style="margin:22px 0;border-top:1px solid {LINE}"></div>
  <div class="label">Size</div><div style="{val}">{s}</div>
  <div class="label">Duration</div><div style="{val}">{d}</div>
  <div class="label">Best for</div><div class="p" style="margin-top:6px">{b}</div>
</div>""" for t, s, d, b in fmts)
slide("light", "Formats", f"""
<div class="content">
  {head("Event formats", "Pick the format", "that fits the goal.")}
  <div class="grid" style="grid-template-columns:repeat(5,1fr)">{cards}</div>
  <p class="src" style="margin-top:24px">Sizes are indicative and agreed per project.</p>
</div>""")

# 10 Run of show -------------------------------------------------------------
ros = [
    ("18:30", "Check-in &amp; networking"),
    ("19:00", "Welcome from Vibe AI Labs &amp; the partner project"),
    ("19:10", "What's new: the project team presents"),
    ("19:30", "2–3 real use cases from community builders"),
    ("20:15", "Hands-on: install and run a first task"),
    ("20:45", "Q&amp;A and networking"),
    ("21:00", "Close"),
]
rows = "".join(f"""
<div style="display:flex;align-items:baseline;gap:30px;padding:14px 0;border-bottom:1px solid rgba(217,226,242,.14)">
  <div style="font:700 {SUB}px 'Plus Jakarta Sans',Arial,sans-serif;color:{AQUA};width:104px;flex:none">{t}</div>
  <div style="font:400 {SUB}px/1.3 'Inter',Arial,sans-serif;color:{WHITE}">{d}</div>
</div>""" for t, d in ros)
take = "".join(f"<li>{x}</li>" for x in ["A Vietnamese quickstart guide", "Trial credits, when the project sponsors them", "A place in the community after the event"])
slide("dark", "A Vibe AI Meetup", f"""
<div class="content">
  {head("A Vibe AI Meetup", "Fewer slides,", "more hands-on.", dark=True)}
  <div style="display:grid;grid-template-columns:1.35fr 1fr;gap:56px">
    <div>{rows}</div>
    <div class="card" style="align-self:start;padding:44px">
      <div class="over" style="margin-bottom:24px">Attendees leave with</div>
      <ul class="clean">{take}</ul>
      <div class="p" style="margin-top:28px;border-top:1px solid rgba(217,226,242,.16);padding-top:26px">
        Every session is livestreamed or recorded, then turned into recap content for the community.</div>
    </div>
  </div>
</div>""")

# 11 Process -----------------------------------------------------------------
steps = [
    ("T–4 weeks", "Brief", "Goals, audience, KPIs, format, venue, speakers."),
    ("T–3 weeks", "Build", "Key visual, registration page, Vietnamese docs."),
    ("T–2 weeks", "Promote", "Campaign across our 4 communities, speakers, KOLs."),
    ("T–1 week", "Rehearse", 'Tech <span class="nw">run-through</span>, credits &amp; swag, <span class="nw">check-in</span>.'),
    ("Day D", "Run", "Host, livestream, photo &amp; video."),
    ("T+1 week", "Follow up", "Recap, video, survey, move attendees into the community."),
    ("T+2 weeks", "Report", "Results and recommended next steps."),
]
cells = ""
for k, (w, t, d) in enumerate(steps):
    dot, ring = (AQUA, "rgba(20,216,196,.18)") if k == 4 else (BLUE, "rgba(37,99,255,.14)")
    cells += f"""
<div style="position:relative;padding-top:58px">
  <div style="position:absolute;top:0;left:0;width:30px;height:30px;border-radius:50%;background:{dot};box-shadow:0 0 0 8px {ring}"></div>
  <div class="label" style="color:{BLUE}">{w}</div>
  <div class="h3" style="margin:10px 0 12px">{t}</div>
  <div class="p">{d}</div>
</div>"""
slide("light", "How we work", f"""
<div class="content">
  {head("How we work", "Six weeks,", "one complete cycle.")}
  <div style="position:relative">
    <div style="position:absolute;top:14px;left:15px;right:40px;height:3px;background:linear-gradient(90deg,{BLUE},{AQUA})"></div>
    <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:26px">{cells}</div>
  </div>
  <div class="card" style="margin-top:64px;display:flex;align-items:center;gap:26px;padding:28px 36px">
    <div class="tile">{icon("automation")}</div>
    <p class="statement">Our method, <b>Audit → Build → Automate → Grow</b>, applied to community.</p>
  </div>
</div>""")

# 12 Packages ----------------------------------------------------------------
pk = [
    ("Community Spotlight", "1 month", "Test how the community responds.", False,
     ["Spotlight in our 4 communities", "1 AMA or livestream", "Vietnamese quickstart", "Recap post", "Month-end report"]),
    ("Meetup Partner", "1 event", "Launch and win your first users.", True,
     ["Everything in Spotlight", "1 meetup or hands-on workshop", "Quickstart + video tutorial", "Full recap: photo, video, article", "Post-event report"]),
    ("Ecosystem Partner", "3–6 months", "Build a lasting user community.", False,
     ["Regular community spotlights", "Monthly meetup series + 1 Build Day", "Full Vietnamese documentation", "Ambassador program", "Dedicated, moderated channel", "Monthly reports"]),
]
cols = ""
for name, dur, goal, hi, items in pk:
    style = f"border:3px solid {BLUE};background:#FBFCFF" if hi else ""
    tag = (f'<div class="label" style="position:absolute;top:-18px;left:36px;background:{BLUE};color:{WHITE};'
           f'padding:8px 18px;border-radius:999px">Recommended start</div>') if hi else ""
    lis = "".join(f"<li>{x}</li>" for x in items)
    cols += f"""
<div class="card" style="position:relative;padding:36px 38px 28px;height:100%;{style}">{tag}
  <div class="label" style="color:{BLUE}">{dur}</div>
  <div class="h3" style="margin:10px 0 8px">{name}</div>
  <div class="p ink" style="margin-bottom:20px">{goal}</div>
  <div style="border-top:1px solid {LINE};margin-bottom:20px"></div>
  <ul class="clean">{lis}</ul>
</div>"""
slide("light", "Partnership", f"""
<div class="content">
  {head("Partnership", "Three ways", "to start together.")}
  <div class="grid" style="grid-template-columns:repeat(3,1fr);gap:34px;height:476px">{cols}</div>
  <div style="margin-top:28px;display:flex;justify-content:space-between;align-items:center">
    <p class="p"><b class="ink">Add-ons:</b> Hackathon · Video production · KOL/KOC · Chinese-language content · Side events at major conferences</p>
    <p style="font:700 {BODY}px 'Plus Jakarta Sans',Arial,sans-serif;color:{BLUE};white-space:nowrap">Pricing: quoted by scope</p>
  </div>
</div>""")

# 13 Measurement & principles ------------------------------------------------
metrics = ["Registrations", "Show-up rate", "Post-event feedback", "Activation via unique links", "Content engagement", "Community growth"]
princ = [
    ("ideas", "Real use cases, no buzzwords", "Speakers are people who actually use the product."),
    ("data", "Honest numbers", "We report real figures. Nothing inflated."),
    ("human-in-the-loop", "Consent-based data", "Attendee data is shared only with consent, under Vietnam's personal data protection law."),
    ("brand", "Respect for your brand", "Logos and product names used exactly as your guidelines require."),
]
pc = "".join(f"""
<div class="card" style="display:flex;gap:24px;padding:30px">
  <div class="tile">{icon(i)}</div>
  <div><div class="h3" style="margin-bottom:8px">{t}</div><div class="p">{d}</div></div>
</div>""" for i, t, d in princ)
chips = "".join(f'<span class="chip">{m}</span>' for m in metrics)
slide("light", "Measurement", f"""
<div class="content">
  {head("Measurement &amp; principles", "Measured.", "Honest.")}
  <div style="display:grid;grid-template-columns:1fr 1.55fr;gap:44px">
    <div class="card" style="padding:40px">
      <div class="over" style="margin-bottom:26px">What we track</div>
      <div>{chips}</div>
      <p class="p" style="margin-top:24px">We commit to the process and to transparent reporting, not to guessed numbers.</p>
    </div>
    <div class="grid" style="grid-template-columns:1fr 1fr;gap:24px">{pc}</div>
  </div>
</div>""")

# 14 Why us ------------------------------------------------------------------
why = [
    ("100,000+ members", "across 4 communities we run ourselves."),
    ("Meetups already hosted", "on AI Agents, OpenClaw and Hermes Agent."),
    ("We know AI from the inside", "We deploy AI agents for our own clients."),
    ("Creative in-house", "Content, design, video and PR without extra vendors."),
    ("Three languages", "Vietnamese, English and Chinese."),
]
rows = "".join(f"""
<div style="display:grid;grid-template-columns:90px 1fr;align-items:baseline;padding:22px 0;border-bottom:1px solid rgba(217,226,242,.14)">
  <div style="font:700 {SUB}px 'Plus Jakarta Sans',Arial,sans-serif;color:{AQUA}">0{k}</div>
  <div><span class="h3">{t}</span><span class="p" style="margin-left:16px">{d}</span></div>
</div>""" for k, (t, d) in enumerate(why, 1))
slide("dark", "Why Vibe AI Labs", f"""
<div class="content">
  {head("Why Vibe AI Labs", "Community, tech and creative,", "in one team.", dark=True)}
  <div style="max-width:1500px">{rows}</div>
</div>""")

# 15 Closing -----------------------------------------------------------------
contacts = [
    ("Website", WEBSITE), ("Facebook", FACEBOOK), ("X", X_HANDLE), ("Email", EMAIL),
    ("Contact", "Henry Le, Marketing Engineer &amp; Founder"), ("Address", ADDRESS),
]
crow = "".join(f"""
<div style="display:grid;grid-template-columns:170px 1fr;align-items:baseline;padding:8px 0">
  <div class="label">{k}</div>
  <div style="font:400 {BODY}px 'Inter',Arial,sans-serif;color:{WHITE}">{v}</div>
</div>""" for k, v in contacts)
slide("dark", "Contact", f"""
<img src="{RIBBON_MARK}" style="position:absolute;left:1100px;top:380px;width:1500px;z-index:1">
<div class="z" style="position:absolute;left:96px;top:180px;width:{CONTENT_W}px">
  {headline("Let's build your", "community in Vietnam.", HERO, 800, -0.03, dark=True)}
  <p class="lead">A 30-minute call to understand your goals in Vietnam and pick the right format.</p>
  <div style="margin:40px 0 36px"><a class="btn" href="{CONTACT_URL}">Book a call</a></div>
  {crow}
</div>""", number=False)

# Build ----------------------------------------------------------------------
html = (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Vibe AI Community &amp; Events</title>"
        f"<style>{font_faces()}{CSS}</style></head><body>{''.join(PAGES)}<script>{FIT_JS}</script></body></html>")
OUT_HTML.write_text(html, encoding="utf-8")

ud = tempfile.mkdtemp(prefix="chr_")
try:
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--user-data-dir=" + ud,
                    "--no-first-run", "--allow-file-access-from-files", "--no-pdf-header-footer",
                    "--virtual-time-budget=8000", "--print-to-pdf=" + str(OUT_PDF), OUT_HTML.as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=240, check=True)
finally:
    shutil.rmtree(ud, ignore_errors=True)
print(f"{len(PAGES)} slides -> {OUT_PDF}")
