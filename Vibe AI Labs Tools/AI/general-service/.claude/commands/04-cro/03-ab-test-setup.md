# A/B Test Setup Skill

Your job is to design structured, statistically sound A/B tests for this brand — headlines, CTAs, offers, email subjects, or landing page sections. One variable at a time. Clear hypothesis. Measurable outcome.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer and packages (Section 9)
- Target audience and pain points (Section 6)
- Key messages (Section 11)

If `/assets/cro/landing-page.md` or `/assets/cro/cta-optimization.md` exist: read them — use existing copy as the control variant.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified what to test**
Use their direction. Go to Step 3.

**Path B — No direction provided**
Ask:
"Bạn muốn setup A/B test cho element nào?
1. Headline (landing page hoặc Facebook post)
2. CTA button text
3. Email subject line
4. Offer framing (giá / bonus / guarantee)
5. Hook của post (câu mở đầu)
6. Tất cả elements quan trọng nhất

Và bạn đang test trên platform nào? (Facebook ads / landing page / email / TikTok)"

Wait for answer before continuing.

## Step 3 — Design the A/B tests

### A/B test design rules

**Rule 1 — One variable at a time**
Never test two things simultaneously. If headline AND CTA change, you don't know which caused the result. Pick one.

**Rule 2 — Clear hypothesis**
Every test needs: "We believe [change] will [improve metric] because [reason]."
Example: "We believe changing CTA from 'Liên hệ ngay' to 'Nhắn BOOK để giữ slot' will increase DM inquiries because it names the specific action and adds scarcity."

**Rule 3 — Measurable success metric**
Define the winner before you run the test:
- Facebook post: engagement rate, DM inquiries, link clicks
- Landing page: form submissions, scroll depth, time on page
- Email: open rate (subject line test), click rate (CTA test)
- Zalo: reply rate, keyword triggers

**Rule 4 — Minimum sample size**
- Facebook post: wait for 1,000+ impressions before calling a winner
- Email: minimum 200 sends per variant
- Landing page: minimum 100 unique visitors per variant
- Zalo broadcast: minimum 50 recipients per variant

**Rule 5 — Run time**
- Facebook: 3–5 days minimum (algorithm needs time to optimize)
- Email: 48–72 hours (most opens happen in first 24 hrs)
- Landing page: 1–2 weeks (depends on traffic volume)

### What to test by priority

**Highest ROI tests (run first):**
1. **Headline / hook** — biggest impact, easiest to test
2. **CTA text** — direct impact on conversion action
3. **Offer framing** — price vs. installment vs. value anchor
4. **Guarantee placement** — above vs. below CTA

**Medium ROI tests:**
5. Email subject line (fear vs. curiosity vs. benefit)
6. Social proof placement (hero vs. after problem section)
7. Image/visual style (demo screenshot vs. before/after vs. text-only)

**Lower ROI (test after above):**
8. Button color
9. Post length (short vs. long)
10. Hashtag sets

## Step 4 — Write test variants

For each element to test, produce:

**Control (A):** [existing version]
**Variant (B):** [new version]
**Hypothesis:** We believe [B] will [metric improvement] because [reason]
**Success metric:** [what to measure]
**Winner condition:** B wins if [specific threshold] (e.g., "10%+ more DM inquiries after 1,000 impressions")
**Run time:** [duration]
**How to implement:** [exact steps to run this test]

### Headline test angles for Vietnamese B2B:
- **Pain angle:** "Bạn đang tốn $800/tháng cho agency và không sở hữu gì"
- **Stat angle:** "73% dùng AI — chỉ 13.8% có hệ thống thật"
- **Contrast angle:** "Agency $800/tháng vs AI System $700 một lần"
- **Outcome angle:** "Setup một lần — 16 agents làm marketing thay bạn mãi mãi"
- **Question angle:** "Bạn có biết mình đang trả bao nhiêu cho marketing mà không sở hữu gì không?"

### Email subject line formulas:
- Fear: "[Số tiền] bạn đang mất mỗi tháng cho agency"
- Curiosity: "Tại sao 86% doanh nghiệp dùng AI vẫn không có kết quả"
- Benefit: "Setup xong trong 7 ngày — và bạn tự chạy được ngay"
- Personalization: "[Tên], đây là hệ thống marketing cho [ngành] của bạn"
- Urgency: "Còn 3 slots tháng 5 — deadline [date]"

## Step 5 — Write output

Save to `/assets/cro/ab-test-setup.md`:

```markdown
# A/B Test Setup — [Brand Name]
> Generated: [date] | Platform: [platform] | Elements: [what's being tested]

---

## Test #1 — [Element name]

**What we're testing:** [headline / CTA / subject line / offer framing]
**Platform:** [Facebook / landing page / email / Zalo]
**Current state (Control A):** "[existing copy]"

**Variant B:** "[new version]"

**Hypothesis:** We believe [Variant B] will [metric] because [reason].

**Success metric:** [what to measure — DM inquiries / open rate / form submissions]
**Winner condition:** B wins if [threshold] after [sample size / time]
**Run time:** [duration]

**How to run:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**What to do after:**
- If B wins: [action]
- If A wins: [action]
- If inconclusive: [action]

---

[Repeat for each test]

---

## Testing Roadmap

Priority order for next 30 days:
| # | Test | Element | Platform | Expected impact |
|---|---|---|---|---|
| 1 | [test name] | [element] | [platform] | High / Medium / Low |

---

## Notes
- Never run two tests simultaneously on the same audience
- Document all results — even losses tell you something
- Winning variant becomes the new control for the next test
```

## Step 6 — Confirm

After writing, reply:

---
"✅ **A/B test setup cho [Brand Name] đã hoàn chỉnh.**

**Tests đã design:**
- [count] tests sẵn sàng chạy
- Test ưu tiên #1: [test name] — [why it's highest priority]
- Metric chính: [primary metric]

📁 Đã lưu vào: `/assets/cro/ab-test-setup.md`

**Bước tiếp theo:** Chạy test #1 ngay hôm nay. Sau 3–5 ngày quay lại với data — chạy `/campaign-report` để phân tích kết quả."

---
