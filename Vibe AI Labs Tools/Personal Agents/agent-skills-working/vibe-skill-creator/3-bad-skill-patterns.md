# Bad Skill Patterns (What to Avoid)

This document catalogs patterns that make skills mediocre. Study these to avoid them.

---

## Pattern 1: Documentation Voice

**The problem:** Skills that read like technical documentation instead of expertise.

### Example (Bad)

```markdown
## Email Sequence Generation

This skill enables the generation of email sequences for marketing purposes.

### Process Overview

1. Define the target audience
2. Determine the sequence objective
3. Create individual emails
4. Review and optimize

### Email Types

- Welcome emails
- Nurture emails
- Sales emails
- Re-engagement emails
```

### Why It Fails

- Sounds like a wiki article, not an expert
- No personality or point of view
- Tells you categories exist without teaching you how to think about them
- Claude could produce this without any skill at all

### What It Should Sound Like

```markdown
## Email Sequences

Most email sequences fail for one reason: they're written like marketing, not conversation.

The emails that convert? They sound like a smart friend who happens to have something you need. Not a funnel. Not a campaign. A person talking to another person.

Here's what separates sequences that make money from sequences that get ignored...
```

---

## Pattern 2: Procedure Over Principle

**The problem:** Step-by-step instructions that don't transfer thinking.

### Example (Bad)

```markdown
## How to Write a Landing Page

### Step 1: Write the Headline
Create a compelling headline that captures attention.

### Step 2: Write the Subheadline
Add a supporting subheadline that expands on the headline.

### Step 3: Add Social Proof
Include testimonials or trust badges.

### Step 4: Write the Body Copy
Explain your product or service benefits.

### Step 5: Create the CTA
Add a clear call-to-action button.
```

### Why It Fails

- Claude already knows these steps
- No guidance on WHAT makes each element good
- Doesn't explain WHY these steps work
- Produces compliant output, not excellent output

### What It Should Look Like

```markdown
## Landing Pages

The headline does 80% of the work. Caples proved one headline can outpull another by 19.5x. Everything else matters less than getting those 10-15 words right.

What separates good headlines from great:

**Specificity beats generality.**
- Generic: "Improve Your Productivity"
- Specific: "Get 4 Hours Back Every Week"

**Outcomes beat features.**
- Feature: "AI-Powered Task Management"
- Outcome: "Never Miss a Deadline Again"

The rest of the page exists to support the headline's promise...
```

---

## Pattern 3: Comprehensive Coverage

**The problem:** Trying to cover everything instead of focusing on what matters.

### Example (Bad)

```markdown
## Complete Social Media Content Guide

### Platform Overview
- Facebook: History, demographics, algorithm changes...
- Instagram: Stories, Reels, Feed posts, IGTV...
- Twitter: Character limits, threads, spaces...
- LinkedIn: Articles, posts, newsletters...
- TikTok: Trends, sounds, duets, stitches...
- Pinterest: Boards, pins, idea pins...
- YouTube: Shorts, long-form, community posts...

### Content Types
[500 lines on every possible content type]

### Posting Schedules
[200 lines on optimal posting times]

### Analytics
[300 lines on metrics for each platform]
```

### Why It Fails

- Information overload dilutes usefulness
- No guidance on what actually matters
- Claude gets lost weighing all factors equally
- User drowns in options instead of getting output

### What It Should Look Like

```markdown
## Social Content

Each platform has ONE thing that matters most:

| Platform | What Actually Matters |
|----------|----------------------|
| Instagram | Visual stopping power in 0.5 seconds |
| YouTube | Thumbnail + title (content is secondary to click) |
| LinkedIn | First line hook (expand button is everything) |
| Twitter | One clear, shareable idea per tweet |

Everything else is optimization. Nail these or nothing else matters.
```

---

## Pattern 4: Generic Tool References

**The problem:** Vague instructions that don't specify HOW to use tools.

### Example (Bad)

```markdown
## Image Generation

Use AI image generation tools to create visuals for your content.

### Available Tools
- DALL-E
- Midjourney
- Stable Diffusion
- Various other options

### Best Practices
- Use descriptive prompts
- Iterate on results
- Consider composition
```

### Why It Fails

