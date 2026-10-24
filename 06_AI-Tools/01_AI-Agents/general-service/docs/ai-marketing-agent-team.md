# AI Marketing Agent Team — Full Blueprint

> 16 agents · 43 skills · APIs + MCPs · 1 orchestrator · Complete professional marketing team

---

## HOW IT WORKS

```
YOU (customer)
  → type one goal in plain English
  → review outputs
  → approve before anything ships

ORCHESTRATOR
  → reads your goal
  → detects what's needed
  → routes to the right agents in the right order

LAYER 1 → LAYER 2 → LAYER 3 → DISTRIBUTION → REVIEW → LAYER 4
                                                              ↓
                                              feeds learning back to LAYER 1
```

---

## THE ORCHESTRATOR

**Job:** Receive one plain-English goal. Route to the right agents. Enforce the sequence.

**Sequence it enforces:**
```
Foundation → Research → Strategy → CRO → Execution → Distribution → Review → Feedback
```

**Single agent mode:** If customer types "write me a blog post" — orchestrator skips everything and routes directly to Content Agent only. No full workflow needed for single tasks.

---

## LAYER 1 — FOUNDATION
> Who you are. What you remember. Everything else reads from here.

### Agent 1 — Brand Foundation Agent

**What it does:**
Extracts brand voice, tone, vocabulary. Defines audience profile and ICP. Sets positioning and USP. Writes the master context file that every other agent reads before doing anything.

**Skills inside:**
- `brand-voice` — extracts personality, tone, vocabulary guide, do's and don'ts
- `audience-profile` — demographics, psychographics, pain points, triggers
- `positioning` — competitive positioning, core promise, positioning statement
- `USP-definition` — unique mechanism, transformation, proof, headline direction

**Input:** website URL, existing content samples, basic brief (5 questions)
**Output:** `/profiles-output/brand.md` — the master file

**Key rule:** No other agent runs until this file exists.

---

### Agent 2 — Research Agent

**What it does:**
Pulls live market data, competitor intelligence, keyword gaps, and trend monitoring. Saves structured research files that all downstream agents read from.

**Skills inside:**
- `market-research` — market landscape, size, trends, opportunities
- `competitor-analysis` — competitor positioning, messaging gaps, weaknesses
- `trend-monitoring` — what's happening in the market right now
- `keyword-research` — search demand, keyword gaps, quick win opportunities

**APIs and MCPs:**
- `Perplexity API` — deep market research, real-time information
- `Firecrawl MCP` — scrapes competitor websites at scale
- `Playwright MCP` — screenshots competitor pages, captures visual patterns
- `DataForSEO API` — keyword volume, difficulty, SERP data

**Input:** business type, target audience, list of competitors
**Output:** `/research/market-research.md`, `/research/competitor-gaps.md`, `/research/keyword-strategy.md`

---

## LAYER 2 — STRATEGY
> What to build, when, and for whom.

### Agent 3 — Strategy Agent

**What it does:**
Reads /profiles-output/ + /research/ and builds the go-to-market plan. Creates campaign briefs, 90-day content calendar, offer positioning, and lead magnet concepts. This is the thinking layer before any content is created.

**Skills inside:**
- `campaign-planning` — full campaign structure, goals, channels, timeline
- `content-calendar` — 90-day plan mapped to keywords and audience stages
- `lead-magnet` — high-converting opt-in concepts that bridge to paid offer
- `campaign-brief` — structured brief that all execution agents read from
- `offer-positioning` — how to frame and present the core offer

**Input:** reads from `/profiles-output/brand.md` + `/research/`
**Output:** `/strategy/campaign-brief.md`, `/strategy/content-calendar.md`, `/strategy/lead-magnet.md`

---

### Agent 4 — CRO Agent

**What it does:**
Converts more of the traffic that already exists. Audits pages, redesigns CTAs, writes conversion copy, and structures A/B tests. Every output comes with reasoning and a recommended winner.

**Skills inside:**
- `lp-builder` — full landing page copy, hero, problem, solution, proof, CTA
- `cta-optimization` — rewrites CTAs with psychology and intent matching
- `ab-test-setup` — structured test variants for headlines, CTAs, subject lines
- `page-audit` — scores existing pages, outputs specific improvements
- `sales-page` — long-form sales letter structure, VSL script

**Input:** existing page URLs or copy, campaign brief
**Output:** `/assets/cro/`

---

## LAYER 3 — EXECUTION
> Build all the marketing assets. Eight agents. Each with one job.

### Agent 5 — Content Agent

**What it does:**
Writes all long-form content. Every output reads from brand voice file so it sounds like the client. Ogilvy's research method baked into the methodology. Self-scores output and recommends revisions before delivering.

