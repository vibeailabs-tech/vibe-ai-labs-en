# Agent 4 — CRO Agent ✅

> AI Marketing Agent Team · Agent 4 of 16

**Purpose:** Turns brand context and strategy into conversion-optimized copy — landing pages, CTAs, A/B tests, page audits, and sales pages that move visitors to action.
**APIs/MCPs required:** None — pure Claude reasoning.
**Prerequisites:** `brand.md` (Agent 1). `/strategy/offer-positioning.md` from Agent 3 improves output quality for lp-builder and sales-page.
**Status:** Complete.

---

## Overview

The CRO Agent's job is simple: more conversions from the traffic you already have. It reads brand.md and strategy files, then writes copy designed to turn skeptical visitors into buyers.

```
brand.md (Agent 1)
       +
/strategy/offer-positioning.md (Agent 3)
/strategy/campaign-brief.md (Agent 3)
       ↓
CRO Agent
       ↓
/assets/cro/landing-page.md
/assets/cro/cta-optimization.md
/assets/cro/ab-test-setup.md
/assets/cro/page-audit.md
/assets/cro/sales-page.md
       ↓
Distribution Agent / Social Agent (drive traffic to these pages)
```

---

## 5 Skills

### `/lp-builder` — Landing Page Builder
**Purpose:** Writes a complete, ready-to-publish landing page — every section, every word. Not a template. Actual copy.
**Input:** brand.md + campaign-brief.md (if exists).
**Output:** `/assets/cro/landing-page.md`

**7-section structure:**
| Section | Purpose |
|---|---|
| 1. Hero | Stop the scroll — headline + subheadline + CTA + trust signal |
| 2. Problem | Make them feel seen — agitate the pain in their own words |
| 3. Solution | Introduce the possibility — what changes, how it works (3 steps) |
| 4. Proof | Stack credibility — stats, testimonials, guarantee |
| 5. Packages | Present all tiers — clear, compared, one recommended |
| 6. FAQ | Kill objections — 6–8 specific questions from brand.md |
| 7. Final CTA | Close — restate promise, one action, remove all risk |

**Copy rules enforced:**
- Specific numbers always: "$700 một lần", "16 agents", "3–5 ngày"
- Vietnamese register: "bạn/mình" throughout
- No forbidden vocabulary from brand.md Section 5
- One CTA per section — no competing actions

---

### `/cta-optimization` — CTA Rewriting
**Purpose:** Audits weak CTAs and rewrites each one with 3 variants — urgency, benefit, and risk-removal angles.
**Input:** brand.md + existing CTAs (user pastes them) or `/assets/cro/landing-page.md`.
**Output:** `/assets/cro/cta-optimization.md`

**5 CTA problems diagnosed:**
1. Too vague ("Liên hệ ngay", "Tìm hiểu thêm")
2. Brand-centric not reader-centric ("Mua ngay" vs "Nhận tư vấn miễn phí")
3. No urgency or scarcity
4. No risk removal
5. Wrong intent match (cold CTA ≠ hot CTA)

**CTA intent ladder:**
| Stage | Example CTAs |
|---|---|
| Cold (awareness) | "Save để đọc lại" / "Comment nếu bạn thấy đúng" |
| Warm (consideration) | "Nhắn mình để tư vấn miễn phí 30 phút" |
| Hot (decision) | "Nhắn 'BOOK' để giữ slot — còn [X] chỗ" |

**5 high-converting CTA formulas:**
1. Action + Reward: "Nhắn mình để nhận tư vấn miễn phí 30 phút"
2. Action + Scarcity: "Nhắn 'BOOK' để giữ slot — chỉ còn 3 chỗ tháng 5"
3. Action + Risk removal: "Book tư vấn miễn phí — không ràng buộc"
4. Keyword trigger: "Nhắn 'CHECKLIST' để nhận PDF miễn phí"
5. Contrast: "Đang trả agency $800/tháng? Nhắn mình — mình tính ROI trong 10 phút"

---

### `/ab-test-setup` — A/B Test Design
**Purpose:** Designs structured, one-variable-at-a-time A/B tests with clear hypotheses, success metrics, and winner conditions.
**Input:** brand.md + existing copy (landing page, social posts, email subjects).
**Output:** `/assets/cro/ab-test-setup.md`

**Core rules:**
- **One variable at a time** — if headline AND CTA both change, you don't know which caused the result
- **Clear hypothesis** — "We believe [change] will [metric] because [reason]"
- **Define the winner before running** — not after

