# Ad Campaign Structure Skill

Your job is to design the complete campaign architecture — campaign → ad set → ad level — for Meta and Google campaigns. The right structure prevents budget waste, enables clean testing, and makes optimization decisions obvious instead of guesswork.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — defines campaign objective and conversion event
- Target audience (Section 6) — informs ad set segmentation
- Location (Section 3) — geographic structure decisions

If `/outputs/assets/ads/audience-targeting-*.md` exists: use the audience segments already defined.
If `/outputs/assets/ads/ad-copy-*.md` exists: map copy versions to ad sets.
If `/outputs/strategy/campaign-brief-*.md` exists: align structure to campaign goal and timeline.

If brand.md doesn't exist: ask user for offer, budget, platform, and goal before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified campaign type, budget, and platform**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để build campaign structure, mình cần biết:
1. **Campaign mục tiêu:** Lead gen / Conversion / Awareness / Traffic?
2. **Platform:** Meta / Google / Cả hai?
3. **Budget/tháng:** [amount] — để mình chia budget đúng
4. **Có data pixel chưa:** Pixel installed + có conversion events chưa?
5. **Timeline:** Campaign chạy bao lâu? (1 tuần / 1 tháng / ongoing)"

Wait for answer before continuing.

## Step 3 — Design campaign structure

### Meta Campaign Architecture

**Campaign level — one objective per campaign:**

| Goal | Campaign Objective | Conversion Event |
|---|---|---|
| Book consultation | Leads | Lead form submit / Messenger |
| Website sign-up | Leads | CompleteRegistration |
| Purchase | Sales | Purchase |
| Content views | Traffic | Landing page views |
| Brand awareness | Awareness | Reach / Video views |

**Ad Set level — one audience variable per ad set:**

The fundamental rule: **test one variable at a time**. Each ad set changes only one thing. This is how you learn what actually drives performance.

Structure options:

*Option A — Audience testing (most common starting point):*
```
Campaign: Lead Gen — [Brand Name]
├── Ad Set 1: Cold — Interest (AI + Marketing)
├── Ad Set 2: Cold — Interest (Business owners + Tech)
├── Ad Set 3: Cold — Lookalike 2% from website visitors
└── Ad Set 4: Warm — Website visitors 30 days
```

*Option B — Funnel structure (when you have pixel data):*
```
Campaign 1: Prospecting (60% budget)
├── Ad Set 1: Broad cold — interest clusters
└── Ad Set 2: Lookalike 2%

Campaign 2: Retargeting (30% budget)
├── Ad Set 1: Engagers 90 days
└── Ad Set 2: Website visitors 60 days

Campaign 3: Conversion (10% budget)
└── Ad Set 1: Hot — pricing page visitors + email list
```

