# Audience Targeting Skill

Your job is to build the complete audience targeting strategy for paid campaigns — Meta (Facebook/Instagram) and Google Ads. Who to target, how to layer interests and behaviors, what lookalikes to build, and how to sequence cold → warm → hot audiences through the funnel.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Target audience (Section 6) — demographics, psychographics, behaviors, pain points
- Industry and location (Sections 2–3) — defines geographic and demographic targeting
- Core offer (Section 9) — determines funnel stage and purchase intent
- Competitors (Section 10) — competitor audiences to target on Meta

If `/outputs/research/market-research-*.md` exists: read it — use market data on where the audience spends time online.
If `/outputs/strategy/campaign-brief-*.md` exists: read it — align targeting to campaign goal.

If brand.md doesn't exist: ask user for audience description, location, and offer before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified campaign goal and platform**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để build audience targeting, mình cần biết:
1. **Platform:** Meta (Facebook/Instagram) / Google / Cả hai?
2. **Campaign goal:** Awareness / Lead gen / Conversion?
3. **Budget/ngày:** Dưới 500k / 500k–2tr / Trên 2tr?
4. **Bạn đã có pixel/data không:** Website pixel đã có data chưa? Email list có không? Custom audience từ trước không?
5. **Địa lý:** TP.HCM only / Hà Nội / Toàn quốc?"

Wait for answer before continuing.

## Step 3 — Build targeting strategy

### Meta Audience Architecture

**3-layer funnel:**

**Layer 1 — Cold (Top of Funnel)**
Reach people who've never heard of the brand.

*Interest targeting — build clusters, not single interests:*
- Layer interests together (AND not OR where possible) to narrow to high-quality matches
- Vietnamese business interests to target for B2B:
  - Business owners: "Kinh doanh", "Khởi nghiệp", "Small business owners" (Meta behavior)
  - Digital marketing: "Digital marketing", "Content marketing", "Social media marketing"
  - AI/Tech: "Artificial intelligence", "Marketing automation", "SaaS"
  - Competitor pages: Target followers of competitor Facebook pages
  - Job titles (Meta): "Marketing Manager", "Founder", "CEO", "CMO" — via job field targeting

*Behavioral targeting:*
- "Business decision makers" (Meta behavior category)
- "Engaged shoppers" if selling product
- Device: Mobile-first for Vietnamese audience (>75% Facebook usage is mobile)

*Geographic precision:*
- TP.HCM: Target by district if budget is limited — Quận 1, 3, 7, Bình Thạnh, Tân Bình for B2B
- Hà Nội: Quận Hoàn Kiếm, Đống Đa, Cầu Giấy, Tây Hồ for SMB owners
- National: Use "currently living in" not "recently in" for local business targeting

**Layer 2 — Warm (Middle of Funnel)**
Re-engage people who've interacted with the brand.

