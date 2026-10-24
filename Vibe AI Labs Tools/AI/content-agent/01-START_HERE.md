# Content Agent — Start Here

Welcome. This system turns one topic into 8 platform-native posts using AI.
Read this file first before touching anything else.

---

## How It Works

You upload all files in this folder to a Claude Project. When you give Claude a topic, it reads the files, follows the wikilinks, and outputs one ready-to-publish post per platform — each one rethought for that platform, not just reformatted.

---

## Step 1 — Fill In Your 4 Files (1-customer/ folder)

These are the only files you need to edit. Everything else is pre-built.

| File | What to fill in |
|------|----------------|
| `1-customer/01-index.md` | Your brand name, niche, and mission |
| `1-customer/02-brand-voice.md` | Your voice, vocabulary, tone markers |
| `1-customer/03-builders.md` | Your primary audience description |
| `1-customer/04-casual.md` | Your secondary audience description |

Files marked with ⚠️ must be filled in before the system works.
Start with `01-index.md` and `02-brand-voice.md` — these two define everything else.

---

## Step 2 — Upload to Claude Projects

1. Go to [claude.ai](https://claude.ai) → open or create a Project
2. Upload ALL files from this folder (all subfolders included)
3. Claude will use them as persistent context for every conversation in that project

---

## Step 3 — Give It a Topic

Start a new conversation in your project and paste this prompt:

```
Topic: [YOUR TOPIC HERE]
```

The Orchestrator (`02-ORCHESTRATOR.md`) will handle the rest — it reads your brand files, selects the best hook, and produces 8 platform-native posts in order.

---

## Step 4 — Save Your Output

Copy the generated posts into the `6-output/` folder.
Suggested naming: `6-output/YYYY-MM-DD-topic-name/` with one file per platform.

---

## Step 5 — Review Performance Weekly

After posting, fill in `5-feedback/01-performance.md` with what worked and what didn't.
Then run: `"Review performance"` in your Claude Project — the system will suggest improvements.

---

## Folder Overview

```
content-agent/
├── 01-START_HERE.md       ← you are here
├── 02-ORCHESTRATOR.md     ← the agent brain
├── 03-EXPLAIN.md          ← full system documentation
│
├── 1-customer/            ← YOUR 4 FILES — fill these in
│   ├── 01-index.md
│   ├── 02-brand-voice.md
│   ├── 03-builders.md
│   └── 04-casual.md
│
├── 2-platforms/           ← fixed — platform rules (do not edit)
├── 3-engine/              ← fixed — hooks, repurpose, scheduling (do not edit)
├── 4-voice/               ← fixed — tone rules (do not edit)
├── 5-feedback/            ← fill weekly — performance + refinement log
└── 6-output/              ← save your generated posts here
```

---

## Tips

- The more specific your `02-brand-voice.md`, the better the output sounds like you
- Run the full repurpose chain in one session — each platform feeds the next
- After a few weeks, update `3-engine/01-hooks.md` with hooks that actually performed well
- Every Friday: fill `5-feedback/01-performance.md` → run Mode 4 → system improves
