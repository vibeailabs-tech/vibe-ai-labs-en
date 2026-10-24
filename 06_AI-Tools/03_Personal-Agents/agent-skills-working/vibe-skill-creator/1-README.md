# Vibe Skill Creator - Shareable Package

This package teaches you how to build world-class Claude skills that actually improve output.

## What's Included

| File | What It Does | Lines |
|------|--------------|-------|
| **SKILL.md** | The main skill - guides you through building skills from scratch | 656 |
| **references/bad-skill-patterns.md** | 10 patterns that make skills mediocre (avoid these) | 531 |
| **cold-outreach/SKILL.md** | Example skill built using this process | 455 |

---

## How to Use

### In Claude Desktop (claude.ai)

**Option A: Install as Custom Skill (Recommended)**
1. Create a folder named `vibe-skill-creator`
2. Save `2-vibe-skill-creator.md` as `SKILL.md` inside that folder
3. ZIP the folder
4. Go to Settings → Capabilities
5. Click "Upload skill" and upload your ZIP
6. The skill appears in your Skills list and can be toggled on/off

**Option B: Add to Project Knowledge**
1. Create a new Project
2. Click "Add Content" → "Add text content"
3. Paste the contents of `2-vibe-skill-creator.md`
4. Start chatting: "Help me create a skill for [your domain]"

**Option C: Upload as File (per-chat)**
1. In any chat, click the attachment icon
2. Upload `2-vibe-skill-creator.md`
3. Say: "Use this skill to help me build a skill for [your domain]"

**Note:** Option A installs the skill permanently and it auto-activates when relevant. Options B and C work per-project or per-chat.

### In Claude Code

**Option A: Project Skill (Recommended for teams)**
1. Create folder in your project: `.claude/skills/vibe-skill-creator/`
2. Save as `SKILL.md` in that folder
3. Commit to git — teammates get it automatically
4. Claude auto-invokes based on the description (no need to reference it)

**Option B: Personal Skill**
1. Create folder: `~/.claude/skills/vibe-skill-creator/`
2. Save as `SKILL.md` in that folder
3. Available in all your Claude Code projects

**Option C: As a Slash Command**
1. Create folder: `.claude/commands/`
2. Save as `build-skill.md`
3. Invoke manually by typing: `/build-skill`

**How Skills Work:**
- Skills are **model-invoked** — Claude decides when to use them based on the description
- You don't explicitly call them like slash commands
- Just say "help me create a skill" and Claude uses it automatically

---

## What Triggers It

Say any of these:
- "Help me create a skill"
- "Build a skill for [domain]"
- "Improve this skill"
- "Help me make a skill"

---

## What Happens

Claude guides you through a 10-step conversation:

```
1. UNDERSTAND → What skill? What problem?
2. EXPLORE    → See where Claude fails without guidance
3. RESEARCH   → Go deep on the domain (web search)
4. SYNTHESIZE → Extract principles from research
5. DRAFT      → Write initial skill
6. CRITIQUE   → Review against quality criteria
7. ITERATE    → Fix gaps, get feedback
8. TEST       → Use on a real scenario
9. FINALIZE   → Structure properly
10. REFERENCE → Build deep expertise docs (if needed)
```

You don't need to know how to build skills. Just have the conversation.

---

## Study the Example

`cold-outreach/SKILL.md` shows what a finished skill looks like:
- Expert voice (not documentation)
- Principles with WHY (not just WHAT)
- Anti-patterns explicitly named
- Real before/after examples
- Quality checklist

---

## Avoid These Mistakes

Read `references/bad-skill-patterns.md` to understand:
- Documentation voice (sounds like a wiki)
- Procedure over principle (step-by-step without thinking)
- Comprehensive coverage (information overload)
- Missing anti-patterns (what to avoid)
- Friction creation (intermediate documents)

---

## Quick Start

Paste this into Claude:

```
I want to build a skill for [YOUR DOMAIN]. Guide me through the process -
explore where you fail without guidance, research the domain, then help me
build a skill that actually improves your output.
```

Then follow the conversation.

---

## Need More Examples?

Other skills built with this process:
- `direct-response-copy` - Copywriting skill with 1,600 lines of embedded reference material
- `ai-creative-strategist` - Visual creative with separate reference files

Each demonstrates different approaches to skill structure.