Custom audiences to build:
- Website visitors (pixel required) — last 30 / 60 / 90 days
- Video viewers — watched 25%, 50%, 75% of any video
- Facebook/Instagram engagers — liked, commented, saved, messaged last 90 days
- Lead form openers (didn't submit) — last 30 days
- Email list upload — current subscribers

Retargeting message: Different from cold — they know you. Skip the education, go to proof and offer.

**Layer 3 — Hot (Bottom of Funnel)**
Convert people close to deciding.

- Website visitors who visited pricing/service page but didn't convert
- Lead form submitters (follow-up before they go cold)
- Cart abandoners (if ecommerce)
- Email list: opened last 3 emails (high intent signal)

### Lookalike Audiences (Meta)

Build from your best existing data in this priority order:
1. Purchasers/paying clients (1% LAL — highest quality)
2. Lead form submitters (2% LAL)
3. Website visitors last 60 days (3% LAL)
4. Video viewers 75%+ (3–5% LAL)
5. Page engagers last 90 days (5% LAL — largest, lowest quality)

Vietnamese market note: Start with 2–3% LAL — 1% is too narrow in Vietnam's smaller data pool. Scale to 5% if 2–3% CPL is acceptable.

### Google Audience Strategy

**Search — Intent-based (highest purchase intent):**
- Keyword targeting owns the intent signal — audience layering is secondary
- Add in-market audiences as observation (don't restrict, just bid adjust)
- Customer match: upload email list to increase bids for known prospects

**Display/YouTube — Audience-based:**
- Custom intent: people who searched competitor keywords in last 7 days
- In-market: "Business software", "Marketing services" (Google's categories)
- Similar audiences: built from your customer list or website visitors
- Affinity: "Business professionals", "Technology enthusiasts"

**Remarketing:**
- Website visitors: Standard remarketing with different creative per page visited
- YouTube viewers: 30%+ watch time → serve follow-up pre-roll

### Vietnamese audience targeting specifics

**Meta Vietnamese B2B signals:**
- "Chủ doanh nghiệp" interest
- Facebook groups: members of large Vietnamese business groups (can't target by group, but page admins can)
- Device: Android-heavy in Vietnam — ensure landing pages load fast on mid-range Android
- Connection type: 4G/LTE dominant — video ads must buffer fast or use shorter formats

**Budget allocation by funnel stage (recommended starting split):**
- Cold (prospecting): 60% of budget
- Warm (retargeting): 30% of budget
- Hot (conversion): 10% of budget

Adjust as pixel data builds — warm audience ROI typically improves after 30 days.

**Exclusions (always set):**
- Current customers (exclude from acquisition campaigns)
- Recent purchasers (last 30 days)
- Competitors (if you can identify their employee emails)
- Low-quality leads from previous campaigns (if you've tagged them)

## Step 4 — Write output

Save to `/outputs/assets/ads/audience-targeting-[campaign-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Audience Targeting Strategy — [Campaign Name]
> Generated: [date] | Platform: [Meta/Google/Both] | Goal: [goal] | Budget: [range]

---

## Meta Audience Plan

### Cold Audience — [Name]
**Size estimate:** [reach]
**Interests:**
- [Interest 1]
- [Interest 2]
**Behaviors:** [Meta behaviors]
**Demographics:** [age, gender, location]
**Exclusions:** [who to exclude]

---

### Warm Audience — [Name]
**Source:** [custom audience source]
**Lookback window:** [days]
**Size estimate:** [reach]

---

### Hot Audience — [Name]
**Source:** [high-intent signal]
**Size estimate:** [reach]
**Message shift:** [different angle vs cold]

---

### Lookalike Audiences
| Source | % | Est. Size | Priority |
|---|---|---|---|
| [source] | [%] | [size] | [1/2/3] |

---

## Google Audience Plan

### Search — Audience Layers
[In-market + customer match strategy]

### Display/YouTube
[Audience segments and bid adjustments]

---

## Budget Allocation
| Funnel Stage | % of Budget | Daily Budget (if [X] total) |
|---|---|---|
| Cold | 60% | [amount] |
| Warm | 30% | [amount] |
| Hot | 10% | [amount] |

---

## Scaling Signals
- Scale cold if: CPL <[amount] for 3+ days
- Scale warm if: Retargeting CVR >[%]
- Pause cold if: CPL >[amount] after [impressions]

---

## Notes
- Pixel status: [installed / not yet / needs events]
- Custom audience availability: [what exists now]
- Lookalike readiness: [when you'll have enough data]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Audience targeting strategy cho '[Campaign]' đã hoàn chỉnh.**

**Audiences built:**
- Cold: [n] audience segments — [est. total reach]
- Warm: [n] custom audiences
- Hot: [n] high-intent segments
- Lookalikes: [n] — ready when [data condition]

📁 Đã lưu vào: `/outputs/assets/ads/audience-targeting-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/ad-campaign-structure` để build campaign architecture sử dụng audiences này, hoặc `/ad-copy` để viết copy cho từng audience stage."

---