**Skills inside:**
- `blog-writer` — SEO-optimised blog posts, 800–2000 words
- `case-study-writer` — structured customer success stories for social proof
- `website-copy` — homepage, about, services, product pages
- `content-brief` — structured brief before any writing starts
- `thought-leadership` — opinion articles, industry commentary

**Input:** reads from `/profiles-output/brand.md` + `/strategy/campaign-brief.md`
**Output:** `/assets/content/`

---

### Agent 6 — SEO Agent

**What it does:**
Owns search visibility end to end. Keyword strategy, on-page optimization, technical audit, local SEO setup, and schema markup. Critical for SMBs who rely on Google to be found.

**Skills inside:**
- `keyword-research` — 6 Circles Method, finds gaps competitors miss
- `on-page-seo` — title tags, meta descriptions, headers, internal linking
- `local-seo` — Google Business Profile, local citations, map pack optimization
- `schema-markup` — structured data for rich results
- `technical-seo-audit` — site speed, crawlability, indexing issues
- `link-building-strategy` — outreach plan for backlinks

**APIs:**
- `DataForSEO API` — keyword data, SERP analysis, rank tracking
- `Semrush API` — competitor keyword gaps, backlink analysis

**Input:** website URL, target keywords, competitor list
**Output:** `/assets/seo/`

---

### Agent 7 — Email Agent

**What it does:**
Builds and runs all email marketing. Schwartz awareness levels baked into every sequence. Knows the difference between someone who just opted in vs someone who almost bought. Each email has one job.

**Skills inside:**
- `email-sequence` — welcome, nurture, conversion flows (DELIVER→CONNECT→VALUE→BRIDGE→PITCH)
- `newsletter` — 9 formats for ongoing relationship content
- `subject-line-ab` — dedicated A/B variants for open rate optimization
- `re-engagement` — win-back sequences for cold subscribers
- `transactional-email` — onboarding, confirmation, receipt emails

**Input:** reads from `/profiles-output/brand.md`, trigger event (e.g. lead magnet download)
**Output:** `/assets/email/`

---

### Agent 8 — Social Media Agent

**What it does:**
Creates platform-native content for every major channel. Knows that LinkedIn posts are not Instagram captions are not tweets. Format, tone, length, and hook strategy tuned per platform.

**Skills inside:**
- `social-copy` — platform-specific post copy for LinkedIn, Instagram, Facebook, X, TikTok
- `social-creative` — creative direction for visual posts, carousel frameworks
- `hashtag-research` — platform-specific hashtag strategy
- `social-calendar` — content scheduling across platforms
- `community-management` — response templates, comment reply frameworks
- `video-script` (short) — Reels and TikTok scripts under 60 seconds

**Input:** reads from `/profiles-output/brand.md` + approved content pieces
**Output:** `/assets/social/`

---

### Agent 9 — Ads Agent

**What it does:**
Writes paid advertising copy and creative direction. Generates 5–10 variants per concept and lets testing pick winners. Knows Meta algorithm, Google Quality Score, and LinkedIn ad formats.

**Skills inside:**
- `ad-creative` — creative concept and visual direction brief
- `ad-copy` — headlines, primary text, descriptions per platform
- `audience-targeting` — detailed targeting strategy per platform
- `ad-campaign-structure` — campaign, ad set, budget architecture
- `ab-test-setup` — structured test for each variable
- `google-pmax-brief` — Performance Max asset group strategy

**APIs:**
- `Meta Ads API` — audience data, creative performance benchmarks
- `Google Ads API` — keyword bids, Quality Score data

**Input:** campaign brief, brand foundation file, budget range
**Output:** `/assets/ads/`

---

### Agent 10 — Video & Creative Agent

**What it does:**
Scripts all video content and produces creative direction briefs. Connects to Glif MCP to generate actual images and video assets. The bridge between strategy and visual execution.

**Skills inside:**
- `video-script` — YouTube long-form, Reels, TikTok, YouTube Shorts scripts
- `creative-brief` — detailed brief for designers or AI image generation
- `branded-deck` — pitch decks, proposal decks, investor presentations
- `ugc-script` — user-generated content style scripts for paid social

**MCPs:**
- `Glif MCP` — generates actual images and video assets at scale

**Input:** campaign brief, brand foundation, visual references
**Output:** `/assets/creative/`

---

### Agent 11 — Cold Outreach Agent

**What it does:**
Generates new pipeline through direct outreach. Personalization frameworks baked in — not spray and pray. Every message reads the prospect's situation and adapts. Follow-up sequences included.

**Skills inside:**
- `cold-email` — prospect-specific cold email with proven frameworks
- `linkedin-dm` — LinkedIn direct message sequences
- `follow-up-sequence` — 5-touch follow-up cadence
- `objection-handler` — responses to common sales objections
- `personalization-framework` — how to research and reference each prospect

