# Agent 5 — Content Agent ✅

> AI Marketing Agent Team · Agent 5 of 16

**Purpose:** Produces brand-accurate, publish-ready content — blog posts, case studies, website copy, content briefs, and thought leadership articles. Every output sounds exactly like the brand and serves a specific marketing goal.
**APIs/MCPs required:** None — pure Claude reasoning.
**Prerequisites:** `brand.md` (Agent 1). Research files from Agent 2 and strategy files from Agent 3 improve output quality but are optional.
**Status:** Complete.

---

## Overview

The Content Agent is the primary writing engine of the system. It reads brand.md + research + strategy files, then produces long-form content that builds trust, ranks on Google, and moves prospects through the funnel.

```
brand.md (Agent 1)
       +
/outputs/research/*.md (Agent 2) — optional, improves quality
/outputs/strategy/campaign-brief.md (Agent 3) — optional, aligns to campaign
       ↓
Content Agent
       ↓
/outputs/assets/content/briefs/
/outputs/assets/content/blog/
/outputs/assets/content/case-studies/
/outputs/assets/content/website/
/outputs/assets/content/thought-leadership/
       ↓
Social Agent (Agent 8) — atomizes content into platform posts
Distribution Agent (Agent 13) — formats and distributes
```

---

## 5 Skills

### `/content-brief` — Brief Before You Write
**Purpose:** Creates a research-backed content brief — keyword strategy, article structure, key argument, proof points — before any writing starts. Prevents rewrites.
**Input:** brand.md + keyword or topic from user.
**Output:** `/outputs/assets/content/briefs/[slug]-brief.md`

**10 brief components:**
| Component | What it defines |
|---|---|
| Content goal | SEO / awareness / consideration / thought leadership |
| Target reader | Specific person, situation, what they already know |
| Keyword strategy | Primary + secondary keywords, search intent, difficulty |
| Headline options | 3 options — SEO / curiosity / outcome angles |
| Key argument | One sentence: what this piece proves |
| Article structure | H2s with specific subheading copy + evidence per section |
| Proof points | Stats, examples, comparisons to use |
| What NOT to include | Topics and framing to avoid |
| SEO checklist | Keyword placement, meta description, internal links |
| CTA | One specific action after reading |

**Rule:** Always run `/content-brief` before `/blog-writer` for important pieces. A 10-minute brief prevents a 2-hour rewrite.

---

### `/blog-writer` — SEO Blog Posts
**Purpose:** Writes complete, publish-ready blog posts — SEO-optimized, brand-voice-accurate, genuinely useful.
**Input:** brand.md + content brief (if exists) or topic + keyword from user.
**Output:** `/outputs/assets/content/blog/[slug].md`

**Post structure:**
| Section | Purpose |
|---|---|
| Opening hook (100–150 words) | First sentence earns the second — bold claim, specific story, surprising stat |
| Body H2s (4–6 sections) | Each makes one point, one argument, one piece of evidence |
| Conclusion (100–150 words) | Restate key argument + one actionable takeaway + CTA |

**SEO requirements enforced:**
- Primary keyword in: H1 title, first 100 words, ≥2 H2s, meta description
- Meta description: 150–160 chars with keyword + benefit
- Internal link suggestions: 2–3 links included
- Image alt text suggestions per section

**Vietnamese writing rules:**
- "bạn/mình" register throughout
- Short paragraphs: 2–4 sentences max
- Specific numbers always: "$700", "16 agents", "3–5 ngày"
- Vietnamese-context examples — not translated English patterns

**Opening rule:** Never open with "Trong bài viết này, mình sẽ..." — start in the middle of the idea.

---

### `/case-study-writer` — Customer Success Stories
**Purpose:** Writes structured before/after client stories that turn skeptical prospects into buyers.
**Input:** brand.md + client details from user (or consent to write composite example).
**Output:** `/outputs/assets/content/case-studies/[slug].md`

**SPSR framework:**
| Section | Content |
|---|---|
| Situation | Who the client is, their marketing situation before, what they'd tried |
| Problem | The specific broken thing, why existing solutions failed |
| Solution | Which package, how setup went (honest including challenges), timeline |
| Result | Specific measurable outcomes, before/after, client quote if available |

**Formats available:**
- Long form (800–1,200 words) — for website, blog, sales conversations
- Short form (300–400 words) — for landing page proof section
- PDF format — for sales calls with sidebar stats

**Honesty rule:** If no real client yet, write a composite example clearly labeled as "representative." Never fabricate quotes or specific metrics.

---

### `/website-copy` — Homepage, About, Services Pages
**Purpose:** Writes complete, conversion-ready website copy for any page.
**Input:** brand.md + page type specified by user.
**Output:** `/outputs/assets/content/website/[page].md`

**Pages covered:**

**Homepage structure (7 sections):**
Hero → Problem → Solution → Social proof bar → Packages preview → About/credibility → Final CTA

**About page structure:**
Opening "why this exists" → Founder story (before/turning point/after) → Methodology → Who it's for + who it's NOT for → CTA

**Services page structure:**
Outcome-focused headline → Each package (who for / included / outcome / price / CTA) → Comparison table → Guarantee → FAQ

**Copy rules:**
- "bạn/mình" throughout — never "quý khách"
- No corporate vocabulary
- Specific numbers everywhere
- One CTA per section
- SEO metadata included for every page

---

### `/thought-leadership` — Opinion Articles & Industry Commentary
**Purpose:** Writes perspective pieces that position the brand as the sharpest, most trustworthy voice in the space. Not content marketing dressed as opinion — real point of view.
**Input:** brand.md + topic/angle from user.
**Output:** `/outputs/assets/content/thought-leadership/[slug].md`

**What makes it thought leadership (not just content):**
- Has a central claim someone can disagree with
- Acknowledges the strongest counterargument — then refutes it
- Can't have the author's name swapped for a competitor and still make sense
- Leaves the reader with a changed perspective, not just new information

**5 article types:**
1. Industry commentary — what everyone is doing wrong
2. Prediction — what's coming that few people see
3. Contrarian take — the opposite of conventional wisdom
4. Lessons from experience — what the founder learned
5. Framework / mental model — a new way to think about a familiar problem

**Formats:**
- Long form (1,000–1,500 words): LinkedIn, blog, Medium
- Short form (400–600 words): Facebook long post, newsletter
- Thread (8–12 points): Facebook/LinkedIn

---

## Recommended Sequence

```
/content-brief → /blog-writer → /thought-leadership → /website-copy → /case-study-writer
```

Brief first always. Website copy and case studies come after blog posts establish voice.

## Individual Skill Use

Any skill runs standalone:
- Need a blog post fast? Run `/blog-writer` directly with topic
- Have a client story? Run `/case-study-writer`
- Need website copy? Run `/website-copy`
- Want to take a position on something? Run `/thought-leadership`

---

## No APIs Required

Content Agent runs entirely on Claude reasoning.

| Input source | Where it comes from |
|---|---|
| Brand voice + audience | `/outputs/profiles-output/brand.md` |
| Keywords and PAA | `/outputs/research/keyword-research.md` |
| Campaign context | `/outputs/strategy/campaign-brief.md` |
| Trend angles | `/outputs/research/trend-monitoring.md` |

---

## Key Rules

1. **Brief before write** — always run `/content-brief` for important pieces
2. **Brand voice non-negotiable** — every output checked against brand.md Section 5
3. **Vietnamese-native** — not translated English; sentence structure and examples must be Vietnamese-context
4. **Never fabricate** — no invented quotes, no made-up stats, no fake client results
5. **One CTA per piece** — never end with competing actions
