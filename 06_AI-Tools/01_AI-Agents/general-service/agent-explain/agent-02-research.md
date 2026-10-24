# Agent 2 — Research Agent ✅

> AI Marketing Agent Team · Agent 2 of 16

**Purpose:** Pulls live market intelligence — market data, competitor profiles, keywords, and trends — so every downstream strategy and content decision is grounded in real data, not guesses.
**APIs/MCPs required:** OpenRouter (Perplexity Sonar), Firecrawl, SerpAPI, Playwright MCP
**Prerequisite:** `brand.md` must exist (Agent 1 output) — every skill reads it first.
**Status:** Complete and tested.

---

## Overview

The Research Agent is always run after Agent 1. It transforms `brand.md` into live market intelligence by querying real APIs. All 4 outputs feed directly into Agent 3 (Strategy Agent) — the more complete the research, the sharper the strategy.

```
brand.md (Agent 1)
       ↓
Research Agent
       ↓
/research/market-research.md
/research/competitor-analysis.md
/research/keyword-research.md
/research/trend-monitoring.md
       ↓
Strategy Agent (Agent 3)
```

---

## 4 Skills

### `/market-research` — Live Market Intelligence
**Purpose:** Pulls real Vietnam market data — size, growth, customer behavior, and opportunities.
**API:** OpenRouter → Perplexity Sonar (web search model)
**Input:** Reads brand.md for industry, location, target audience. User selects focus (or runs full overview).
**Output:** `/research/market-research.md`

**Runs 2 queries:**
1. Market size + trends — broad industry overview with specific numbers
2. Customer behavior — how this specific target audience makes buying decisions in Vietnam

**Produces:**
- Market size (USD/VND) + CAGR growth rate
- Key market drivers and Vietnam-specific dynamics
- Customer platform preferences (Facebook, TikTok, Zalo)
- Market gaps and underserved segments
- Threats and risks to watch

**4 focus options when no input provided:**
1. Quy mô và tăng trưởng thị trường (market size + growth)
2. Hành vi khách hàng (customer behavior)
3. Cơ hội thị trường (gaps + opportunities)
4. Tất cả (full market overview)

---

### `/competitor-analysis` — Competitor Intelligence
**Purpose:** Scrapes real competitor websites and extracts messaging, offers, CTAs, and weaknesses.
**APIs/MCPs:** Firecrawl (website scraping) + Playwright MCP (screenshots)
**Input:** Competitor URLs — from brand.md Section 10, or user provides them directly.
**Output:** `/research/competitor-analysis.md`

**For each competitor, extracts:**
- Hero headline and value proposition
- Target audience and key offers + pricing
- CTAs and content themes
- Tone (formal/casual, Vietnamese/English)
- Design quality and trust signals (visual analysis via screenshot)
- Strengths and exploitable weaknesses

**Gap analysis produces:**
- Overcrowded positioning angles (avoid these)
- Unclaimed positioning gaps (own these)
- Content topics competitors are ignoring
- Underserved audience segments

**Note on Playwright MCP:** Screenshots only work in Claude Desktop app. In VSCode extension, Firecrawl REST API is used as fallback — same scraping result, no screenshot.

**Path options:**
- Path A: Competitor URLs already in brand.md → scrape immediately
- Path B: Competitor names only → ask user for URLs
- Path C: No competitors identified → ask user to name 2–3

---

### `/keyword-research` — Search Keyword Map
**Purpose:** Finds what real customers are typing into Google — mapped to content opportunities the brand can win.
**API:** SerpAPI (Google autocomplete + SERP data)
**Input:** Reads brand.md for industry, location, competitors, core offer. User selects focus (or full map).
**Output:** `/research/keyword-research.md`

**Runs 4 queries:**
1. Google Autocomplete — seed keywords from brand's core service in Vietnamese
2. Competitor SERP analysis — what terms competitors rank for
3. People Also Ask mining — `related_questions` + `related_searches` fields
4. Local intent — service + city combinations (e.g., "dịch vụ marketing TPHCM")

