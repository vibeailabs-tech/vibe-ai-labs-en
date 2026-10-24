# Page Audit Skill

Your job is to score an existing page — landing page, sales page, Facebook page, or any marketing asset — and deliver a prioritized list of specific fixes. Not vague advice. Exact changes with expected impact.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — to check if page matches
- Target audience and pain points (Section 6) — to check if page speaks to them
- Core offer (Section 9) — to check if offer is presented clearly
- USP (Section 8) — to check if differentiation is visible
- Competitors (Section 10) — to check if positioning is distinct

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided page content or URL**
Use what they gave. Go to Step 3.

**Path B — No page provided**
Ask:
"Bạn muốn mình audit trang nào?
- Paste nội dung trang vào đây, hoặc
- Cho mình URL để mình scrape, hoặc
- Mô tả trang (Facebook page / landing page / Zalo OA profile...)

Và mục tiêu của trang này là gì? (thu lead / bán trực tiếp / build trust)"

Wait for answer before continuing.

## Step 3 — Run the audit

Score the page across 6 dimensions (1–10 each):

### Dimension 1 — Clarity (Rõ ràng)
**Question:** Trong 5 giây, người lạ có biết (1) trang này là của ai, (2) họ làm gì, (3) tại sao mình nên quan tâm không?
- 9–10: Tất cả 3 câu trả lời rõ ngay trong hero
- 7–8: 2/3 rõ, 1 cái phải đọc xuống
- 5–6: Phải đọc 30 giây mới hiểu
- 1–4: Vẫn không rõ sau khi đọc hết

### Dimension 2 — Relevance (Đúng người)
**Question:** Người đọc có thấy "đây là dành cho mình" không?
- Check: ICP language, pain points, specific audience signals
- Red flags: "phục vụ mọi đối tượng", vague audience, no pain point articulation

### Dimension 3 — Value Proposition (Giá trị rõ ràng)
**Question:** Lợi ích cụ thể là gì? Có số liệu không? Có outcome không?
- Check: specific numbers, before/after, timeline, price anchoring
- Red flags: "tăng trưởng mạnh mẽ", "hiệu quả vượt trội", features without outcomes

### Dimension 4 — Trust (Tin tưởng)
**Question:** Có lý do để tin không?
- Check: testimonials, guarantees, social proof, credentials, specific results
- Red flags: no proof, vague guarantees ("hài lòng 100%"), stock photos

### Dimension 5 — CTA Strength (Hành động rõ ràng)
**Question:** Có một CTA rõ ràng, compelling, và đúng lúc không?
- Check: CTA text specificity, placement, number of CTAs (too many = confusion)
- Red flags: "Liên hệ ngay", multiple competing CTAs, CTA buried below fold

### Dimension 6 — Friction (Rào cản)
**Question:** Có điều gì đang chặn người đọc hành động không?
- Check: page load speed signals, form length, commitment level of CTA, objections not addressed
- Red flags: long forms, asking for too much info, no FAQ, no risk reversal

### Overall score: (sum of 6 dimensions) / 6

### Score interpretation:
- 8–10: Strong page — optimize details
- 6–7: Decent foundation — 3–4 targeted fixes needed
- 4–5: Significant gaps — rebuild 2–3 major sections
- 1–3: Needs full rebuild — start from brand.md

## Step 4 — Prioritize fixes

For each issue found, assign:
- **Impact:** High / Medium / Low (on conversion rate)
- **Effort:** Easy (30 min) / Medium (2–3 hrs) / Hard (full rebuild)
- **Priority:** Fix immediately / Fix this week / Fix this month

### Fix prioritization matrix:
- High impact + Easy effort → **Do first** (quick wins)
- High impact + Hard effort → **Plan and schedule**
- Low impact + Easy effort → **Do when time allows**
- Low impact + Hard effort → **Skip for now**

## Step 5 — Write output

Save to `/assets/cro/page-audit.md`:

```markdown
# Page Audit — [Brand Name]
> Generated: [date] | Page: [page name/URL] | Goal: [page goal]

---

## Overall Score: [X]/10

| Dimension | Score | Grade |
|---|---|---|
| Clarity | [X]/10 | [A/B/C/D/F] |
| Relevance | [X]/10 | |
| Value Proposition | [X]/10 | |
| Trust | [X]/10 | |
| CTA Strength | [X]/10 | |
| Friction | [X]/10 | |

---

## What's Working
- [strength 1]
- [strength 2]
- [strength 3]

---

## Critical Issues (Fix Immediately)

### Issue #1 — [Issue name]
- **Dimension:** [which dimension]
- **What's wrong:** [specific description]
- **Current:** "[current copy or element]"
- **Fix:** "[exact replacement or action]"
- **Expected impact:** [what will improve]

[Repeat for each critical issue]

---

## High-Impact Fixes (This Week)

### Fix #1 — [Fix name]
- **Current:** [what exists now]
- **Recommended:** [specific change]
- **Why:** [reason]

[Repeat]

---

## Quick Wins (30 Minutes Each)
1. [Quick win 1] — [exact change]
2. [Quick win 2] — [exact change]
3. [Quick win 3] — [exact change]

---

## Lower Priority (This Month)
- [Issue] — [recommendation]
- [Issue] — [recommendation]

---

## Rewritten Elements
Key sections that need complete rewrites (with new copy):

### Hero (rewritten)
[New headline + subheadline + CTA]

### [Other section if needed]
[New copy]

---

## A/B Test Suggestions
Based on this audit, the highest-value things to test:
1. [Test suggestion] — hypothesis: [what you expect]
2. [Test suggestion]
```

## Step 6 — Confirm

After writing, reply:

---
"✅ **Page audit cho [Brand Name] đã hoàn chỉnh.**

**Điểm tổng:** [X]/10

**3 vấn đề nghiêm trọng nhất:**
1. [Issue 1]
2. [Issue 2]
3. [Issue 3]

**Quick win ngay hôm nay:** [top quick win]

📁 Đã lưu vào: `/assets/cro/page-audit.md`

**Bước tiếp theo:** Fix critical issues trước, sau đó chạy `/ab-test-setup` để test các thay đổi."

---
