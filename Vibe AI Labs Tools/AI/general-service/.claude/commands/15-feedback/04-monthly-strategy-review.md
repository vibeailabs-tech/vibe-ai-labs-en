# Monthly Strategy Review (Feedback Layer) Skill

Your job is to close the feedback loop — run the full end-of-month review from the Feedback Agent's perspective. Unlike the Performance Agent's monthly review (which analyzes numbers), this skill synthesizes all updates from the Feedback Agent (audience, messaging, positioning) and writes a consolidated strategy brief for the next month. It is the last step before the cycle resets.

## Step 1 — Read ALL inputs

Read everything available:
- `/outputs/profiles-output/brand.md` — current state after this month's updates
- `/outputs/performance/monthly-review-[current month].md` — performance analysis
- `/outputs/performance/audience-update-[current month].md` — audience changes
- `/outputs/performance/messaging-refinement-[current month].md` — messaging changes
- `/outputs/performance/positioning-evolution-[current month].md` — positioning changes
- `/outputs/strategy/campaign-brief-*.md` — last month's strategy
- `/outputs/research/` — any recent research

This skill requires all other feedback skills to have run first. If audience-update, messaging-refinement, or positioning-evolution files don't exist for this month, run those first.

## Step 2 — Synthesize and write next month's strategy

### The synthesis question

After all updates: what is the one most important thing the brand should do differently next month?

This is not a list of everything that changed. It is a strategic decision about priority — given everything learned this month, where should next month's energy go?

### Strategy brief structure

**1. This month in one paragraph:**
What happened, what was learned, what changed. Anyone reading this brief should be caught up in 60 seconds.

**2. Brand foundation updates summary:**
What changed in brand.md this month? Audience, messaging, positioning. List changes clearly so the execution agents know to work from the updated version.

**3. Strategic priority for next month:**
One primary strategic thrust — not a list of tactics.
- If conversion is the problem: priority is CRO + bottom-funnel content
- If reach is the problem: priority is distribution + paid acquisition
- If credibility is the problem: priority is case studies + thought leadership
- If retention is the problem: priority is email sequences + community

**4. Channel focus:**
Based on ROI data — which 2–3 channels to invest in next month, which to hold steady, which to reduce.

**5. Content calendar direction:**
What content themes to emphasize next month. Based on what worked, what audience questions came up, what's seasonal.

**6. Experiments to run:**
1–2 specific tests to run next month. Each with a clear hypothesis and success metric.

**7. What NOT to do next month:**
Explicitly state what to stop, pause, or deprioritize. This is as important as the priority list.

### Vietnamese business cycle context

**Monthly rhythm:**
- First week of month: execute on last month's plan
- Week 2–3: production and distribution
- Week 4: data collection, analysis
- Last 3 days of month: run this review, write next month's brief

**Quarterly considerations:**
- Q1 (Jan–Mar): Post-Tết recovery; March is the ramp-up month
- Q2 (Apr–Jun): Best B2B quarter; push campaigns hard here
- Q3 (Jul–Sep): Summer slowdown for B2B; good for relationship-building content
- Q4 (Oct–Dec): Year-end budget push; good time for ROI-focused campaigns

## Step 3 — Write output

Save to `/outputs/strategy/campaign-brief-[YYYY-MM].md` (overwrites as next month's brief):

```markdown
# Campaign Brief — [Month YYYY]
> Generated: [date] | Based on: [previous month] learnings

## Month in Review (60-second catch-up)
[One paragraph: what happened, what was learned, what changed]

---

## Brand Foundation — Current State
*All execution agents should read brand.md before running any skill this month.*

**Audience (Section 6):** [Key update — or "no changes this month"]
**Messaging (Section 11):** [Key update]
**Positioning (Section 7):** [Key update]
**Offer (Section 9):** [Key update or "unchanged"]

---

## Strategic Priority for [Month YYYY]
**Primary thrust:** [One sentence — the main strategic direction]
**Why:** [Data that supports this priority]

---

## Channel Focus

| Channel | Investment | Direction | Reason |
|---|---|---|---|
| Facebook Ads | [budget] | Increase/Hold/Reduce | [Why] |
| Google Ads | [budget] | | |
| Email | [effort] | | |
| Organic Content | [effort] | | |
| Cold Outreach | [effort] | | |

---

## Content Themes for [Month]

**Must cover (based on what worked):**
1. [Theme] — [why: performance data]
2. [Theme]

**Must cover (based on audience questions):**
1. [Theme] — [why: common objection or question]

**Seasonal/topical:**
1. [Theme] — [why: Vietnamese calendar or market timing]

---

## Experiments to Run

### Experiment 1
**Hypothesis:** If we [change X], then [metric Y] will improve because [reason]
**Test:** [Specific A/B test or campaign]
**Success metric:** [Specific number]
**Duration:** [weeks]

### Experiment 2
[Same structure]

---

## What NOT to Do This Month
- **Stop:** [Specific activity to kill] — [Why: cost vs. result data]
- **Pause:** [Specific activity to hold] — [Why]
- **Don't start:** [Tempting thing to avoid right now] — [Why not yet]

---

## Quick Wins (do these in week 1)
1. [Specific action that will produce results fast]
2. [Second quick win]

---

## Monthly Goals

| KPI | Target | How we'll hit it |
|---|---|---|
| Revenue | [VND] | [Strategy] |
| Leads | [n] | |
| Demos booked | [n] | |
| CAC | [VND max] | |
| [Key channel metric] | | |

---

## Notes
[Seasonal factors, upcoming Vietnamese holidays, external market context]
```

## Step 4 — Confirm

After writing, reply:

---
"✅ **Monthly strategy review hoàn chỉnh. Hệ thống đã reset cho tháng [Next Month].**

**Tháng vừa rồi:** [One-sentence verdict]
**Thay đổi brand.md:** [What updated]
**Priority tháng [Next Month]:** [Strategic thrust]
**Mục tiêu chính:** [Key KPI target]

📁 Brief mới lưu tại: `/outputs/strategy/campaign-brief-[YYYY-MM].md`
📁 brand.md đã được cập nhật với tất cả feedback từ tháng này

**Hệ thống sẵn sàng cho tháng mới:**
→ Execution agents sẽ đọc brand.md mới nhất
→ Strategy agents sẽ đọc campaign-brief mới nhất
→ Vòng lặp tiếp tục"

---
