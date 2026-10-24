# Agent 12 — Sales Enablement Agent
> Deep-dive explanation | Layer 3 — Execution

## What this agent does

The Sales Enablement Agent produces everything needed to close deals — from the long-form sales page prospects read before deciding, to the customized proposal that lands in their inbox after a discovery call, to the objection responses that unlock stuck conversations.

It covers the full conversion layer: awareness → interest → decision → proof → close.

---

## 5 Skills

### 1. `/sales-page` — Long-Form Sales Page
**What it does:** Writes a complete 12-section sales page — pre-headline qualifier through final CTA — designed to handle every objection before the prospect raises it.

**Different from a landing page:** Landing pages (CRO Agent) are short, single-focus, designed for cold paid traffic. Sales pages are longer, deeper, designed for warm traffic that needs to be fully convinced. They speak to someone who is interested but not yet ready to buy.

**The 12 sections:** Pre-headline qualifier → Headline → Sub-headline → The stakes (cost of inaction) → Problem (symptoms they live with) → Why existing solutions fail → The offer → How it works (3 steps) → What's included → Proof → FAQ/objections → CTA with guarantee.

**Price anchoring is mandatory:** Every sales page includes a price comparison — against the cost of the alternative (agency monthly × 12 months), the cost of doing nothing, or the value of the outcome. Vietnamese buyers need this frame before they can evaluate the price.

**Output:** `/outputs/assets/sales/sales-page-[slug].md`

---

### 2. `/proposal-writer` — Customized Proposals
**What it does:** Writes a 7-section customized proposal for a specific prospect — reflecting back their exact situation from the discovery call, recommending one package with clear reasoning, stating the guarantee, and specifying next steps.

**The mirror principle:** The most powerful thing a proposal can do is prove you were listening. The "Understanding their situation" section uses the prospect's exact words and pain points from the discovery call. When they read it and think "this is exactly what I said" — trust is established.

**One recommendation, not a menu:** Most proposals list all options and let the prospect choose. This creates decision paralysis and signals you don't know what's right for them. This skill recommends one package and explains why it fits their specific situation.

**Valid until date:** Every proposal includes a "Hiệu lực đến" date (14 days). This creates real urgency — not fake scarcity.

**Output:** `/outputs/assets/sales/proposal-[prospect-slug].md`

---

### 3. `/objection-handler` — ACCA Objection Responses
**What it does:** Writes responses to 7 universal B2B sales objections for email, Zalo, and call contexts — with a quick-reference cheat sheet.

**The ACCA framework:** Acknowledge → Clarify → Counter → Ask. The Clarify step is what separates good objection handling from bad. "Giá cao quá" almost never means the price is literally too high — it means ROI isn't clear enough. Asking one clarifying question surfaces the real block.

**7 objections covered:** Price too high / Need to think / Already using competitor / No budget / AI doesn't fit our industry / Already tried AI, didn't work / Can do it ourselves.

**Three formats per objection:** Email (3–5 sentences), Zalo (2–3 sentences, conversational), call script (spoken format with pause notes). Different situations require different response styles.

**Vietnamese cultural specifics:** Vietnamese buyers rarely say "no" directly. "Để xem xét" has multiple meanings — the skill helps distinguish between genuine consideration, soft no, and "need to consult someone." Different responses for each.

**Output:** `/outputs/assets/sales/objection-handler.md`

---

### 4. `/case-study` — Before/After Stories
**What it does:** Writes case studies in three formats — full version (600–900 words), short version (300–400 words for sales pages and email), and quote card (50 words for social and ads).

**Specificity is credibility:** "Tiết kiệm thời gian đáng kể" is not a case study. "Từ 3 giờ/ngày xuống 45 phút/tuần — đo trong 30 ngày đầu" is a case study. The skill enforces specificity at every section.

**The 5-question interview framework:** The skill includes the exact questions to ask the client to extract a strong case study: before state, initial hesitation (counters future objections), specific results, who they'd recommend it to, and unexpected benefits. Question 2 (their hesitation) and question 5 (unexpected benefit) consistently produce the most powerful quotes.

**Vietnamese privacy norms:** Many Vietnamese business owners prefer anonymity. The skill defaults to first name + industry + city (e.g., "Minh Tuấn, Co-founder SaaS B2B, TPHCM") rather than full company name — higher permission rate, still credible.

**Output:** `/outputs/assets/sales/case-study-[slug].md`

---

### 5. `/testimonial-framework` — Proof Collection System
**What it does:** Builds the complete system for collecting, formatting, and deploying testimonials — collection timing, request message templates, 5-question interview, formatting standards, deployment map, and objection-to-testimonial mapping.

**Why timing matters:** The best moment to ask for a testimonial is right after a client milestone — when they're feeling the win. Not immediately after purchase (no results yet). Not months later (momentum is gone). The skill defines the exact trigger moments for each offer type.

**The 5-question interview:** Structured to extract: the before state (specific), their initial hesitation (counters future objections), specific results (credibility), who they'd recommend it to (qualification signal), and unexpected benefits (the most authentic element).

**Deployment map:** Each testimonial is mapped to the funnel stage where it does the most work — result-focused testimonials for awareness (social, ads), process testimonials for consideration (sales page), outcome + quote for decision (proposal, closing email).

**Objection-to-testimonial mapping:** For each of the 7 universal objections, the framework specifies what kind of testimonial counters it and where to place it. "Giá cao" objection → ROI testimonial → FAQ section of sales page.

**Output:** `/outputs/assets/sales/testimonial-framework.md`

---

## No APIs Required

Agent 12 is a pure writing agent. All sales assets are produced from brand context and prospect details provided inline.

---

## Layer Position and Data Flow

```
brand.md (L1) ──────────────────────────┐
offer-positioning.md (L2) ──────────────┤
Discovery call notes (user input) ───────┤──→ Agent 12 Sales ──→ /assets/sales/
Case studies + testimonials (L3 output) ─┘
                                                    ↓
                                        Prospect closes / pays
                                                    ↓
                                        Performance Agent (L4)
                                        → tracks revenue and CAC
```

**Key upstream dependency:** Cold Outreach Agent (Agent 11) generates the warm leads. Sales Enablement Agent (Agent 12) closes them. The handoff point is when a prospect replies to outreach and expresses interest.

---

## What This Agent Doesn't Do

- Process payments or manage contracts
- Send proposals automatically (no CRM integration yet)
- Track open rates on proposals
- Write cold outreach (Cold Outreach Agent)
- Write landing pages for paid traffic (CRO Agent)
