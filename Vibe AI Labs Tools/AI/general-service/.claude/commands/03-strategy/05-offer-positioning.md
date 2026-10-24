---
name: offer-positioning
description: Refines and sharpens the brand's core offer based on market data, competitor gaps, and audience insights. Use this skill when the user wants to make their offer more compelling, adjust pricing, create package tiers, or reframe their value proposition. Trigger whenever the user mentions offer, pricing, packages, value proposition, or making the offer more attractive.
---

# Offer Positioning Skill

Your job is to make the brand's core offer impossible to ignore — sharper framing, clearer value, better structure, stronger risk-reversal. Not inventing a new product. Repositioning what already exists so the right buyer says yes immediately.

## Step 1 — Read inputs

Read:
- `/outputs/profiles-output/brand.md` — core offer (Section 9), USP (Section 8), competitors (Section 10), ICP (Section 6)
- `/outputs/research/market-research-*.md` — price sensitivity, spending patterns (if exists)
- `/outputs/research/competitor-analysis-*.md` — competitor pricing and offer structures (if exists)
- `/outputs/research/trend-monitoring-*.md` — what buyers expect right now (if exists)

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User described what they want to improve**
Use their direction. Go to Step 3.

**Path B — No direction provided**
Ask:
"Bạn muốn mình tập trung vào phần nào của offer?
1. Cấu trúc gói dịch vụ (packages + tiers)
2. Định giá (pricing strategy)
3. Cách trình bày giá trị (value framing)
4. Risk-reversal và cam kết (guarantee)
5. Tất cả (full offer audit)"

Wait for answer before continuing.

## Step 3 — Audit and rebuild the offer

### Offer audit framework

**Problem 1 — Offer is too vague**
"Dịch vụ marketing toàn diện" means nothing. A strong offer names: who it's for, what they get, the outcome, the timeline, and the price. Test: can a stranger read your offer and instantly know if it's for them?

**Problem 2 — Price is floating**
No anchor = buyer creates their own (usually too high). Always frame price relative to something — the cost of NOT buying, the cost of the alternative, or the value of the outcome.

**Problem 3 — No risk-reversal**
Vietnamese buyers are risk-averse. A guarantee that's specific and measurable removes the last objection. "Hài lòng 100%" means nothing. "Nếu sau X tuần chưa thấy Y, hoàn tiền Z — không hỏi lý do" means something.

**Problem 4 — Package structure creates confusion**
Too many options = no decision. Ideal: 3 tiers where the middle one looks most reasonable. Each tier should have one clear "it's obvious who this is for" signal.

**Problem 5 — Features listed instead of outcomes**
"16 agents" is a feature. "Hệ thống marketing chạy được mà không cần agency" is an outcome. Buyers buy outcomes.

### Offer optimization checklist

**Naming:**
- Does the offer have a specific name? (not "gói dịch vụ")
- Does the name signal the outcome? ("The 3-Bước Bloom System" vs "Gói chăm sóc da cơ bản")

**Packaging:**
- Are there 3 clear tiers? (starter / growth / full)
- Is each tier clearly mapped to a buyer type?
- Is the price gap between tiers justified by value difference?

**Value framing:**
- Is the price anchored to something? (cost of alternative, value of outcome)
- Is the ROI or result stated in the offer?
- Is the timeline clear? ("Kết quả sau 3 buổi" not "kết quả nhanh chóng")

**Risk-reversal:**
- Is there a specific, measurable guarantee?
- Is the guarantee credible? (matches what the brand can actually deliver)
- Does the guarantee remove the buyer's primary objection?

**Social proof integration:**
- Is proof embedded in the offer? (not just on a separate page)
- Does the proof speak to the buyer's specific fear?

### Vietnamese market-specific considerations
- **Installment framing:** Vietnamese buyers respond well to monthly/phased payment options even for one-time purchases. "3.5 triệu" feels bigger than "700k x 5 buổi"
- **Comparison anchoring:** Frame against what they're already paying (agency, freelancer, DIY time cost)
- **Relationship signals:** Vietnamese B2B buyers want to feel they're working WITH someone, not buying FROM someone. Zalo support, follow-up calls, personal check-ins add perceived value at low cost
- **Scarcity that's real:** "Chỉ nhận 3 khách mới mỗi tháng" — only use if true. Vietnamese buyers are skeptical of fake urgency
- **Proof of process:** Showing the HOW (your methodology, system, steps) is as important as showing results

## Step 4 — Write output

Save to `/outputs/strategy/offer-positioning-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Offer Positioning — [Brand Name]
> Generated: [date]

## Current Offer Audit

### What's working:
- 

### What needs sharpening:
- 

---

## Refined Offer Structure

### Package 1 — [Name] (Entry / Starter)
**Who it's for:** 
**What they get:**
- 
- 
**Outcome:** 
**Timeline:** 
**Price:** [amount] — framed as: [anchor comparison]
**Ideal for:** [one sentence buyer description]

---

### Package 2 — [Name] (Core / Most Popular)
**Who it's for:** 
**What they get:**
- 
- 
**Outcome:** 
**Timeline:** 
**Price:** [amount] — framed as: [anchor comparison]
**Ideal for:** [one sentence buyer description]

---

### Package 3 — [Name] (Premium / Full System)
**Who it's for:** 
**What they get:**
- 
- 
**Outcome:** 
**Timeline:** 
**Price:** [amount] — framed as: [anchor comparison]
**Ideal for:** [one sentence buyer description]

---

## Guarantee / Risk-Reversal
**Guarantee statement:** 
**What it covers:** 
**What makes it credible:** 

---

## Value Framing — How to Present the Price

**Anchor 1 (vs alternative):** 
**Anchor 2 (vs outcome value):** 
**Installment framing (if applicable):** 
**ROI statement:** 

---

## Offer Headline Options
5 ways to introduce this offer:
1. 
2. 
3. 
4. 
5. 

---

## Objection Handling
| Objection | Response |
|---|---|
| "Giá cao quá" | |
| "Để tôi suy nghĩ thêm" | |
| "Tôi chưa chắc có phù hợp không" | |
| "Tôi đã thử X rồi, không hiệu quả" | |
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Offer positioning cho [Brand Name] đã hoàn chỉnh.**

**Thay đổi chính:**
- [What was sharpened / restructured]
- Guarantee mới: [guarantee statement]
- Value anchor: [how price is now framed]

📁 Đã lưu vào: `/outputs/strategy/offer-positioning-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/sales-page` để viết trang bán hàng dựa trên offer này, hoặc `/campaign-brief` để build brief cho chiến dịch launch offer mới."

---
