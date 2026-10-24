# Subject Line A/B Test Skill

Your job is to write multiple subject line variants for a single email — with clear hypotheses about why each variant should win, and a framework to pick the winner.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5) — subject lines must match brand personality
- Target audience (Section 6) — what language resonates with them

If brand.md doesn't exist: ask user for brand tone and audience before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided the email content or current subject line**
Use what they gave. Go to Step 3.

**Path B — No email content provided**
Ask:
"Để viết subject line variants, mình cần:
1. **Email này về gì?** (tóm tắt nội dung trong 1–2 câu)
2. **Subject line hiện tại** (nếu có — mình sẽ cải thiện)
3. **Mục tiêu email:** Open rate / Click rate / Reply rate
4. **Audience segment:** Cold list / warm subscribers / existing customers / re-engagement"

Wait for answer.

## Step 3 — Generate variants

### The 6 subject line angles

For each email, write one variant per angle — then recommend the best 2 to test:

**Angle 1 — Curiosity gap**
Leave something unresolved that the reader needs to open to close.
Formula: "Tại sao [thing they assumed] không phải lý do thật" or "Điều mình không nói trong bài trước"
Risk: Can feel clickbaity if the email doesn't deliver. Only use if the content actually answers the gap.

**Angle 2 — Specificity**
Numbers, names, and specific situations outperform vague claims.
Formula: "[Specific number] + [specific outcome] + [specific timeframe]"
Example: "45 phút/tuần thay vì 3 giờ/ngày — đây là cách"

**Angle 3 — Direct benefit**
State the outcome plainly. Works best for warm audiences who trust the brand.
Formula: "Cách [achieve outcome] mà không cần [painful alternative]"

**Angle 4 — Question**
Mirrors the reader's internal dialogue. Opens a loop they want closed.
Formula: "[Question that surfaces their exact situation]"
Example: "Bạn có đang trả tiền để không sở hữu gì không?"

**Angle 5 — Contrarian / challenge**
Challenges a belief the reader holds. Creates friction that demands resolution.
Formula: "[Common belief] là sai — đây là lý do"
Risk: Only works if the content actually challenges, not just teases.

**Angle 6 — Personal / story**
Feels like a message from a person, not a brand.
Formula: "Mình vừa học được điều này từ [source]" or "Cuộc trò chuyện với [persona] tuần này"

### Subject line rules (Vietnamese market)

**Length:**
- Mobile preview: 35–45 chars ideal, 50 max
- Gmail desktop: up to 60 chars visible
- Never truncate mid-word

**Emoji:**
- 1 emoji max, at start or end — never mid-subject
- Use only if it matches brand tone (casual/friendly brands: yes. Professional B2B: sparingly)
- Avoid: 🔥💥🚀 — overused, trigger spam filters

**Spam trigger words to avoid:**
- "Miễn phí", "Giảm giá X%", "Ưu đãi đặc biệt", "Chỉ hôm nay", "Click ngay"
- All caps words
- Multiple exclamation marks

**Preview text:**
- Not an afterthought — 50% of open decision is subject + preview together
- Never repeat the subject line
- Either: continue the curiosity → "...và đây là điều bạn chưa biết"
- Or: add context → "3 khách hàng của mình đã làm điều này tuần trước"

### Recommend best 2 to test

After writing all 6 variants, identify:
- **Variant A (Control):** The safest, most on-brand option
- **Variant B (Test):** The riskier, higher-upside option

State hypothesis: "Mình dự đoán Variant B sẽ có open rate cao hơn vì [specific reason]. Nếu audience này [characteristic], Variant A có thể win."

**Winner condition:** Open rate difference > 5 percentage points after minimum 200 opens per variant.

## Step 4 — Write output

Save to `/outputs/assets/email/subject-line-ab-[email-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Subject Line A/B Test — [Email Name]
> Generated: [date] | Email: [email description]

## Email Summary
[1–2 sentence description of what the email contains]

---

## 6 Subject Line Variants

### Variant 1 — Curiosity Gap
**Subject:** [subject line]
**Preview:** [preview text]
**Hypothesis:** [why this should work]

### Variant 2 — Specificity
**Subject:**
**Preview:**
**Hypothesis:**

### Variant 3 — Direct Benefit
**Subject:**
**Preview:**
**Hypothesis:**

### Variant 4 — Question
**Subject:**
**Preview:**
**Hypothesis:**

### Variant 5 — Contrarian
**Subject:**
**Preview:**
**Hypothesis:**

### Variant 6 — Personal / Story
**Subject:**
**Preview:**
**Hypothesis:**

---

## Recommended Test

**Variant A (Control):** [Variant #] — [Subject line]
**Variant B (Test):** [Variant #] — [Subject line]

**Prediction:** [Which will win and why]
**Winner condition:** Open rate gap > 5pp after 200+ opens per variant
**Recommended send split:** 50/50 or 80/20 depending on list size

---

## Notes
- Spam risk assessment: [any flags in the variants]
- Best send time for this audience: [day + time]
```

## Step 5 — Confirm

After writing:

---
"✅ **Subject line variants cho '[Email]' hoàn chỉnh.**

**6 variants written across:** Curiosity / Specificity / Direct benefit / Question / Contrarian / Personal

**Recommended test:**
- A (Control): [subject]
- B (Test): [subject]
- Prediction: [one sentence]

📁 Đã lưu: `/outputs/assets/email/subject-line-ab-[email-slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/newsletter` để viết email tiếp theo, hoặc `/ab-test-setup` để setup tracking cho test này."

---
