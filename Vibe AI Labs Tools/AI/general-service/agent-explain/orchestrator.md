# Orchestrator — Deep Dive

## What this agent does

The Orchestrator is the traffic controller for the entire 15-agent system. It doesn't write marketing content — it decides which agent writes it, in what order, and makes sure nothing runs before its prerequisites are met. It's the first agent you talk to when you don't know what to do next, and the last piece that ties all 15 agents into a coherent system.

---

## Why the Orchestrator is built last

Every other agent was designed with the Orchestrator in mind — specific I/O paths, clear skill triggers, consistent output formats. Building the Orchestrator last means it can map the actual system as it exists, not an idealized version.

If the Orchestrator were built first, it would route to agents that didn't match the actual skill structures. Built last, it can route precisely to every skill that actually exists.

---

## Two modes of operation

### Mode 1 — Direct routing (most common)

User asks for something specific. Orchestrator maps it to the correct agent and skill, then runs it.

```
User: "Write me 3 cold emails for Vietnamese SMB owners"
Orchestrator: reads brand.md → routes to agent-11-cold-outreach /cold-email → done
```

### Mode 2 — State check and recommendation

User asks "what should I do next?" or is new to the system. Orchestrator checks what files exist in `/outputs/`, diagnoses the current state, and recommends the next logical step.

```
User: "What should I work on this week?"
Orchestrator: checks /outputs/ → finds brand.md + research but no campaign brief
→ "Strategy is missing. Run /campaign-planning."
```

---

## System state check logic

The Orchestrator checks 7 layers in sequence:

| Layer | Check | Missing action |
|---|---|---|
| 1 | brand.md exists? | Route to /brand-setup |
| 2 | Research files in /outputs/research/? | Recommend /market-research |
| 3 | Campaign brief in /outputs/strategy/? | Recommend /campaign-planning |
| 4 | Execution assets in /outputs/assets/? | Route to relevant execution agent |
| 5 | Distribution in /outputs/distribution/? | Recommend /content-atomizer |
| 6 | Performance in /outputs/performance/? | Recommend /weekly-report |
| 7 | brand.md updated in 30 days? | Recommend feedback loop |

Output is a clear diagnostic with ✅/⚠️/❌ status per layer and one specific recommendation.

---

## Workflow enforcement

**The gate rules:**

1. **brand.md gate:** No execution agent runs until brand.md exists. Hard rule.

2. **Research gate (soft):** If user skips research, Orchestrator flags it but doesn't block. "Kết quả tốt hơn nếu chạy /market-research trước — bạn muốn proceed không?"

3. **Strategy gate (soft):** If user jumps to content without campaign strategy, Orchestrator asks if they want to align first.

4. **Data gate for feedback:** Feedback skills require at least one monthly-review. Running audience-update without data = guess, not improvement.

5. **Human review reminder:** Outputs land in `/outputs/` — system proposes, human decides.

---

## Full workflow sequence

When a user wants a complete campaign built end-to-end:

```
Phase 1: Foundation
Brand setup + Market research + Competitor analysis

Phase 2: Strategy
Campaign planning + Campaign brief + Content calendar

Phase 3: Assets (parallel-eligible)
Content + SEO + Email + Social + Ads + Video + Outreach + Sales + CRO

Phase 4: Distribution
Content atomizer + Platform formatter

Phase 5: Performance (weekly/monthly)
Weekly report + Campaign report + ROI calculator

Phase 6: Feedback (end of month)
Audience update + Messaging refinement + Positioning evolution + Monthly strategy review

↺ Cycle repeats with updated brand.md
```

The Orchestrator presents this plan and asks for confirmation before starting. It identifies where in the sequence the user currently is and starts from there — never from scratch if work already exists.

---

## Model choice

The Orchestrator runs on `claude-opus-4-7` — the most capable model. This is intentional. The Orchestrator makes judgment calls about:
- Which agent is the right fit for an ambiguous request
- Whether to proceed without research or block
- How to sequence a complex multi-agent run
- What the system state is and what it means

These decisions require more reasoning than content generation. All 15 execution agents run on `claude-sonnet-4-5` (fast, capable for structured outputs). The Orchestrator runs on Opus because routing correctly is more expensive than running the individual skill.

---

## What the Orchestrator doesn't do

- Doesn't write content (delegates to execution agents)
- Doesn't make strategic decisions (presents options, human decides)
- Doesn't run parallel agents that have dependencies on each other
- Doesn't skip brand.md check — ever
- Doesn't run multi-agent sequences without user confirmation

---

## Single-agent mode

Most users don't need the Orchestrator for simple requests. Any agent can be called directly:

```
/blog-writer → goes straight to agent-05-content
/social-copy → goes straight to agent-08-social
/campaign-report → goes straight to agent-14-performance
```

The Orchestrator's value shows up when:
- The user doesn't know which agent to use
- The user wants a full campaign, not just one asset
- Something is missing upstream and needs to be diagnosed
- The user asks "what should I do next?"