- Doesn't specify WHICH tool to use
- No actual prompts or examples
- "Use descriptive prompts" is useless advice
- Claude will pick randomly or ask

### What It Should Look Like

```markdown
## Image Generation

**ALWAYS use Nano Banana Pro via Glif.**

| Model | Glif ID | Speed |
|-------|---------|-------|
| 🍌 Nano Banana Pro | `cmi7ne4p40000kz04yup2nxgh` | ~20sec |

**Do NOT use:** imagen-3, DALL-E, or direct Replicate calls unless specifically requested.

**Execution:**
```
mcp__glif__run_glif
id: cmi7ne4p40000kz04yup2nxgh
inputs: ["your natural language prompt here"]
```

**Prompt structure:**
"[Subject] in [setting], [lighting description], [artistic style], [mood/atmosphere]"
```

---

## Pattern 5: Missing Anti-Patterns

**The problem:** Only explaining what to do, not what to avoid.

### Example (Bad)

```markdown
## Writing Headlines

Good headlines are:
- Clear
- Compelling
- Concise
- Customer-focused

### Examples of Good Headlines
- "How to Win Friends and Influence People"
- "The 4-Hour Work Week"
```

### Why It Fails

- Claude's defaults often produce bad headlines
- Without explicit "don't do this," Claude will do it
- "Clear" and "compelling" aren't actionable
- No contrast to understand what good actually means

### What It Should Look Like

```markdown
## Headlines

What Claude gets wrong without guidance:

**AI slop patterns (avoid these):**
- "Unlock the Power of X" (generic hype)
- "Revolutionary Solution for Y" (empty claim)
- "Discover How to Z" (weak verb)
- "In Today's Fast-Paced World..." (dated opener)
- Questions that nobody actually asks

**Human patterns that work:**
- Specific numbers: "Save 4 Hours Every Week"
- Unexpected specificity: "At 60mph, the Loudest Noise..."
- Direct address: "You're Leaving Money on the Table"
- Curiosity gap: "What I Learned From 1,000 Sales Calls"

If your headline could describe any product, it describes none.
```

---

## Pattern 6: Friction Creation

**The problem:** Skills that produce intermediate outputs instead of final deliverables.

### Example (Bad)

```markdown
## Audience Research Skill

### Output Format

After analysis, I will provide:

1. **Audience Segments**
   - Demographic breakdowns
   - Psychographic profiles
   - Behavioral patterns

2. **Pain Point Analysis**
   - Primary frustrations
   - Secondary concerns
   - Underlying fears

3. **Language Patterns**
   - Common phrases
   - Objections
   - Motivational triggers

4. **Competitive Landscape**
   - Who else serves this audience
   - How competitors position
   - Gaps in the market

Use this research to inform your content creation.
```

### Why It Fails

- Creates a document that feels obligatory to use
- "Use this research" means MORE work, not less
- Comprehensive research creates pressure to be comprehensive
- The next step (writing) often gets WORSE with this input

### The Audience-Intel Lesson

We built this exact skill. The research it produced was excellent — detailed segments, specific pain points, real language patterns.

Then we wrote copy using that research. The copy was worse than copy written without it.

Why? The comprehensive research created obligation. Cover all segments. Address all pain points. Be thorough. The result: diluted, verbose, trying to do everything.

### What Works Instead

If research is needed, use a subagent that:
- Goes deep
- Returns a SUMMARY, not a document
- Hands back 3-5 key insights, not 30
- Gets out of the way

Or better: bake the research INTO the skill itself, so the expertise is embedded, not the raw research.

---

## Pattern 7: Over-Engineered Structure

**The problem:** Complex frameworks that add friction without adding value.

### Example (Bad)

```markdown
## Content Creation Framework

### Phase 1: Strategic Foundation
#### 1.1 Objective Definition Matrix
| Objective Type | Business Goal | Content Goal | Success Metric |
|----------------|---------------|--------------|----------------|
| Awareness | Brand recognition | Reach | Impressions |
| Consideration | Lead generation | Engagement | CTR |
| Conversion | Sales | Action | Conversion rate |

#### 1.2 Audience Mapping Protocol
Step 1: Define primary segment...
Step 2: Define secondary segment...
Step 3: Create overlap analysis...

### Phase 2: Content Architecture
#### 2.1 Message Hierarchy Framework
[Complex diagram of primary, secondary, tertiary messages]

#### 2.2 Channel-Content Matrix
[Grid of every channel vs every content type]

### Phase 3: Execution Protocol
[Another 500 lines of process]
```