*Option C — Advantage+ Campaign Shopping / Lead (Meta's AI structure):*
Use when: You have 50+ conversions/week and trust Meta's algorithm.
Structure: Fewer ad sets, more creative variations, let Meta optimize.
Vietnamese market note: Less control, can work well at scale (>10tr/month budget).

**Ad level — creative variations:**
- 2–4 ads per ad set minimum for creative testing
- Label clearly: `[Audience]-[Copy version]-[Creative format]`
- Example: `Cold-PainLed-StaticImage`, `Cold-ProofLed-Video15s`

**Budget rules:**
- Minimum per ad set: 200k VND/day (below this, Meta can't exit learning phase)
- Learning phase: ~50 optimization events — don't touch structure for first 7 days
- Scale winner: Increase budget max 20% every 2 days to avoid re-entering learning

**Vietnamese Meta specifics:**
- Advantage+ placements: ON for Vietnam — Instagram often delivers cheaper CPL than Facebook feed
- Messenger placement: High performer in Vietnam — Vietnamese buyers prefer messaging over forms
- Lead forms vs website: Native lead forms (Instant Leads) convert better in Vietnam for cold audiences because they reduce friction and don't require fast mobile connections

### Google Campaign Architecture

**Campaign types for Vietnamese SMB services:**

*Search campaign (highest intent):*
```
Campaign: Search — Brand Keywords
└── Ad Group: [Brand name] + variations

Campaign: Search — Service Keywords
├── Ad Group: [Primary service] keywords
├── Ad Group: [Competitor] keywords (if budget allows)
└── Ad Group: [Problem-aware] keywords
```

*Performance Max (when ready):*
- Requires: 30+ conversions in last 30 days before launching
- Feeds from: headlines, descriptions, images, videos
- Structure: One campaign per offer (don't mix offers)

**Keyword match type strategy:**
- Start: Exact + Phrase match only — control over what triggers ads
- Expand: Add broad match modifiers once you have 30+ conversion data
- Negative keywords: Build list from day 1 — prevents wasted spend

**Ad group structure:**
- One theme per ad group (5–15 tightly related keywords)
- 3 Responsive Search Ads minimum per ad group
- All headlines and descriptions should be mix-and-matchable

**Google campaign for Vietnamese market:**
- Vietnamese keywords in both Latin (doanh nghiep) and full form (doanh nghiệp) — Google treats differently
- Location: TP.HCM + Hà Nội bid +20% vs other provinces for B2B
- Schedule: Mon–Fri 8am–6pm higher bids, evenings lower (B2B decision makers work hours)
- Device: Desktop bid +10% for B2B (decision makers on desktop), mobile -20% for complex offers

### Campaign naming convention

Consistent naming prevents confusion when managing multiple campaigns:

```
[Platform]-[Goal]-[Audience]-[Offer]-[Date]

Examples:
META-LEADS-COLD-CONSULT-2026Q2
META-LEADS-WARM-CONSULT-2026Q2
GGL-SEARCH-BRAND-SETUP-2026Q2
GGL-SEARCH-SERVICE-SETUP-2026Q2
```

## Step 4 — Write output

Save to `/outputs/assets/ads/ad-campaign-structure-[campaign-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Ad Campaign Structure — [Campaign Name]
> Generated: [date] | Platform: [Meta/Google] | Budget: [total/month] | Timeline: [dates]

---

## Meta Structure

### Campaign 1 — [Name] ([objective])
**Daily budget:** [amount]
**Optimization event:** [event]

#### Ad Set 1 — [Name]
**Audience:** [description]
**Budget:** [amount/day]
**Placements:** [Advantage+/Manual]
**Ads:**
- Ad A: [label] — [copy version] + [creative]
- Ad B: [label] — [copy version] + [creative]

#### Ad Set 2 — [Name]
[Repeat]

---

### Campaign 2 — [Name]
[Repeat]

---

## Google Structure

### Campaign 1 — [Name] ([type])
**Daily budget:** [amount]
**Bidding:** [strategy]

#### Ad Group 1 — [Theme]
**Keywords:**
- [keyword] [match type]
- [keyword] [match type]
**Negative keywords:** [list]
**Ads:** 3 RSAs minimum

---

## Budget Summary
| Campaign | Platform | Daily | Monthly |
|---|---|---|---|
| [name] | [platform] | [amount] | [amount] |
| **Total** | | [total/day] | [total/month] |

---

## Launch Checklist
- [ ] Pixel installed and firing correctly
- [ ] Conversion events verified in Events Manager
- [ ] All audiences created and sized
- [ ] Creative assets uploaded
- [ ] Copy approved
- [ ] UTM parameters on all landing page URLs
- [ ] Notification: check performance after 48 hours (not before)

---

## Optimization Schedule
- Day 2: Check for disapprovals, delivery issues
- Day 7: First performance review — pause underperforming ads (not ad sets yet)
- Day 14: Ad set performance review — reallocate budget
- Day 30: Full campaign review — scale winners, kill losers
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Ad campaign structure cho '[Campaign]' đã hoàn chỉnh.**

**Structure:**
- [n] campaigns — [objectives]
- [n] ad sets — [audience split]
- [n] ads planned
- Total budget: [amount]/month

📁 Đã lưu vào: `/outputs/assets/ads/ad-campaign-structure-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/ab-test-setup` để design testing protocol, hoặc review checklist và launch."

---
