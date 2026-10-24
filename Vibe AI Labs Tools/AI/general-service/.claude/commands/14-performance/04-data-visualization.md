# Data Visualization Skill

Your job is to turn raw marketing data into clear visual descriptions and chart specifications that a human or designer can build in Google Sheets, Canva, or any visualization tool. You don't render charts — you spec them with precision so whoever builds them gets it right on the first try.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — chart titles and labels should match brand tone
- Core offer (Section 9) — context for which metrics matter most

Read any available data from `/outputs/performance/`.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided data to visualize**
Use their input. Go to Step 3.

**Path B — No data provided**
Ask:
"Để tạo data visualization, mình cần:
1. **Data:** Paste data bạn muốn visualize (metrics, table, CSV)
2. **Purpose:** Bạn muốn chart này nói lên điều gì? (trend / comparison / funnel / breakdown)
3. **Audience:** Chart này dùng để: báo cáo nội bộ / pitch khách hàng / social post / presentation?
4. **Tool:** Bạn sẽ build chart trong tool nào? (Google Sheets / Canva / Figma / PowerPoint)"

Wait for answer before continuing.

## Step 3 — Design the visualizations

### Chart selection rules

**Use a line chart when:** showing a trend over time (weekly leads, monthly revenue, follower growth)

**Use a bar chart when:** comparing values across categories (channel performance, campaign comparison, ad creative A/B)

**Use a funnel chart when:** showing drop-off through stages (impression → click → lead → close)

**Use a pie/donut when:** showing composition where parts add to 100% (traffic sources, budget allocation) — never use for more than 5 segments

**Use a scatter plot when:** showing correlation (spend vs. revenue, post frequency vs. engagement rate)

**Use a table when:** data has multiple dimensions that charts can't capture cleanly

### Visualization principles

**One chart = one insight:** Every chart must have one clear conclusion. If you need to say three things, make three charts.

**Label everything:** Axes, data points, percentages, time periods. Never make the viewer guess.

**Hierarchy:** Title (what this is) → Subtitle (what period/context) → Chart → Source/notes

**Vietnamese charts:**
- Use VND for currency (not $) — format as "triệu đồng" or "tỷ đồng" for large numbers
- Dates: DD/MM/YYYY format
- Week labels: "Tuần 1", "Tuần 2" not "Week 1"
- Platform names: giữ nguyên English (Facebook, TikTok, Google) — these are brand names

### Chart types to produce

For each dataset, spec:
1. **Primary chart:** Main visualization — the one that tells the story
2. **Supporting chart (optional):** Adds context or drill-down
3. **KPI summary card:** Single-number callouts for dashboards (e.g., "ROAS: 4.2×")

## Step 4 — Write output

Save to `/outputs/performance/data-viz-[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Data Visualization Spec — [Topic/Campaign]
> Generated: [date] | Data period: [range] | Target tool: [tool]

---

## Chart 1 — [Title]

**Type:** [Line / Bar / Funnel / Donut / Scatter / Table]
**Title:** [Exact chart title]
**Subtitle:** [Date range and context]
**Insight it communicates:** [One sentence — what conclusion the viewer should draw]

**Data:**
| [Column A] | [Column B] | [Column C] |
|---|---|---|
| [data] | [data] | [data] |

**Axis labels:**
- X-axis: [label]
- Y-axis: [label] (unit: [VND / % / count])

**Colors:**
- Primary series: [hex or description]
- Secondary series: [hex]
- Highlight (peak or key data point): [hex]

**Annotations:**
- Mark: [specific data point to call out] — label: "[annotation text]"

**Build instructions (for [tool]):**
[Step-by-step for the specific tool if provided]

---

## Chart 2 — [Title]

[Same structure as above]

---

## KPI Summary Cards

### Card 1
**Metric:** [Metric name]
**Value:** [Value with unit]
**Context:** [vs. last period or benchmark]
**Color:** [Green = good / Yellow = warning / Red = bad]

### Card 2
[Same structure]

### Card 3
[Same structure]

---

## Dashboard Layout Recommendation

If building a performance dashboard:
```
[Row 1] KPI Cards: [Metric 1] | [Metric 2] | [Metric 3] | [Metric 4]
[Row 2] [Primary trend chart — full width]
[Row 3] [Channel comparison — left half] | [Funnel — right half]
[Row 4] [Table: top performing assets]
```

---

## Export Specifications
- For presentations: export as PNG at 1920×1080 (16:9) or 1080×1080 (square)
- For reports: export as PDF
- For social: 1080×1350 (portrait) for Instagram/Facebook
- Chart background: white (#FFFFFF) for print, dark (#1A1A2E) for social

---

## Narrative Summary
[3–5 sentences: what the data shows, what's driving the numbers, what decision this data supports]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Data visualization spec cho '[Topic]' đã hoàn chỉnh.**

**Charts specified:** [n] charts + [n] KPI cards
**Key insight:** [One-sentence finding from the data]
**Build in:** [recommended tool]

📁 Đã lưu vào: `/outputs/performance/data-viz-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Build charts trong [tool], hoặc chạy `/monthly-strategy-review` để present data này trong monthly review."

---
