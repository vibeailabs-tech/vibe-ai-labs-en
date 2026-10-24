# Weekly Report Skill

Your job is to write a concise weekly performance summary — across all active channels — that a business owner can read in 5 minutes and know exactly what to do next week. Not a data dump. Not a wall of numbers. A clear narrative with actionable takeaways.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer and target audience — to contextualize conversion data
- Key messages (Section 11) — to evaluate content performance

Read any available data from:
- `/outputs/performance/` — prior reports, campaign data
- `/outputs/assets/social/`, `/outputs/assets/email/` — content published this week
- User-provided weekly metrics

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided weekly data**
Use their input. Go to Step 3.

**Path B — No data provided**
Ask:
"Để viết weekly report, mình cần metrics từ tuần này:
1. **Website:** Sessions / New users / Bounce rate / Conversions?
2. **Social:** Reach / Engagement / Followers gained / Top post?
3. **Email:** Sent / Open rate / Click rate / Unsubscribes?
4. **Ads:** Spend / Leads / CPA / ROAS?
5. **Sales:** Leads / Demos / Closes / Revenue?
6. **Week:** [Start date] – [End date]?"

Wait for answer before continuing.

## Step 3 — Write the weekly report

### Weekly report structure

**The narrative (what actually happened):**
Don't just list numbers. Tell the story: what moved this week, why, and what it means.

**Week-over-week comparison:**
Every metric needs context. "100 leads" means nothing without: was that up or down from last week? On track for monthly goal?

**The one most important thing:**
Every weekly report must end with one clear priority for next week. Not five priorities. One.

### Channel coverage

**Website (GA4 or equivalent):**
- Sessions: total + vs last week
- New users: acquisition trend
- Top traffic source this week
- Conversion rate: goal completions / sessions

**Social media:**
- Reach and impressions: total across platforms
- Engagement rate: (likes + comments + shares) / reach
- Follower change: gained / lost
- Top performing post: what it was, why it worked

**Email:**
- Open rate vs. average
- Click rate vs. average
- List growth: new subscribers
- Revenue/conversions attributed to email (if tracked)

**Paid ads:**
- Total spend
- Leads generated
- CPA: cost per lead vs. last week
- ROAS (if e-commerce)

**Sales pipeline:**
- New leads
- Demos / calls booked
- Deals closed
- Pipeline value

### Vietnamese reporting context
- Report in VND for budget/revenue figures
- GMT+7 for any time-based observations
- Note if results were affected by Vietnamese holidays/events (Tết, national holidays affect performance significantly)
- Zalo metrics if available: separate from email (Zalo typically 2–3× higher open rate)

## Step 4 — Write output

Save to `/outputs/performance/weekly-report-[YYYY-WXX].md`:

```markdown
# Weekly Performance Report — Week [XX], [Year]
> Period: [Mon DD] – [Sun DD, YYYY] | Generated: [date]

## The Week in One Sentence
[What happened this week — the most important story in one sentence]

---

## Scorecard

| Channel | Key Metric | This Week | Last Week | Trend |
|---|---|---|---|---|
| Website | Sessions | | | ↑ / ↓ / → |
| Social | Reach | | | |
| Email | Open rate | | | |
| Ads | CPA | | | |
| Sales | Leads | | | |

---

## What Moved

### ✅ Wins this week
- [Specific result — what happened and why it's a win]
- [Second win]

### ⚠️ Concerns
- [What underperformed — and likely reason]
- [Second concern]

---

## Channel Breakdown

### Website
- Sessions: [n] ([+/-]% vs last week)
- New users: [n]
- Top source: [organic / paid / social / direct]
- Conversion rate: [%]

### Social
- Reach: [n] ([+/-]%)
- Engagement rate: [%]
- New followers: [+n]
- Top post: "[Post description]" — [platform] — [engagement stats]

### Email
- Open rate: [%] (avg: [benchmark]%)
- Click rate: [%]
- New subscribers: [+n]

### Paid Ads
- Total spend: [VND amount]
- Leads: [n]
- CPA: [VND amount]
- Best performing ad: [description]

### Sales Pipeline
- New leads: [n]
- Demos booked: [n]
- Deals closed: [n]
- Revenue this week: [VND amount]

---

## Content Published This Week
| Date | Platform | Content | Performance |
|---|---|---|---|
| | | | |

---

## #1 Priority for Next Week
**[One specific action to take, with measurable expected outcome]**

Supporting actions:
- [Second priority]
- [Third priority]

---

## Notes
[Holiday effects / external factors / platform changes / one-off events that affected data]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Weekly report tuần [XX] đã hoàn chỉnh.**

**This week:** [One-sentence summary]
**Top win:** [Specific result]
**#1 priority next week:** [Action]

📁 Đã lưu vào: `/outputs/performance/weekly-report-[YYYY-WXX].md`

**Bước tiếp theo:** Chạy `/monthly-strategy-review` vào cuối tháng, hoặc `/campaign-report` để deep-dive vào một campaign cụ thể."

---
