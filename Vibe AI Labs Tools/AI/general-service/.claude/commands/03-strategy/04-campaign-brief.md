---
name: campaign-brief
description: Creates a structured campaign brief that all execution agents read before producing any content. Use this skill when the user wants to brief content writers, social media agents, or email agents on a specific campaign. Trigger whenever the user mentions campaign brief, briefing, creative brief, or wants to kick off a specific campaign.
---

# Campaign Brief Skill

Your job is to produce a single, structured brief that every execution agent reads before creating any content for this campaign. Think of it as the "single source of truth" for a specific campaign — just like brand.md is the source of truth for the brand.

## Step 1 — Read inputs

Read:
- `/outputs/profiles-output/brand.md` — voice, audience, positioning, key messages
- `/outputs/strategy/campaign-plan-*.md` — campaign goals, monthly themes (if exists)
- `/outputs/strategy/content-calendar-*.md` — specific content pieces planned (if exists)
- `/outputs/strategy/lead-magnets-*.md` — lead magnet being promoted (if exists)
- `/outputs/research/competitor-analysis-*.md` — angles to counter (if exists)

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User described the campaign**
Use their description. Go to Step 3.

**Path B — No campaign described**
Ask:
"Brief này cho chiến dịch nào?
1. Mô tả ngắn: tên chiến dịch, mục tiêu, thời gian chạy
2. Sản phẩm/dịch vụ đang quảng bá trong chiến dịch này?
3. Có offer đặc biệt không? (giảm giá, bonus, deadline)
4. Kênh chính: Facebook / TikTok / Email / Zalo / Tất cả?"

Wait for answers before continuing.

## Step 3 — Build the campaign brief

A campaign brief has 8 components:

### 1. Campaign Overview
- Campaign name (memorable, internal use)
- Campaign goal (one primary goal — awareness / leads / conversion)
- Duration (start date → end date)
- Budget range (if known)

### 2. The Offer
- What exactly is being promoted
- Price + any special incentive
- Deadline or scarcity (if applicable)
- Guarantee or risk-reversal

### 3. Target Audience (from brand.md + campaign-specific)
- Primary segment for this campaign
- Where they are in the buying journey (cold / warm / hot)
- Their #1 pain point this campaign addresses
- Their biggest objection to buying

### 4. Core Message
- The single sentence this campaign comes back to
- Tone direction for this campaign (urgent / educational / inspirational / proof-driven)
- What NOT to say (off-brand angles for this campaign)

### 5. Proof Points
- 2–3 specific stats, results, or testimonials to reference
- The strongest single proof point — the one that closes skeptics

### 6. Content Direction
- Hook angles to test (3 different opening lines/hooks)
- Content formats for each platform
- Emotional arc: awareness → interest → desire → action
- CTAs at each stage

### 7. Platform-Specific Instructions
For each active platform:

**Facebook:**
- Post frequency
- Format mix (text / image / video / carousel)
- Targeting notes (if running ads)
- Boosting budget recommendation

**TikTok:**
- Video length and style
- Hook structure (first 3 seconds)
- Trending sounds or formats to use
- Hashtag strategy

**Zalo:**
- Broadcast timing
- Message tone (more personal)
- ZNS or OA notes if applicable

**Email:**
- Sequence length
- Subject line direction
- Send timing

### 8. Success Metrics
- Primary KPI (the one number that defines success)
- Secondary metrics to track
- What "good" looks like vs "needs adjustment"
- Review checkpoint: when to evaluate and optimize

## Step 4 — Write output

Save to `/outputs/strategy/campaign-brief-[campaign-name]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Campaign Brief — [Campaign Name]
> Brand: [Brand Name] | Created: [date] | Status: Active

---

## 1. Campaign Overview
- **Name:** 
- **Goal:** 
- **Duration:** [start] → [end]
- **Budget:** 

---

## 2. The Offer
- **What:** 
- **Price:** 
- **Incentive:** 
- **Deadline:** 
- **Guarantee:** 

---

## 3. Target Audience
- **Segment:** 
- **Funnel stage:** Cold / Warm / Hot
- **Primary pain point:** 
- **Primary objection:** 

---

## 4. Core Message
- **Campaign headline:** 
- **One-sentence core message:** 
- **Tone:** 
- **Do NOT say:** 

---

## 5. Proof Points
- 
- 
- **Strongest single proof:** 

---

## 6. Content Direction

**3 Hook angles to test:**
1. 
2. 
3. 

**Emotional arc:**
- Awareness → [emotion/insight to trigger]
- Interest → [what makes them lean in]
- Desire → [what makes them want it]
- Action → [what removes final hesitation]

**CTAs by stage:**
- Cold audience: 
- Warm audience: 
- Hot audience: 

---

## 7. Platform Instructions

### Facebook
- Frequency: 
- Format mix: 
- Targeting: 
- Boost budget: 

### TikTok
- Video length: 
- Hook structure: 
- Hashtags: 

### Zalo
- Broadcast timing: 
- Tone: 

### Email
- Sequence: 
- Subject direction: 
- Send timing: 

---

## 8. Success Metrics
- **Primary KPI:** 
- **Secondary metrics:** 
- **Review checkpoint:** 
- **"Good" benchmark:** 
- **"Needs adjustment" signal:** 
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Campaign brief cho '[Campaign Name]' đã hoàn chỉnh.**

**Overview:**
- Goal: [goal]
- Duration: [dates]
- Core message: [one sentence]
- Primary platform: [platform]

📁 Đã lưu vào: `/outputs/strategy/campaign-brief-[name]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chia sẻ file này với execution agents:
- `/blog-writer` — để viết bài blog theo brief này
- `/social-copy` — để viết caption Facebook/TikTok
- `/email-sequence` — để viết chuỗi email"

---
