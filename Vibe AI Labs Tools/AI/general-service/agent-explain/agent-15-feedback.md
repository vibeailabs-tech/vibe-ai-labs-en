# Agent 15 — Feedback Agent: Deep Dive

## What this agent does

The Feedback Agent closes the loop. Every other agent in the system creates, executes, or measures. The Feedback Agent learns and updates. It takes what the Performance Agent measured and uses it to rewrite the assumptions every other agent runs on — specifically, `brand.md`.

This is the mechanism that makes the system compound over time. Month 1, agents run on guesses. Month 6, agents run on 6 months of real customer data. Month 12, the system understands the audience better than the founder did at launch.

---

## Why this agent exists

Without a feedback loop, every marketing system plateaus. You run campaigns, measure results, note what worked — and then run the same thing again because the foundation documents haven't been updated. The Feedback Agent forces the update to happen systematically, at the right interval (monthly), with the right inputs (performance data + customer language + competitor moves).

---

## Skills (4)

### Skill 1 — Audience Update (`/audience-update`)

**What it does:** Updates Section 6 (Target Audience) and Section 12 (Content Pillars) in brand.md based on who actually buys and what they respond to.

**Input:** Monthly performance review, campaign reports, user observations about customers

**Output:** Updated brand.md Sections 6 + 12 + `/outputs/performance/audience-update-[YYYY-MM].md`

**What it updates:**
- Demographics: if the real buyer is different from the assumed buyer
- Pain points: reordered by conversion performance (highest-converting first)
- Buying triggers: updated with what sales calls revealed
- Objections: updated with what prospects actually push back on
- ICP persona: updated if a different segment is outperforming assumptions
- Online behavior: updated with actual attribution data (where leads really come from)
- Content pillars: reordered/adjusted based on what content topics drove engagement and conversions

**Vietnamese-specific intelligence:**
- Tracks Zalo response patterns (often more revealing of buying intent than social media)
- Notes regional differences (HCM vs Hanoi buyers behave differently)
- Identifies community-based acquisition (which Facebook groups, industry associations drive referrals)

**Safety rule:** Doesn't overwrite core ICP based on one month. Requires 60–90 day pattern before structural changes. New segments are noted as "emerging" until confirmed.

---

### Skill 2 — Messaging Refinement (`/messaging-refinement`)

**What it does:** Updates Section 8 (USP) and Section 11 (Key Messages) in brand.md based on which messages actually drove conversions and what language customers used to describe their own problems.

**Input:** Top and bottom performing content, ad copy, email subject lines; customer language from sales conversations

**Output:** Updated brand.md Sections 8 + 11 + `/outputs/performance/messaging-refinement-[YYYY-MM].md`

**What it updates:**
- USP mechanism name: if a different framing proved more compelling
- Transformation promise: sharpened with real before/after from customers
- Proof points: updated with newest case study data
- Key messages: remove underperformers, add proven messages, reorder by conversion rate

**The customer language mining principle:**
The most valuable messaging data is the exact words customers use — not translated or polished. If a prospect says "mình không biết bắt đầu từ đâu", that phrase goes directly into messaging. Customer language beats founder language every time because it perfectly mirrors how the buyer is thinking.

**4 refinement rules baked in:**
1. Specific beats vague (always)
2. Customer language beats your language
3. Pain before solution (for cold audiences)
4. Proof in the headline, not the footnote

---

### Skill 3 — Positioning Evolution (`/positioning-evolution`)

**What it does:** Evaluates whether the brand's market positioning is still differentiated, credible, and relevant — and updates it if competitors, the market, or the brand's own track record have shifted.

**Input:** Current brand.md, competitor analysis, market research, performance data on which positioning claims converted

**Output:** Updated brand.md Sections 7 + 9 + 10 + `/outputs/performance/positioning-evolution-[YYYY-MM].md`

**4-dimension health check:**
1. Still differentiated? (can competitors make the same claim without changing a word?)
2. Still credible? (does new proof strengthen it, or does missing proof weaken it?)
3. Still relevant? (has the pain it addresses been solved another way, or become more urgent?)
4. Stronger position available? (has 3–6 months of real data revealed a better angle?)

**3 update types:**
- Minor: same position, sharper language (most common)
- Moderate: same territory, new angle (when competitors have copied or market has shifted)
- Major: new position entirely (rare — requires user confirmation before writing)

**Vietnamese dynamics tracked:**
- Competitor copying (common in Vietnamese markets — specific claims get copied faster than in Western markets)
- Community endorsement shifts (who's endorsing who in the industry)
- Category creation opportunities (naming a new category = owning it)

---

### Skill 4 — Monthly Strategy Review (Feedback Layer) (`/monthly-strategy-review`)

**What it does:** The capstone skill. Synthesizes all three update skills plus the Performance Agent's monthly review into next month's campaign brief. Resets the system for the next cycle.

**Input:** All files from the Feedback Agent's other 3 skills + Performance Agent's monthly review

**Output:** `/outputs/strategy/campaign-brief-[YYYY-MM].md` — next month's strategy brief

**What it produces:**
- Month in review (60-second catch-up paragraph)
- Brand foundation status (what changed in brand.md this month)
- Strategic priority for next month (one primary thrust)
- Channel investment table (increase / hold / reduce per channel)
- Content themes with data-backed rationale
- 2 experiments to run (hypothesis + success metric + duration)
- Explicit "what NOT to do" list (as important as the priority list)
- Monthly KPI targets

**The cycle completion mechanism:**
When the monthly strategy review completes, the system is ready to restart:
- brand.md has been updated with this month's learning
- campaign-brief has next month's strategy
- All execution agents will automatically read the updated files on their next run

---

## Workflow position

```
Performance Agent → [YOU] → Resets to Brand Foundation (next cycle)
```

**End-of-month sequence (in order):**
1. Performance Agent runs `/monthly-strategy-review` (measures results)
2. Feedback Agent runs `/audience-update` (updates ICP)
3. Feedback Agent runs `/messaging-refinement` (updates messages)
4. Feedback Agent runs `/positioning-evolution` (updates positioning)
5. Feedback Agent runs `/monthly-strategy-review` (synthesizes + writes next month's brief)
6. System resets — all execution agents now run on updated foundations

---

## The compounding math

| Month | What agents know |
|---|---|
| 1 | Launch assumptions |
| 3 | 3 months of real buyer data |
| 6 | Refined ICP, proven messages, competitive intelligence |
| 12 | Deep audience model — system outperforms any static playbook |

This is why the Feedback Agent is built last but matters most for long-term value. The system doesn't just run — it learns.

---

## What the Feedback Agent never does

- Never updates brand.md based on a single week of data
- Never changes brand voice (Section 5) — that's set by the client and only changes with explicit request
- Never makes a major positioning pivot without user confirmation
- Never writes optimistic updates — if data shows a strategy isn't working, it says so directly
- Never runs the monthly strategy review before the other 3 skills have completed for the month
