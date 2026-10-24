# Content Agent — How It Works

This document explains the full architecture of the Content Agent system — what each file does, how they connect, and why the system produces better output than a single prompt.

---

## The Core Idea

Most people use AI for content like this:

1. Open Claude
2. Type "write me a LinkedIn post about X"
3. Get a generic post
4. Spend 20 minutes making it sound human
5. Repeat for every platform

That's not a system. That's a chore.

The problem isn't the AI. It's that you're giving it zero context — no brand, no audience, no voice, no platform rules. You're hiring a genius with amnesia every single time.

**The Content Agent fixes this.**

Instead of one prompt, you give Claude a folder of 23 interconnected markdown files organized into 4 layers. Claude reads the files, follows the wikilinks, understands your brand deeply, and produces platform-native posts that actually sound like you — across 8 platforms, from one topic.

---

## System Architecture

```
L1 Foundation → L2 Execution → L3 Feedback
(Who we are)    (Make content)  (Improve system)
```

| Layer | Folder | Role |
|-------|--------|------|
| L1 Foundation | `1-customer/` | Brand identity, voice, audience — master context |
| L2 Execution | `2-platforms/` `3-engine/` `4-voice/` | Platform rules, hooks, repurpose chain, tone |
| L3 Feedback | `5-feedback/` | Track performance, refine system over time |
| Output | `6-output/` | All generated posts saved here |

---

## How the System Thinks

When you give Claude a topic, it doesn't just start writing. It follows a reading chain:

```
Topic (input)
    ↓
02-ORCHESTRATOR.md    ← routing logic, reads this first
    ↓
1-customer/01-index.md        ← brand identity + node map
1-customer/02-brand-voice.md  ← voice DNA
1-customer/03-builders.md     ← primary audience
1-customer/04-casual.md       ← secondary audience
    ↓
3-engine/01-hooks.md          ← select best hook formula
3-engine/02-repurpose.md      ← follow the chain order
    ↓
2-platforms/[platform].md     ← rules for each platform
4-voice/01-platform-tone.md   ← tone adjustment per platform
    ↓
8 platform-native posts (output)
    ↓
5-feedback/01-performance.md  ← log results weekly
5-feedback/02-refinement.md   ← update system based on data
```

The wikilinks (`[[02-brand-voice]]`, `[[01-hooks]]`, `[[02-repurpose]]`) tell Claude which files to read before executing each step. This is what makes output coherent — not one file, but a network of connected knowledge.

---

## Folder Structure

```
content-agent/
├── 01-START_HERE.md      — setup guide for new users
├── 02-ORCHESTRATOR.md    — the agent brain (5 modes)
├── 03-EXPLAIN.md         — this file
│
├── 1-customer/           — YOUR 4 FILES — fill these in
│   ├── 01-index.md
│   ├── 02-brand-voice.md
│   ├── 03-builders.md
│   └── 04-casual.md
│
├── 2-platforms/          — 8 platform playbooks (fixed)
│   ├── 01-x.md
│   ├── 02-linkedin.md
│   ├── 03-instagram.md
│   ├── 04-tiktok.md
│   ├── 05-youtube.md
│   ├── 06-newsletter.md
│   ├── 07-threads.md
│   └── 08-facebook.md
│
├── 3-engine/             — production logic (fixed)
│   ├── 01-hooks.md
│   ├── 02-repurpose.md
│   ├── 03-content-types.md
│   └── 04-scheduling.md
│
├── 4-voice/              — tone rules (fixed)
│   └── 01-platform-tone.md
│
├── 5-feedback/           — performance loop
│   ├── 01-performance.md
│   └── 02-refinement.md
│
└── 6-output/             — generated posts saved here
```

---

## File-by-File Breakdown

### 1-customer/ — Your Identity Layer
The only files you edit. They define who you are. All other files read from here.

**`01-index.md` — Command Center**
The most important file in the system. Claude reads this first on every task. Contains your brand identity, a map of all knowledge files with context, and execution instructions. Think of it as the CEO of your content operation.

**`02-brand-voice.md` — Your Voice DNA**
Defines your core personality: tone markers, vocabulary you use, phrases you never say, formatting rules. Every platform file references this. If this file is weak, everything downstream sounds generic.

**`03-builders.md` — Primary Audience**
Who your main audience is, what they want, what turns them off, and how to talk to them. Platform files reference this to calibrate angle and depth.

**`04-casual.md` — Secondary Audience**
Your wider, less technical audience. Helps Claude shift tone when writing for discovery-focused platforms like TikTok or Instagram.

---

### 2-platforms/ — Platform Playbooks
One file per platform, numbered in repurpose chain order. Each contains: platform DNA, content rules, formats that work, posting strategy, repurposing notes.

