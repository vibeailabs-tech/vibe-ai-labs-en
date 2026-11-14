"""Build the "Gói dịch vụ" pages for the Vibe AI Labs company profile (A4 landscape) and insert them into the
existing PDF before the "Toàn cảnh dịch vụ" page, renumbering the pages that follow (09-45 -> 12-48).

The original deck source is not in the repo, so the page chrome (logo, section label, footer, cards, pills,
type scale) is re-created from measurements of the exported PDF. `--calib` adds replicas of the original
pages 11 and 9 to the build so the styles can be compared against the source PDF.

Run:  python3 build_packages.py --lang vi            -> builds into the temp folder only
      python3 build_packages.py --lang vi --write    -> also overwrites 01_General/01_Company-Profile/..._VI.pdf
The source PDF must be the original 45-page export (restore it with git before re-running).
"""
import argparse
import html
import pathlib
import shutil
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[4]
BK = ROOT / "02_Brandkit" / "01_General-Brandkit"
PROFILE_DIR = ROOT / "01_General" / "01_Company-Profile"
WORK = pathlib.Path(tempfile.gettempdir()) / "vibe_profile_packages"
SOURCE_PAGES = 45
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

MIDNIGHT, INK, BODY, SLATE = "#0B1026", "#111827", "#4B5563", "#667085"
PILLARS = {  # text color, strong color, pill bg, pill border, tile bg
    "mkt": dict(text="#2563FF", strong="#2563FF", bg="#EBF1FF", line="#B3C9FF", tile="rgba(37,99,255,.09)"),
    "ai": dict(text="#15803D", strong="#16A34A", bg="#EAF7EF", line="#AADDBD", tile="rgba(22,163,74,.09)"),
    "cre": dict(text="#C2410C", strong="#F97316", bg="#FEF1E7", line="#FCC6A0", tile="rgba(249,115,22,.10)"),
}


def uri(p):
    return pathlib.Path(p).as_uri()


def icon(name, size=30):
    svg = (BK / "05_Icons" / "SVG_currentColor" / f"{name}.svg").read_text()
    return svg.replace('width="24" height="24"', f'width="{size}" height="{size}"', 1)


def e(s):
    return html.escape(s, quote=False)


FONT_DIR = BK / "03_Typography" / "fonts"
CSS = f"""
@font-face{{font-family:'Plus Jakarta Sans';src:url('{uri(FONT_DIR / "PlusJakartaSans[wght].ttf")}');font-weight:200 800}}
@font-face{{font-family:'Inter';src:url('{uri(FONT_DIR / "Inter[opsz,wght].ttf")}');font-weight:100 900}}
@page{{size:A4 landscape;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:'Inter',Arial,sans-serif;color:{INK};font-optical-sizing:auto}}
.slide{{width:1122.5px;height:794px;position:relative;overflow:hidden;break-after:page;background:#F8FAFC}}
.slide::before{{content:'';position:absolute;inset:0;background:
  radial-gradient(480px 324px at 100% 0%,rgba(37,99,255,.125),transparent),
  radial-gradient(400px 284px at 0% 100%,rgba(20,216,196,.17),transparent)}}
.slide>*{{position:absolute}}
.jk{{font-family:'Plus Jakarta Sans',Arial,sans-serif}}
.logo{{left:52px;top:25.9px;height:30px}}
.section{{right:52px;top:34.7px;font:700 9.5px/12px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;
  text-transform:uppercase;color:{SLATE};white-space:nowrap}}
.foot{{left:52px;right:52px;top:758px;display:flex;justify-content:space-between;font:400 10px/12px 'Inter',Arial,sans-serif;color:{SLATE}}}
.foot b{{font-weight:700;color:{INK}}}
.note{{left:52px;top:728px;font:400 10px/12px 'Inter',Arial,sans-serif;color:{SLATE}}}

/* title pages */
.over{{left:52px;top:88.6px;font:700 10.5px/13px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#2563FF;white-space:nowrap}}
.title{{left:52px;top:111px;font:800 34px/42px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.025em;color:{MIDNIGHT};white-space:nowrap}}
.title em{{font-style:normal;color:#2563FF}}
.lead{{left:52px;top:160px;font:400 12.5px/19px 'Inter',Arial,sans-serif;color:{BODY};white-space:nowrap}}

/* service-style page: left column */
.tile{{left:52px;top:82px;width:54px;height:54px;border-radius:16px;background:rgba(37,99,255,.09);color:#2563FF;
  display:flex;align-items:center;justify-content:center}}
.left{{left:52px;top:145px;width:292px}}
.num{{font:800 58px/64px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.043em;color:#2563FF}}
.name{{font:800 25px/29px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.025em;color:{MIDNIGHT};margin-top:3px}}
.desc{{font:400 12.5px/19.375px 'Inter',Arial,sans-serif;color:{BODY};margin-top:9.5px}}
.flow{{display:flex;flex-wrap:wrap;align-items:center;gap:4px 0;margin-top:12.4px}}
.flow b{{font:600 10.5px/21px 'Inter',Arial,sans-serif;color:#2563FF;background:rgba(37,99,255,.09);border-radius:6px;padding:0 7px}}
.flow i{{font:400 10px/21px 'Inter',Arial,sans-serif;font-style:normal;color:{SLATE};padding:0 3px}}
.meta{{margin-top:22px;display:grid;grid-template-columns:auto 1fr;gap:9px 12px;align-items:baseline}}
.meta dt{{font:800 9.5px/14px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#2563FF;white-space:nowrap}}
.meta dd{{font:400 12px/16px 'Inter',Arial,sans-serif;color:{INK}}}
.role{{left:52px;bottom:48px;width:292px;border:1px solid #A6C5FA;border-radius:12px;padding:15px 16px 14px;
  background:linear-gradient(60deg,#CBE8F6 0%,#D6EAF9 50%,#E2EDFB 100%)}}
.role h4{{font:800 9.5px/12px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#2563FF}}
.role p{{font:400 12px/18px 'Inter',Arial,sans-serif;color:{INK};margin-top:6px}}

/* right card */
.card{{left:370px;top:82px;width:700.5px;height:664px;background:#fff;border:1px solid #CBD6EA;border-radius:22px;padding:0 20px}}
.card h3{{font:800 10px/12px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#2563FF;
  padding:18.5px 0 11.5px;border-bottom:1px solid #E6ECF7}}
.fitbox{{height:var(--fit-h);overflow:hidden}}
.fit{{zoom:var(--zoom,1);padding-top:6.3px}}
.grp{{margin-bottom:13px}}
.grp:last-child{{margin-bottom:0}}
.grp h5{{font:700 11px/14px 'Plus Jakarta Sans',Arial,sans-serif;color:var(--c);display:flex;align-items:center;gap:4px;margin-bottom:7px}}
.grp h5::before{{content:'';width:4px;height:4px;border-radius:50%;background:var(--dot,var(--c));flex:none}}
.pills{{display:flex;flex-wrap:wrap;gap:5px 5px}}
.pills span{{white-space:nowrap;font:500 10.5px/13.4px 'Inter',Arial,sans-serif;color:{INK};background:var(--bg);border:1px solid var(--line);
  border-radius:12px;padding:3.95px 9px;font-variation-settings:'opsz' calc(10.5 * var(--zoom,1))}}
.split{{display:grid;grid-template-columns:var(--split,1.55fr 1fr);gap:0 18px;border-top:1px solid #E6ECF7;padding-top:12px;margin-top:13px}}
.split .grp{{margin-bottom:0}}
.cardnote{{left:391px;top:722px;font:400 10px/12px 'Inter',Arial,sans-serif;color:{SLATE}}}

/* overview page: two package cards */
.pkg{{top:196px;width:501px;height:514px;background:#fff;border:1px solid #CBD6EA;border-top-width:5px;border-radius:22px;padding:22px 24px 20px;
  display:flex;flex-direction:column}}
.pkg .hd{{display:flex;align-items:center;gap:14px}}
.pkg .n{{font:800 40px/40px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.04em;color:#2563FF}}
.pkg .t{{font:800 22px/26px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.025em;color:{MIDNIGHT}}}
.pkg .who{{font:700 12px/16px 'Inter',Arial,sans-serif;color:#2563FF;margin-top:2px}}
.pkg .lb{{font:800 9.5px/14px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#2563FF;white-space:nowrap}}
.pkg .goal{{margin-top:18px}}
.pkg .goal p{{font:400 13px/19px 'Inter',Arial,sans-serif;color:{INK};margin-top:5px}}
.pkg .rows{{margin-top:16px;flex:1;display:flex;flex-direction:column;gap:8px}}
.pkg .row{{flex:1;display:flex;gap:14px;align-items:center;background:var(--bg);border-radius:12px;padding:0 16px}}
.pkg .row .ic{{flex:none;width:40px;height:40px;border-radius:12px;background:#fff;color:var(--strong);display:flex;align-items:center;justify-content:center}}
.pkg .row h5{{font:700 12px/15px 'Plus Jakarta Sans',Arial,sans-serif;color:var(--c)}}
.pkg .row p{{font:400 13px/18px 'Inter',Arial,sans-serif;color:{INK};margin-top:4px}}
.pkg .ft{{display:grid;grid-template-columns:auto 1fr;gap:10px 12px;align-items:center;margin-top:16px}}
.pkg .ft dt{{font:800 9.5px/14px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#2563FF;white-space:nowrap}}
.pkg .ft dd{{font:400 12px/16px 'Inter',Arial,sans-serif;color:{INK}}}
.pkg .ft .flow{{margin-top:0}}
"""

