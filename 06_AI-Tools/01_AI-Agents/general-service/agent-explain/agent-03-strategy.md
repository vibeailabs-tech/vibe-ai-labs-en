# Agent 3 — Strategy Agent ✅

> AI Marketing Agent Team · Agent 3 of 16

**Purpose:** Turns brand context and market research into concrete, actionable marketing plans — campaign structure, content calendar, lead magnets, campaign briefs, and offer positioning.
**APIs/MCPs required:** None — pure Claude reasoning.
**Prerequisites:** `brand.md` (Agent 1). Research files from Agent 2 improve output quality but are optional.
**Status:** Complete and tested.

---

## Overview

The Strategy Agent bridges research and execution. It reads brand.md + research outputs and produces structured plans that all execution agents (Content, Social, Email, Ads) read before creating any content.

```
brand.md (Agent 1)
       +
/research/*.md (Agent 2)
       ↓
Strategy Agent
       ↓
/strategy/offer-positioning.md
/strategy/campaign-plan.md
/strategy/content-calendar.md
/strategy/lead-magnets.md
/strategy/campaign-brief-[name].md
       ↓
Execution Agents (Agents 5–12)
```

---

## 5 Skills

### `/offer-positioning` — Offer Audit & Sharpening
**Purpose:** Audits the current core offer and restructures it to be clearer, more compelling, and easier to say yes to.
**Input:** brand.md Section 9 (Core Offer), Section 8 (USP), Section 10 (Competitors), research files.
**Output:** `/strategy/offer-positioning.md`

**Audits and rebuilds:**
- Package structure (3 tiers: starter / core / premium)
- Price framing and anchoring (vs alternative cost, vs outcome value)
- Outcome language (replaces feature lists with results)
- Guarantee / risk-reversal (specific and measurable, not "hài lòng 100%")
- Objection handling table (4 most common objections + responses)
- 5 offer headline directions

**Common fixes:**
- Vague offer name → specific outcome-driven name
- Price floating alone → anchored to what they're currently paying
- Feature list → outcome + timeline statement
- No guarantee → specific measurable guarantee

**Vietnamese market notes:**
- Installment framing: "700k x 5 buổi" beats "3.5 triệu"
- Relationship signals matter: Zalo support, follow-up calls add perceived value
- Only use scarcity if it's real ("chỉ nhận 3 khách/tháng")

---

### `/campaign-planning` — 90-Day Campaign Structure
**Purpose:** Builds a focused, phased 90-day marketing plan with clear monthly themes, weekly actions, and measurable KPI targets.
**Input:** brand.md + all research files + campaign goal from user.
**Output:** `/strategy/campaign-plan.md`

**3-month structure:**
| Month | Theme | Primary Goal |
|---|---|---|
| 1 | Awareness & Trust | Get right people to know and trust the brand |
| 2 | Consideration & Engagement | Move warm audience toward wanting the offer |
| 3 | Conversion & Retention | Turn interested prospects into paying customers |

**Each month defines:**
- Single narrative theme
- Primary platform (where most energy goes)
- Content mix ratio (educational : proof : promotional)
- Key milestone (what must be live by end of month)
- Success metric (one number that proves the month worked)

**Weekly breakdown:** Specific theme → content type → platform → CTA for each of the 4 weeks in Month 1.

**5 campaign goal options:**
1. Brand awareness
2. Lead generation
3. Product launch
4. Re-engagement
5. Mixed (brand + leads)

---

### `/content-calendar` — Weekly Content Schedule
**Purpose:** Produces a concrete, ready-to-execute content calendar with specific titles, formats, platforms, and CTAs — not vague topic categories.
**Input:** brand.md content pillars + campaign-plan.md + keyword-research.md + trend-monitoring.md.
**Output:** `/strategy/content-calendar.md`

**Content mix per week (4-1-1 rule):**
- 4 pieces — educational / value (no selling)
- 1 piece — proof / social proof (case study, review, result)
- 1 piece — promotional / CTA (offer, booking, lead magnet)

