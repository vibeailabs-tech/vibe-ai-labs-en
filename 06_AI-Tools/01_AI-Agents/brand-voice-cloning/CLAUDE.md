# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A collection of 6 Claude skills that together form a **Brand Voice Cloning Agent** — analyzing brand content samples and producing a Brand Voice Card (JSON + Markdown) that captures a brand's writing style, tone, vocabulary, and personality for consistent reproduction.

## Project structure

```
brand-voice-cloning/
├── skill-0-platform-intake/    # Ask brand name + platform context
│   └── SKILL.md
├── skill-1-ingest/             # Receive content, run quality gate
│   └── SKILL.md
├── skill-2-analyze/            # Extract Brand Voice Card (10 dimensions)
│   ├── SKILL.md
│   └── references/
├── skill-3-review/             # Human checkpoint — user confirms before saving
│   └── SKILL.md
├── skill-4-store-load/         # Persist/load Voice Cards per brand
│   └── SKILL.md
├── skill-5-export/             # Render JSON → .md guideline file
│   ├── SKILL.md
│   └── references/
│       └── export_template.md  # Template for the final .md output
└── brand-voices/               # Runtime data — Voice Cards saved per brand
    └── {brand_name}_voice_card.json   (created at runtime)
    └── {brand_name}_voice_card.md     (created at runtime)
```

## Workflow

The 6 skills run in sequence. Each skill has a clear handoff to the next:

```
First time:
Skill 0 → Skill 1 → Skill 2 → Skill 3 → Skill 4 (store) → Skill 5

Returning user (brand already saved):
Skill 4 (load) → Skill 5  [or → Skill 3 if user wants to update]
```

| Skill | Name | Input | Output |
|---|---|---|---|
| 0 | Platform Intake | nothing | `platform_map` (brand + platform labels) |
| 1 | Ingest + Quality Gate | raw content | cleaned content + quality tier |
| 2 | Analyze | cleaned content | Brand Voice Card JSON (10 groups) |
| 3 | User Review | Voice Card JSON | confirmed Voice Card JSON |
| 4 | Store / Load | confirmed JSON | saved `.json` file in `brand-voices/` |
| 5 | Export | Voice Card JSON | `brand_name_voice_card.md` |

## The 10 Voice Card dimensions (Skill 2 output)

`brand_identity_foundation` · `tone_and_personality` · `vocabulary_and_language` · `sentence_and_rhythm` · `formatting_dna` · `storytelling_and_angles` · `channel_adaptation` · `emotional_signature` · `dos_and_donts` · `sample_fingerprints`

## Key design decisions

- **Platform-aware from the start**: Skill 0 always runs first to label content by platform. Facebook copy and email copy from the same brand analyze differently — platform convention must not be mistaken for brand voice.
- **Quality Gate in Skill 1**: Three tiers — Draft (<15 samples), Reliable (15–25), Deep (30+). Skill warns but doesn't block if sample count is low; quality tier is always reported so users understand confidence level.
- **Skill 3 is a hard checkpoint**: Never auto-saves. User must explicitly confirm the Voice Card before it's written to disk.
- **brand-voices/ is the persistent store**: JSON is source of truth, MD is the human-readable export. Skill 4 manages both. On session start, Skill 4 checks for existing brands and offers to load.
- **Skills are independent**: Each skill can be invoked standalone. Context flows through the conversation, not through shared state files between skills.
