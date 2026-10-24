# System Refinement

This file is the feedback loop. It reads `performance.md` and applies improvements back into the system — making the agent smarter over time.

This is what separates a static template from a living system.

---

## Refinement Workflow

Run this process every Friday after filling `performance.md`:

```
Read performance.md
    ↓
Identify what changed (voice, hooks, topics, platforms)
    ↓
Update the relevant files
    ↓
Log the change below
```

---

## What to Update and Where

| If you found... | Update this file |
|----------------|-----------------|
| Your tone sounds off on a platform | `4-voice/01-platform-tone.md` |
| A hook type consistently underperforms | `3-engine/01-hooks.md` — mark as low performer |
| A hook type consistently overperforms | `3-engine/01-hooks.md` — add more variants |
| Your audience description is wrong | `1-customer/03-builders.md` or `casual.md` |
| Your brand voice has evolved | `1-customer/02-brand-voice.md` |
| Platform rules have changed (algo update) | `2-platforms/[platform].md` |
| A new content format is working | `3-engine/03-content-types.md` |
| Posting times are off | `3-engine/04-scheduling.md` |

---

## Refinement Log

Track every change made to the system here.

| Date | File Updated | What Changed | Why |
|------|-------------|-------------|-----|
| | | | |

---

## Brand Voice Evolution

When your voice evolves, document it here before updating `brand-voice.md`:

**Before:**
[old voice description]

**After:**
[new voice description]

**Why it changed:**
[what performance data triggered this]

---

## Hook Graveyard

Hooks that have been retired and why:

| Hook | Platform | Reason Dropped |
|------|----------|---------------|
| | | |

---

## Hook Hall of Fame

Hooks that consistently outperform — study these:

| Hook | Platform | Why It Works |
|------|----------|-------------|
| | | |

---

## Quarterly System Review

Every 3 months, run a deeper audit:

1. Re-read `1-customer/02-brand-voice.md` — does it still sound like you?
2. Re-read `1-customer/03-builders.md` + `casual.md` — has your audience shifted?
3. Check every platform file — have platform rules changed?
4. Review Hook Hall of Fame — are these still working?
5. Review Hook Graveyard — should any be reinstated?

The system should feel noticeably smarter after each quarterly review.