FIT_JS = """
<script>
document.fonts.ready.then(() => {
  document.querySelectorAll('.fitbox').forEach(box => {
    const fit = box.firstElementChild, max = parseFloat(box.dataset.max || '1.5');
    const ok = z => { fit.style.setProperty('--zoom', z); return fit.getBoundingClientRect().height <= box.clientHeight + 0.5; };
    let z = max;
    while (z > 0.6 && !ok(z)) z = Math.round((z - 0.005) * 1000) / 1000;
    box.dataset.zoom = z;
  });
  if (location.hash === '#debug') document.title = 'ZOOM ' + [...document.querySelectorAll('.fitbox')].map(b => b.dataset.zoom).join(',');
});
</script>
"""

T = {
    "vi": dict(
        doc_title="Vibe AI Labs — Gói dịch vụ",
        footer="Vibe AI Labs · Ideas. Intelligence. Real Growth.",
        section="GÓI DỊCH VỤ",
        over="GÓI DỊCH VỤ",
        title=("Hai gói dịch vụ.", "Chọn theo giai đoạn của bạn."),
        lead="Mỗi gói kết hợp Marketing, Trí tuệ nhân tạo (AI) và Sáng tạo thành một hệ thống, thay vì chọn lẻ từng dịch vụ.",
        note="Chi phí được báo theo phạm vi của từng doanh nghiệp. Bước đầu tiên là một buổi trao đổi để xác định gói phù hợp.",
        pillars=dict(mkt="Marketing số", ai="Trí tuệ nhân tạo (AI) & Tự động hóa", cre="Thiết kế & Sáng tạo"),
        l_goal="Mục tiêu", l_focus="Trọng tâm", l_mode="Hình thức", l_scope="PHẠM VI GÓI", l_role="VAI TRÒ",
        l_deliver="Bàn giao", l_kpi="Chỉ số theo dõi",
        packages=[
            dict(
                num="01", name="Khởi động", icon="ideas",
                who="Dành cho doanh nghiệp mới bắt đầu",
                goal="Có thương hiệu, kênh bán và công cụ cơ bản để tìm khách và đo lường.",
                brief=dict(mkt="Định vị, landing page, kênh mạng xã hội, đo lường",
                           ai="Chatbot trả lời khách, tự động hóa tác vụ đơn giản",
                           cre="Logo, nhận diện cơ bản, template, ảnh sản phẩm bằng AI"),
                focus=["Audit", "Build"], mode="Theo dự án",
                desc="Dành cho doanh nghiệp mới bắt đầu. Xây nền tảng thương hiệu, kênh số và công cụ AI cơ bản để bắt đầu "
                     "tìm khách hàng và đo lường được kết quả.",
                flow=["Định vị", "Nhận diện", "Kênh số", "Tự động hóa cơ bản", "Đo lường"],
                role="Giúp doanh nghiệp mới có một hệ thống gọn, đủ dùng và sẵn sàng mở rộng, thay vì làm từng phần rời rạc.",
                scope=dict(
                    mkt=["Xây dựng chân dung khách hàng", "Định vị thương hiệu", "Xây dựng thông điệp thương hiệu",
                         "Landing Page (1 trang)", "Thiết lập biểu mẫu thu khách hàng tiềm năng",
                         "Thiết lập Google Analytics và theo dõi chuyển đổi",
                         "Xây dựng định hướng kênh (1–2 kênh: Facebook, TikTok hoặc Zalo OA)", "Lập lịch nội dung tháng đầu"],
                    ai=["Xác định bài toán ứng dụng AI", "Chatbot AI cho website hoặc Trợ lý FAQ",
                        "Tự động hóa tác vụ: biểu mẫu → danh sách khách hàng → thông báo qua email hoặc Zalo",
                        "Đào tạo AI cho đội ngũ (1 buổi căn bản)"],
                    cre=["Thiết kế logo", "Hệ thống màu sắc", "Typography", "Bộ hướng dẫn thương hiệu (bản rút gọn)",
                         "Danh thiếp & văn phòng phẩm", "Thiết kế mạng xã hội: bộ template bài đăng", "Hình ảnh sản phẩm bằng AI"]),
                deliver=["File logo và bộ nhận diện", "Landing page đang chạy, kèm tài khoản và quyền truy cập",
                         "Chatbot và quy trình tự động đã cấu hình", "Lịch nội dung tháng đầu", "Tài liệu hướng dẫn sử dụng",
                         "Hỗ trợ 30 ngày sau bàn giao"],
                kpi=["Lưu lượng truy cập", "Số khách hàng tiềm năng", "Tỷ lệ chuyển đổi của landing page", "Thời gian phản hồi khách"],
                cardnote=None,
            ),
            dict(
                num="02", name="Tăng tốc", icon="speed",
                who="Dành cho doanh nghiệp đã hoạt động, muốn nâng cao hiệu quả",
                goal="Giảm việc thủ công, tăng chuyển đổi và mở rộng quy mô.",
                brief=dict(mkt="Quảng cáo hiệu suất, CRO, SEO và tìm kiếm bằng AI, CRM",
                           ai="AI Agent, chatbot RAG, tự động hóa bán hàng và báo cáo",
                           cre="Key visual, video, nội dung số lượng lớn bằng AI tạo sinh"),
                focus=["Automate", "Grow"], mode="Theo dự án, sau đó hợp tác định kỳ",
                desc="Dành cho doanh nghiệp đã có thương hiệu, kênh bán và khách hàng. Ứng dụng AI, dữ liệu và tự động hóa để "
                     "hệ thống chạy hiệu quả hơn và mở rộng được.",
                flow=["Đánh giá", "Tối ưu", "Tự động hóa", "Mở rộng"],
                role="Tìm điểm nghẽn trong hệ thống hiện có, tự động hóa những việc lặp lại và mở rộng những gì đã chứng minh hiệu quả.",
                scope=dict(
                    mkt=["Đánh giá tổng thể hoạt động Marketing", "Phân tích phễu Marketing", "Meta Ads", "Google Ads", "TikTok Ads",
                         "Quảng cáo bám đuổi", "CRO", "Tối ưu Landing Page", "Thử nghiệm A/B", "Chiến lược SEO", "GEO", "AEO",
                         "Thiết lập CRM", "Lead Scoring", "Lead Nurturing", "Email Marketing", "Zalo OA", "ZNS",
                         "Xây dựng bảng điều khiển báo cáo"],
                    ai=["Đánh giá mức độ sẵn sàng cho AI", "Lập bản đồ cơ hội ứng dụng AI", "AI Agent", "Quy trình nhiều AI Agent",
                        "Quy trình có con người kiểm soát và phê duyệt", "RAG Chatbot", "Trợ lý AI bán hàng",
                        "Trợ lý AI chăm sóc khách hàng", "Messenger / Zalo AI Bot", "Tự động hóa CRM", "Tự động hóa bán hàng",
                        "Tự động hóa báo cáo", "Tích hợp với phần mềm đang sử dụng"],
                    cre=["Thiết kế Key Visual", "Hình ảnh chiến dịch", "Nội dung quảng cáo bằng AI", "Tạo video bằng AI", "Video ngắn",
                         "Tạo biến thể nội dung sáng tạo ở quy mô lớn", "Làm mới hình ảnh (nếu cần)"]),
                deliver=["Báo cáo đánh giá hiện trạng và lộ trình", "AI Agent, chatbot và quy trình tự động đã cấu hình",
                         "Bảng điều khiển báo cáo", "Bộ key visual và thư viện nội dung", "Tài liệu kỹ thuật và hướng dẫn vận hành",
                         "Đào tạo người quản trị và người sử dụng"],
                kpi=["CPL", "Tỷ lệ chuyển đổi", "ROAS", "Thời gian tiết kiệm", "Tỷ lệ tự động hóa", "Sản lượng nội dung"],
                cardnote="Phạm vi cụ thể được điều chỉnh theo kết quả đánh giá hiện trạng.",
            ),
        ],
    ),
    "en": dict(
        doc_title="Vibe AI Labs — Service packages",
        footer="Vibe AI Labs · Ideas. Intelligence. Real Growth.",
        section="SERVICE PACKAGES",
        over="SERVICE PACKAGES",
        title=("Two service packages.", "Choose by your stage."),
        lead="Each package combines Marketing, Artificial Intelligence (AI) and Creative into one system, instead of picking services one by one.",
        note="Cost is quoted by each business's scope. The first step is a conversation to find the right package.",
        pillars=dict(mkt="Digital Marketing", ai="Artificial Intelligence (AI) & Automation", cre="Design & Creative Studio"),
        l_goal="Goal", l_focus="Focus", l_mode="Engagement", l_scope="PACKAGE SCOPE", l_role="ROLE",
        l_deliver="Deliverables", l_kpi="KPIs to track",
        packages=[
            dict(
                num="01", name="Kickstart", icon="ideas",
                who="For businesses just starting out",
                goal="A brand, sales channels and the basic tools to find customers and measure results.",
                brief=dict(mkt="Positioning, landing page, social channels, measurement",
                           ai="Customer-facing chatbot, simple task automation",
                           cre="Logo, basic identity, templates, AI product images"),
                focus=["Audit", "Build"], mode="Project-based",
                desc="For businesses just starting out. Build the brand foundation, digital channels and basic AI tools to start "
                     "finding customers and measuring results.",
                flow=["Positioning", "Identity", "Digital channels", "Basic automation", "Measurement"],
                role="Gives a new business a lean, sufficient system that is ready to scale, instead of building it piece by piece.",
                scope=dict(
                    mkt=["Customer persona development", "Brand positioning", "Brand messaging development",
                         "Landing page (1 page)", "Lead capture form setup", "Google Analytics and conversion tracking setup",
                         "Channel direction setting (1–2 channels: Facebook, TikTok or Zalo OA)", "First-month content calendar"],
                    ai=["AI use case definition", "AI chatbot for websites or FAQ assistant",
                        "Task automation: form → customer list → email or Zalo notification",
                        "AI training for teams (1 foundation session)"],
                    cre=["Logo design", "Color system", "Typography", "Brand guidelines (condensed version)",
                         "Business cards & stationery", "Social media design: post template set", "AI product images"]),
                deliver=["Logo files and identity kit", "Live landing page, with accounts and access rights",
                         "Configured chatbot and automation workflows", "First-month content calendar", "User guides",
                         "30 days of support after handover"],
                kpi=["Traffic", "Leads", "Landing page conversion rate", "Customer response time"],
                cardnote=None,
            ),
            dict(
                num="02", name="Accelerate", icon="speed",
                who="For established businesses looking to raise performance",
                goal="Less manual work, higher conversion and room to scale.",
                brief=dict(mkt="Performance advertising, CRO, SEO & AI search, CRM",
                           ai="AI Agents, RAG chatbot, sales and reporting automation",
                           cre="Key visuals, video, high-volume content with generative AI"),
                focus=["Automate", "Grow"], mode="Project-based, then ongoing retainer",
                desc="For businesses that already have a brand, sales channels and customers. Apply AI, data and automation so "
                     "the system runs more efficiently and can scale.",
                flow=["Assess", "Optimize", "Automate", "Scale"],
                role="Find the bottlenecks in the existing system, automate repetitive work and scale what has proven effective.",
                scope=dict(
                    mkt=["Overall Marketing review", "Marketing funnel analysis", "Meta Ads", "Google Ads", "TikTok Ads",
                         "Retargeting ads", "CRO", "Landing page optimization", "A/B testing", "SEO strategy", "GEO", "AEO",
                         "CRM setup", "Lead scoring", "Lead nurturing", "Email marketing", "Zalo OA", "ZNS",
                         "Reporting dashboard development"],
                    ai=["AI readiness assessment", "AI opportunity mapping", "AI Agent", "Multi-AI Agent workflows",
                        "Workflows with human oversight and approval", "RAG chatbot", "AI sales assistant",
                        "AI customer care assistant", "Messenger / Zalo AI Bot", "CRM automation", "Sales automation",
                        "Reporting automation", "Integration with the software you already use"],
                    cre=["Key visual design", "Campaign visuals", "AI ad content", "AI video generation", "Short-form video",
                         "Creative content variations at scale", "Visual refresh (if needed)"]),
                deliver=["Current-state assessment report and roadmap", "Configured AI Agents, chatbots and automation workflows",
                         "Reporting dashboard", "Key visual set and content library", "Technical documentation and operations guides",
                         "Administrator and end-user training"],
                kpi=["CPL", "Conversion rate", "ROAS", "Time saved", "Automation rate", "Content output"],
                cardnote="The exact scope is adjusted based on the current-state assessment.",
            ),
        ],
    ),
    "zh": dict(
        doc_title="Vibe AI Labs — 服务套餐",
        footer="Vibe AI Labs · Ideas. Intelligence. Real Growth.",
        section="服务套餐",
        over="服务套餐",
        title=("两个服务套餐。", "按你所处的阶段选择。"),
        lead="每个套餐都将营销、人工智能（AI）与创意结合成一套体系，而不是零散地挑选单项服务。",
        note="费用按每家企业的具体范围报价。第一步是通过一次沟通确定合适的套餐。",
        pillars=dict(mkt="数字营销", ai="人工智能（AI）与自动化", cre="设计与创意"),
        l_goal="目标", l_focus="重点", l_mode="合作方式", l_scope="套餐范围", l_role="作用",
        l_deliver="交付内容", l_kpi="跟踪指标",
        packages=[
            dict(
                num="01", name="起步", icon="ideas",
                who="适合刚起步的企业",
                goal="拥有品牌、销售渠道和基础工具，能够获客并衡量效果。",
                brief=dict(mkt="定位、落地页、社交媒体渠道、衡量",
                           ai="客户问答聊天机器人、简单任务自动化",
                           cre="标志、基础品牌识别、模板、AI 产品图片"),
                focus=["Audit", "Build"], mode="按项目合作",
                desc="适合刚起步的企业。搭建品牌基础、数字渠道和基础 AI 工具，开始获取客户并衡量成果。",
                flow=["定位", "识别", "数字渠道", "基础自动化", "衡量"],
                role="帮助新企业拥有一套精简、够用且随时可扩展的体系，而不是零散地逐项去做。",
                scope=dict(
                    mkt=["客户画像构建", "品牌定位", "品牌信息构建", "落地页（1 页）", "设置潜在客户收集表单",
                         "设置 Google Analytics 与转化跟踪", "确定渠道方向（1–2 个渠道：Facebook、TikTok 或 Zalo OA）", "首月内容排期"],
                    ai=["确定 AI 应用问题", "网站 AI 聊天机器人或 FAQ 助手", "任务自动化：表单 → 客户名单 → 邮件或 Zalo 通知",
                        "团队 AI 培训（1 场基础课）"],
                    cre=["标志设计", "色彩体系", "字体排印", "品牌指南（精简版）", "名片与办公用品", "社交媒体设计：帖子模板套组",
                         "AI 产品图片"]),
                deliver=["标志文件与品牌识别套件", "已上线的落地页，含账号与访问权限", "已配置的聊天机器人与自动化流程",
                         "首月内容排期", "使用指南", "交付后 30 天支持"],
                kpi=["流量", "潜在客户数", "落地页转化率", "客户响应时间"],
                cardnote=None,
            ),
            dict(
                num="02", name="加速", icon="speed",
                who="适合已在运营、希望提升成效的企业",
                goal="减少手工工作、提高转化并扩大规模。",
                brief=dict(mkt="效果广告、CRO、SEO 与 AI 搜索、CRM",
                           ai="AI Agent、RAG 聊天机器人、销售与报告自动化",
                           cre="主视觉、视频、生成式 AI 批量内容"),
                focus=["Automate", "Grow"], mode="先按项目合作，之后定期合作",
                desc="适合已有品牌、销售渠道和客户的企业。运用 AI、数据与自动化，让体系运转更高效并可扩展。",
                flow=["评估", "优化", "自动化", "扩展"],
                role="找出现有体系中的瓶颈，将重复工作自动化，并扩展已被验证有效的部分。",
                scope=dict(
                    mkt=["营销工作整体评估", "营销漏斗分析", "Meta 广告", "Google 广告", "TikTok 广告", "再营销广告", "CRO",
                         "落地页优化", "A/B 测试", "SEO 战略", "GEO", "AEO", "CRM 搭建", "潜在客户评分", "潜在客户培育",
                         "邮件营销", "Zalo OA", "ZNS", "搭建报告仪表板"],
                    ai=["AI 就绪度评估", "AI 应用机会图谱", "AI Agent", "多 AI Agent 工作流", "有人工把关与审批的流程",
                        "RAG 聊天机器人", "AI 销售助手", "AI 客户服务助手", "Messenger / Zalo AI Bot", "CRM 自动化",
                        "销售自动化", "报告自动化", "与现有软件集成"],
                    cre=["主视觉设计", "活动视觉", "AI 广告内容", "AI 视频生成", "短视频", "规模化生成创意内容变体",
                         "形象焕新（如需要）"]),
                deliver=["现状评估报告与路线图", "已配置的 AI Agent、聊天机器人与自动化流程", "报告仪表板",
                         "主视觉套组与内容库", "技术文档与运营指南", "管理员与使用者培训"],
                kpi=["CPL", "转化率", "ROAS", "节省的时间", "自动化率", "内容产量"],
                cardnote="具体范围将根据现状评估结果调整。",
            ),
        ],
    ),
}

