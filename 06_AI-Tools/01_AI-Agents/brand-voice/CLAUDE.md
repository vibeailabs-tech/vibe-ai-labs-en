# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A pure markdown agent — no code, no APIs required. Consists of 12 SKILL.md files that Claude reads and follows to onboard brand voice for any SMB.

## How to run

Open this project in Claude Code and say: **"xây dựng brand voice"** — the orchestrator triggers automatically.

To run drift check on existing content: share the content and say **"drift check"**.

## Architecture

```
00_orchestrator/SKILL.md        ← entry point, routes between all skills
01_intake/
  01_brand-brief/               ← collects 7 fields → session/brief.json
02_discovery/
  01_competitor-analyzer/
    01_with-competitor/         ← WebSearch (+ optional Perplexity API)
    02_without-competitor/      ← Claude knowledge only
  02_content-scanner/           ← WebFetch URLs or accept pasted text
  03_interview/                 ← 8-question brand DNA interview
03_extraction/
  01_voice-synthesizer/         ← synthesizes all session data → Voice DNA
04_output/                      ← runs in parallel after synthesis
  01_brand-voice-card/          → 01_brand-voice-card.md
  02_platform-adaptor/          → 03_platform-variants.json
  03_geo-brand-summary/         → 04_geo-brand-summary.md
  04_skill-file-generator/      → 02_brand-voice-system-prompt.md + 05_drift-checker-rubric.json
05_maintenance/
  01_drift-detector/            ← scores content against rubric, suggests rewrites
```

## Session state

Skills communicate via `session/*.json` — read before writing to avoid repeating work:

| File | Written by | Read by |
|------|-----------|---------|
| `session/brief.json` | brand-brief | interview, voice-synthesizer |
| `session/competitor-analysis.json` | competitor skills | interview, voice-synthesizer |
| `session/content-scan.json` | content-scanner | interview, voice-synthesizer |
| `session/interview.json` | interview | voice-synthesizer |
| `session/voice-dna.json` | voice-synthesizer | all output skills |

## Output

5 files written to `brand-voice-output/{brand-name}-{date}/`:

| File | Purpose |
|------|---------|
| `01_brand-voice-card.md` | Human-readable reference |
| `02_brand-voice-system-prompt.md` | Paste into any AI agent's system prompt |
| `03_platform-variants.json` | Per-platform rules |
| `04_geo-brand-summary.md` | For Google Business, LinkedIn, About pages |
| `05_drift-checker-rubric.json` | Rubric for drift-detector |

## Routing logic (orchestrator)

After brand-brief, route based on two flags:

| Path | has_old_content | knows_competitor |
|------|-----------------|-----------------|
| A | true | true |
| B | true | false |
| C | false | true |
| D | false | false |

## Optional: Perplexity API

Set `PERPLEXITY_API_KEY` in shell env to use Perplexity instead of WebSearch in `02_discovery/01_competitor-analyzer/01_with-competitor/SKILL.md`. Falls back to WebSearch if not set.
