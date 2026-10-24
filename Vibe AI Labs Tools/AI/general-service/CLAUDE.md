# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is an **architecture blueprint**, not a runnable codebase. It contains the design specification for an AI-powered marketing automation system built on Claude Code and Claude Skills. There are no source files, build tools, or test frameworks.

**Key files:**
- [docs/ai-marketing-agent-team.md](docs/ai-marketing-agent-team.md) — The complete system spec (497 lines)
- [docs/brand-foundation-diagram.html](docs/brand-foundation-diagram.html) — Visual diagram of the Brand Foundation Agent
- [agent-explain/](agent-explain/) — Deep-dive documentation for each of the 16 agents

---

## System Architecture

**16 agents + 1 orchestrator, organized into 4 layers:**

| Layer | Agents | Role |
|---|---|---|
| L1 — Foundation | Brand Foundation, Research | Build master context; pull live market intelligence |
| L2 — Strategy | Strategy, CRO | Plan campaigns; optimize conversion |
| L3 — Execution | Content, SEO, Email, Social, Ads, Video & Creative, Cold Outreach, Sales Enablement, Distribution | Produce all marketing assets |
| L4 — Feedback | Performance, Feedback | Read results; rewrite L1 foundations |
| — | Orchestrator | Routes requests; enforces sequence |

**Enforced workflow sequence:**
```
Foundation → Research → Strategy → CRO → Execution → Distribution → Review → Feedback
```

The Orchestrator also supports **single agent mode** — e.g., "write me a blog post" routes directly to the Content Agent, skipping the full workflow.

---

## Key Design Rules

1. **`/profiles-output/brand.md` is the single source of truth.** No agent runs until this file exists. Every skill reads it before executing.
2. **Predictable I/O paths.** Every skill reads from and writes to fixed paths so the next skill in the chain can consume output without transformation.
3. **Human review checkpoint.** All outputs land in a review folder before anything ships. The system proposes; the human decides.
4. **Build the orchestrator last.** Design every skill with orchestrator compatibility from step 1 (Kieran Flanagan's rule).
5. **Feedback loop.** Layer 4 rewrites Layer 1 foundations — system improves over time.

---

## Folder Architecture (when implemented)

```
/profiles-output/          ← brand.md (master file — all agents read this first)
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

---

## External Integrations

| Tool | Type | Agent | Purpose |
|---|---|---|---|
| Perplexity | API | Research | Live market research |
| Firecrawl | MCP | Research | Competitor website scraping |
| Playwright | MCP | Research | Screenshot competitor pages |
| DataForSEO | API | Research + SEO | Keyword data, SERP analysis |
| Semrush | API | SEO | Competitor keyword gap analysis |
| Meta Ads | API | Ads + Performance | Creative data, performance benchmarks |
| Google Ads | API | Ads | Keyword bids, Quality Score |
| GA4 | API | Performance | Website traffic and conversions |
| Meta Insights | API | Performance | Social and ad performance |
| Glif | MCP | Video & Creative | Image and video generation |
| Mailchimp/Klaviyo | API | Performance | Email open/click/revenue data |

---

## 43 Skills by Agent

- **Foundation (4):** brand-voice, audience-profile, positioning, USP-definition
- **Research (4):** market-research, competitor-analysis, trend-monitoring, keyword-research
- **Strategy (5):** campaign-planning, content-calendar, lead-magnet, campaign-brief, offer-positioning
- **CRO (5):** lp-builder, cta-optimization, ab-test-setup, page-audit, sales-page
- **Content (5):** blog-writer, case-study-writer, website-copy, content-brief, thought-leadership
- **SEO (6):** keyword-research, on-page-seo, local-seo, schema-markup, technical-seo-audit, link-building-strategy
- **Email (5):** email-sequence, newsletter, subject-line-ab, re-engagement, transactional-email
- **Social (6):** social-copy, social-creative, hashtag-research, social-calendar, community-management, video-script
- **Ads (6):** ad-creative, ad-copy, audience-targeting, ad-campaign-structure, ab-test-setup, google-pmax-brief
- **Video & Creative (4):** video-script, creative-brief, branded-deck, ugc-script
- **Outreach (5):** cold-email, linkedin-dm, follow-up-sequence, objection-handler, personalization-framework
- **Sales (5):** sales-page, proposal-writer, objection-handler, case-study, testimonial-framework
- **Distribution (5):** content-atomizer, platform-formatter, press-release, podcast-pitch, partnership-brief
- **Performance (5):** campaign-report, weekly-report, roi-calculator, data-visualization, monthly-strategy-review
- **Feedback (4):** audience-update, messaging-refinement, positioning-evolution, monthly-strategy-review

---

## Build Sequence

When implementing this system:

1. Brand Foundation Agent skills
2. Set up folder architecture (all paths must be predictable from day 1)
3. Research Agent + connect Perplexity, Firecrawl, Playwright APIs/MCPs
4. Strategy Agent
5. Execution Agents: Content → SEO → Email → Social → Ads → Video → Outreach → Sales
6. Distribution Agent
7. Performance + Feedback Agents (the compounding loop)
8. Orchestrator last
