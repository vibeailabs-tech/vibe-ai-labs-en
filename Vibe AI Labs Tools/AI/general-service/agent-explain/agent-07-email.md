# Agent 7 — Email Agent
> Layer: 3 (Execution) | Skills: 5 | APIs: None | Output: /outputs/assets/email/

---

## What This Agent Does

The Email Agent writes every type of email a Vietnamese business needs — from automated nurture sequences to single broadcast newsletters to transactional confirmations. It applies brand voice from brand.md to every email, with specific adaptations for Vietnamese mobile reading habits, Zalo integration context, and Vietnamese market timing norms.

No external APIs. Pure Claude reasoning across all 5 skills.

---

## 5 Skills

### Skill 1 — `/email-sequence`
**What it does:** Writes a complete multi-email nurture sequence — welcome, sales, onboarding, or post-purchase. Each email has one job and one CTA.

**Sequence types supported:**
- Welcome sequence (new subscriber → first engagement)
- Lead nurture (cold/warm lead → sales conversation)
- Post-purchase onboarding (new customer → successful user)
- Sales sequence (warm lead → conversion)
- Re-engagement (handled by separate skill)

**Job structure for 5-email sales sequence:**
1. Welcome + expectations
2. Problem education (make them feel understood)
3. Solution introduction (concept, not pitch)
4. Social proof (specific result, not generic testimonial)
5. The offer (clear ask, real urgency, risk-reversal)

**Vietnamese rules enforced:**
- "bạn/mình" register throughout
- Short paragraphs (1–3 sentences)
- Specific numbers over vague claims
- Best send times built into cadence: Tuesday–Thursday, 8–9am or 7–9pm GMT+7
- One CTA per email — never two

**Saves to:** `/outputs/assets/email/email-sequence-[name].md`

---

### Skill 2 — `/newsletter`
**What it does:** Writes a single broadcast newsletter in one of 4 formats — chosen based on what content is available.

**4 formats:**
| Format | When to use | Length |
|---|---|---|
| Insight Letter | Deep take on one idea | 300–500 từ |
| Curation Letter | 3–5 curated items + commentary | 250–400 từ |
| Story Letter | Behind-the-scenes, client situation, personal experience | 400–600 từ |
| Number Letter | Lead with surprising stat, unpack it | 300–450 từ |

**Newsletter vs. sequence difference:**
- Newsletters are broadcast (sent to full list at once)
- Sequences are automated (triggered by user action)
- Newsletter CTAs are softer: "Đọc full", "Reply cho mình biết", not "MUA NGAY"

**Repurpose flag:** Every newsletter output includes a note on whether the content can be atomized into a Facebook post, LinkedIn post, or blog section.

**Saves to:** `/outputs/assets/email/newsletter-[topic].md`

---

### Skill 3 — `/subject-line-ab`
**What it does:** Writes 6 subject line variants for a single email, recommends 2 for A/B testing, and states the winner condition.

**6 angles:**
1. Curiosity gap — leaves something unresolved
2. Specificity — number + outcome + timeframe
3. Direct benefit — state the outcome plainly
4. Question — mirrors reader's internal dialogue
5. Contrarian — challenges a held belief
6. Personal/story — sounds like a human message

**Output per variant:** Subject line + preview text + hypothesis (why this should win)

**Recommended test:** Identifies Control (safest) and Test (riskier, higher upside) variant
**Winner condition:** Open rate gap >5pp after minimum 200 opens per variant

**Vietnamese spam triggers avoided:** "Miễn phí", "Giảm giá X%", "Ưu đãi đặc biệt", "Chỉ hôm nay", all-caps, multiple exclamation marks

**Saves to:** `/outputs/assets/email/subject-line-ab-[email].md`

---

### Skill 4 — `/re-engagement`
**What it does:** 3-email sequence to win back inactive subscribers or lapsed customers — with a sunset policy for non-responders.

**3-email structure:**
- Email 1 — Pattern interrupt: acknowledge inactivity directly, offer value with no ask
- Email 2 — Reason to return: what's new, what's changed, soft invitation
- Email 3 — Honest ask: "Mình sẽ xóa bạn khỏi danh sách sau email này"

**Why Email 3 is a win either way:**
- They engage → active subscriber back
- They don't → list is cleaner, deliverability improves

**Vietnamese market notes:**
- Direct acknowledgment of inactivity outperforms "we miss you" framing
- Zalo alternative offered in Email 3 (many Vietnamese prefer Zalo to email for response)
- Guilt framing doesn't work — frame it as "there's a real reason to return"
- Sunset window: 90–180 days inactive

**Saves to:** `/outputs/assets/email/re-engagement-[segment].md`

---

### Skill 5 — `/transactional-email`
**What it does:** Writes utility emails that are also on-brand — confirmations, receipts, onboarding triggers, booking confirmations, notifications.

**7 types supported:**
1. Order/payment confirmation
2. Welcome/onboarding (highest-read email in any customer relationship)
3. Delivery/fulfillment/access
4. Password reset/account security
5. Appointment/booking confirmation
6. Invoice/receipt (with VAT note for Vietnamese businesses)
7. Trigger-based notification (payment due, expiry, usage milestone)

**Structure every transactional email follows:**
1. Confirmation statement — first 2 lines, no burying
2. Key details — what, when, amount, reference number
3. What happens next — 1–3 bullet points
4. One helpful resource or next step
5. Support info — Zalo number preferred for Vietnamese users
6. On-brand sign-off

**Vietnamese specifics built in:**
- VND amount always shown (even for USD transactions)
- Bank transfer reference field for Vietnamese payment method
- Google Maps link in appointment confirmations
- VAT invoice request note
- Zalo support link > email for fastest response

**Saves to:** `/outputs/assets/email/transactional-[type].md`

---

## No API Requirements

| Skill | External API | Required |
|---|---|---|
| email-sequence | None | — |
| newsletter | None | — |
| subject-line-ab | None | — |
| re-engagement | None | — |
| transactional-email | None | — |

All 5 skills run entirely on Claude reasoning.

---

## Workflow Position

```
Strategy Agent (campaign-brief, lead-magnet)
    ↓
Email Agent (email-sequence → newsletter → subject-line-ab)
    ↓
Distribution Agent (Mailchimp/Klaviyo scheduling)
    ↓
Performance Agent (open rate, click rate, revenue per email)
```

The Performance Agent's data loops back to refine future sequences — which emails got opens, which subjects won A/B tests, which CTAs drove clicks.

---

## Output Files Summary

| File | Skill | Contents |
|---|---|---|
| `email-sequence-[name].md` | `/email-sequence` | Full sequence: subject + preview + body per email, timing, A/B notes |
| `newsletter-[topic].md` | `/newsletter` | Single email: subject + preview + full body, send time, repurpose note |
| `subject-line-ab-[email].md` | `/subject-line-ab` | 6 variants, recommended A/B pair, winner condition |
| `re-engagement-[segment].md` | `/re-engagement` | 3-email sequence, post-sequence actions, sunset policy |
| `transactional-[type].md` | `/transactional-email` | Full email, dynamic fields list, send trigger, VAT note |
