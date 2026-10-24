# Content Agent — Customer Guide

Welcome. This guide walks you through everything from setup to your first post.
Follow the steps in order. The whole setup takes under 60 minutes.

---

## What You Need Before Starting

- A **Claude Pro account** (claude.ai — $20/month). Free tier does not support Projects.
- This folder of files (you already have it).
- 30-45 minutes to fill in your brand files.

That's it. No coding. No technical setup.

---

## Step 1 — Fill In Your 4 Brand Files

Open the `1-customer/` folder. You'll see 4 files with placeholder text.
Fill these in before anything else — the system doesn't work without them.

**Not sure what to write? Open `1-customer/EXAMPLE/` first.**
There's a complete filled-in example for a freelancing brand. Use it as a reference.

---

### File 1: `1-customer/01-index.md`

This is the most important file. Claude reads this first on every task.

Replace these placeholders:

| Placeholder | Replace with |
|-------------|-------------|
| `[YOUR BRAND/NAME]` | Your name or brand name |
| `[YOUR NAME / BRAND]` | Same as above |
| `[YOUR NICHE]` | What you create content about (be specific) |

**Niche examples:**
- ❌ Too vague: "business and marketing"
- ✅ Good: "helping Vietnamese freelancers earn $2,000+/month using AI tools"
- ✅ Good: "fitness for busy professionals over 35"
- ✅ Good: "personal finance for Gen Z in Vietnam"

Also update the audience descriptions in the Node Map to match your actual audience (not the default "indie hackers / AI engineers").

---

### File 2: `1-customer/02-brand-voice.md`

This file defines how you sound. The more specific this is, the better every post will sound like you.

Fill in:

**Core Personality** — 3-5 sentences describing your brand's personality. Write it in first person. Read it out loud — it should sound like you.

**Vocabulary:**
- Words you use: list 10-15 words you naturally use in your niche
- Words you NEVER use: list words that feel fake or corporate to you

**Phrases you use:** things you actually say. Look at your past posts for these.

**Phrases you never use:** things that sound like generic AI content. Be specific.

> Tip: copy 5 of your best past posts into a doc and read them. The patterns you see are your voice.

---

### File 3: `1-customer/03-builders.md`

Your primary audience — the people most likely to buy from you or follow you actively.

Replace the placeholder text with:
- Who they are (role, age, situation)
- What they want (be specific — not "good content", but what outcome)
- What frustrates them
- How to talk to them

---

### File 4: `1-customer/04-casual.md`

Your secondary audience — people who follow you but aren't deep into your niche yet.

Same structure as builders.md but for a wider, less committed audience.

---

## Step 2 — Set Up Claude Projects

1. Go to **claude.ai** and log in to your Pro account
2. Click **"Projects"** in the left sidebar
3. Click **"New Project"**
4. Name it: `Content Agent — [Your Brand Name]`
5. Click **"Add content"** or **"Upload files"**
6. Upload **ALL files** from the `content-agent/` folder — including all subfolders
7. Done. Claude now has your full skill graph as persistent context.

> Important: upload every file, not just the customer files. The platform files, engine files, and voice files are what make the system work.

---

## Step 3 — Test With Your First Topic

In your new Claude Project, start a conversation and type:

```
Topic: [your topic here]
```

Example:
```
Topic: Why most freelancers undercharge and how to fix it
```

The agent will:
1. Load your brand files
2. Select the best hook type
3. Write 8 platform-native posts in order
4. Add a scheduling suggestion at the end

Your first output might not be perfect — that's normal. The next step is how you fix it.

---

## Step 4 — Review and Adjust

After your first run, check each post against these questions:

| Question | If No → Fix |
|----------|------------|
| Does this sound like me? | Update `02-brand-voice.md` — add more specific vocabulary and phrases |
| Is the X post punchy enough? | Check your hook type in `01-hooks.md` — try a different one |
| Does LinkedIn feel personal? | Add a real story or number to your brand-voice Core Personality |
| Is TikTok script speakable? | Add a note in `04-tiktok.md` to "write like you're texting a friend" |
| Does Facebook feel warm enough? | Check `04-casual.md` — is your casual audience described well? |

The system improves as you refine your files. Most people get to a great output by the 3rd run.

---

## Step 5 — Publish and Track

After publishing your posts, fill in `5-feedback/01-performance.md` at the end of the week:

- Which post got the most engagement?
- Which hook type worked best?
- Which platform is growing fastest?

Then in your Claude Project, type:
```
Review performance
```

The agent will read your performance file and suggest specific improvements to your system files.

**This is the feedback loop.** Every week you run it, the system gets smarter.

---

## The 5 Commands

Use these in your Claude Project to get different outputs:

| Command | What it does |
|---------|-------------|
| `Topic: [topic]` | Full repurpose — all 8 platforms |
| `Write LinkedIn post about [topic]` | Single platform only |
| `Topics: [topic 1], [topic 2], [topic 3]` | Batch — 3 topics in one run |
| `Review performance` | Reads your performance file, suggests updates |
| `Update brand voice` | Refines your voice file based on what's working |

---

## Common Questions

**Q: The output doesn't sound like me. What do I do?**
A: Your `02-brand-voice.md` needs more specifics. Add real phrases you use, words you avoid, and examples of your best past posts at the bottom of the file. Re-upload and try again.

**Q: Can I use this without Claude Pro?**
A: You can paste files manually into any Claude chat, but you'll need to re-paste them every session. Claude Projects (Pro) keeps everything persistent — worth the $20/month for daily use.

**Q: Can I add more platforms?**
A: Yes. Create a new file in `2-platforms/` following the same structure as the existing platform files. Add it to the node map in `01-index.md`.

**Q: Can I use this for a client?**
A: Yes. For each client, create a separate Claude Project and upload a copy of this folder with their brand files filled in. Keep the engine files identical across all clients.

**Q: How often should I update the files?**
A: `02-brand-voice.md` — update when your voice evolves or you notice the output drifting.
`01-hooks.md` — update monthly based on what's performing.
Platform files — update when platform algorithms change significantly.

---

## Quick Reference

```
content-agent/
├── 01-START_HERE.md       ← quick 5-step setup
├── 02-ORCHESTRATOR.md     ← the agent brain (don't edit)
├── 03-EXPLAIN.md          ← full system documentation
│
├── 1-customer/            ← FILL THESE IN
│   ├── 01-index.md        ← brand + niche (most important)
│   ├── 02-brand-voice.md  ← your voice DNA
│   ├── 03-builders.md     ← primary audience
│   ├── 04-casual.md       ← secondary audience
│   └── EXAMPLE/           ← filled reference (freelance niche)
│
├── 2-platforms/           ← don't edit — platform rules
├── 3-engine/              ← don't edit — production logic
├── 4-voice/               ← don't edit — tone rules
├── 5-feedback/            ← fill weekly after posting
└── 6-output/              ← your generated posts live here
```

---

## If You Get Stuck

The most common issue is brand-voice.md being too vague.

Before reaching out for support, try this:
1. Open `1-customer/EXAMPLE/02-brand-voice.md`
2. Compare it to your own `02-brand-voice.md`
3. Look for anything that's still a placeholder or too generic
4. Update it and run the agent again

90% of "the output sounds generic" problems are fixed by a better brand-voice file.