# Chinese pages: CJK falls back to PingFang SC; labels are larger and not letter-spaced like the Latin caps.
LANG_CSS = {
    "en": ".over{letter-spacing:.16em}",
    "zh": """
.section{font-size:11.5px;letter-spacing:.1em}
.over{font-size:12.5px;letter-spacing:.1em;top:91px}
.title{top:114px;letter-spacing:0}
.lead{top:165px}
.name,.pkg .t{letter-spacing:-.008em}
.card h3{font-size:11px;letter-spacing:.1em;padding:19.5px 0 12.5px}
.role h4,.meta dt,.pkg .lb,.pkg .ft dt{font-size:11px;letter-spacing:.1em}
.role{padding-top:16px;padding-bottom:15px}
.role p{line-height:20px;margin-top:7px}
.desc{line-height:21px}
.pills span{line-height:13.85px;padding:4.6px 9px 3.3px}
""",
}

CALIB = {
    "vi": dict(section="MARKETING SỐ · 01 / 10", name="Chiến lược Marketing",
               desc="Lớp nền giúp hiểu thị trường, khách hàng, đối thủ và xác định hướng đi trước khi triển khai các hoạt động Marketing.",
               flow=["Nghiên cứu", "Khách hàng", "Đối thủ", "Chiến lược", "Kế hoạch"], l_role="VAI TRÒ",
               role="Giúp doanh nghiệp xác định đúng thị trường, đúng khách hàng, đúng thông điệp, đúng kênh và đúng hướng triển khai.",
               hdr="PHẠM VI DỊCH VỤ", grp="Nghiên cứu & phân tích", column=True,
               pills=["Nghiên cứu thị trường", "Nghiên cứu ngành hàng", "Phân tích xu hướng thị trường", "Phân tích đối thủ cạnh tranh"],
               section9="DỊCH VỤ", over="TOÀN CẢNH DỊCH VỤ", title="19 nhóm dịch vụ, ba năng lực, một hệ thống"),
    "en": dict(section="DIGITAL MARKETING · 01 / 10", name="Marketing strategy",
               desc="The base layer for understanding the market, customers and competitors, and setting direction before any Marketing activity begins.",
               flow=["Research", "Customers", "Competitors", "Strategy", "Plan"], l_role="ROLE",
               role="Helps businesses pinpoint the right market, the right customers, the right message, the right channels and the right way to execute.",
               hdr="SCOPE OF SERVICES", grp="Research & analysis", column=True,
               pills=["Market research", "Category research", "Market trend analysis", "Competitor analysis"],
               section9="SERVICES", over="SERVICES AT A GLANCE", title="19 service groups, three capabilities, one system"),
    "zh": dict(section="数字营销 · 01 / 10", name="营销战略",
               desc="在开展营销活动之前，先了解市场、客户和竞争对手并确定方向的基础层。",
               flow=["研究", "客户", "对手", "战略", "计划"], l_role="作用",
               role="帮助企业找准市场、客户、信息、渠道和执行方向。",
               hdr="服务范围", grp="研究与分析", column=False,
               pills=["市场研究", "品类研究", "市场趋势分析", "竞争对手分析", "目标客户分析", "消费者行为分析", "客户画像构建", "客户细分"],
               section9="服务", over="服务总览", title="19 个服务板块，三大能力，一套体系"),
}