| File | Platform | Key trait |
|------|----------|-----------|
| `01-x.md` | X / Twitter | Written first. Forces brevity. Hook-driven |
| `02-linkedin.md` | LinkedIn | Personal narrative. Professional tone. 1,300+ chars |
| `03-instagram.md` | Instagram | Visual-first. Carousel format. Aspirational |
| `04-tiktok.md` | TikTok | Raw, spoken, hook in 2 seconds. Script format |
| `05-youtube.md` | YouTube | SEO-driven. Structured. 8-12 min format |
| `06-newsletter.md` | Newsletter | Deepest and most personal. You own the audience |
| `07-threads.md` | Threads | Casual opinion. Conversational. Under 500 chars |
| `08-facebook.md` | Facebook | Community-focused. Ends with a question |

---

### 3-engine/ — The Operational Backbone
These files define HOW content is produced.

**`01-hooks.md` — Hook Formulas**
6 proven hook types with templates: Playbook, Proof, Contrarian, Replacement, Discovery, Behind-the-Scenes. Claude selects the best formula for each topic and adapts it per platform.

**`02-repurpose.md` — The Production Chain**
Defines the exact order to write across platforms and what changes at each step. X is always first. Each version rethinks the angle — same topic, different entry point, format, and depth.

**`03-content-types.md` — Format Definitions**
Defines each content format: thread, carousel, short-form video, long-form video, long-form text, short take.

**`04-scheduling.md` — Posting Calendar**
Best posting times and frequency per platform. Contains the weekly batch workflow.

---

### 4-voice/ — Tone Bridge

**`01-platform-tone.md` — Tone Adaptation Rules**
Your voice stays consistent across all platforms — but the delivery changes. More casual on X, more professional on LinkedIn, most energetic on TikTok, most personal in the newsletter. Same person, different room.

---

### 5-feedback/ — The Feedback Loop
This is what separates a static template from a living system.

**`01-performance.md` — Weekly Performance Log**
Track what worked and what didn't per platform, per hook type, per topic. Updated every Friday after reviewing the week's content.

**`02-refinement.md` — System Update Log**
Reads performance data and applies improvements back into the system files — updating brand voice, hook formulas, platform strategies based on real results. The system gets smarter over time.

---

## The Repurposing Chain

One topic enters. Eight platform-native posts come out. The key rule: each version **rethinks** the topic, it doesn't just reformat it.

| Step | Platform | What changes |
|------|----------|-------------|
| 1 | X | Core idea, sharpest hook, most concise |
| 2 | LinkedIn | Personal narrative added, professional framing |
| 3 | Instagram | Extracted into visual carousel slides |
| 4 | TikTok | Condensed into 45-60 second spoken script |
| 5 | YouTube | Expanded into full structured tutorial outline |
| 6 | Newsletter | Deepest version, behind-the-scenes, exclusive insights |
| 7 | Threads | Relaxed opinion-driven take |
| 8 | Facebook | Community framing, ends with discussion question |

The litmus test: if someone followed you on all 8 platforms, would they feel annoyed seeing the same thing everywhere? If yes — you're reformatting. If no — you're repurposing correctly.

---

## The 5 Modes

The Orchestrator handles 5 types of requests:

| Mode | Trigger | What happens |
|------|---------|-------------|
| 1 — Full Repurpose | `"Topic: [topic]"` | All 8 platforms in one run |
| 2 — Single Platform | `"Write LinkedIn post about [topic]"` | One platform only |
| 3 — Batch | `"Topics: [1], [2], [3]"` | Multiple topics, full chain each |
| 4 — Feedback Review | `"Review performance"` | Reads performance.md, suggests updates |
| 5 — System Refinement | `"Update brand voice"` | Updates system files based on data |

---

## Why It Works Better Than a Single Prompt

| Single Prompt | Content Agent |
|--------------|---------------|
| No brand context | Full voice DNA in `02-brand-voice.md` |
| No audience context | Detailed audience files |
| No platform rules | One playbook file per platform |
| Generic hooks | 6 proven hook formulas |
| Same post reformatted | Each platform rethought from scratch |
| Starts from zero every time | Persistent context across all sessions |
| No improvement over time | Feedback loop updates system weekly |

The difference isn't the AI. It's the context you give it.

---

## What to Customize vs What to Leave

**Edit these (`1-customer/` folder):**
- `01-index.md` — your brand, niche, mission
- `02-brand-voice.md` — your voice, vocabulary, tone
- `03-builders.md` — your primary audience
- `04-casual.md` — your secondary audience

**Leave these as-is (everything else):**
- Platform rules don't change per person
- Hook formulas are universal
- The repurpose chain order works for any niche
- Tone adaptation rules are platform-standard

The engine is fixed. Your identity layer is what makes it yours.
