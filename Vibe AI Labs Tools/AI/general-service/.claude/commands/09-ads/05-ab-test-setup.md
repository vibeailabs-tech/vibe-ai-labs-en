# A/B Test Setup Skill

Your job is to design statistically sound A/B tests for paid ads — what to test, how to isolate variables, what sample size is needed, and what the winner condition is. Bad A/B tests waste budget and teach you nothing. This skill prevents that.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — conversion goal determines the test metric
- Target audience (Section 6) — audience size affects minimum test budget

If `/outputs/assets/ads/ad-copy-*.md` exists: identify copy variations already written.
If `/outputs/assets/ads/ad-creative-*.md` exists: identify creative concepts available to test.
If `/outputs/assets/ads/ad-campaign-structure-*.md` exists: check test structure already planned.

If brand.md doesn't exist: ask user for offer, current performance baseline, and what they want to test before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified what to test**
Use their direction. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để setup A/B test, mình cần biết:
1. **Test variable:** Bạn muốn test gì? (creative / headline / audience / landing page / offer)
2. **Baseline hiện tại:** CPL / CTR hiện tại là bao nhiêu? (nếu có)
3. **Budget test:** Bạn có thể dành bao nhiêu budget cho test này?
4. **Platform:** Meta / Google?
5. **Improvement goal:** Bạn muốn improve metric nào bao nhiêu %?"

Wait for answer before continuing.

## Step 3 — Design the A/B test

### The fundamental rule: test ONE variable at a time

Testing headline AND creative AND audience simultaneously tells you nothing. You won't know which variable drove the change. Every test must isolate exactly one element.

**Testable variables by priority (test in this order):**

1. **Creative concept** — biggest impact, test first
   - Static image vs video
   - Pain-led visual vs outcome-led visual
   - Person in ad vs no person

2. **Hook / headline** — second biggest lever
   - Pain angle vs benefit angle vs social proof angle
   - Question vs statement vs number lead

3. **Audience** — third (after you know what creative works)
   - Cold interest cluster A vs cluster B
   - Lookalike 1% vs 2% vs 3%
   - Age range split

4. **Landing page / offer** — test last (most expensive to change)
   - Free consult vs lead magnet
   - Long form vs short form
   - Price anchoring variation

5. **Ad format** — quick test, clear signal
   - Single image vs carousel
   - 15s video vs 30s video

### Sample size and budget requirements

**Meta minimum for statistical significance:**

| Metric | Min impressions needed | Min conversions needed |
|---|---|---|
| CTR | 5,000 per variant | N/A |
| CPC | 5,000 per variant | N/A |
| CPL (lead forms) | N/A | 50 per variant |
| CPL (website) | N/A | 100 per variant |
| Purchase CVR | N/A | 50 per variant |

**Budget estimation:**
- If current CPL = 200k VND → need 50 conversions → need 10tr per variant → 20tr total test budget
- If you can't afford 50 conversions per variant, test CTR/CPC instead (cheaper, faster, directional signal)

**Vietnamese market note:** Meta's learning phase requires ~50 optimization events per ad set. Plan test budgets around this — tests below minimum budget just teach Meta's algorithm, not you.

### Test duration

- Minimum: 7 days (capture full weekly cycle — weekend behavior differs from weekday)
- Maximum: 30 days (performance often degrades after 3–4 weeks due to creative fatigue)
- Don't end early even if one variant looks like a clear winner — wait for the full sample

### Meta A/B Test feature vs manual test

**Meta A/B Test (Experiments tool):**
- Best for: Clean, controlled tests with budget split
- Pros: Meta handles traffic split evenly, no audience overlap
- Cons: Takes longer, minimum budget requirements
- Use for: Creative tests, audience tests when budget >5tr/day

**Manual test (duplicate ad sets):**
- Best for: Quick directional tests with smaller budgets
- Pros: Faster to set up, more flexible
- Cons: Some audience overlap possible
- Use for: Copy variations, quick creative tests, budget <2tr/day

### Winner condition framework

Define the winner BEFORE launching. Don't change criteria mid-test.

| Test type | Primary metric | Winner condition | Confidence level |
|---|---|---|---|
| Creative | CPL | >20% lower CPL | After 50 conversions each |
| Copy angle | CTR | >15% higher CTR | After 5,000 impressions each |
| Audience | CPL + LTV proxy | >20% lower CPL | After 50 conversions each |
| Landing page | CVR | >10% higher CVR | After 100 visitors each |

**"Too close to call" rule:** If variants are within 10% of each other after full sample, call it a tie. Keep the one with better brand alignment, don't declare a winner.

### What to do after the test

- **Clear winner:** Scale winner, pause loser, run next test on the winning variant
- **Tie:** Run secondary metric analysis (CPC, quality of leads), keep both or default to brand preference
- **Winner underperforms baseline:** Both were bad — rethink the angle entirely, don't optimize further

## Step 4 — Write output

Save to `/outputs/assets/ads/ab-test-[test-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# A/B Test Setup — [Test Name]
> Generated: [date] | Platform: [platform] | Variable: [what's being tested] | Budget: [amount]

---

## Test Overview

**Hypothesis:** If we [change X], then [metric] will [improve/decrease] by [%] because [reason].

**Variable being tested:** [exactly one variable]
**Everything else:** Identical between variants

---

## Variant A — Control
**Description:** [What this is]
**Key element:** [The specific thing being tested in this variant]

---

## Variant B — Test
**Description:** [What this is]
**Key element:** [The specific thing being tested in this variant — different from A]

---

## Test Parameters

**Platform:** [Meta/Google]
**Test method:** [Meta Experiments / Manual duplicate]
**Budget per variant:** [amount/day]
**Test duration:** [start date] → [end date] ([n] days)
**Traffic split:** 50/50

---

## Sample Size Requirements

**Primary metric:** [metric]
**Minimum per variant:** [n conversions / n impressions]
**Estimated budget to reach minimum:** [amount]

---

## Winner Condition

**Primary:** Variant [X] wins if [metric] is >[threshold] better after [n] events
**Secondary (tiebreaker):** [secondary metric]
**Too close to call:** Within [10%] → [decision rule]
**End test if:** Either variant reaches [n] minimum OR [n] days pass — whichever comes first

---

## Decision Rules

| Result | Action |
|---|---|
| Variant B wins | Scale B, pause A, run next test on B |
| Variant A wins | Keep A, document why B failed, try different approach |
| Tie | Keep A (control), move to next variable |
| Both underperform | Pause both, rethink angle |

---

## Tracking Setup

- [ ] UTM parameters: `?utm_source=[platform]&utm_medium=paid&utm_campaign=[name]&utm_content=[variant-a/b]`
- [ ] Conversion event verified firing
- [ ] Both variants in same campaign (no budget favoritism)
- [ ] All other variables confirmed identical
- [ ] Calendar reminder set for [end date]

---

## Notes
- Do NOT check results before Day 7
- Do NOT increase budget mid-test (resets learning)
- Do NOT add new creatives mid-test
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **A/B test setup cho '[Test Name]' đã hoàn chỉnh.**

**Test:**
- Variable: [what's being tested]
- Variants: A ([control]) vs B ([test])
- Duration: [n] days
- Budget needed: [amount] total
- Winner condition: [primary metric] >[threshold] after [n] events

📁 Đã lưu vào: `/outputs/assets/ads/ab-test-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Launch campaign với structure đã có, hoặc chạy `/ad-campaign-structure` nếu chưa build structure."

---