PILLAR_ICONS = dict(mkt="growth", ai="ai", cre="design")
LOGO = uri(BK / "01_Logos" / "SVG" / "vibe-ai-labs_horizontal_color.svg")


def chrome(t, section, page_no):
    return (f'<img class="logo" src="{LOGO}" alt="Vibe AI Labs">'
            f'<div class="section">{e(section)}</div>'
            f'<div class="foot"><span>{e(t["footer"])}</span><b>{page_no:02d}</b></div>')


def flow(items):
    return '<div class="flow">' + "<i>→</i>".join(f"<b>{e(x)}</b>" for x in items) + "</div>"


def pvars(key):
    p = PILLARS[key]
    return f'--c:{p["text"]};--strong:{p["strong"]};--bg:{p["bg"]};--line:{p["line"]}'


def group(title, items, style):
    return (f'<div class="grp" style="{style}"><h5>{e(title)}</h5><div class="pills">'
            + "".join(f"<span>{e(x)}</span>" for x in items) + "</div></div>")


def overview_page(t, page_no):
    cards = []
    for i, p in enumerate(t["packages"]):
        rows = "".join(
            f'<div class="row" style="{pvars(k)}"><div class="ic">{icon(PILLAR_ICONS[k], 22)}</div>'
            f'<div><h5>{e(t["pillars"][k])}</h5><p>{e(p["brief"][k])}</p></div></div>' for k in ("mkt", "ai", "cre"))
        cards.append(
            f'<div class="pkg" style="left:{52 + i * 518}px">'
            f'<div class="hd"><div class="n">{p["num"]}</div><div><div class="t">{e(p["name"])}</div>'
            f'<div class="who">{e(p["who"])}</div></div></div>'
            f'<div class="goal"><div class="lb">{e(t["l_goal"])}</div><p>{e(p["goal"])}</p></div><div class="rows">{rows}</div>'
            f'<dl class="ft"><dt>{e(t["l_focus"])}</dt><dd>{flow(p["focus"])}</dd>'
            f'<dt>{e(t["l_mode"])}</dt><dd>{e(p["mode"])}</dd></dl></div>')
    return (f'<section class="slide">{chrome(t, t["section"], page_no)}'
            f'<div class="over">{e(t["over"])}</div>'
            f'<div class="title">{e(t["title"][0])} <em>{e(t["title"][1])}</em></div>'
            f'<div class="lead">{e(t["lead"])}</div>{"".join(cards)}'
            f'<div class="note">{e(t["note"])}</div></section>')


