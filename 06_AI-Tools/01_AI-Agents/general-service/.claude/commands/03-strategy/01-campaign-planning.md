---
name: campaign-planning
description: Builds a full 90-day marketing campaign plan for a Vietnamese business. Use this skill when the user wants to plan a campaign, map out a marketing timeline, or structure their marketing activities. Trigger whenever the user mentions campaign planning, 90-day plan, marketing roadmap, or wants to know what to do next in their marketing.
---

# Campaign Planning Skill

Your job is to build a focused, actionable 90-day marketing campaign — not a vague strategy document. Every week should have a clear goal, content theme, and measurable output.

## Step 1 — Read inputs

Read the following files:
- `/outputs/profiles-output/brand.md` — brand positioning, ICP, USP, core offer
- `/outputs/research/market-research-*.md` — market size, opportunities, threats (if exists)
- `/outputs/research/competitor-analysis-*.md` — competitor gaps to exploit (if exists)
- `/outputs/research/keyword-research-*.md` — keyword priorities (if exists)
- `/outputs/research/trend-monitoring-*.md` — trends to ride (if exists)

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.
If research files don't exist: proceed with brand.md data only, note the gap.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified campaign goal or focus**
Use their goal. Go to Step 3.

**Path B — No goal provided**
Ask:
"Chiến dịch 90 ngày này hướng đến mục tiêu nào?
1. Tăng nhận diện thương hiệu (brand awareness)
2. Tạo leads và khách hàng mới (lead generation)
3. Ra mắt sản phẩm/dịch vụ mới (product launch)
4. Tái kích hoạt khách hàng cũ (re-engagement)
5. Kết hợp (mixed — brand + leads)"

Wait for answer before continuing.

## Step 3 — Build the 90-day campaign structure

### Campaign Architecture

**Month 1 — Awareness & Trust (Weeks 1–4)**
Goal: Get the right people to know this brand exists and trust it enough to engage.
- Lead with educational content that addresses top pain points
- Build SEO foundation with Tier 3 keywords
- Establish social presence rhythm (consistency > volume)
- No hard selling in Month 1 — build credibility first

**Month 2 — Consideration & Engagement (Weeks 5–8)**
Goal: Move warm audience from "interesting" to "I want this."
- Introduce comparison content (us vs alternatives)
- Publish proof: case studies, testimonials, before/after
- Capture leads with a lead magnet offer
- Start retargeting anyone who engaged in Month 1

**Month 3 — Conversion & Retention (Weeks 9–12)**
Goal: Turn interested prospects into paying customers.
- Direct offer content: pricing, packages, CTA-forward
- Run a limited-time incentive (bonus, discount, free consultation)
- Email sequence for leads captured in Month 2
- Referral or review ask for new customers

### For each month, define:
- **Theme:** The single narrative thread for the month
- **Primary platform:** Where most energy goes (Facebook / TikTok / Zalo / Blog / LinkedIn)
- **Content mix:** Ratio of educational : proof : promotional content
- **Key milestones:** What must be live by end of month
- **Success metric:** The one number that proves this month worked

### Weekly breakdown (for Month 1 as example):
- Week 1: [specific theme] → [content type] → [platform] → [CTA]
- Week 2: [specific theme] → [content type] → [platform] → [CTA]
- Week 3: [specific theme] → [content type] → [platform] → [CTA]
- Week 4: [specific theme] → [content type] → [platform] → [CTA]

Use brand.md content pillars to assign weekly themes. Use keyword-research.md to assign SEO targets per week. Use trend-monitoring.md to inject timely angles.

### Budget allocation framework (if user has a budget):
- 40% — content production (writing, design, video)
- 35% — paid distribution (Facebook/TikTok ads, boosted posts)
- 15% — tools and automation
- 10% — testing and experimentation

## Step 4 — Define campaign KPIs

Set measurable targets for the 90-day period. Base on industry benchmarks for Vietnam:

| Metric | Conservative | Realistic | Aggressive |
|---|---|---|---|
| Organic reach/month | — | — | — |
| Leads generated | — | — | — |
| Email subscribers | — | — | — |
| Conversion rate | — | — | — |
| Revenue target | — | — | — |

Fill in numbers based on the brand's current stage, audience size, and market data from research files.

## Step 5 — Write output

Save to `/outputs/strategy/campaign-plan-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# 90-Day Campaign Plan — [Brand Name]
> Generated: [date] | Goal: [campaign goal] | Market: Vietnam

## Campaign Overview
- Goal: 
- Primary audience: 
- Core message for this campaign:
- Platforms: 
- Budget range (if provided):

---

## Month 1 — [Theme Name] (Weeks 1–4)
**Goal:** 
**Content ratio:** X% educational / X% proof / X% promotional
**Primary platform:**
**Key milestone:**
**Success metric:**

### Week-by-Week
| Week | Theme | Content Type | Platform | CTA |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

---

## Month 2 — [Theme Name] (Weeks 5–8)
[same structure]

---

## Month 3 — [Theme Name] (Weeks 9–12)
[same structure]

---

## 90-Day KPI Targets
| Metric | Target |
|---|---|
| | |

---

## Quick Wins (Do in Week 1)
[3–5 actions to take immediately that cost nothing but time]

---

## Risks & Contingencies
[What could go wrong and what to do about it]
```

## Step 6 — Confirm

After writing, reply:

---
"✅ **Kế hoạch chiến dịch 90 ngày cho [Brand Name] đã hoàn chỉnh.**

**Tóm tắt:**
- Tháng 1: [theme] — [primary action]
- Tháng 2: [theme] — [primary action]
- Tháng 3: [theme] — [primary action]
- Quick win đầu tiên: [top action for week 1]

📁 Đã lưu vào: `/outputs/strategy/campaign-plan-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/content-calendar` để lập lịch nội dung chi tiết từng tuần."

---
