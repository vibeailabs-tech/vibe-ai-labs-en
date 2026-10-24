# Sales Page Skill

Your job is to write a complete long-form sales page — the kind that takes a skeptical stranger and walks them all the way to "I want this." Every section earns the next. No filler. No corporate speak. Real copy that sells.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — the entire page must sound like this brand
- ICP and pain points (Section 6) — the page opens by speaking directly to them
- Positioning (Section 7) — the core promise lives here
- USP and proof points (Section 8) — use the before/after transformation and proof points
- Core offer and packages (Section 9) — the offer section is built from this
- Competitor table (Section 10) — for the comparison/differentiation section
- Key messages (Section 11) — the 3 core messages must appear in the page

If `/outputs/strategy/offer-positioning-*.md` exists: read it — use the refined offer structure, guarantee, and value framing.
If `/outputs/strategy/campaign-brief-*.md` exists: read it — use campaign-specific hooks and CTAs.

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified the offer or campaign**
Use their direction. Go to Step 3.

**Path B — No direction provided**
Ask:
"Sales page này cho offer nào?
1. Toàn bộ service (tất cả packages)
2. Một package cụ thể (Starter / Growth / Full System)
3. Campaign đặc biệt (Labor Day / launch offer...)
4. Free consultation funnel (trang thu lead trước)

Và đây là trang dài (1,500–3,000 từ) hay ngắn (800–1,000 từ)?"

Wait for answer before continuing.

## Step 3 — Write the sales page

Use the Halbert copywriting structure — proven for high-ticket B2B sales in Vietnam:

### Section 1 — Headline + Subheadline
The most important part. Must stop the scroll.

**Headline formula options:**
- Pain + promise: "[Pain they feel right now] — [Promise of what changes]"
- Contrast: "[What they have] vs [What they could have]"
- Specific outcome: "[Specific result] trong [specific timeframe] — [risk removal]"
- Bold claim: "[Claim that challenges their current belief]"

Write 3 headline options. Mark the recommended one.

### Section 2 — The Opening Hook (Agitation)
First 150 words must make them feel seen.
- Describe their current situation in their own words
- Agitate the cost of the problem (time, money, emotional toll)
- Show you understand them — not selling yet

### Section 3 — The Turning Point
"Nhưng có một cách khác..."
- Introduce the idea that things don't have to be this way
- Not the product yet — the possibility

### Section 4 — The Mechanism
What makes this different from everything they've tried.
- Name the unique mechanism (from brand.md Section 8)
- Explain HOW it works — in simple, visual terms
- "It works because..." — the logic that makes it believable

### Section 5 — What You Get (The Offer)
Be exhaustive. Buyers need to feel the value before the price.
- List every deliverable with its value
- Use the "if you had to pay separately" framing to stack value
- Timeline: be specific ("Setup hoàn chỉnh trong 7–10 ngày")

### Section 6 — Proof Section
Stack multiple types of proof:
- Market data / stats (from brand.md Section 8)
- Testimonials or case study (if available — if not, use demo description)
- Logic proof: why the mechanism works
- Guarantee: state it in full — specific, measurable, no-questions-asked

### Section 7 — The Price Reveal
Never reveal price without anchoring first.
- Anchor 1: cost of the problem (what they're losing/paying now)
- Anchor 2: cost of alternatives
- Then: "[Brand]: [price] — một lần"
- Installment option if available
- Reframe: "$700 = less than 1 month agency retainer — and you own it forever"

### Section 8 — The Packages
If multiple tiers:
- Present all 3 clearly
- Each: name, who it's for, what's included, price, CTA
- Highlight recommended tier
- Include Labor Day bonus if campaign-specific

### Section 9 — Objection Handling
Address the top 5 objections directly — in a "You might be thinking..." format.
Use objections from brand.md Section 6 and competitor table Section 10.

### Section 10 — The Guarantee
Full guarantee statement — stand-alone section, not buried.
Make it specific: what exactly is guaranteed, by when, what happens if not met.

### Section 11 — Urgency + Scarcity
Only include if real.
- Real scarcity: "Chỉ 5 slots tháng 5 — mỗi setup cần thời gian thật để làm đúng"
- Real deadline: "Bonus hết hạn 1/5/2026"
- Never fake urgency

### Section 12 — Final CTA
- Restate the core promise in one sentence
- State what happens when they click/message
- Remove all remaining risk
- One clear action

### Copy rules
- Vietnamese register: "bạn/mình" throughout
- Specific numbers always: prices, timelines, agent counts, hours saved, % improvement
- Short paragraphs: 2–3 sentences max
- Bold key phrases — scannable for mobile readers
- Never: "giải pháp toàn diện", "đội ngũ chuyên nghiệp", AI hype language
- Yes: "$700 một lần", "16 agents", "tự chạy được hoặc setup lại miễn phí"

## Step 4 — Write output

Save to `/assets/cro/sales-page.md`:

```markdown
# Sales Page — [Brand Name]
> Generated: [date] | Offer: [offer name] | Length: [word count]

---

## HEADLINE OPTIONS
1. [Option 1] ← Recommended
2. [Option 2]
3. [Option 3]

---

## OPENING HOOK
[Full section — ~150 words]

---

## THE TURNING POINT
[Full section]

---

## THE MECHANISM
[Full section — name the system, explain how it works]

---

## WHAT YOU GET
[Full deliverables list with value framing]

---

## PROOF
[Stats + testimonials/demo description + logic proof]

---

## THE PRICE
[Full price reveal with anchoring]

---

## PACKAGES
[All tiers with full details]

---

## OBJECTIONS
[5+ objections handled in "You might be thinking..." format]

---

## GUARANTEE
[Full guarantee statement — standalone]

---

## URGENCY / SCARCITY
[Only if real — deadline and slot count]

---

## FINAL CTA
[Full closing section]

---

## Page Metadata
- Recommended word count: [count]
- Primary keyword: [keyword for SEO if applicable]
- Mobile notes: [any adjustments for mobile]
- A/B test priority: [top element to test first]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Sales page cho [Brand Name] đã hoàn chỉnh.**

**Cấu trúc:**
- Headline (3 options): [preview of recommended]
- Offer presented: [packages or single offer]
- Proof elements: [count]
- Objections handled: [count]
- Guarantee: [guarantee statement summary]
- Word count: ~[count] từ

📁 Đã lưu vào: `/assets/cro/sales-page.md`

**Bước tiếp theo:** Chạy `/page-audit` để score trang vừa viết và tìm điểm cải thiện, hoặc `/ab-test-setup` để test headline options."

---