def package_page(t, p, idx, page_no):
    neutral = f"--c:{MIDNIGHT};--dot:#2563FF;--bg:#EEF3FF;--line:#C1D3FF"
    groups = "".join(group(t["pillars"][k], p["scope"][k], pvars(k)) for k in ("mkt", "ai", "cre"))
    split = f'<div class="split">{group(t["l_deliver"], p["deliver"], neutral)}{group(t["l_kpi"], p["kpi"], neutral)}</div>'
    fit_h = 596 - (20 if p["cardnote"] else 0)
    note = f'<div class="cardnote">{e(p["cardnote"])}</div>' if p["cardnote"] else ""
    label = "%s · %02d / %d" % (t["section"], idx, len(t["packages"]))
    return (f'<section class="slide">{chrome(t, label, page_no)}'
            f'<div class="tile">{icon(p["icon"])}</div>'
            f'<div class="left"><div class="num">{p["num"]}</div><div class="name">{e(p["name"])}</div>'
            f'<div class="desc">{e(p["desc"])}</div>{flow(p["flow"])}'
            f'<dl class="meta"><dt>{e(t["l_mode"])}</dt><dd>{e(p["mode"])}</dd>'
            f'<dt>{e(t["l_focus"])}</dt><dd>{e(" · ".join(p["focus"]))}</dd></dl></div>'
            f'<div class="role"><h4>{e(t["l_role"])}</h4><p>{e(p["role"])}</p></div>'
            f'<div class="card"><h3>{e(t["l_scope"])}</h3>'
            f'<div class="fitbox" style="--fit-h:{fit_h}px"><div class="fit">{groups}{split}</div></div></div>{note}</section>')