**Input:** prospect list, ICP from `/profiles-output/brand.md`, offer details
**Output:** `/assets/outreach/`

---

### Agent 12 — Sales Enablement Agent

**What it does:**
Helps the business close deals, not just generate awareness. Builds the assets the sales process needs — from the first conversation to signed contract. Halbert copywriting principles inside.

**Skills inside:**
- `sales-page` — long-form sales letter, VSL script
- `proposal-writer` — professional business proposals for B2B clients
- `objection-handler` — FAQ sections, objection responses for sales pages
- `case-study` — customer success stories formatted for sales conversations
- `testimonial-framework` — how to collect and present social proof

**Input:** offer details, case study interviews, brand foundation file
**Output:** `/assets/sales/`

---

## LAYER 3 — DISTRIBUTION
> One input becomes 16 assets across 8 platforms.

### Agent 13 — Distribution Agent

**What it does:**
Takes any approved content piece and atomizes it. One blog post becomes a month of content across every channel. Formatted natively for each platform — not copy-paste.

**Skills inside:**
- `content-atomizer` — breaks one piece into platform-specific formats
- `platform-formatter` — rewrites for each platform's native style
- `press-release` — news announcements for media coverage
- `podcast-pitch` — outreach to get on relevant podcasts
- `partnership-brief` — collaboration and partnership proposals

**One blog post becomes:**
- LinkedIn: long-form post + carousel + poll
- Instagram: carousel (3–5 slides) + Reel script + story series
- Facebook: long-form post + event if relevant
- Twitter/X: thread + 3 single tweets + quote card
- Email: newsletter section + nurture email
- YouTube: script outline + Shorts script
- Google Ads: 3 headlines + 2 descriptions
- TikTok: 30–60 second script

**Input:** any approved content from `/assets/`
**Output:** `/distribution/`

---

## HUMAN REVIEW CHECKPOINT

> Nothing ships without your eyes on it.

After every agent run, outputs land in a review folder. The customer reads, adjusts if needed, and approves. Only then does content publish, emails send, or ads launch.

This is what separates this system from AI slop. The system proposes. You decide.

---

## LAYER 4 — FEEDBACK
> The system learns and rewrites its own foundations.

### Agent 14 — Performance Agent

**What it does:**
Reads what actually happened after content ships. Campaign results, open rates, click-throughs, conversion data. Generates weekly and monthly reports in plain language. Identifies what worked and what didn't.

**Skills inside:**
- `campaign-report` — full campaign performance summary
- `weekly-report` — automated weekly summary for client review
- `roi-calculator` — ties marketing activity to actual revenue
- `data-visualization` — turns data into readable charts and tables
- `monthly-strategy-review` — formal monthly review document

**APIs:**
- `GA4 API` — website traffic, conversion tracking
- `Meta Insights API` — ad and post performance data
- `Mailchimp / Klaviyo API` — email open rates, click rates, revenue

**Input:** live campaign data, analytics platforms
**Output:** `/performance/reports/`

---

### Agent 15 — Feedback Agent

**What it does:**
Takes performance data and rewrites the Layer 1 foundations. This is the compounding mechanism. Every run, the system gets smarter. Month 6 output is fundamentally better than Month 1 because this agent continuously updates what all other agents read from.

**Skills inside:**
- `audience-update` — sharpens audience profile based on who actually converted
- `messaging-refinement` — updates brand voice based on what resonated
- `positioning-evolution` — adjusts positioning based on competitive performance
- `monthly-strategy-review` — formal review that triggers foundation updates

**Input:** reads from `/performance/`
**Output:** updates `/profiles-output/brand.md` → triggers Layer 1 refresh for all agents

**This is the feedback loop:**
```
Layer 4 (what happened) → rewrites → Layer 1 (who we are)
                                              ↓
                          every downstream agent now runs smarter
```

---

## COMPLETE SYSTEM SUMMARY

### Agents

| # | Agent | Layer | Primary Job |
|---|---|---|---|
| 1 | Brand Foundation | L1 | Build the master context file |
| 2 | Research | L1 | Pull live market intelligence |
| 3 | Strategy | L2 | Plan campaigns and calendar |
| 4 | CRO | L2 | Optimize conversion |
| 5 | Content | L3 | Write long-form content |
| 6 | SEO | L3 | Own search visibility |
| 7 | Email | L3 | Build email sequences |
| 8 | Social Media | L3 | Platform-native social content |
| 9 | Ads | L3 | Paid advertising copy |
| 10 | Video & Creative | L3 | Scripts and visual direction |
| 11 | Cold Outreach | L3 | Direct outreach sequences |
| 12 | Sales Enablement | L3 | Close deals |
| 13 | Distribution | L3 | Atomize content everywhere |
| 14 | Performance | L4 | Read and report results |
| 15 | Feedback | L4 | Rewrite foundations from data |
| + | Orchestrator | All | Route and sequence everything |

