# Agent 08 — Social Media Agent
> Deep-dive explanation | Layer 3 — Execution

## What this agent does

The Social Media Agent takes brand context and content strategy and turns them into publish-ready social media assets. It's the most output-dense agent in the system — everything the brand posts on Facebook, TikTok, Zalo, and LinkedIn flows through here.

Its job isn't just writing posts. It's maintaining brand voice across 4 different platforms, each with completely different norms, formats, and audience behaviors — without losing consistency or quality.

---

## 6 Skills

### 1. `/social-copy` — Platform-Specific Posts
**What it does:** Takes one input (blog post, topic, or campaign) and produces 4 platform-specific posts: Facebook, TikTok caption, Zalo broadcast, LinkedIn.

**Why 4 versions instead of 1:** Each platform has different optimal length, format, hashtag use, and reader expectation. A 300-word Facebook post copy-pasted to TikTok will perform poorly. The skill adapts tone, length, and structure for each — same message, different packaging.

**When to use:**
- Atomizing a blog post into social content
- Launching a campaign across all platforms
- Promoting a new offer or service

**Output:** `/outputs/assets/social/social-copy-[slug].md`

---

### 2. `/social-creative` — Visual Direction Briefs
**What it does:** Writes detailed creative direction for images and videos — what to shoot, what text overlay to use, camera angle, production notes. Not the visual itself, but the brief to create it.

**Why this exists:** Most brands post visuals that are either completely generic (stock photos) or inconsistent with the written content. A creative brief ensures the visual and the copy work together — and gives a designer, videographer, or the founder a clear production spec they can execute without guessing.

**6 elements in every brief:** Visual concept, text overlay, hook (for video), platform specs, caption alignment, production notes.

**When to use:**
- Before any visual content production
- When planning a TikTok or Reels video
- When briefing a designer or photographer

**Output:** `/outputs/assets/social/social-creative-[slug].md`

---

### 3. `/hashtag-research` — Vietnamese Hashtag Clusters
**What it does:** Builds hashtag clusters per content pillar and per platform — sized correctly (mega / large / mid / niche) and Vietnamese-specific.

**Why Vietnamese-specific matters:** Global hashtags like `#marketing` or `#AI` are dominated by English-language content. Vietnamese audiences find content through Vietnamese hashtags — `#marketingvietnam`, `#doanhnghiepviet`, `#AIvietnam`. Using the wrong hashtag size means competing with millions of posts or reaching an audience of zero.

**Platform differences:**
- Facebook: 3–5 niche hashtags — community, not discovery
- TikTok: 5–8 mixed size — discovery-first platform
- LinkedIn: 3–5 professional, topic-based
- Zalo: No hashtags

**Output:** `/outputs/assets/social/hashtag-research-[topic].md`

---

### 4. `/social-calendar` — 30-Day Posting Calendar
**What it does:** Builds a complete 30-day calendar with every post planned: day, platform, format, topic, hook, angle, CTA, assets needed, status.

**Content mix formula:**
- 40% Education / tips — builds authority
- 30% Social proof / results — builds trust
- 20% Behind-the-scenes / founder — builds connection
- 10% Promotional / offer — converts

**Campaign arcs:** When there's a launch or promotion, the skill builds a 3–5 post narrative: Tease → Build → Launch → Social proof → Last call. Campaign posts are surrounded by value content so they don't feel isolated.

**Vietnamese calendar specifics:** Monday is weak for Facebook. Holiday tie-ins for 30/4, 1/5, 2/9. Tết period needs different content strategy.

**Output:** `/outputs/assets/social/social-calendar-[month-year].md`

---

### 5. `/community-management` — Reply Templates
**What it does:** Writes reply templates for 4 categories: engagement replies (comments), sales inquiry replies (DMs), negative review/complaint handling, common Vietnamese questions.

**Why templates instead of on-the-fly replies:** At scale, brands respond inconsistently — sometimes warm, sometimes corporate, sometimes defensive. Templates trained in the brand voice ensure every interaction sounds like the same person, regardless of who's managing the account.