### Why It Fails

- Framework bloat that nobody actually uses
- Claude gets lost in the structure
- User asked for content, got a project plan
- Complexity doesn't improve output

### What Works

Skip the framework. Transfer the thinking:

```markdown
## Content

One message. One audience. One action.

If you're trying to reach multiple audiences, you're reaching none.
If you're trying to say multiple things, you're saying nothing.
If you have multiple CTAs, you have no CTA.

Start with: Who exactly is this for, and what exactly should they do?

Everything else follows.
```

---

## Pattern 8: Theoretical Examples

**The problem:** Made-up examples instead of real ones.

### Example (Bad)

```markdown
## Product Descriptions

### Example
**Product:** Widget Pro 3000
**Description:** "The Widget Pro 3000 is an innovative solution that streamlines your workflow. With advanced features and intuitive design, it helps you accomplish more in less time."
```

### Why It Fails

- "Widget Pro 3000" is obviously fake
- The description is generic AI slop
- No contrast between good and bad
- Doesn't demonstrate the principles being taught

### What Works

Use real examples, or at least realistic transformations:

```markdown
## Product Descriptions

**Before (generic):**
"Streamline your workflow with our innovative solution. Advanced features help you accomplish more."

**After (specific):**
"Stop losing 3 hours a day to manual data entry. One click syncs your Salesforce contacts to your email platform. Your team gets back to selling. You stop babysitting spreadsheets."

The first could describe anything. The second describes one product solving one problem for one person.
```

---

## Pattern 9: Missing the WHY

**The problem:** Instructions without explanation.

### Example (Bad)

```markdown
## Email Subject Lines

### Rules
- Keep under 50 characters
- Use personalization
- Create urgency
- A/B test everything
- Avoid spam words
```

### Why It Fails

- Claude can follow rules but not adapt them
- No understanding of WHY these rules exist
- When rules conflict, Claude can't prioritize
- No principles to apply to edge cases

### What Works

```markdown
## Subject Lines

Mobile shows ~35 characters. Desktop shows ~60. Most people read email on phones. That's why subject lines should front-load the hook.

"[Name], your cart expires in 2 hours" puts the urgency first.
"Don't miss out — [Name], your cart expires soon" buries it.

Same content, different results. The principle: put the most important word in the first 4-5 words, because that's all many people see.
```

---

## Pattern 10: The "Just In Case" Addition

**The problem:** Including sections that don't improve output.

### Signs of This Pattern

- "We should probably include X for completeness"
- "What if someone needs Y?"
- "It would be more comprehensive with Z"
- Sections that exist but don't improve actual output

### Example

A copywriting skill that includes:
- History of direct response advertising
- Biography of Eugene Schwartz
- Complete list of cognitive biases
- Typography guidelines
- Legal disclaimer templates

None of these improve the copy Claude writes. They just make the skill longer.

### The Test

For every section, ask: **"Does removing this make the output worse?"**

If the answer is "no" or "probably not," remove it.

More skill ≠ better skill. Focused skill = better skill.

---

## The Meta-Pattern

All bad skills share one trait: they're written for comprehensiveness, not effectiveness.

Good skills are opinionated. They make choices. They say "do this, not that." They have voice and point of view. They transfer thinking, not information.

If your skill could be a Wikipedia article, it's not a skill. It's documentation.

Skills should make Claude think like an expert, not like an assistant following instructions.

---

## Quick Reference: Bad vs Good

| Bad Pattern | Good Pattern |
|-------------|--------------|
| Documentation voice | Domain expert voice |
| "Step 1, Step 2, Step 3" | Principles that transfer thinking |
| Comprehensive coverage | Ruthless focus |
| Generic tool references | Specific tools, IDs, prompts |
| Only what to do | What to do AND what to avoid |
| Intermediate documents | Final deliverables |
| Complex frameworks | Simple, actionable guidance |
| Theoretical examples | Real before/after |
| Rules without reasons | Principles with WHY |
| Everything "just in case" | Only what improves output |

If you recognize these patterns in your skill, refactor. The output will improve.
