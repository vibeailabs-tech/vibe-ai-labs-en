# Campaign Report Skill

Your job is to write a clear, decision-ready campaign performance report. Not a data dump — an analysis that tells the business owner what worked, what didn't, and exactly what to do next.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — context for conversion metrics
- Target audience (Section 6) — context for audience performance data
- Key messages (Section 11) — to evaluate message resonance

Read campaign data from:
- `/outputs/performance/` — any previously saved data
- User-provided data (pasted metrics, CSV, or screenshot descriptions)

If no data provided: ask user to paste metrics before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided campaign data**
Use their input. Go to Step 3.

**Path B — No data provided**
Ask:
"Để viết campaign report, mình cần data sau:
1. **Campaign:** Tên campaign và thời gian chạy?
2. **Spend:** Tổng chi phí quảng cáo?
3. **Results:** Impressions / Reach / Clicks / Conversions / Revenue?
4. **Platform:** Facebook / Google / TikTok / Email / tất cả?
5. **Goal:** KPI chính của campaign này là gì? (leads / sales / traffic / brand awareness)"

Wait for answer before continuing.

## Step 3 — Analyze the campaign

### Core metrics framework

**Funnel analysis — calculate each stage:**
- **Awareness:** Impressions, Reach, CPM (Cost per 1,000 impressions)
- **Engagement:** CTR (Click-through rate), CPC (Cost per click), Engagement rate
- **Conversion:** CVR (Conversion rate), CPA (Cost per acquisition), CPL (Cost per lead)
- **Revenue:** ROAS (Return on ad spend), CAC (Customer acquisition cost), Revenue generated

**Benchmark against Vietnamese market standards:**
- Facebook CTR: 0.9–1.5% (good), <0.5% (needs new creative)
- Google Search CTR: 3–6% (good), <1% (poor keyword match or headlines)
- Email open rate: 20–30% (good), <15% (subject line or list quality issue)
- Landing page CVR: 2–5% (good), <1% (page or offer issue)
- Facebook CPA (lead gen): 50,000–200,000 VND for B2B, 20,000–80,000 VND for B2C
- ROAS: 3× minimum for sustainable paid, 5×+ = strong

**What to diagnose if metrics are off:**
- High impressions, low CTR → Creative or audience mismatch
- High CTR, low CVR → Landing page or offer mismatch
- High CVR, high CPA → Audience too small or bid too high
- Low open rate → Subject line or sending time issue
- Low click rate in email → CTA or offer in body

### Vietnamese market context
- Zalo performance: open rates 40–60% (much higher than email) — if Zalo available, compare
- Weekend ad performance: Saturday 7–9pm and Sunday morning are peak in Vietnam
- Mobile-first: if mobile CTR << desktop CTR, mobile creative is broken
- Vietnamese language ads vs. English: typically 20–40% better CTR for Vietnamese-language copy

## Step 4 — Write output

Save to `/outputs/performance/campaign-report-[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Campaign Report — [Campaign Name]
> Generated: [date] | Period: [start–end] | Platform: [platforms] | Total spend: [amount]

## Executive Summary
**Result in one sentence:** [Did this campaign hit its goal? Why or why not?]

**Top 3 findings:**
1. [Most important insight]
2. [Second insight]
3. [Third insight]

**Recommended action:** [One thing to do differently next campaign]

---

## Metrics Snapshot

| Metric | Result | Benchmark | Status |
|---|---|---|---|
| Impressions | | | |
| Reach | | | |
| CTR | | 0.9–1.5% (FB) | ✅ / ⚠️ / ❌ |
| CPC | | | |
| CVR | | 2–5% | ✅ / ⚠️ / ❌ |
| CPA / CPL | | | |
| ROAS | | 3× minimum | ✅ / ⚠️ / ❌ |
| Revenue | | | |

---

## Funnel Analysis

### Awareness stage
[What happened at impressions/reach level — good or broken?]

### Engagement stage
[CTR and CPC analysis — creative and audience performance]

### Conversion stage
[CVR and CPA — landing page + offer performance]

### Revenue stage
[ROAS and total return]

---

## What Worked
- [Specific element that outperformed]
- [Creative angle, audience, or placement that drove results]

## What Didn't Work
- [Element that underperformed — with likely root cause]
- [What to test or fix]

---

## Creative Performance (if A/B data available)
| Ad | CTR | CVR | CPA | Winner? |
|---|---|---|---|---|
| [Ad A] | | | | |
| [Ad B] | | | | |

---

## Audience Performance (if available)
| Segment | Impressions | CTR | CVR | CPA |
|---|---|---|---|---|
| | | | | |

---

## Budget Efficiency
- **Spend by platform:** [breakdown]
- **Best performing allocation:** [where money worked hardest]
- **Recommended next budget split:** [suggestion]

---

## Recommendations for Next Campaign
1. **Keep:** [what to keep exactly the same]
2. **Fix:** [what to change and how]
3. **Test:** [new hypothesis to test — one thing only]
4. **Kill:** [what to stop spending on]

---

## Next Campaign Forecast
Based on this data, if we [change X], we expect [metric Y] to improve by approximately [range].
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Campaign report cho '[Campaign]' đã hoàn chỉnh.**

**Result:** [One-sentence verdict]
**Top finding:** [Most actionable insight]
**Next action:** [Specific recommendation]

📁 Đã lưu vào: `/outputs/performance/campaign-report-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/weekly-report` để tổng hợp kết quả tuần này, hoặc `/feedback` để cập nhật strategy dựa trên performance data."

---
