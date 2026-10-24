# Agent 10 — Video & Creative Agent
> Deep-dive explanation | Layer 3 — Execution

## What this agent does

The Video & Creative Agent produces all video scripts and visual asset briefs. It doesn't generate images or videos — it writes the production documents that make asset creation fast, consistent, and brand-accurate.

Think of it as the creative director on the team: it knows what to make, how to make it, and why it will work — then hands it off to a human or tool to execute.

---

## 4 Skills

### 1. `/video-script` — Full Video Scripts
**What it does:** Writes complete two-column scripts for any video format — YouTube long-form, Facebook video, TikTok extended, website explainer. Every line has [VISUAL] and [SPOKEN] side by side, timestamped, with production notes where needed.

**Why two-column format:** Most scripts are written as prose or teleprompter text. The creator then has to figure out what to show while saying each line. This wastes shoot time and produces mismatched audio/visual. The two-column format solves this — the creator sees exactly what to say and what to show simultaneously.

**4 formats covered:** Talking head, tutorial/screen recording, B-roll + narration, animation/explainer. Each has different structural rules — the skill enforces the right one.

**Vietnamese spoken word rules:** Short sentences (5–10 words), conversational register ("thật ra", "nói thật nhé"), emphasis through repetition ("7 ngày. Không phải 7 tuần — 7 NGÀY."), and marked pauses [PAUSE 2 SECONDS] for key moments to land.

**Output:** `/outputs/assets/creative/video-script-[slug].md`

---

### 2. `/creative-brief` — Visual Asset Briefs
**What it does:** Writes production-ready briefs for any visual asset: YouTube thumbnails, blog featured images, social graphics, email headers, ad banners, presentation slide templates. 8 elements per brief — specific enough that a designer executes without asking follow-up questions.

**The 8 elements:** Asset name/purpose, dimensions/format, visual concept, focal point, color direction (with hex codes), typography, mood (3 adjectives), and — most importantly — what NOT to do.

**Why "what NOT to do" is the most important element:** Creative briefs fail when they're misinterpreted in the obvious wrong direction. Listing 2–3 specific exclusions prevents the most common mistakes. "No white background — blends into Facebook UI" is worth more than 5 adjectives describing what you want.

**Output:** `/outputs/assets/creative/creative-brief-[slug].md`

---

### 3. `/branded-deck` — Presentation Decks
**What it does:** Writes complete slide-by-slide content for sales pitch decks, client onboarding decks, webinar decks, and product explainer decks. Each slide gets: headline (the point), body copy (max 3 bullets × 8 words), visual direction, and full speaker notes.

**The headline rule:** Every slide headline is a complete thought, not a topic label. "Our Process" is a label. "Setup takes 9 days — then you run it yourself" is a point. The difference is whether the viewer learns something just by reading the headline — they should.

**Speaker notes are full sentences:** The deck shows the point; the notes tell the story. This is critical — most founders read off the slides, which is why their pitches feel rehearsed. Notes written as natural speech help them sound like they're having a conversation.

**3 deck types built in:** Sales pitch (10–15 slides), client onboarding (8–12 slides), webinar/educational (20–30 slides). Each has a different goal and different structural logic.

**Output:** `/outputs/assets/creative/branded-deck-[slug].md`

---

### 4. `/ugc-script` — User Generated Content Scripts
**What it does:** Writes scripts for customers, micro-creators, or brand advocates to perform — not the founder or brand itself. 3 versions per format: emotional angle, logical angle, social angle. Includes creator profile, casting notes, and usage rights guidance.

**Why UGC needs scripts:** Unscripted UGC from customers is often vague and forgettable ("Sản phẩm tốt, mình rất thích"). Scripted UGC that still sounds natural and specific is significantly more effective — it tells the right story with the right details while feeling authentic.

**The authenticity engineering problem:** A script that sounds scripted defeats the purpose. The skill writes in first-person conversational Vietnamese, marks where natural pauses and ad-lib space exist, and includes authenticity direction (real home background, natural light, everyday clothes). "Credible" beats "polished."

**3 angles for testing:** Emotional (how it felt), Logical (numbers and time saved), Social (what others noticed). Different audience segments respond differently — all 3 are written, then the best performer is scaled.

**Output:** `/outputs/assets/creative/ugc-script-[slug].md`

---

## No APIs Required

Agent 10 is a pure writing agent. The optional upgrade is **Glif MCP** — for AI-generated images and videos based on the briefs this agent produces. Without it, briefs go to human designers or Canva. With it, the pipeline becomes: brief → auto-generate → human review → publish.

---

## Layer Position and Data Flow

```
brand.md (L1) ─────────────────────────┐
campaign-brief.md (L2) ────────────────┤
blog posts — Content Agent (L3) ────────┤──→ Agent 10 Video & Creative ──→ /assets/creative/
ad creative direction — Ads Agent (L3) ─┘
                                                         ↓
                                            Human production / Glif MCP
                                                         ↓
                                            Distribution Agent (L3)
```

**Key relationship with Ads Agent:** Ad Creative (Agent 9) briefs the ad visual. Video & Creative (Agent 10) scripts the actual video content and briefs the thumbnail. They should be used together for video ad campaigns.

---

## Common Use Patterns

**Pattern 1 — Blog to video pipeline**
```
Blog post written (Content Agent) → /video-script → YouTube/TikTok video
                                  → /creative-brief → thumbnail
```

**Pattern 2 — Sales pitch prep**
```
/branded-deck → full pitch deck content
/creative-brief → deck visual design brief
```

**Pattern 3 — UGC ad campaign**
```
/ugc-script → 3 creator script versions
/ad-campaign-structure (Ads Agent) → campaign to run UGC as paid ads
```

---

## What This Agent Doesn't Do

- Generate actual images or videos (writes briefs and scripts)
- Publish videos to YouTube or TikTok
- Edit video files
- Manage creator relationships or payments
- Write short social video scripts (that's Agent 8 Social — `/video-script` in Agent 8 is for TikTok/Reels shorts; Agent 10's `/video-script` is for longer-form brand video)