def calib_page(t, lang):
    """Replicas of the original pages 11 and 9, used only to check the re-created styles against the source PDF."""
    c = CALIB[lang]
    blue = pvars("mkt")
    col = "flex-direction:column;align-items:flex-start" if c["column"] else ""
    return (f'<section class="slide">{chrome(t, c["section"], 11)}'
            f'<div class="tile">{icon("strategy")}</div>'
            f'<div class="left"><div class="num">01</div><div class="name">{e(c["name"])}</div>'
            f'<div class="desc">{e(c["desc"])}</div>{flow(c["flow"])}</div>'
            f'<div class="role"><h4>{e(c["l_role"])}</h4><p>{e(c["role"])}</p></div>'
            f'<div class="card"><h3>{e(c["hdr"])}</h3><div class="fitbox" style="--fit-h:596px" data-max="1.5"><div class="fit" style="--zoom:1.5">'
            f'<div class="grp" style="{blue};width:215px"><h5>{e(c["grp"])}</h5><div class="pills" style="{col}">'
            + "".join(f"<span>{e(x)}</span>" for x in c["pills"]) + '</div></div></div></div></div>'
            f'</section><section class="slide">{chrome(t, c["section9"], 9)}'
            f'<div class="over">{e(c["over"])}</div><div class="title">{e(c["title"])}</div></section>')


def build_html(lang, first_page, calib=False):
    t = T[lang]
    pages = [overview_page(t, first_page)] + [package_page(t, p, i + 1, first_page + 1 + i) for i, p in enumerate(t["packages"])]
    if calib:
        pages = [calib_page(t, lang)] + pages
    return (f'<!doctype html><html lang="{"zh-CN" if lang == "zh" else lang}"><head><meta charset="utf-8"><title>{e(t["doc_title"])}</title>'
            f'<style>{CSS}{LANG_CSS.get(lang, "")}</style></head><body>{"".join(pages)}{FIT_JS}</body></html>')


def render(html_path, pdf_path, debug=False):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    f"--print-to-pdf={pdf_path}", uri(html_path) + ("#debug" if debug else "")], check=True, capture_output=True)


def _tounicode(font):
    import re
    m, data = {}, font["/ToUnicode"].get_data().decode("latin1")
    for blk in re.findall(r"beginbfchar(.*?)endbfchar", data, re.S):
        for a, b in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", blk):
            m[int(a, 16)] = bytes.fromhex(b).decode("utf-16-be", "replace")
    for blk in re.findall(r"beginbfrange(.*?)endbfrange", data, re.S):
        for a, b, c in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", blk):
            for k in range(int(a, 16), int(b, 16) + 1):
                m[k] = chr(int(c, 16) + k - int(a, 16))
    return m


def renumber_page(page, expected_old, new_no):
    """Rewrite the two-digit footer page number in a Chrome/Skia page content stream (Type3 font, one glyph per Tj)."""
    import re
    stream = page["/Contents"].get_object()
    data = stream.get_data()
    pat = re.compile(rb"BT\n/(F\d+) (\d+(?:\.\d+)?) Tf\n1 0 0 -1 ([\d.]+) ([\d.]+) Tm\n<([0-9A-F]{2})> Tj\n([\d.]+) 0 Td <([0-9A-F]{2})> Tj\nET\nQ\nQ\nEMC\n$")
    m = pat.search(data)
    assert m, "page-number block not found"
    font = page["/Resources"]["/Font"]["/" + m.group(1).decode()].get_object()
    size = float(m.group(2))
    to_uni = _tounicode(font)
    code_of = {v: k for k, v in to_uni.items()}
    old = to_uni[int(m.group(5), 16)] + to_uni[int(m.group(7), 16)]
    assert old == "%02d" % expected_old, (old, expected_old)
    scale = float(font["/FontMatrix"][0]) * size
    first = int(font["/FirstChar"])
    width = lambda ch: float(font["/Widths"][code_of[ch] - first]) * scale
    right = float(m.group(3)) + width(old[0]) + width(old[1])
    new = "%02d" % new_no
    x = right - width(new[0]) - width(new[1])
    block = (b"BT\n/%s %s Tf\n1 0 0 -1 %s %s Tm\n<%02X> Tj\n%s 0 Td <%02X> Tj\nET\nQ\nQ\nEMC\n" % (
        m.group(1), m.group(2), ("%.5f" % x).encode(), m.group(4), code_of[new[0]], ("%.7f" % width(new[0])).encode(), code_of[new[1]]))
    stream.set_data(data[:m.start()] + block)


