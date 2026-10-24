import os, re, json, shutil
OUT="/tmp/kit_out"
BRAND="Vibe AI Labs"
DESCRIPTOR="AI-Powered Growth & Creative Agency"
DESCRIPTOR_VI="Agency tăng trưởng & sáng tạo ứng dụng AI"
BRAND_LINE="Ideas. Intelligence. Real Growth."
CAMPAIGN_LINE="Turn Brands into Growth"
WEBSITE="https://vibe-ai-labs.vibeailabs.workers.dev"
WEBSITE_SHORT="vibe-ai-labs.vibeailabs.workers.dev"
EMAIL="vibeailabs@gmail.com"
ADDRESS1="WORC@Q2 Building, 21 Võ Trường Toản"
ADDRESS2="An Khánh, TP. Hồ Chí Minh"
FACEBOOK="facebook.com/vibe.ai.labs"
XHANDLE="x.com/vibe_ai_labs"
FOUNDER="Henry Le"; FOUNDER_TITLE="Marketing Engineer · Founder"
C=dict(midnight="#0B1026",blue="#2563FF",aqua="#14D8C4",violet="#8B5CF6",cloud="#F8FAFC",
       ink="#111827",slate="#667085",line="#D9E2F2",white="#FFFFFF",green="#16A34A",orange="#F97316")
def w(path,text,mode="w"):
    p=os.path.join(OUT,path); os.makedirs(os.path.dirname(p),exist_ok=True)
    if isinstance(text,bytes): open(p,"wb").write(text)
    else: open(p,"w",encoding="utf8").write(text)
    return p
def vb(svg):
    m=re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)"',svg); return [float(v) for v in m.groups()]
