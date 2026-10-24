# Agent 14 — Performance Agent: Deep Dive

## What this agent does

The Performance Agent reads results, explains them, and decides what to do next. Every other agent in this system creates — the Performance Agent measures and interprets. Without it, the system runs on assumptions. With it, every decision is grounded in data.

This is also the system's **memory layer** — by writing monthly reviews, it creates a record of what worked and what didn't that feeds back into brand.md and strategy files through Agent 15 (Feedback).

---

## Why this agent exists

Vietnamese SMBs typically have two failure modes: (1) they run campaigns without measuring anything, or (2) they drown in raw data without knowing what it means. This agent solves both. It collects what data is available, benchmarks it against Vietnamese market standards, and produces one clear action per report.

---

## Skills (5)

### Skill 1 — Campaign Report (`/campaign-report`)

**What it does:** Deep-dive analysis of a specific campaign — what happened at each funnel stage, what drove performance, what to change next time.

**Input:** Campaign metrics (spend, impressions, clicks, leads, conversions, revenue) + platform

**Output:** `/outputs/performance/campaign-report-[slug].md`

**Funnel analysis covers:**
- Awareness: Impressions, Reach, CPM
- Engagement: CTR, CPC, Engagement rate
- Conversion: CVR, CPA, CPL
- Revenue: ROAS, CAC, Revenue generated

**Diagnosis framework:** Maps weak metrics to root causes:
- High impressions, low CTR → Creative or audience mismatch
- High CTR, low CVR → Landing page or offer mismatch
- High CVR, high CPA → Audience too small or bid too high

**Output includes:** Metrics snapshot with benchmark comparison, funnel analysis, what worked/didn't, creative performance table, 4-point recommendations (Keep / Fix / Test / Kill).

---

### Skill 2 — Weekly Report (`/weekly-report`)

**What it does:** A 5-minute weekly summary across all active channels — website, social, email, ads, sales pipeline.

**Input:** Weekly metrics from any available source (GA4, Meta, email platform, CRM, or user-pasted data)

**Output:** `/outputs/performance/weekly-report-[YYYY-WXX].md`

**Channels covered:** Website (sessions, conversions), Social (reach, engagement, followers), Email (open/click rates, list growth), Paid ads (spend, leads, CPA), Sales pipeline (leads, demos, closes)

**Format philosophy:** Narrative first, then numbers. The report tells the story of the week before listing metrics — what moved, why, and what it means. Ends with exactly one #1 priority for next week.

**Vietnamese specifics:**
- Notes holiday effects on performance (Tết, national holidays)
- Separate Zalo metrics from email (very different benchmarks)
- GMT+7 time context for any timing observations

---

### Skill 3 — ROI Calculator (`/roi-calculator`)

**What it does:** Calculates true return on investment — not just ROAS, but the full picture: ROI %, CAC, LTV:CAC ratio, payback period, and channel-by-channel breakdown.

**Input:** Revenue, total marketing cost breakdown, leads, closes, average deal size, LTV estimate

**Output:** `/outputs/performance/roi-calculator-[slug].md`

**Core calculations:**
- Marketing ROI = (Revenue - Cost) / Cost × 100
- ROAS = Revenue / Ad Spend
- CAC = Total Marketing Cost / New Customers
- LTV:CAC ratio = Customer Lifetime Value / CAC
- Payback period = CAC / Monthly Revenue per Customer

**LTV:CAC benchmarks:**
- <1:1 = losing money on every customer
- 1:1 to 3:1 = marginal
- 3:1 = healthy
- 5:1+ = strong (may be under-investing)

**Output includes:** Investment summary table, revenue attribution, core metrics vs. benchmarks, funnel conversion rates, channel ROI comparison, LTV analysis, 50% budget scale projection, and specific recommendations.

---

### Skill 4 — Data Visualization (`/data-visualization`)

**What it does:** Specs every chart precisely — type, data, axis labels, colors, annotations, build instructions — so a human or designer can build it without guessing.

**Input:** Any dataset + target visualization tool (Google Sheets, Canva, PowerPoint, Figma)

**Output:** `/outputs/performance/data-viz-[slug].md`

**Chart selection rules:**
- Line chart → trend over time
- Bar chart → comparison across categories
- Funnel → drop-off through stages
- Donut → composition (max 5 segments)
- Scatter → correlation

**Per-chart spec includes:** Chart type, exact title, insight it communicates (one sentence), data table, axis labels with units, color specs (hex), annotations with text, tool-specific build instructions, export dimensions.

**Vietnamese specifics:**
- Currency in VND ("triệu đồng" / "tỷ đồng" for large numbers)
- Date format: DD/MM/YYYY
- Platform names in English (Facebook, TikTok — brand names)
- Week labels in Vietnamese ("Tuần 1", not "Week 1")

---

### Skill 5 — Monthly Strategy Review (`/monthly-strategy-review`)

**What it does:** The most important skill. Synthesizes all weekly reports, campaign reports, and ROI data from the month, compares against strategy goals, identifies what the data reveals about audience/messaging/channels/offer, and writes concrete updates for next month.

**Input:** All `/outputs/performance/` files + `/outputs/strategy/campaign-brief.md` + user-provided data

**Output:** `/outputs/performance/monthly-review-[YYYY-MM].md`

**Review structure:**
1. Monthly verdict (Hit / Partial / Missed)
2. Scorecard: goal vs. actual for all KPIs
3. What the data is telling us (4 dimensions: audience, messaging, channels, offer)
4. Performance by channel (table)
5. Content performance (top 3 + pattern analysis)
6. Strategy gaps (what didn't match reality — type: strategy issue vs. execution issue)
7. Next month's 3 priorities (each with owner + success metric)
8. Upstream updates required (brand.md changes, strategy changes, content calendar changes)

**Key feature — upstream updates checklist:** Each monthly review generates a concrete list of what needs to change in brand.md, strategy files, and content calendar. This is the mechanism that makes the system improve over time.

**Vietnamese seasonal calendar built-in:**
- The skill knows Vietnamese business seasonality (Tết slowdown, April–June B2B peak, Q4 planning season) and applies it automatically to contextualize results.

---

## Workflow position

```
Agent 13 (Distribution) → [YOU] → Agent 15 (Feedback)
```

The Performance Agent runs after content has shipped and data has had time to accumulate. It reads from all execution agents' outputs. It passes structured insights to the Feedback Agent, which makes the actual updates to brand.md and strategy files.

---

## API integrations (future)

The agent currently works from user-provided data or pasted metrics. When APIs are connected, it will pull live data directly:

| API | What it provides |
|---|---|
| GA4 | Website sessions, conversions, traffic sources |
| Meta Insights | Facebook/Instagram reach, engagement, ad performance |
| Meta Ads API | Campaign spend, creative performance, audience data |
| Google Ads API | Search campaign CTR, CPC, Quality Score |
| Mailchimp/Klaviyo | Email open rates, click rates, revenue attribution |

Until APIs are connected, the agent prompts for data paste at the start of each skill run.

---

## What makes this agent different from a spreadsheet

A spreadsheet shows numbers. This agent:
1. Compares against Vietnamese market benchmarks (not global averages)
2. Diagnoses root causes of weak metrics
3. Accounts for seasonal effects (Tết, holidays)
4. Writes narrative analysis — the "why" behind the numbers
5. Produces one clear recommendation per report
6. Generates an upstream update checklist that keeps the system improving