**Keyword tiers:**
| Tier | Signal words | Priority |
|---|---|---|
| 1 — Buy now | giá, thuê, dịch vụ, chi phí, city name | Highest — convert directly |
| 2 — Comparison | tốt nhất, uy tín, so sánh, review | High — decision stage |
| 3 — Education | cách, làm sao, là gì, hướng dẫn | Medium — build authority |
| 4 — Awareness | broad industry terms | Low — after authority built |

**Also identifies:** Quick win keywords (long-tail, weak competition, brand can rank in 4–8 weeks)

**4 focus options:**
1. Từ khóa khách hàng tìm để mua (buyer intent)
2. Từ khóa đối thủ đang dùng (competitor keywords)
3. Từ khóa nội dung và blog (informational)
4. Tất cả (full keyword map)

---

### `/trend-monitoring` — Live Trend Intelligence
**Purpose:** Surfaces emerging trends in the industry right now — before they're obvious to everyone.
**API:** OpenRouter → Perplexity Sonar (web search model)
**Input:** Reads brand.md for industry, audience, content pillars. User selects focus (or full scan).
**Output:** `/research/trend-monitoring.md`

**Runs 3 queries:**
1. Industry trend scan — new behaviors, platform shifts, regulatory changes, tech shifts in Vietnam
2. Consumer behavior shifts — how target audience is changing in 2025–2026
3. Content + marketing trend scan — what formats are winning, what's losing on Facebook/TikTok/Zalo

**Classifies trends by urgency:**
- 🔴 Act now — trend is peaking, window closing fast
- 🟡 Build toward — trend growing, 3–6 month runway
- 🟢 Watch — early signal, not yet actionable

**Also produces:**
- 2-week content calendar with trend-driven angles
- What's losing momentum (tactics to de-prioritize)
- Specific content angles ready to publish immediately

**4 focus options:**
1. Xu hướng ngành và thị trường (industry trends)
2. Xu hướng hành vi người dùng (consumer behavior)
3. Xu hướng nội dung và marketing (content/marketing trends)
4. Tất cả (full trend scan)

---

## APIs & Keys

| API | Purpose | Key variable |
|---|---|---|
| OpenRouter | Proxy to Perplexity Sonar (web search) | `OPENROUTER_API_KEY` |
| Firecrawl | Competitor website scraping (REST API) | `FIRECRAWL_API_KEY` |
| SerpAPI | Google autocomplete + SERP data | `SERPAPI_KEY` |
| Playwright MCP | Competitor screenshots | No key — MCP config only |

All keys stored in `.claude/settings.local.json` under `env`.

---

## Output Files

| Skill | Output path |
|---|---|
| `/market-research` | `/research/market-research.md` |
| `/competitor-analysis` | `/research/competitor-analysis.md` |
| `/keyword-research` | `/research/keyword-research.md` |
| `/trend-monitoring` | `/research/trend-monitoring.md` |

**Multi-project support:** Skills work without brand.md if user pastes brand data directly. Save outputs to a subfolder (e.g., `/research/bloom-skin-studio/keyword-research.md`) to keep projects separated.

---

## Workflow Paths

**Full research sequence (recommended):**
```
/market-research → /competitor-analysis → /keyword-research → /trend-monitoring
```

**Single skill (refresh specific data):**
```
Run any skill standalone → updates only its own output file
```

**Other project (no brand.md):**
```
User pastes brand info → skill uses that data → save to project subfolder
```

---

## Key Rules

1. **Always reads brand.md first** — every skill uses industry, audience, and competitor data from brand.md to scope its queries.
2. **Never fabricates data** — only reports what comes back from APIs. If an API fails, reports the error clearly.
3. **Works standalone or in sequence** — any skill can run independently when a client needs to refresh one data point.
4. **Multi-client safe** — when no brand.md exists, user can paste data directly and specify a custom output path.
5. **All outputs feed Agent 3** — Strategy Agent reads all 4 research files before building any campaign.