**Per content piece specifies:**
- Date / week
- Platform (Facebook / TikTok / Blog / Zalo / Email)
- Content type (story post / hook video / long-form blog / carousel)
- Specific title or hook (e.g. "3 lý do da bạn vẫn bị kích ứng dù dùng sản phẩm đắt tiền")
- Content pillar from brand.md Section 12
- Keyword target (for blog/SEO pieces)
- Goal (awareness / trust / leads / conversion)
- CTA

**Time period options:**
- 2 weeks (most detailed, ready to execute immediately)
- 1 month (4 weeks overview + detailed weeks 1–2)
- 3 months (aligned to campaign plan)

---

### `/lead-magnet` — Lead Capture Concepts
**Purpose:** Designs 3 lead magnet concepts at different funnel stages to attract qualified buyers and move them toward the core offer.
**Input:** brand.md ICP pain points + core offer + content pillars + keyword PAA questions.
**Output:** `/strategy/lead-magnets.md`

**3 concepts at different funnel stages:**
| Concept | Funnel Stage | Audience | Volume |
|---|---|---|---|
| 1 | Top of funnel | Broad, problem-aware | High volume, lower intent |
| 2 | Middle of funnel | Considering solutions | Medium volume, qualified |
| 3 | Bottom of funnel | Ready to buy | Low volume, highest intent |

**Best performing formats for Vietnam:**
1. Calculator / quiz — personalized result ("Chi phí thật của bạn là...")
2. Checklist — quick scan, immediate value
3. Template — copy-paste ready
4. Mini video / screen-record — show don't tell
5. Cheat sheet — condensed 1-page reference
6. Free consultation / audit — highest intent, for high-ticket offers

**Each concept defines:**
- Specific name (benefit-driven, not "Free Guide")
- Format
- Problem it solves (in ICP's language)
- What's inside (3–5 bullets)
- The "aha" moment that makes paid offer feel obvious
- Delivery method (Zalo / email / direct download)
- CTA to paid offer

---

### `/campaign-brief` — Execution Brief
**Purpose:** Packages all strategy decisions into one structured brief that every execution agent reads before creating content for a specific campaign.
**Input:** brand.md + campaign-plan.md + content-calendar.md + lead-magnets.md + offer-positioning.md.
**Output:** `/strategy/campaign-brief-[campaign-name].md`

**8 components of a campaign brief:**
1. Campaign overview (name, goal, duration, budget)
2. The offer (what, price, incentive, deadline, guarantee)
3. Target audience (segment, funnel stage, pain point, objection)
4. Core message (headline, tone, what NOT to say)
5. Proof points (stats, testimonials, strongest single closer)
6. Content direction (3 hook angles, emotional arc, CTAs by stage)
7. Platform-specific instructions (Facebook / TikTok / Zalo / Email)
8. Success metrics (primary KPI, secondary metrics, review checkpoint)

**This is the file execution agents read.** When `/blog-writer`, `/social-copy`, or `/email-sequence` runs — they read this brief first to stay on-message.

---

## Recommended Sequence

```
/offer-positioning → /campaign-planning → /content-calendar → /lead-magnet → /campaign-brief
```

Run offer-positioning first — all other plans are built around a sharp offer.

## Individual Skill Use

Any skill can run standalone:
- Offer changed? Re-run `/offer-positioning` only
- New month starting? Re-run `/content-calendar` only
- New campaign launching? Run `/campaign-brief` with new campaign details

---

## No APIs Required

Strategy Agent runs entirely on Claude reasoning. No keys, no external calls.

| Input source | Where it comes from |
|---|---|
| Brand context | `/profiles-output/brand.md` |
| Market data | `/research/market-research.md` |
| Competitor gaps | `/research/competitor-analysis.md` |
| Keyword targets | `/research/keyword-research.md` |
| Trend angles | `/research/trend-monitoring.md` |

---

## Key Rules

1. **Always grounded in brand.md** — no generic advice, everything references brand voice, ICP, positioning.
2. **Specific over vague** — content calendar entries have real titles, not "post about X."
3. **Measurable targets only** — every plan has a KPI, not "increase engagement."
4. **Campaign brief is the handoff** — execution agents don't read the full strategy, they read the brief.
5. **No APIs needed** — fastest agent to run, can produce output in one session with no setup.
