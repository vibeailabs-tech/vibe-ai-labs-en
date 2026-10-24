# Monthly Strategy Review Skill

Your job is to run the end-of-month review — synthesize all performance data, compare against strategy goals, identify what the data is telling you about the audience and market, and update strategic direction for next month. This is the bridge between Layer 3 (execution) and Layer 4 (feedback). It ends with concrete updates to the plan.

## Step 1 — Read inputs

Read ALL available outputs:
- `/outputs/profiles-output/brand.md` — current brand foundation
- `/outputs/strategy/campaign-brief-*.md` — original goals for this month (if exists)
- `/outputs/strategy/content-calendar-*.md` — what was planned (if exists)
- `/outputs/performance/weekly-report-*.md` — all weekly reports for this month
- `/outputs/performance/campaign-report-*.md` — any campaign reports
- `/outputs/performance/roi-calculator-*.md` — ROI data if available
- `/outputs/research/` — any research done this month

Synthesize all of it before writing the review.

## Step 2 — Collect any missing data

If critical data is missing (no weekly reports exist, no spend data):
Ask: "Để viết monthly review, mình cần data của tháng [X]:
1. Tổng doanh thu tháng này?
2. Tổng chi phí marketing (ads + tools + agency)?
3. Leads mới / Deals chốt?
4. Channel nào perform tốt nhất — có data gì không?"

Wait for answer before continuing.

## Step 3 — Write the monthly strategy review

### Review structure

**1. Monthly scorecard — did we hit goals?**
Compare actual results vs. stated goals from campaign-brief.md (or user's stated goals). Not just "did we grow" — did we hit the specific targets we set?

**2. What the data is telling us**
This is the analytical layer. What patterns emerged? What did we learn about:
- Audience behavior (when they engage, what they respond to)
- Messaging (which angles resonated, which flopped)
- Channel efficiency (where money worked hardest)
- Offer performance (what conversion rates tell you about the offer)

**3. Strategy gaps — where the plan didn't match reality**
Honest assessment: was the strategy wrong, or was execution off? This matters because the fix is different.
- Strategy wrong → update positioning, offer, or channel mix
- Execution off → improve process, creative quality, or consistency

**4. Next month's priorities**
Not a wish list. Ranked by expected impact. Maximum 3 priorities.

**5. Updates to push upstream**
This review should trigger updates to:
- `brand.md` — if audience understanding has sharpened
- `strategy/campaign-brief.md` — next month's plan
- Content calendar — based on what content performed

### Vietnamese market seasonal context (apply automatically)

**April:** Post-Tết ramp-up complete; April–June is peak B2B buying season
**May:** Labor Day holiday (May 1st) — 3-day weekend affects B2B engagement; B2C opportunity
**June:** Mid-year review season for enterprises — decision budgets open
**July–August:** Summer slowdown for B2B; B2C peak for travel/lifestyle
**September:** Back-to-business — strong month for B2B re-engagement
**October–November:** Year-end planning begins; Q4 budget pushes
**December:** Slower business decisions; relationship-building season
**January–February:** Tết preparation and slowdown; post-Tết surge follows

## Step 4 — Write output

Save to `/outputs/performance/monthly-review-[YYYY-MM].md`:

```markdown
# Monthly Strategy Review — [Month YYYY]
> Generated: [date] | Period: [01/MM/YYYY – 31/MM/YYYY]

## Monthly Verdict
**Goal:** [What was the stated goal for this month]
**Result:** [What actually happened]
**Status:** ✅ Hit / ⚠️ Partial / ❌ Missed

---

## Scorecard

| Goal | Target | Actual | Status |
|---|---|---|---|
| Revenue | [VND] | [VND] | ✅/⚠️/❌ |
| Leads | [n] | [n] | |
| Deals closed | [n] | [n] | |
| Ad ROAS | [X]× | [X]× | |
| Email open rate | [%] | [%] | |
| [Custom KPI] | | | |

---

## What the Data Is Telling Us

### About our audience
[2–3 specific observations from the data — not generic, based on actual numbers]

### About our messaging
[Which angles, headlines, or CTAs worked vs. didn't — with data]

### About our channels
[Which channels drove the best ROI — specific metrics]

### About our offer
[What conversion rates and objections tell you about offer-market fit]

---

## Performance by Channel

| Channel | Spend | Revenue | ROAS | Leads | CPA | Verdict |
|---|---|---|---|---|---|---|
| Facebook Ads | | | | | | |
| Google Ads | | | | | | |
| Email | | | | | | |
| Organic Content | | | | | | |
| Cold Outreach | | | | | | |

---

## Content Performance

**Top 3 content pieces this month:**
1. [Title / Platform] — [Key metric: views/engagement/conversions]
2. 
3. 

**What made them work:** [Pattern across top performers]

**Bottom performers:** [What underperformed and likely reason]

---

## Strategy Gaps

### Gap 1: [Description]
**Type:** Strategy issue / Execution issue
**Evidence:** [Data that proves this gap]
**Fix:** [Specific change for next month]

### Gap 2: [Description]
[Same structure]

---

## Next Month Priorities

**Priority 1 (highest impact):** [Specific action]
- Why: [Data-backed reason]
- Owner: [Role]
- Success metric: [Measurable KPI]

**Priority 2:** [Specific action]
- Why:
- Owner:
- Success metric:

**Priority 3:** [Specific action]
- Why:
- Owner:
- Success metric:

---

## Upstream Updates Required

### brand.md updates
- [ ] [Section] — [What to update] — [Why the data supports this change]

### Strategy updates
- [ ] Next month's campaign goal: [updated goal]
- [ ] Channel budget reallocation: [what to shift and where]
- [ ] Offer adjustment: [if conversion data suggests changes]

### Content calendar updates
- [ ] Double down on: [content type/angle that worked]
- [ ] Drop: [content type/angle that didn't]
- [ ] Add: [new angle based on this month's learnings]

---

## Notes
[Seasonal factors, platform changes, external events that affected this month's results]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Monthly strategy review cho tháng [Month] đã hoàn chỉnh.**

**Verdict:** [Hit / Partial / Missed] — [one sentence]
**Key learning:** [Most important insight from the data]
**Top priority next month:** [Specific action]

📁 Đã lưu vào: `/outputs/performance/monthly-review-[YYYY-MM].md`

**Bước tiếp theo:** Chạy `/audience-update` và `/positioning-evolution` để cập nhật brand.md dựa trên findings này — đây là feedback loop của hệ thống."

---
