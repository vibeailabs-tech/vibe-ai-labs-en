# Agent 09 — Ads Agent
> Deep-dive explanation | Layer 3 — Execution

## What this agent does

The Ads Agent produces everything needed to run paid campaigns — before the first dollar is spent. Creative briefs, ad copy in 3 angles, audience targeting strategy, campaign architecture, A/B test protocols, and Google PMax asset briefs.

It does not connect to Meta Ads or Google Ads APIs to launch or read campaigns — that's the Performance Agent's job. The Ads Agent is a creative and strategy writing agent. APIs are added later.

---

## 6 Skills

### 1. `/ad-creative` — Visual Direction Briefs
**What it does:** Writes creative direction for paid ad visuals across Facebook/Instagram, TikTok, and Google Display. Produces 3 concepts minimum per campaign, each with: visual concept, text overlay, hook/first frame, platform specs, production notes, and why-this-works justification.

**The 6th element matters:** "Why this will work" forces the brief writer to justify the creative choice based on audience insight. Without this, creative becomes guesswork. With it, it becomes a hypothesis you can test.

**Vietnamese insight:** Foreign stock photos underperform significantly in Vietnamese ads. Vietnamese faces, familiar environments, and local context increase CTR. The brief always flags this.

**Output:** `/outputs/assets/ads/ad-creative-[slug].md`

---

### 2. `/ad-copy` — All Ad Copy Components
**What it does:** Writes 3 copy versions (pain-led, proof-led, contrarian) for each campaign — covering primary text, headlines, descriptions, and CTA buttons for Meta; on-screen text and captions for TikTok; and 10 headlines + 4 descriptions for Google Search.

**3 angles, not 1:** Most brands write one version of ad copy and wonder why it underperforms. Different audience segments respond to different angles. Pain-led works for cold audiences who don't know the solution exists. Proof-led works for warm audiences who need confirmation. Contrarian works for educated audiences who've heard every pitch.

**Negative qualifier copy:** The skill includes a specific technique — write copy that filters out wrong-fit buyers. "Dành cho doanh nghiệp đang trả >$300/tháng cho agency" tells bad-fit prospects they're not the target, reducing irrelevant clicks and CPL waste.

**Output:** `/outputs/assets/ads/ad-copy-[slug].md`

---

### 3. `/audience-targeting` — Meta + Google Audience Strategy
**What it does:** Builds the complete 3-layer audience funnel — cold (prospecting), warm (retargeting), hot (conversion) — with interest clusters, behavioral signals, lookalike audiences, and budget allocation recommendations.

**The lookalike priority order matters:**
1. Purchasers (best)
2. Lead form submitters
3. Website visitors
4. Video viewers 75%+
5. Page engagers (worst quality)

This order is often reversed by inexperienced advertisers who build from page engagers because they have the most data. The skill enforces the correct priority.

**Vietnamese-specific:** Start with 2–3% lookalike — 1% is too narrow for Vietnam's smaller data pool. Metro district targeting for B2B (Quận 1, 3, 7 in TPHCM).

**Output:** `/outputs/assets/ads/audience-targeting-[slug].md`

---

### 4. `/ad-campaign-structure` — Campaign Architecture
**What it does:** Designs the campaign → ad set → ad hierarchy with naming convention, budget allocation per layer, and launch checklist.

**The structure prevents a common mistake:** Brands often put all audiences in one campaign, making it impossible to control budget allocation or understand which audience drives performance. This skill enforces clean separation: one variable per ad set, one objective per campaign.

**Budget rule:** 200k VND/day minimum per ad set — below this, Meta can't exit the learning phase (50 optimization events needed). Many small Vietnamese businesses under-fund ad sets and blame the platform when it's actually a structural problem.

**Naming convention:** `META-LEADS-COLD-CONSULT-2026Q2` — platform, goal, audience stage, offer, quarter. Anyone looking at the account knows exactly what each campaign does.

**Output:** `/outputs/assets/ads/ad-campaign-structure-[slug].md`

---

### 5. `/ab-test-setup` — Statistically Sound Test Design
**What it does:** Designs A/B tests with proper variable isolation, sample size requirements, duration, and pre-defined winner conditions.

**The core problem it solves:** Most "A/B tests" in Vietnamese SMB marketing are not A/B tests — they're "we ran two ads and one performed better." Without controlling for variables, sample size, and duration, you learn nothing. This skill forces proper test design.

**Key discipline:** Define the winner condition BEFORE launching. Never change criteria mid-test. Never end early because one variant looks like a winner. The "too close to call" rule (within 10% = tie) prevents false positives.

**Priority order for what to test:** Creative concept first (biggest impact) → Copy angle → Audience → Landing page. Most brands test landing pages first because they're obvious, but creative is where the biggest gains hide.

**Output:** `/outputs/assets/ads/ab-test-[slug].md`

---

### 6. `/google-pmax-brief` — Performance Max Complete Asset Brief
**What it does:** Writes all 15 headlines, 5 long headlines, 5 descriptions, image briefs in 3 ratios, video briefs, audience signals, sitelinks, and callouts needed to launch a Google PMax campaign.

**Why PMax needs its own skill:** PMax requires more upfront assets than any other Google campaign type. Brands who don't prepare all assets get auto-generated creatives from Google — these are typically poor quality and can undermine campaign performance. This skill ensures nothing is missing.

**The 15 headline rule:** Each headline must make standalone sense because Google combines them randomly. Headlines with wordplay or context-dependent meaning break when mixed with unrelated headlines. The skill writes 3 headlines per angle (5 angles) to ensure variety without incoherence.

**PMax readiness requirement:** PMax performs best with 30+ conversions/month as a baseline. The skill notes this — brands without data are better served by Search + Display campaigns first.

**Output:** `/outputs/assets/ads/google-pmax-brief-[slug].md`

---

## No APIs Required (Now)

Agent 09 produces all ad assets without API access. Meta Ads API and Google Ads API are planned integrations for:
- Reading live campaign performance data → Performance Agent
- Automated campaign creation → future upgrade
- Creative performance benchmarks → future upgrade

The writing workflow is complete without them. Add APIs when ready to automate or read data.

---

## Layer Position and Data Flow

```
brand.md (L1) ─────────────────────────┐
campaign-brief.md (L2) ────────────────┤
CRO landing pages (L3) ────────────────┤──→ Agent 09 Ads ──→ /assets/ads/
Social creative briefs (L3) ───────────┘
                                                   ↓
                                        Performance Agent (L4)
                                        → campaign reports, ROI data
```

**Key dependency:** Ads Agent should run AFTER the CRO Agent has built the landing page. Sending paid traffic to a poorly converting page is the most common and expensive paid ads mistake.

---

## Recommended Campaign Launch Sequence

```
1. /audience-targeting → define who
2. /ad-creative → brief what to show
3. /ad-copy → write what to say (3 angles)
4. /ad-campaign-structure → organize everything
5. /ab-test-setup → design what to learn
6. /google-pmax-brief → if adding Google PMax
```

Then: produce assets → launch → Performance Agent tracks results → Feedback Agent updates brand.md.

---

## What This Agent Doesn't Do

- Launch campaigns to Meta or Google (no API yet)
- Read campaign performance data (Performance Agent)
- Create actual images or videos (writes briefs, doesn't produce)
- Manage active campaigns (manual or future automation)
- Write landing page copy (CRO Agent)