def insert_into_profile(lang, src_pdf, pages_pdf, out_pdf, before_page=9):
    """Insert the package pages before `before_page` (1-based) and shift the printed numbers of the pages after them."""
    import pypdf
    from pypdf.generic import NameObject
    reader, add = pypdf.PdfReader(src_pdf), pypdf.PdfReader(pages_pdf)
    if len(reader.pages) != SOURCE_PAGES:
        raise SystemExit(f"{src_pdf} has {len(reader.pages)} pages, expected the original {SOURCE_PAGES}-page export")
    writer = pypdf.PdfWriter(clone_from=reader)
    n_new = len(add.pages)
    for i in range(before_page - 1, len(writer.pages)):
        renumber_page(writer.pages[i], i + 1, i + 1 + n_new)
    for k, page in enumerate(add.pages):
        new = writer.insert_page(page, before_page - 1 + k)
        for key in ("/StructParents", "/Tabs"):  # the inserted pages are not part of the source structure tree
            if key in new:
                del new[NameObject(key)]
    with open(out_pdf, "wb") as f:
        writer.write(f)
    return len(writer.pages)


# ---------------------------------------------------------------- One Pager, page 2 (A4 portrait)
OP = {
    "vi": dict(labels=["WEBSITE", "EMAIL", "NGƯỜI PHỤ TRÁCH", "ĐỊA CHỈ"], city="TP. Hồ Chí Minh", cta="Đặt lịch trao đổi",
               cta_note="Bước đầu tiên: một buổi trao đổi để chọn gói phù hợp."),
    "en": dict(labels=["WEBSITE", "EMAIL", "CONTACT PERSON", "ADDRESS"], city="Ho Chi Minh City", cta="Book a call",
               cta_note="First step: a conversation to find the right package."),
    "zh": dict(labels=["网站", "邮箱", "负责人", "地址"], city="胡志明市", cta="预约沟通",
               cta_note="第一步：通过一次沟通确定合适的套餐。"),
}
OP_CSS = f"""
@font-face{{font-family:'Plus Jakarta Sans';src:url('{uri(FONT_DIR / "PlusJakartaSans[wght].ttf")}');font-weight:200 800}}
@font-face{{font-family:'Inter';src:url('{uri(FONT_DIR / "Inter[opsz,wght].ttf")}');font-weight:100 900}}
@page{{size:A4 portrait;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:'Inter',Arial,sans-serif;color:{INK}}}
.page{{width:794px;height:1122.5px;position:relative;overflow:hidden;background:#F8FAFC}}
.page>*{{position:absolute}}
.top{{left:0;top:0;width:794px;height:150px;background:
  radial-gradient(520px 300px at 100% 0%,rgba(37,99,255,.55),transparent 70%),
  radial-gradient(420px 260px at 0% 100%,rgba(20,216,196,.22),transparent 70%),{MIDNIGHT}}}
.logo{{left:44px;top:29px;height:31px}}
.tag{{right:44px;top:36px;font:700 9px/12px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;margin-right:-.2em;
  text-transform:uppercase;color:rgba(255,255,255,.72);white-space:nowrap}}
.h{{left:44px;top:86px;font:800 26px/34px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.025em;color:#fff;white-space:nowrap}}
.h em{{font-style:normal;color:#14D8C4}}
.lead{{left:44px;top:170px;width:706px;font:400 12.5px/19px 'Inter',Arial,sans-serif;color:#1F2937}}
.fitbox{{left:44px;top:224px;width:706px;height:752px;overflow:hidden}}
.fit{{zoom:var(--zoom,1);display:flex;flex-direction:column;gap:12px}}
.pk{{background:#fff;border:1px solid #CBD6EA;border-top:4px solid #2563FF;border-radius:16px;padding:14px 18px 16px}}
.pk .hd{{display:flex;align-items:center;gap:12px}}
.pk .n{{font:800 32px/32px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.04em;color:#2563FF}}
.pk .t{{font:800 18px/22px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.02em;color:{MIDNIGHT}}}
.pk .who{{font:700 9.5px/13px 'Inter',Arial,sans-serif;color:#2563FF;margin-top:1px}}
.pk .meta{{margin-left:auto;display:grid;grid-template-columns:auto auto;gap:5px 10px;align-items:center}}
.lb{{font:800 8px/12px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#2563FF;white-space:nowrap}}
.pk .meta dd{{font:400 10px/13px 'Inter',Arial,sans-serif;color:{INK}}}
.flow{{display:flex;align-items:center}}
.flow b{{font:600 9.5px/18px 'Inter',Arial,sans-serif;color:#2563FF;background:rgba(37,99,255,.09);border-radius:6px;padding:0 6px}}
.flow i{{font:400 9px/18px 'Inter',Arial,sans-serif;font-style:normal;color:{SLATE};padding:0 3px}}
.pk .goal{{font:400 10.5px/15px 'Inter',Arial,sans-serif;color:{BODY};margin:9px 0 11px;padding-bottom:10px;border-bottom:1px solid #E6ECF7}}
.grp{{margin-bottom:9px}}
.grp:last-child{{margin-bottom:0}}
.grp h5{{font:700 10.5px/14px 'Plus Jakarta Sans',Arial,sans-serif;color:var(--c);display:flex;align-items:center;gap:4px;margin-bottom:6px}}
.grp h5::before{{content:'';width:4px;height:4px;border-radius:50%;background:var(--c);flex:none}}
.pills{{display:flex;flex-wrap:wrap;gap:4px}}
.pills span{{white-space:nowrap;font:500 9.6px/12.5px 'Inter',Arial,sans-serif;color:{INK};background:var(--bg);border:1px solid var(--line);
  border-radius:11px;padding:3.2px 8px}}
.pknote{{font:400 9px/12px 'Inter',Arial,sans-serif;color:{SLATE};margin-top:9px}}
.bot{{left:0;top:995px;width:794px;height:128px;background:
  radial-gradient(420px 240px at 100% 0%,rgba(37,99,255,.5),transparent 70%),{MIDNIGHT}}}
.ct{{left:44px;top:1019px;display:grid;grid-template-columns:118px auto;gap:0;align-items:baseline}}
.ct dt{{font:700 8px/20.6px 'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#14D8C4;white-space:nowrap}}
.ct dd{{font:400 10.5px/20.6px 'Inter',Arial,sans-serif;color:#fff;white-space:nowrap}}
.btn{{left:535px;top:1018px;height:40px;padding:0 22px;border-radius:20px;background:#2563FF;color:#fff;
  font:600 12px/40px 'Inter',Arial,sans-serif;white-space:nowrap}}
.btnnote{{left:535px;top:1066px;font:400 8.5px/11px 'Inter',Arial,sans-serif;color:rgba(255,255,255,.85);white-space:nowrap}}
.brandline{{left:535px;top:1085px;font:400 8.5px/11px 'Inter',Arial,sans-serif;color:rgba(217,226,242,.6);white-space:nowrap}}
"""
OP_LANG_CSS = {
    "zh": ".tag{font-size:11px;letter-spacing:.1em;margin-right:-.1em}.lb,.ct dt{font-size:9.5px;letter-spacing:.1em}.h{letter-spacing:0}"
          ".pk .t{letter-spacing:0}.pk .who{font-size:10.5px}.pills span{line-height:13.5px}",
}
LOGO_REV = uri(BK / "01_Logos" / "SVG" / "vibe-ai-labs_horizontal_reversed.svg")


