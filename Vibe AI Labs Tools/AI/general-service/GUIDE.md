# AI Marketing Agent Team — Complete User Guide

> 16 agents · 43 skills · Full AI-powered marketing automation for Vietnamese businesses

---

## Table of Contents

1. [What This System Is](#1-what-this-system-is)
2. [Before You Start — Requirements](#2-before-you-start--requirements)
3. [Step-by-Step Setup: APIs](#3-step-by-step-setup-apis)
4. [Step-by-Step Setup: MCPs](#4-step-by-step-setup-mcps)
5. [Folder Structure Setup](#5-folder-structure-setup)
6. [How to Use the System](#6-how-to-use-the-system)
7. [All 16 Agents Explained](#7-all-16-agents-explained)
8. [All 43 Skills — Quick Reference](#8-all-43-skills--quick-reference)
9. [Workflow Sequence Reference](#9-workflow-sequence-reference)
10. [Troubleshooting](#10-troubleshooting)

---

## 1. What This System Is

This is a complete AI marketing automation system that runs inside **Claude Code** (Anthropic's CLI tool). It gives you a team of 16 AI agents — each with a specific job — that work together to run your entire marketing operation.

**What it replaces:**
- A brand strategist
- A market researcher
- A content writer
- An SEO specialist
- An email marketer
- A social media manager
- A paid ads specialist
- A video scriptwriter
- A cold outreach specialist
- A sales copywriter
- A distribution coordinator
- A performance analyst

**How it works:**
```
You type one goal in plain language
       ↓
Orchestrator reads it and routes to the right agent
       ↓
Agent runs the right skill and produces output
       ↓
Output saves to /outputs/ folder for your review
       ↓
You approve → content ships
```

The system improves over time: every month, the Feedback Agent reads your performance data and rewrites your brand foundations — so Month 6 output is fundamentally better than Month 1.

---

## 2. Before You Start — Requirements

### What you need to install

| Tool | What it is | Required? |
|---|---|---|
| **Claude Code** | The CLI that runs this system | Yes — the system runs inside it |
| **Node.js** (v18+) | Runtime for MCP servers | Yes — MCPs won't work without it |
| **npx** | Comes with Node.js | Yes |

### Install Claude Code

```bash
npm install -g @anthropic/claude-code
```

Then authenticate:
```bash
claude
```

Follow the login prompts. You need an Anthropic account with Claude Code access.

### Install Node.js (if not already installed)

Download from [nodejs.org](https://nodejs.org) — choose the LTS version.

Verify:
```bash
node --version   # should show v18 or higher
npx --version
```

---

## 3. Step-by-Step Setup: APIs

This system uses several external APIs. Here is exactly how to connect each one.

### API Overview

| API | Used By | Required? | Cost |
|---|---|---|---|
| **OpenRouter** (Perplexity Sonar) | Research Agent | Recommended | Pay-per-use |
| **Firecrawl** | Research Agent | Recommended | Free tier available |
| **SerpAPI** | SEO Agent, Research Agent | Recommended | Free tier (100/month) |
| Perplexity (direct) | Alternative to OpenRouter | Optional | Pay-per-use |
| DataForSEO | SEO Agent (keyword data) | Optional | Pay-per-use |
| Semrush | SEO Agent (competitor gaps) | Optional | Paid |
| Meta Ads | Ads + Performance Agent | Optional | Requires ad account |
| Google Ads | Ads Agent | Optional | Requires ad account |
| GA4 | Performance Agent | Optional | Free |
| Meta Insights | Performance Agent | Optional | Requires page/ad account |
| Mailchimp / Klaviyo | Performance Agent | Optional | Free tier available |

**Start with the first 3** (OpenRouter, Firecrawl, SerpAPI) — they unlock the core Research workflow. Add the others as needed.

---

### 3.1 OpenRouter API (for Perplexity Sonar)

OpenRouter is an API gateway that gives you access to Perplexity's Sonar model (used for live market research and trend monitoring).

**Step 1 — Get your API key:**
1. Go to [openrouter.ai](https://openrouter.ai)
2. Sign up for a free account
3. Click your avatar → **API Keys** → **Create Key**
4. Copy the key (starts with `sk-or-v1-`)

**Step 2 — Add it to your project settings:**

Open `.claude/settings.local.json` in this project and add under `"env"`:

```json
{
  "env": {
    "OPENROUTER_API_KEY": "sk-or-v1-your-key-here"
  }
}
```

**Step 3 — Verify it works:**
```bash
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer YOUR_KEY_HERE" \
  https://openrouter.ai/api/v1/models
```
You should see `200`.

**What it unlocks:** `/market-research` and `/trend-monitoring` skills (live web research via Perplexity Sonar model).

---

### 3.2 Firecrawl API

Firecrawl scrapes competitor websites — turning any URL into clean, structured text the agents can analyze.

**Step 1 — Get your API key:**
1. Go to [firecrawl.dev](https://www.firecrawl.dev)
2. Sign up → go to **Dashboard** → **API Keys**
3. Copy your key (starts with `fc-`)

**Step 2 — Add to `.claude/settings.local.json`:**

```json
{
  "env": {
    "FIRECRAWL_API_KEY": "fc-your-key-here"
  },
  "mcpServers": {
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-your-key-here"
      }
    }
  }
}
```

**Step 3 — Verify:**
```bash
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer YOUR_KEY_HERE" \
  https://api.firecrawl.dev/v1/scrape \
  -X POST -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}'
```
You should see `200`.

**What it unlocks:** `/competitor-analysis` skill — scrapes competitor homepages, extracts headlines, CTAs, pricing, and messaging gaps.

---

### 3.3 SerpAPI

SerpAPI pulls live Google search results — used for keyword research and SEO competitive analysis.

**Step 1 — Get your API key:**
1. Go to [serpapi.com](https://serpapi.com)
2. Sign up → go to **Dashboard** → copy your API key
3. Free plan includes 100 searches/month

**Step 2 — Add to `.claude/settings.local.json`:**

```json
{
  "env": {
    "SERPAPI_KEY": "your-serpapi-key-here"
  }
}
```

**Step 3 — Verify:**
```bash
curl -s -o /dev/null -w "%{http_code}" \
  "https://serpapi.com/account?api_key=YOUR_KEY_HERE"
```
You should see `200`.

**What it unlocks:** `/keyword-research` skill — finds keywords your competitors rank for, keyword volumes, and ranking opportunities.

---

### 3.4 DataForSEO API (Optional)

Provides keyword volume, CPC, and SERP data for Vietnamese market. More detailed than SerpAPI for SEO work.

**Step 1 — Get credentials:**
1. Go to [dataforseo.com](https://dataforseo.com)
2. Sign up → Dashboard gives you a **login** (email) and **password**

**Step 2 — Add to `.claude/settings.local.json`:**

```json
{
  "env": {
    "DATAFORSEO_LOGIN": "your-email@example.com",
    "DATAFORSEO_PASSWORD": "your-dataforseo-password"
  }
}
```

**Step 3 — Verify:**
```bash
curl --user "YOUR_LOGIN:YOUR_PASSWORD" \
  --header "Content-Type: application/json" \
  --data '[{"language_code":"vi","location_code":2704}]' \
  https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live
```
Location code `2704` = Vietnam. You should get a JSON response.

---

### 3.5 Meta Ads API (Optional)

Used by the Ads Agent and Performance Agent for ad creative data and campaign metrics.

**Step 1 — Get your access token:**
1. Go to [developers.facebook.com](https://developers.facebook.com)
2. Create an app → add **Marketing API** product
3. Go to **Tools** → **Graph API Explorer** → generate a User Access Token
4. Required permissions: `ads_read`, `ads_management`

**Step 2 — Add to `.claude/settings.local.json`:**

```json
{
  "env": {
    "META_ACCESS_TOKEN": "your-meta-access-token",
    "META_AD_ACCOUNT_ID": "act_your-account-id"
  }
}
```

---

### 3.6 GA4 API (Optional)

Used by the Performance Agent to pull website traffic and conversion data.

**Step 1 — Enable the API:**
1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a project → enable **Google Analytics Data API**
3. Create a **Service Account** → download the JSON key file
4. In GA4, go to **Admin** → **Account Access Management** → add the service account email with Viewer role

**Step 2 — Add to `.claude/settings.local.json`:**

```json
{
  "env": {
    "GA4_PROPERTY_ID": "your-ga4-property-id",
    "GOOGLE_APPLICATION_CREDENTIALS": "/path/to/your/service-account-key.json"
  }
}
```

---

### 3.7 Mailchimp API (Optional)

Used by the Performance Agent to pull email open rates, click rates, and revenue data.

**Step 1 — Get your API key:**
1. Log into Mailchimp → click your avatar → **Profile**
2. Go to **Extras** → **API Keys** → **Create A Key**

**Step 2 — Add to `.claude/settings.local.json`:**

```json
{
  "env": {
    "MAILCHIMP_API_KEY": "your-key-here",
    "MAILCHIMP_SERVER_PREFIX": "us1"
  }
}
```

The server prefix is the part before `.api.mailchimp.com` in your API calls (e.g., `us1`, `us6`).

---

## 4. Step-by-Step Setup: MCPs

MCPs (Model Context Protocol servers) give agents tools beyond text generation — like browser control, website scraping, and image generation. They run as local processes that Claude Code connects to.

### MCP Overview

| MCP | Used By | Required? |
|---|---|---|
| **Firecrawl MCP** | Research Agent | Recommended |
| **Playwright MCP** | Research Agent | Recommended |
| Glif MCP | Video & Creative Agent | Optional |

---

### 4.1 Firecrawl MCP

Already covered in Section 3.2 — the `mcpServers` entry in `settings.local.json` is all you need.

**Verify it's loaded:**

Start Claude Code in this project folder and type:
```
/mcp
```
You should see `firecrawl-mcp` listed as connected.

---

### 4.2 Playwright MCP

Playwright gives the Research Agent a real browser — it can visit competitor websites, take screenshots, and see pages exactly as a user would.

**Step 1 — Add to `.claude/settings.local.json`:**

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

**Step 2 — Install browser binaries** (first time only):
```bash
npx playwright install chromium
```

**Step 3 — Verify:**

Start Claude Code and type `/mcp` — you should see `playwright` listed.

**What it unlocks:** The `/competitor-analysis` skill can now take actual screenshots of competitor pages — visual evidence of their design, layout, and above-the-fold messaging.

---

### 4.3 Glif MCP (Optional)

Glif generates images and video assets. Used by the Video & Creative Agent to produce actual visual assets (not just briefs).

**Step 1 — Get your Glif API key:**
1. Go to [glif.app](https://glif.app)
2. Sign up → go to Settings → API Keys

**Step 2 — Add to `.claude/settings.local.json`:**

```json
{
  "mcpServers": {
    "glif": {
      "command": "npx",
      "args": ["-y", "@glifxyz/glif-mcp-server"],
      "env": {
        "GLIF_API_TOKEN": "your-glif-token-here"
      }
    }
  }
}
```

---

### Full `settings.local.json` Example

Here is a complete example with all connections filled in:

```json
{
  "env": {
    "OPENROUTER_API_KEY": "sk-or-v1-your-key",
    "FIRECRAWL_API_KEY": "fc-your-key",
    "SERPAPI_KEY": "your-serpapi-key",
    "DATAFORSEO_LOGIN": "your@email.com",
    "DATAFORSEO_PASSWORD": "your-password",
    "META_ACCESS_TOKEN": "your-meta-token",
    "META_AD_ACCOUNT_ID": "act_123456",
    "GA4_PROPERTY_ID": "123456789",
    "MAILCHIMP_API_KEY": "your-mailchimp-key",
    "MAILCHIMP_SERVER_PREFIX": "us1"
  },
  "mcpServers": {
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-your-key"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "glif": {
      "command": "npx",
      "args": ["-y", "@glifxyz/glif-mcp-server"],
      "env": {
        "GLIF_API_TOKEN": "your-glif-token"
      }
    }
  }
}
```

---

## 5. Folder Structure Setup

When you first use the system, create the output folders. Run this once from the project root:

```bash
mkdir -p outputs/profiles-output
mkdir -p outputs/research
mkdir -p outputs/strategy
mkdir -p outputs/assets/content
mkdir -p outputs/assets/seo
mkdir -p outputs/assets/email
mkdir -p outputs/assets/social
mkdir -p outputs/assets/ads
mkdir -p outputs/assets/creative
mkdir -p outputs/assets/outreach
mkdir -p outputs/assets/sales
mkdir -p outputs/assets/cro
mkdir -p outputs/distribution
mkdir -p outputs/performance
```

Every agent reads from and writes to these fixed paths. Do not rename or move them.

---

## 6. How to Use the System

### Starting Claude Code

From the project root folder:
```bash
claude
```

This opens the Claude Code chat interface with all 16 agents and 43 skills available.

### Two ways to work

**Option A — Let the Orchestrator decide**

Just tell it what you want in plain language:
```
"I want to start marketing my business"
"What should I do next?"
"Build me a full marketing campaign"
"Write a blog post about [topic]"
```

The Orchestrator reads your goal, checks what's already been done, and routes to the right agent.

**Option B — Run a specific skill directly**

Type the slash command:
```
/brand-setup
/market-research
/blog-writer
/social-copy
/email-sequence
```

### The mandatory first step

**Before anything else runs, you must have a `brand.md` file.**

Run `/brand-setup` on day one. It will ask you 18 questions about your business and build the complete brand profile that every other agent reads. This takes 10–20 minutes and you only do it once.

### The recommended workflow order

```
1. /brand-setup          → builds your brand profile (do this once)
2. /market-research      → understand your market
3. /competitor-analysis  → see what competitors are doing
4. /keyword-research     → find what customers search for
5. /campaign-planning    → build your 90-day plan
6. /campaign-brief       → structured brief for execution agents
7. /content-calendar     → 30-day posting plan
8. /blog-writer          → write content
9. /social-copy          → adapt content for social
10. /email-sequence      → set up email nurture
11. /ad-copy             → write paid ads
12. /content-atomizer    → distribute everything
13. /weekly-report       → track what's working
14. /audience-update     → improve based on real data (monthly)
```

### Review everything before it ships

All outputs save to `/outputs/`. Nothing publishes automatically. Read each output, make edits if needed, then approve. **The system proposes. You decide.**

---

## 7. All 16 Agents Explained

---

### LAYER 1 — FOUNDATION

---

### Agent 1 — Brand Foundation Agent

**What it does:** Builds the master context file (`brand.md`) that every other agent reads. Extracts your brand voice, defines your target audience, sets your competitive positioning, and writes your USP. This is the starting point — no other agent runs without this file.

**When to use:** Day one with a new client. Also run it when the brand needs a complete reset.

**Skills:**

#### `/brand-setup` — Master Onboarding
The full brand foundation in one smooth conversation. Asks you 18 questions covering voice, audience, positioning, and USP — then builds all 12 sections of `brand.md` at once. Run this first, always.

#### `/brand-voice`
Defines how your brand sounds. Extracts personality traits, tone of voice, vocabulary choices, words to use and avoid, and writing style. Adapts voice guidelines per platform (Facebook vs LinkedIn vs TikTok). Output: Section 1–5 of `brand.md`.

#### `/audience-profile`
Builds your Ideal Customer Profile (ICP). Covers demographics, psychographics, top pain points, buying triggers, objections, and online behavior. Creates a named, real-feeling persona. Output: Section 6 and 12 of `brand.md`.

#### `/positioning`
Defines where you sit in the market relative to competitors. Writes your positioning statement using the formula: *"For [audience], [brand] is the only [category] that [benefit] — unlike [competitors] who [weakness]."* Output: Sections 7, 9, 10 of `brand.md`.

#### `/USP-definition`
Defines your Unique Selling Point — your unique mechanism, the before/after transformation you create, and your proof points. Writes 5 headline directions and 3 key messages the brand always returns to. Output: Sections 8 and 11 of `brand.md`.

---

### Agent 2 — Research Agent

**What it does:** Pulls live, real-world intelligence from external sources — market data, competitor analysis, keyword research, and trend monitoring. Everything is live; nothing is guessed from training data.

**When to use:** After brand setup, before building any strategy. Also run monthly to stay current.

**APIs used:** OpenRouter (Perplexity Sonar), Firecrawl MCP, Playwright MCP, SerpAPI

**Skills:**

#### `/market-research`
Runs live queries via Perplexity Sonar to pull: market size, growth rate, consumer behavior patterns, geographic dynamics, market gaps, and opportunities. Produces a structured market research report saved to `/outputs/research/market-research.md`.

#### `/competitor-analysis`
Uses Firecrawl to scrape competitor websites and Playwright to screenshot them. Extracts each competitor's headline, core message, CTA, pricing, features, and social proof. Then identifies the messaging gaps — what none of them are saying, which is your opportunity. Output: `/outputs/research/competitor-analysis.md` + screenshots.

#### `/keyword-research`
Uses SerpAPI to pull real Google search data. Finds keywords your competitors rank for, keyword volumes, difficulty, and quick-win opportunities. Organizes into awareness / consideration / conversion / local SEO tiers. Output: `/outputs/research/keyword-research.md`.

#### `/trend-monitoring`
Runs live Perplexity queries to identify emerging trends in your industry right now — new consumer behaviors, platform shifts, content formats gaining traction. Appended to the market research file so strategy stays current.

---

### LAYER 2 — STRATEGY

---

### Agent 3 — Strategy Agent

**What it does:** Reads your brand profile and all research outputs, then builds the go-to-market plan. This is the thinking layer — it produces the briefs and calendars that tell all execution agents what to build and why.

**When to use:** After research is complete. Before writing any content, ads, or emails.

**Skills:**

#### `/campaign-planning`
Builds a full 90-day marketing campaign plan — goals, channels, timeline, budget allocation, and success metrics. Maps activity to your audience's buying journey stages. Output: `/outputs/strategy/campaign-planning.md`.

#### `/content-calendar`
Builds a detailed 30-day content calendar — specific posts planned by day, platform, format, topic, hook, and CTA. Tied to your keyword strategy and campaign goals. Output: `/outputs/strategy/content-calendar.md`.

#### `/lead-magnet`
Creates 3 lead magnet concepts — high-value free offers that convert traffic into email subscribers and bridge to your paid offer. Each concept includes format, title, content outline, and delivery mechanism. Output: `/outputs/strategy/lead-magnet.md`.

#### `/campaign-brief`
Writes the structured campaign brief that all execution agents read before producing any content. One document that tells every agent: the goal, the audience segment, the key message, the offer, the channels, and success criteria. Output: `/outputs/strategy/campaign-brief.md`.

#### `/offer-positioning`
Refines how your core offer is framed and presented — based on competitor gaps and audience insights from research. Produces multiple framing angles, pricing presentation options, and risk-reversal language. Output: `/outputs/strategy/offer-positioning.md`.

---

### Agent 4 — CRO Agent

**What it does:** Conversion Rate Optimization. Takes existing traffic and converts more of it. Audits pages, rewrites CTAs, builds landing pages, and structures A/B tests. Every output comes with reasoning and expected impact.

**When to use:** When you have traffic but it isn't converting. When launching a campaign and need a landing page. When CTAs feel generic.

**Skills:**

#### `/lp-builder`
Writes a complete landing page — hero section, problem statement, solution, social proof, offer details, FAQ, and CTA. Not a template. Actual copy ready to publish. Output: `/outputs/assets/cro/landing-page.md`.

#### `/cta-optimization`
Rewrites weak, generic CTAs into high-converting calls-to-action grounded in psychology and intent matching. Produces 5+ variants per CTA with reasoning for each. Output: `/outputs/assets/cro/cta-variants.md`.

#### `/ab-test-setup`
Designs structured A/B tests — one variable at a time. Defines hypothesis, variants, sample size needed, duration, and winner condition. Works for headlines, CTAs, subject lines, or landing page sections. Output: `/outputs/assets/cro/ab-test-plan.md`.

#### `/page-audit`
Scores an existing page against conversion principles. Delivers a prioritized list of specific fixes with expected impact ranked high/medium/low. Not vague recommendations — exact changes. Output: `/outputs/assets/cro/page-audit.md`.

#### `/sales-page`
Writes a complete long-form sales page — the kind that takes a skeptical visitor and walks them to "I want this." Handles every objection before the reader raises it. Longer and deeper than a landing page. Output: `/outputs/assets/cro/sales-page.md`.

---

### LAYER 3 — EXECUTION

---

### Agent 5 — Content Agent

**What it does:** Writes all long-form content. Every output is in your brand's voice (read from `brand.md`) and aligned to your campaign strategy. Self-scores outputs before delivering. No filler content — every piece has a purpose.

**When to use:** When you need blog posts, case studies, website copy, or thought leadership articles.

**Skills:**

#### `/content-brief`
Writes a research-backed brief before any content is created. Covers: target keyword, audience intent, content goal, outline, competitor comparison, and success criteria. Ensures every piece of content earns its place before a word is written. Output: `/outputs/assets/content/brief-[topic].md`.

#### `/blog-writer`
Writes a complete, publish-ready blog post — SEO-optimized, brand-voice-accurate, 800–2,000 words. Structured with proper H2/H3 hierarchy, internal link suggestions, and meta description. Output: `/outputs/assets/content/blog-[topic].md`.

#### `/case-study-writer`
Writes structured customer success stories with specific before/after numbers. Not a vague testimonial — a real proof document with the client situation, challenge, solution, and measurable results. Output: `/outputs/assets/content/case-study-[client].md`.

#### `/website-copy`
Writes complete website copy — homepage, about page, services page, or any other page. Every section earns its place. Visitor lands, reads, understands, acts. Output: `/outputs/assets/content/website-[page].md`.

#### `/thought-leadership`
Writes opinion articles and industry commentary. Real perspective with a clear point of view — something worth disagreeing with. Positions the brand as the sharpest voice in the space. Output: `/outputs/assets/content/thought-leadership-[topic].md`.

---

### Agent 6 — SEO Agent

**What it does:** Owns search visibility end to end. Keyword strategy, on-page optimization, local SEO, technical audits, and link building. Critical for Vietnamese businesses that rely on Google to be found.

**When to use:** When improving organic search rankings, setting up a new site for SEO, or auditing an existing site.

**APIs used:** SerpAPI (keyword research)

**Skills:**

#### `/keyword-research`
Uses SerpAPI to find keyword opportunities — including gaps competitors rank for that you don't. Organizes into a priority keyword map by volume, difficulty, and intent. Output: `/outputs/assets/seo/keyword-map.md`.

#### `/on-page-seo`
Optimizes a specific page for a target keyword — title tag, meta description, H1/H2 structure, internal linking, image alt text, and content density. Produces exact rewrites, not recommendations. Output: `/outputs/assets/seo/on-page-[page].md`.

#### `/local-seo`
Optimizes for local Vietnamese search — Google Business Profile signals, local keyword targeting, location-specific landing pages, and citation strategy. Essential for brick-and-mortar and service-area businesses. Output: `/outputs/assets/seo/local-seo-plan.md`.

#### `/schema-markup`
Writes valid JSON-LD structured data — FAQ schema, LocalBusiness schema, Review schema, BreadcrumbList — ready to paste into your site's `<head>`. Helps Google display rich results. Output: `/outputs/assets/seo/schema-[page].json`.

#### `/technical-seo-audit`
Audits your site's technical health — crawlability, indexability, page speed signals, Core Web Vitals readiness, redirect chains, and structural issues blocking rankings. Output: `/outputs/assets/seo/technical-audit.md`.

#### `/link-building-strategy`
Builds a realistic link acquisition plan for the Vietnamese market — which sites to target, what outreach angle to use, and ready-to-send outreach templates. Output: `/outputs/assets/seo/link-building-plan.md`.

---

### Agent 7 — Email Agent

**What it does:** Builds and runs all email marketing. Every sequence is structured around awareness levels — it knows the difference between someone who just opted in vs. someone who almost bought. Each email has one job and does it.

**When to use:** Setting up a new email nurture sequence, writing a newsletter, recovering inactive subscribers, or writing transactional emails.

**No APIs required — works out of the box.**

**Skills:**

#### `/email-sequence`
Writes a complete email nurture sequence — 5–7 emails from first contact to conversion. Structured as DELIVER → CONNECT → VALUE → BRIDGE → PITCH. Every email has one job and a clear next step. Output: `/outputs/assets/email/sequence-[name].md`.

#### `/newsletter`
Writes a single broadcast newsletter — educational and valuable, with a natural CTA. Structured around 9 possible formats (how-to, story, list, opinion, case study, and more). Output: `/outputs/assets/email/newsletter-[date].md`.

#### `/subject-line-ab`
Writes 5–10 subject line variants for a single email with clear hypotheses about why each variant should win. Includes a framework for picking the winner after testing. Output: `/outputs/assets/email/subject-lines-[email].md`.

#### `/re-engagement`
Writes a win-back sequence for inactive subscribers or lapsed customers — 3–5 emails with escalating reasons to re-engage, ending with a clean list removal. No passive "we miss you" emails. Output: `/outputs/assets/email/re-engagement-[segment].md`.

#### `/transactional-email`
Writes order confirmations, receipts, onboarding triggers, and notifications. Transforms routine transactional emails into trust-building moments — the highest-opened email type in any brand's stack. Output: `/outputs/assets/email/transactional-[type].md`.

---

### Agent 8 — Social Media Agent

**What it does:** Creates platform-native content for every major channel. Knows that LinkedIn posts are not Facebook posts are not TikTok captions. Format, length, hook strategy, and tone tuned per platform. Built for Vietnamese platforms including Zalo.

**When to use:** Writing social posts, planning a content calendar, scripting short videos, briefing visual content, or managing community replies.

**No APIs required — works out of the box.**

**Skills:**

#### `/social-copy`
Takes one topic and produces platform-specific posts for Facebook, TikTok, Zalo, and LinkedIn. One input, four outputs — each written natively for that platform's format and audience behavior. Output: `/outputs/assets/social/posts-[topic].md`.

#### `/social-creative`
Writes creative direction briefs for social visuals — what to shoot, what to design, what text overlay to use, and what the visual must communicate. Production-ready brief for a designer or videographer. Output: `/outputs/assets/social/creative-brief-[post].md`.

#### `/hashtag-research`
Finds the right hashtag clusters per platform — Vietnamese-specific, niche-targeted, sized correctly for the brand's reach. Organized by platform and content type. Output: `/outputs/assets/social/hashtag-strategy.md`.

#### `/social-calendar`
Builds a 30-day posting calendar — specific posts planned by day, platform, format, topic, hook, and CTA. Tied to campaign dates and platform best practices for Vietnam. Output: `/outputs/assets/social/calendar-[month].md`.

#### `/community-management`
Writes reply templates for comments, DMs, and negative reviews — so the brand can respond at scale without losing voice. Every template sounds like a real human, not a script. Output: `/outputs/assets/social/community-templates.md`.

#### `/video-script` (short-form)
Writes TikTok and Reels scripts — hook, build, payoff, CTA. Two-column format: spoken word and visual direction on the same line. Creator can shoot without asking follow-up questions. Output: `/outputs/assets/social/video-script-[topic].md`.

---

### Agent 9 — Ads Agent

**What it does:** Writes all paid advertising copy and creative direction. Generates 5–10 variants per concept and structures campaigns for clean testing. Knows Meta algorithm, Google Quality Score, and LinkedIn ad formats.

**When to use:** Launching paid campaigns, writing Facebook/Instagram/TikTok/Google ads, building campaign architecture, or setting up creative tests.

**No APIs required for writing — APIs add performance data later.**

**Skills:**

#### `/ad-creative`
Writes creative direction briefs for paid ad visuals — what to show, what text overlay, what the first frame communicates, and why the creative will stop a scroll. Not the design — the brief that makes production consistent and fast. Output: `/outputs/assets/ads/creative-brief-[campaign].md`.

#### `/ad-copy`
Writes all ad copy components — headlines (30 chars), primary text, descriptions, and CTAs — for Facebook/Instagram, TikTok, and Google Search. Every word tested against: does it make the right person click and the wrong person scroll? Output: `/outputs/assets/ads/copy-[campaign].md`.

#### `/audience-targeting`
Builds the complete targeting strategy for Meta and Google — interest stacking, behavioral layers, lookalike audiences, and cold → warm → hot funnel sequencing. Detailed enough to implement directly in Ads Manager. Output: `/outputs/assets/ads/targeting-[campaign].md`.

#### `/ad-campaign-structure`
Designs the full campaign architecture — campaign level, ad set level, ad level — for Meta and Google. Prevents budget waste, enables clean testing, and makes optimization decisions obvious. Output: `/outputs/assets/ads/campaign-structure-[name].md`.

#### `/ab-test-setup`
Designs A/B tests for paid ads — one variable at a time, with sample size requirements, duration, and clear winner conditions. Prevents testing that wastes budget and teaches nothing. Output: `/outputs/assets/ads/ab-test-[variable].md`.

#### `/google-pmax-brief`
Writes the complete asset brief for Google Performance Max campaigns — all headlines (15), descriptions (4), images, videos, and audience signals. PMax requires more upfront preparation than any other campaign type. Output: `/outputs/assets/ads/pmax-brief-[campaign].md`.

---

### Agent 10 — Video & Creative Agent

**What it does:** Scripts all video content and produces creative direction briefs. The bridge between strategy and visual execution — every output tells a creator or designer exactly what to produce without a follow-up question.

**When to use:** Writing YouTube scripts, Reels/TikTok long-form, UGC scripts, branded decks, or creative briefs for visual assets.

**No APIs required — works out of the box. (Glif MCP adds image generation.)**

**Skills:**

#### `/video-script` (long-form)
Writes complete video scripts for YouTube, Facebook video, TikTok long-form, and website explainer videos. Full two-column format: spoken word and visual direction on the same line, timestamped. Ready to shoot from. Output: `/outputs/assets/creative/video-script-[topic].md`.

#### `/creative-brief`
Writes complete creative briefs for all visual assets — thumbnails, cover images, branded graphics, email headers, and ad creatives. Specific enough that a designer can execute without a single follow-up question. Output: `/outputs/assets/creative/brief-[asset].md`.

#### `/branded-deck`
Writes the complete content for a presentation deck — slide by slide, with headline, body copy, speaker notes, and visual direction per slide. Production-ready for Canva, Figma, or PowerPoint. Output: `/outputs/assets/creative/deck-[name].md`.

#### `/ugc-script`
Writes User Generated Content scripts designed to be performed by customers or creators — not the brand itself. Looks and sounds organic, not like an ad. The most trusted ad format because it feels real. Output: `/outputs/assets/creative/ugc-script-[brief].md`.

---

### Agent 11 — Cold Outreach Agent

**What it does:** Generates new pipeline through direct outreach. Every message is personalized to the specific prospect's situation — not spray and pray. Follow-up sequences and objection responses included.

**When to use:** B2B prospecting, LinkedIn outreach, cold email campaigns, or building a repeatable outreach system.

**No APIs required — works out of the box.**

**Skills:**

#### `/cold-email`
Writes cold outreach emails that get replies — not just opens. Short, specific, and about the prospect. Every word earns its place. Includes 3 variants per prospect type. Output: `/outputs/assets/outreach/cold-email-[segment].md`.

#### `/linkedin-dm`
Writes LinkedIn direct messages — connection request notes (300 chars), opening DMs, and follow-up messages. Shorter and more conversational than cold email. Output: `/outputs/assets/outreach/linkedin-dm-[segment].md`.

#### `/follow-up-sequence`
Writes 5-touch follow-up sequences — what to send after the first outreach gets no reply. Most deals close on follow-up touch 4–6. Most salespeople stop at 1. This sequence closes the gap. Output: `/outputs/assets/outreach/follow-up-[segment].md`.

#### `/objection-handler`
Writes responses to common outreach objections — "not interested," "not the right time," "already using someone else." Acknowledges honestly, then redirects toward finding if there's a real fit. Output: `/outputs/assets/outreach/objections-[segment].md`.

#### `/personalization-framework`
Builds a repeatable system for personalizing outreach at scale — what to research per prospect, where to find it, and how to reference it naturally. Every message feels written specifically for that person, without writing every message from scratch. Output: `/outputs/assets/outreach/personalization-system.md`.

---

### Agent 12 — Sales Enablement Agent

**What it does:** Builds the assets that close deals — from the first conversation to a signed contract. Sales pages, proposals, objection responses, case studies, and testimonial collection systems. Halbert copywriting principles inside.

**When to use:** Closing B2B deals, writing sales pages, building proposals, or creating social proof systems.

**No APIs required — works out of the box.**

**Skills:**

#### `/sales-page`
Writes a complete long-form sales page — headline to order button — designed for warm traffic. Longer and deeper than a landing page. Handles every objection before the reader raises it. Output: `/outputs/assets/sales/sales-page-[offer].md`.

#### `/proposal-writer`
Writes customized sales proposals for specific prospects. Reflects back the prospect's specific situation, shows understanding of their problem, and makes the decision to proceed feel obvious. Output: `/outputs/assets/sales/proposal-[client].md`.

#### `/objection-handler`
Writes responses to sales objections for email, Zalo, and sales calls. Acknowledges, clarifies, counters with evidence, and re-opens the conversation. Not aggressive — consultative. Output: `/outputs/assets/sales/objections-[context].md`.

#### `/case-study`
Writes customer case studies formatted for sales conversations — before/after stories with specific numbers that mirror the prospect's own situation. Turns skeptical prospects into buyers. Output: `/outputs/assets/sales/case-study-[client].md`.

#### `/testimonial-framework`
Builds a complete system for collecting, formatting, and deploying testimonials — interview questions, collection process, formatting templates, and a placement strategy for every stage of the sales funnel. Output: `/outputs/assets/sales/testimonial-system.md`.

---

### Agent 13 — Distribution Agent

**What it does:** Takes any approved content piece and turns it into assets for every channel. One blog post becomes a month of content across 8 platforms. Formatted natively for each — not copy-paste.

**When to use:** After any content piece is approved. Before publishing anything.

**No APIs required — works out of the box.**

**One blog post becomes:**
- LinkedIn: long-form post + carousel + poll
- Instagram: carousel + Reel script + story series
- Facebook: long-form post
- Twitter/X: thread + 3 standalone tweets
- Email: newsletter section + nurture email
- YouTube: script outline + Shorts script
- Google Ads: 3 headlines + 2 descriptions
- TikTok: 30–60 second script

**Skills:**

#### `/content-atomizer`
Takes one long-form piece and breaks it into every smaller asset it contains. A 2,000-word blog post contains at least 10 social posts, 3 email angles, 2 video hooks, and 5 quote cards. This skill finds them all. Output: `/outputs/distribution/atoms-[piece].md`.

#### `/platform-formatter`
Takes any piece of content and formats it correctly for each platform's technical and cultural requirements — character limits, hashtag placement, link handling, and posting conventions. Output: `/outputs/distribution/formatted-[piece].md`.

#### `/press-release`
Writes press releases in journalistic style for Vietnamese media — product launches, milestones, partnerships. Gives editors everything they need to run a story without additional research. Output: `/outputs/distribution/press-release-[topic].md`.

#### `/podcast-pitch`
Writes cold pitches to podcast hosts for the founder to appear as a guest. Shows knowledge of their audience, proposes a specific topic, and makes it easy to say yes. Output: `/outputs/distribution/podcast-pitch-[show].md`.

#### `/partnership-brief`
Writes partnership outreach for co-marketing, referral programs, and content collaborations. Answers one question for the other party: "What's in it for us?" Output: `/outputs/distribution/partnership-brief-[partner].md`.

---

### LAYER 4 — FEEDBACK

---

### Agent 14 — Performance Agent

**What it does:** Reads what actually happened after content ships. Campaign results, open rates, click-throughs, and conversion data. Generates reports in plain language with clear next actions — not a data dump.

**When to use:** End of week (weekly report), end of campaign (campaign report), or end of month (strategy review).

**APIs used (optional):** GA4, Meta Insights, Mailchimp/Klaviyo. Works without them using data you paste in manually.

**Skills:**

#### `/campaign-report`
Writes a complete campaign performance report — what ran, what the numbers say, what worked, what didn't, and exactly what to change next campaign. Decision-ready format. Output: `/outputs/performance/campaign-report-[name].md`.

#### `/weekly-report`
Writes a concise weekly performance summary across all active channels — readable in 5 minutes, with clear next actions for next week. Output: `/outputs/performance/weekly-[date].md`.

#### `/roi-calculator`
Calculates the true return on marketing investment — ties paid ads, content, email, and system costs to actual revenue. Produces a format the business owner can use to make budget decisions. Output: `/outputs/performance/roi-[period].md`.

#### `/data-visualization`
Turns raw marketing data into chart specifications that can be built in Google Sheets or Canva. Describes exactly what each chart should show and how to build it. Output: `/outputs/performance/charts-[report].md`.

#### `/monthly-strategy-review`
Runs the end-of-month review — synthesizes all performance data, compares against strategy goals, and updates strategic direction for next month. The bridge between execution and feedback. Output: `/outputs/performance/monthly-review-[month].md`.

---

### Agent 15 — Feedback Agent

**What it does:** Takes performance data and rewrites the Layer 1 foundations. This is the compounding mechanism — every run, the system gets smarter. The audience profile, messaging, and positioning evolve based on what actually worked. Month 6 output is fundamentally better than Month 1.

**When to use:** Monthly — after Performance Agent has produced at least one monthly review. This is the last step before the cycle resets.

**Skills:**

#### `/audience-update`
Updates the target audience profile in `brand.md` based on who actually converted — not who you thought would. The ICP you built on day one was a hypothesis. Real conversion data is the truth. Output: Updates `brand.md` Section 6.

#### `/messaging-refinement`
Updates key messages and USP based on what's actually resonating — what people click on, respond to, and buy from. Replaces the launch hypothesis with reality. Output: Updates `brand.md` Sections 8 and 11.

#### `/positioning-evolution`
Evaluates whether the brand's market positioning still holds — and updates it if the market has moved, competitors have copied, or a stronger claim is now available. Output: Updates `brand.md` Section 7.

#### `/monthly-strategy-review` (Feedback Layer)
Closes the feedback loop — synthesizes all Feedback Agent updates (audience, messaging, positioning) into one consolidated strategy brief for next month. The last step before the cycle resets at Month Start. Output: `/outputs/performance/strategy-brief-[month+1].md`.

---

### The Orchestrator

**What it does:** Receives your goal in plain language, checks the system state, and routes to the right agent or sequence of agents. Enforces workflow order — no execution agent runs without a brand profile, no strategy runs without research.

**When to use:** When you're not sure what to do next. When you want a full campaign built end-to-end. When you want the system to decide the sequence.

**Just say:** `"What should I do next?"` or describe your goal and the Orchestrator handles the rest.

---

## 8. All 43 Skills — Quick Reference

| Skill Command | Agent | What It Produces |
|---|---|---|
| `/brand-setup` | Brand Foundation | Complete brand.md (all 12 sections) |
| `/brand-voice` | Brand Foundation | Voice, tone, vocabulary guide |
| `/audience-profile` | Brand Foundation | ICP, demographics, pain points |
| `/positioning` | Brand Foundation | Positioning statement, competitive angle |
| `/USP-definition` | Brand Foundation | USP, transformation story, key messages |
| `/market-research` | Research | Market size, trends, opportunities |
| `/competitor-analysis` | Research | Competitor scrape + gap analysis |
| `/keyword-research` | Research / SEO | Keyword map with volumes |
| `/trend-monitoring` | Research | Emerging trends right now |
| `/campaign-planning` | Strategy | 90-day campaign plan |
| `/content-calendar` | Strategy | 30-day posting calendar |
| `/lead-magnet` | Strategy | 3 lead magnet concepts |
| `/campaign-brief` | Strategy | Execution brief for all agents |
| `/offer-positioning` | Strategy | Offer framing and pricing angles |
| `/lp-builder` | CRO | Full landing page copy |
| `/cta-optimization` | CRO | 5+ CTA variants with reasoning |
| `/ab-test-setup` | CRO / Ads | Structured test plan |
| `/page-audit` | CRO | Scored page audit with fixes |
| `/sales-page` | CRO / Sales | Long-form sales page |
| `/content-brief` | Content | Research-backed content brief |
| `/blog-writer` | Content | Complete SEO blog post |
| `/case-study-writer` | Content | Customer success story |
| `/website-copy` | Content | Homepage / page copy |
| `/thought-leadership` | Content | Opinion article |
| `/on-page-seo` | SEO | Page optimization |
| `/local-seo` | SEO | Local search optimization plan |
| `/schema-markup` | SEO | JSON-LD structured data |
| `/technical-seo-audit` | SEO | Technical health audit |
| `/link-building-strategy` | SEO | Link acquisition plan |
| `/email-sequence` | Email | 5–7 email nurture sequence |
| `/newsletter` | Email | Single broadcast newsletter |
| `/subject-line-ab` | Email | Subject line test variants |
| `/re-engagement` | Email | Win-back sequence |
| `/transactional-email` | Email | Confirmation / onboarding emails |
| `/social-copy` | Social | Posts for 4 platforms |
| `/social-creative` | Social | Visual direction briefs |
| `/hashtag-research` | Social | Hashtag clusters per platform |
| `/social-calendar` | Social | 30-day social calendar |
| `/community-management` | Social | Reply templates |
| `/video-script` | Social / Video | TikTok/Reels shooting script |
| `/ad-creative` | Ads | Ad visual direction brief |
| `/ad-copy` | Ads | Headlines, primary text, descriptions |
| `/audience-targeting` | Ads | Meta + Google targeting strategy |
| `/ad-campaign-structure` | Ads | Campaign architecture |
| `/google-pmax-brief` | Ads | Performance Max asset brief |
| `/video-script` | Video & Creative | YouTube / long-form video script |
| `/creative-brief` | Video & Creative | Visual asset production brief |
| `/branded-deck` | Video & Creative | Slide-by-slide deck content |
| `/ugc-script` | Video & Creative | Creator / customer UGC script |
| `/cold-email` | Cold Outreach | Personalized cold emails |
| `/linkedin-dm` | Cold Outreach | LinkedIn connection + DM sequence |
| `/follow-up-sequence` | Cold Outreach | 5-touch follow-up cadence |
| `/objection-handler` | Cold Outreach / Sales | Objection response scripts |
| `/personalization-framework` | Cold Outreach | Outreach personalization system |
| `/proposal-writer` | Sales | Custom client proposal |
| `/case-study` | Sales | Sales-formatted case study |
| `/testimonial-framework` | Sales | Testimonial collection system |
| `/content-atomizer` | Distribution | 1 piece → assets for 8 platforms |
| `/platform-formatter` | Distribution | Platform-ready formatting |
| `/press-release` | Distribution | Journalistic press release |
| `/podcast-pitch` | Distribution | Guest pitch to podcast hosts |
| `/partnership-brief` | Distribution | Co-marketing proposal |
| `/campaign-report` | Performance | Full campaign analysis |
| `/weekly-report` | Performance | 5-minute weekly summary |
| `/roi-calculator` | Performance | Marketing ROI analysis |
| `/data-visualization` | Performance | Chart specs for dashboards |
| `/monthly-strategy-review` | Performance | End-of-month review |
| `/audience-update` | Feedback | Updates brand.md audience section |
| `/messaging-refinement` | Feedback | Updates brand.md key messages |
| `/positioning-evolution` | Feedback | Updates brand.md positioning |
| `/monthly-strategy-review` | Feedback | Strategy brief for next month |

---

## 9. Workflow Sequence Reference

### Full Campaign (first time)

```
Week 1 — Foundation
  Day 1:  /brand-setup
  Day 2:  /market-research
  Day 3:  /competitor-analysis
  Day 4:  /keyword-research
  Day 5:  /trend-monitoring

Week 2 — Strategy
  Day 6:  /campaign-planning
  Day 7:  /campaign-brief
  Day 8:  /content-calendar
  Day 9:  /offer-positioning
  Day 10: /lead-magnet

Week 3 — Assets
  Day 11: /lp-builder         (landing page for campaign)
  Day 12: /email-sequence     (welcome + nurture)
  Day 13: /blog-writer        (SEO article)
  Day 14: /social-copy        (launch posts)
  Day 15: /ad-copy + /ad-campaign-structure

Week 4 — Launch + Distribute
  Day 16: /content-atomizer   (break blog into social assets)
  Day 17: /platform-formatter (finalize per platform)
  Day 18: Review and approve all outputs
  Day 19: Launch

End of Week 1 (after launch):
  /weekly-report

End of Month:
  /campaign-report
  /monthly-strategy-review (Performance)
  /audience-update
  /messaging-refinement
  /monthly-strategy-review (Feedback)
  → System resets smarter for Month 2
```

---

## 10. Troubleshooting

### Agent says "brand.md not found"
Run `/brand-setup` first. No agent runs without this file at `/outputs/profiles-output/brand.md`.

### Market research returns no data
Check that `OPENROUTER_API_KEY` is set in `.claude/settings.local.json`. Test with:
```bash
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer YOUR_KEY" \
  https://openrouter.ai/api/v1/models
```
Should return `200`.

### Competitor analysis fails to scrape
- Check `FIRECRAWL_API_KEY` is correct
- Some sites block scrapers — try the `/about` or `/services` page URL instead of the homepage
- Check the Firecrawl MCP is connected: type `/mcp` in Claude Code

### Playwright screenshots not saving
Run `npx playwright install chromium` to install browser binaries. This is a one-time setup.

### SerpAPI returns no keyword data
Free plan is limited to 100 searches/month. Check your usage at serpapi.com dashboard. If exhausted, DataForSEO is the alternative.

### Output files not being created
Ensure the output folder structure exists. Run the mkdir commands from Section 5.

### MCP not showing in `/mcp` list
Restart Claude Code. MCPs load at startup from `settings.local.json`. If still missing, check for JSON syntax errors in the settings file.

---

*AI Marketing Agent Team — User Guide v1*
*Built on Claude Code + Claude Skills*