**The 4-step negative review framework:**
1. Acknowledge the specific complaint
2. Empathize (don't argue — the audience is watching)
3. Own or clarify briefly
4. Redirect to private channel (Zalo / inbox)

**What never to write:** "Cảm ơn bạn đã quan tâm đến sản phẩm/dịch vụ của chúng tôi" — the most hated corporate reply in Vietnamese social media. The skill knows to avoid this.

**Output:** `/outputs/assets/social/community-management-templates.md`

---

### 6. `/video-script` — TikTok/Reels Scripts
**What it does:** Writes complete video scripts in a two-column format: [VISUAL] and [SPOKEN] on the same line, timestamped. The creator knows exactly what to say and what to show simultaneously.

**The hook problem:** The first 3 seconds determine whether viewers keep watching. Most video scripts skip this — they start with context and get to the point at second 15. This skill starts with the hook and works backward. No hook, no script.

**4 proven hook formulas for Vietnamese market:**
- Contrast: "Agency $3,000/tháng vs hệ thống AI $80/tháng"
- Problem: "Nếu bạn đang dùng ChatGPT như thế này..."
- Curiosity: "Mình vừa test X trong 1 tuần. Đây là điều mình không ngờ tới."
- Result-first: "Từ 3 giờ/ngày xuống 45 phút/tuần — đây là cách mình làm được."

**Optimal length for Vietnamese B2B content: 45–60 seconds.** Long enough to deliver value, short enough to hold attention.

**Output:** `/outputs/assets/social/video-script-[slug].md`

---

## No External APIs

Agent 08 is a pure writing agent. No API keys, no MCP servers, no web scraping required. This means:
- Can run immediately after brand.md setup
- Works offline
- Zero additional cost beyond API calls to Claude

The only optional upgrade: SerpAPI for live Vietnamese hashtag volume data in the hashtag-research skill. Without it, the skill uses known platform patterns and size frameworks — still useful, just not real-time verified.

---

## Layer Position and Data Flow

```
brand.md (L1) ──────────────────────────┐
content-calendar.md (L2) ───────────────┤
campaign-brief.md (L2) ─────────────────┤──→ Agent 08 Social ──→ /assets/social/
blog posts from Content Agent (L3) ──────┤
SEO keywords from SEO Agent (L3) ────────┘
                                                      ↓
                                         Distribution Agent (L3)
                                         → atomizes to platform-specific formats
```

**Key relationship:** Agent 08 is a primary consumer of Content Agent output. Every blog post written by the Content Agent should be atomized into social posts by Agent 08. The blog provides the depth; Agent 08 provides the reach.

---

## Isolated Execution

Agent 08 can run without brand.md. Useful for:
- Writing social posts for a topic unrelated to the brand
- Testing what content would look like for a prospect's brand
- Demonstrating the system to a new client

When running isolated: ask for brand name, voice tone (3 adjectives), target audience, and platform before writing. Takes 2 minutes and produces the same quality output.

---

## Common Use Patterns

**Pattern 1 — Blog-to-social pipeline**
```
Blog post written → /social-copy → 4 platform versions
                  → /video-script → TikTok script from the same post
                  → /social-creative → thumbnail brief
```

**Pattern 2 — Monthly calendar build**
```
/social-calendar → 30-day plan
/hashtag-research → hashtag clusters per pillar
/social-copy → write copy for week 1 posts
/social-creative → brief visuals for week 1
```

**Pattern 3 — Campaign launch**
```
/campaign-brief (Strategy Agent) → /social-copy → campaign arc posts
                                 → /video-script → launch video
                                 → /social-calendar → campaign dates blocked in calendar
```

---

## What This Agent Doesn't Do

- Publish to platforms directly (no social media API integrations)
- Generate images or videos (writes briefs, doesn't create)
- Analyze performance data (that's Performance Agent, Layer 4)
- Write paid ad copy (that's Ads Agent — different skill set and format)
