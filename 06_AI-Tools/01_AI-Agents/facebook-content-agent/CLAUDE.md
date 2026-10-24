# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **Facebook Content Agent** — a Claude Code custom command system that writes, optimizes, and quality-checks Facebook content. Users invoke `/fb-content-agent` and the orchestrator coordinates 29 specialist skills automatically.

Spec source of truth: [fb-content-agent-skills.md](fb-content-agent-skills.md) (v3.2, 29 skills).  
Spec is written in mixed Vietnamese/English — preserve that style in skill files and docs.

## How to use (for end users)

1. Fill in the 5 brand voice files in `brand-voice/` (templates are provided)
2. In Claude Code, run: `/fb-content-agent [your request]`
3. Confirm the execution plan when shown
4. Receive the full content package

## Repository structure

```
.claude/commands/fb-content-agent.md   ← Entry point (orchestrator)
skills/                                 ← 29 skill prompt files (read by orchestrator)
brand-voice/                            ← Customer fills these 5 files
  01-tone.md, 02-audience.md, 03-pillars.md, 04-examples.md, 05-glossary.json
memory/
  post-history.json                     ← Performance history (written by performance-memory skill)
  task-state.json                       ← Pipeline checkpoint (resume on interruption)
```

## Pipeline architecture

Every publishing request flows through this pipeline:

```
brand-voice-loader (HARD GATE)
  → task-router → fb-format-selector → performance-memory (read)
  → [fb-content-brief — optional, khi user cung cấp nội dung có sẵn]
  → [content skill] → fb-discussion-architect → fb-first-comment-strategy
  → fb-readability-formatter → fb-visual-brief → fb-vietnamese-localizer → fb-policy-checker
  → fb-save-share-optimizer → fb-send-time-optimizer
  → fb-review-queue (HITL) → output-validator (HARD GATE)
```

Lightweight pipelines exist for strategy, analytics, comment-reply, and content-brief tasks (see spec).

## Two hard gates — never bypass

1. **`brand-voice-loader`**: Must successfully load all 5 brand voice files before any skill runs. No context = full stop.
2. **`output-validator`**: 11-point checklist. Fail = bounce back to the responsible skill (max 2 retries).
3. **`fb-policy-checker` Block result**: Pipeline stops, forces rewrite. Cannot be bypassed even if user asks.

## HITL confidence routing

| Confidence | Action |
|---|---|
| ≥ 90% | Auto — straight to output-validator |
| 70–89% | Pause for human review (show bài, ask approve/edit/reject) |
| < 70% | Auto-reject — bounce to content skill for rewrite |

## Brand voice folder contract

The loader reads exactly these filenames — do not rename:
- `01-tone.md`, `02-audience.md`, `03-pillars.md`, `04-examples.md` — Markdown
- `05-glossary.json` — `{ "approved": [...], "banned": [...], "reasoning": {...} }`

## Adding or editing skills

Each file in `skills/` defines one skill: purpose, input, processing logic, and YAML output schema. The orchestrator reads the skill file at runtime and follows its instructions.

When editing a skill:
- Keep input/output schema compatible with upstream/downstream skills
- `banned_terms` and `approved_glossary` come from brand-voice-loader — skills must not re-read brand-voice folder
- `fb-policy-checker` must always run before `fb-review-queue`
- `fb-save-share-optimizer` output feeds into `output-validator` checklist point 10

## No build system

There is no build step, test runner, or package manifest. Skills are markdown prompt files executed by Claude at runtime.