**Priority test order (highest ROI first):**
| Priority | Element | Why |
|---|---|---|
| 1 | Headline / hook | Biggest impact, easiest to test |
| 2 | CTA text | Direct impact on conversion action |
| 3 | Offer framing | Price vs installment vs value anchor |
| 4 | Guarantee placement | Above vs below CTA |
| 5 | Email subject line | Open rate = everything |

**Minimum sample sizes:**
- Facebook post: 1,000+ impressions before calling winner
- Email: 200 sends per variant
- Landing page: 100 unique visitors per variant
- Zalo broadcast: 50 recipients per variant

---

### `/page-audit` — Conversion Audit
**Purpose:** Scores an existing page across 6 dimensions (1–10 each) and delivers a prioritized fix list — critical issues first, quick wins flagged.
**Input:** brand.md + page content (user pastes) or URL.
**Output:** `/assets/cro/page-audit.md`

**6 scoring dimensions:**
| Dimension | Key question |
|---|---|
| Clarity | In 5 seconds: who is this, what do they do, why should I care? |
| Relevance | Does the reader immediately feel "this is for me"? |
| Value Proposition | Are benefits specific with numbers? Is there an outcome? |
| Trust | Are there real proof points, specific guarantees, credibility signals? |
| CTA Strength | Is there one clear, compelling CTA at the right moment? |
| Friction | Is anything blocking the reader from taking action? |

**Score interpretation:**
- 8–10: Strong page — optimize details
- 6–7: Decent foundation — 3–4 targeted fixes needed
- 4–5: Significant gaps — rebuild 2–3 major sections
- 1–3: Needs full rebuild

**Fix prioritization matrix:**
- High impact + Easy effort → **Do first** (quick wins)
- High impact + Hard effort → **Plan and schedule**
- Low impact + Easy effort → **Do when time allows**
- Low impact + Hard effort → **Skip for now**

---

### `/sales-page` — Long-Form Sales Letter
**Purpose:** Writes a complete long-form sales page using the Halbert copywriting structure — takes a skeptical stranger all the way to "I want this."
**Input:** brand.md + offer-positioning.md + campaign-brief.md (if campaign-specific).
**Output:** `/assets/cro/sales-page.md`

**12-section Halbert structure:**
| Section | Purpose |
|---|---|
| 1. Headline | Stop the scroll — 3 options written, 1 recommended |
| 2. Opening hook | Make them feel seen — describe their situation in their words |
| 3. Turning point | "Có một cách khác..." — introduce the possibility |
| 4. The mechanism | Name the unique system — explain HOW it works |
| 5. What you get | Exhaustive deliverable list — stack the value before price |
| 6. Proof | Stats + testimonials/demo + logic + guarantee |
| 7. Price reveal | Anchor first (agency cost) → then reveal price |
| 8. Packages | All tiers with full details + recommended highlighted |
| 9. Objections | 5+ "You might be thinking..." responses |
| 10. Guarantee | Full statement — standalone section |
| 11. Urgency/scarcity | Only if real — slots, deadline |
| 12. Final CTA | Restate promise + one clear action + risk removal |

**Key principle:** Proof before price. The reader must feel the value before seeing the number.

---

## Recommended Sequence

```
/page-audit → /lp-builder → /cta-optimization → /sales-page → /ab-test-setup
```

Audit what exists first — then build or rebuild. Test last.

## Individual Skill Use

Any skill can run standalone:
- Have a page to review? Run `/page-audit`
- Need to launch fast? Run `/lp-builder` directly
- CTAs feel weak? Run `/cta-optimization` on any existing copy
- Ready to test? Run `/ab-test-setup`

---

## No APIs Required

CRO Agent runs entirely on Claude reasoning.

| Input source | Where it comes from |
|---|---|
| Brand voice + audience | `/profiles-output/brand.md` |
| Refined offer | `/strategy/offer-positioning.md` |
| Campaign context | `/strategy/campaign-brief.md` |
| Existing page content | User pastes or provides URL |

---

## Key Rules

1. **Specificity converts** — "$700 một lần" beats "giá hợp lý". Numbers always.
2. **Risk-reversal is non-negotiable** — Vietnamese buyers are risk-averse. Every page needs a specific, measurable guarantee.
3. **One CTA per section** — multiple competing CTAs create decision paralysis.
4. **Proof before price** — stack proof (stats, guarantee, demo) before the price reveal.
5. **No fake urgency** — only use scarcity if it's real. Fake urgency destroys trust with Vietnamese buyers.
6. **Match CTA to funnel stage** — cold audience gets "Save này" not "Book ngay".