**Total: 16 agents + 1 orchestrator**

---

### Skills (43 total)

**Foundation (4):** brand-voice, audience-profile, positioning, USP-definition

**Research (4):** market-research, competitor-analysis, trend-monitoring, keyword-research

**Strategy (5):** campaign-planning, content-calendar, lead-magnet, campaign-brief, offer-positioning

**CRO (5):** lp-builder, cta-optimization, ab-test-setup, page-audit, sales-page

**Content (5):** blog-writer, case-study-writer, website-copy, content-brief, thought-leadership

**SEO (6):** keyword-research, on-page-seo, local-seo, schema-markup, technical-seo-audit, link-building-strategy

**Email (5):** email-sequence, newsletter, subject-line-ab, re-engagement, transactional-email

**Social (6):** social-copy, social-creative, hashtag-research, social-calendar, community-management, video-script

**Ads (6):** ad-creative, ad-copy, audience-targeting, ad-campaign-structure, ab-test-setup, google-pmax-brief

**Video & Creative (4):** video-script, creative-brief, branded-deck, ugc-script

**Outreach (5):** cold-email, linkedin-dm, follow-up-sequence, objection-handler, personalization-framework

**Sales (5):** sales-page, proposal-writer, objection-handler, case-study, testimonial-framework

**Distribution (5):** content-atomizer, platform-formatter, press-release, podcast-pitch, partnership-brief

**Performance (5):** campaign-report, weekly-report, roi-calculator, data-visualization, monthly-strategy-review

**Feedback (4):** audience-update, messaging-refinement, positioning-evolution, monthly-strategy-review

---

### APIs and MCPs

| Tool | Type | Used By | Purpose |
|---|---|---|---|
| Perplexity | API | Research Agent | Live market research |
| Firecrawl | MCP | Research Agent | Competitor website scraping |
| Playwright | MCP | Research Agent | Screenshot competitor pages |
| DataForSEO | API | Research + SEO Agent | Keyword data, SERP analysis |
| Semrush | API | SEO Agent | Competitor gap analysis |
| Meta Ads | API | Ads + Performance Agent | Ad creative, performance data |
| Google Ads | API | Ads Agent | Keyword bids, Quality Score |
| GA4 | API | Performance Agent | Website traffic and conversions |
| Meta Insights | API | Performance Agent | Social and ad performance |
| Glif | MCP | Video & Creative Agent | Image and video generation |

---

### Folder Architecture

```
/profiles-output/          ← brand.md (master file — all agents read this)
/research/          ← market data, keywords, competitor gaps
/strategy/          ← campaign brief, content calendar, lead magnet
/assets/
  /content/         ← blog posts, case studies, website copy
  /seo/             ← keyword maps, schema, audit reports
  /email/           ← sequences, newsletters
  /social/          ← platform posts, calendars
  /ads/             ← ad copy, creative briefs
  /creative/        ← video scripts, decks
  /outreach/        ← cold email, LinkedIn sequences
  /sales/           ← sales pages, proposals
  /cro/             ← landing pages, A/B tests
/distribution/      ← atomized content per platform
/performance/       ← campaign reports, weekly reviews
```

Every skill reads from predictable paths. Every skill writes to predictable paths. When something breaks, you know exactly which layer to fix.

---

### The Compounding Loop

```
Run 1   → brand voice + first draft
Run 5   → + performance data → tighter headlines
Run 20  → + audience feedback → your voice, your patterns

Layer 4 (Feedback) rewrites Layer 1 (Foundation)
Every agent now runs with better context
Month 6 output is fundamentally better than Month 1
```

---

## BUILD SEQUENCE (for development)

```
Step 1  Build Brand Foundation Agent skills
Step 2  Set up folder architecture (all paths predictable from day 1)
Step 3  Build Research Agent + connect Perplexity, Firecrawl, Playwright
Step 4  Build Strategy Agent
Step 5  Build Execution Agents (Content → SEO → Email → Social → Ads)
Step 6  Build Distribution Agent (best demo moment)
Step 7  Build Performance + Feedback Agents (the compounding loop)
Step 8  Build Orchestrator last (but design every skill for it from step 1)
```

**Key rule from Kieran Flanagan:**
> Build the orchestrator last. But design it from the first skill you write.
> Every skill should read from predictable paths, write to predictable paths,
> and produce output that the next skill in the chain can consume without transformation.

---

*AI Marketing Agent Team — Professional Prototype v1*
*Built on Claude Code + Claude Skills*