def onepager_html(lang):
    t, o = T[lang], OP[lang]
    cards = []
    for p in t["packages"]:
        groups = "".join(group(t["pillars"][k], p["scope"][k], pvars(k)) for k in ("mkt", "ai", "cre"))
        note = f'<div class="pknote">{e(p["cardnote"])}</div>' if p["cardnote"] else ""
        cards.append(
            f'<div class="pk"><div class="hd"><div class="n">{p["num"]}</div><div><div class="t">{e(p["name"])}</div>'
            f'<div class="who">{e(p["who"])}</div></div>'
            f'<dl class="meta"><dt class="lb">{e(t["l_focus"])}</dt><dd>{flow(p["focus"])}</dd>'
            f'<dt class="lb">{e(t["l_mode"])}</dt><dd>{e(p["mode"])}</dd></dl></div>'
            f'<div class="goal">{e(p["goal"])}</div>{groups}{note}</div>')
    addr = f"WORC@Q2 Building, 21 Võ Trường Toản, An Khánh, {o['city']}"
    vals = ["vibe-ai-labs.vibeailabs.workers.dev", "vibeailabs@gmail.com", "Henry Le — Marketing Engineer", addr]
    contact = "".join(f"<dt>{e(a)}</dt><dd>{e(b)}</dd>" for a, b in zip(o["labels"], vals))
    return (f'<!doctype html><html lang="{"zh-CN" if lang == "zh" else lang}"><head><meta charset="utf-8">'
            f'<title>Vibe AI Labs</title><style>{OP_CSS}{OP_LANG_CSS.get(lang, "")}</style></head><body><section class="page">'
            f'<div class="top"></div><img class="logo" src="{LOGO_REV}" alt="Vibe AI Labs"><div class="tag">{e(t["section"])}</div>'
            f'<div class="h">{e(t["title"][0])} <em>{e(t["title"][1])}</em></div><div class="lead">{e(t["lead"])}</div>'
            f'<div class="fitbox" data-max="1.3"><div class="fit">{"".join(cards)}</div></div>'
            f'<div class="bot"></div><dl class="ct">{contact}</dl><div class="btn">{e(o["cta"])}</div>'
            f'<div class="btnnote">{e(o["cta_note"])}</div><div class="brandline">{e(t["footer"])}</div>'
            f'</section>{FIT_JS}</body></html>')


def build_onepager(lang, write=False):
    """Append the packages page as page 2 of the One Pager (source must be the original 1-page export)."""
    import pypdf
    from pypdf.generic import NameObject
    hp, pp = WORK / f"onepager_p2_{lang}.html", WORK / f"onepager_p2_{lang}.pdf"
    hp.write_text(onepager_html(lang), encoding="utf-8")
    render(hp, pp)
    add = pypdf.PdfReader(pp)
    assert len(add.pages) == 1, f"page 2 overflowed to {len(add.pages)} pages"
    src = PROFILE_DIR / f"Vibe_AI_Labs_One_Pager_{lang.upper()}.pdf"
    reader = pypdf.PdfReader(src)
    if len(reader.pages) != 1:
        raise SystemExit(f"{src} has {len(reader.pages)} pages, expected the original 1-page export")
    writer = pypdf.PdfWriter(clone_from=reader)
    new = writer.add_page(add.pages[0])
    for key in ("/StructParents", "/Tabs"):
        if key in new:
            del new[NameObject(key)]
    out = WORK / src.name
    with open(out, "wb") as f:
        writer.write(f)
    print(out, "pages:", len(writer.pages))
    if write:
        shutil.copyfile(out, src)
        print("written:", src)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="vi")
    ap.add_argument("--calib", action="store_true")
    ap.add_argument("--first-page", type=int, default=9)
    ap.add_argument("--write", action="store_true", help="overwrite the company profile PDF with the result")
    ap.add_argument("--onepager", action="store_true", help="build page 2 of the One Pager instead of the profile pages")
    a = ap.parse_args()
    WORK.mkdir(parents=True, exist_ok=True)
    if a.onepager:
        build_onepager(a.lang, a.write)
        raise SystemExit
    name = f"packages_{a.lang}" + ("_calib" if a.calib else "")
    hp, pp = WORK / f"{name}.html", WORK / f"{name}.pdf"
    hp.write_text(build_html(a.lang, a.first_page, a.calib), encoding="utf-8")
    render(hp, pp)
    import pypdf
    r = pypdf.PdfReader(pp)
    print(pp, "pages:", len(r.pages), "mediabox:", [float(x) for x in r.pages[0].mediabox])
    if not a.calib:
        src = PROFILE_DIR / f"Vibe_AI_Labs_Company_Profile_{a.lang.upper()}.pdf"
        out = WORK / src.name
        print(out, "pages:", insert_into_profile(a.lang, src, pp, out, a.first_page))
        if a.write:
            shutil.copyfile(out, src)
            print("written:", src)
