# Google Performance Max Brief Skill

Your job is to write a complete asset brief for Google Performance Max (PMax) campaigns — all headlines, descriptions, images, videos, and audience signals needed to launch. PMax requires more upfront asset preparation than any other campaign type. This skill makes sure nothing is missing and every asset is optimized.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — PMax needs one clear conversion goal per campaign
- USP (Section 8) — headlines must communicate differentiators
- Target audience (Section 6) — informs audience signals
- Key messages (Section 11) — drives headline and description angles
- Competitors (Section 10) — informs asset messaging

If `/outputs/assets/ads/ad-copy-*.md` exists: pull strongest headlines and descriptions from there.
If `/outputs/assets/ads/audience-targeting-*.md` exists: use audience signals already defined.

If brand.md doesn't exist: ask user for offer, conversion goal, and key differentiators before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified offer and conversion goal**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để build PMax brief, mình cần biết:
1. **Conversion goal:** Bạn muốn PMax optimize cho gì? (lead form submit / phone call / purchase / consultation booking)
2. **Offer:** Campaign này promote gì cụ thể?
3. **Budget:** PMax cần bao nhiêu/ngày?
4. **Có conversion data không:** Bạn đã có ít nhất 30 conversions/tháng từ Google chưa? (PMax performs better với existing data)
5. **Có video không:** Bạn có video assets sẵn chưa, hay cần mình brief video concept?"

Wait for answer before continuing.

## Step 3 — Write the PMax brief

### PMax asset requirements

Google PMax requires:
- **Headlines:** up to 15 (30 chars each) — provide all 15
- **Long headlines:** up to 5 (90 chars each)
- **Descriptions:** up to 5 (90 chars each)
- **Images:** up to 20 images in multiple ratios
- **Videos:** up to 5 videos (Google auto-creates if not provided — always provide your own)
- **Logo:** 1:1 ratio required
- **Sitelinks:** up to 4 (optional but recommended)
- **Callouts:** up to 10 short phrases
- **Structured snippets:** optional

### Writing PMax headlines (15 total)

Headlines must be mix-and-matchable — Google combines them automatically. Every combination must make sense.

Write headlines across 5 angles (3 per angle):

**Angle 1 — Primary keyword / service (3 headlines)**
These anchor what the campaign is about. Must include the primary keyword.

**Angle 2 — Key outcome / benefit (3 headlines)**
What the customer gets. Specific and measurable.

**Angle 3 — Differentiator / USP (3 headlines)**
What makes this offer different from competitors. Specific, verifiable claim.

**Angle 4 — Social proof (3 headlines)**
Numbers, results, clients served. Credibility signals.

**Angle 5 — Offer / CTA (3 headlines)**
The action + incentive. Urgency if real.

**Vietnamese PMax headline rules:**
- 30 chars is tight in Vietnamese — count carefully (Vietnamese characters are 1 char each)
- Avoid abbreviations that lose meaning
- No pun or wordplay — PMax mixes headlines randomly, puns break when combined differently
- Each headline must make standalone sense

### Long headlines (5 total, 90 chars)

These appear alone — full sentence format. Write as standalone value propositions:
- "Setup hệ thống AI marketing hoàn chỉnh trong 9 ngày — bạn tự chạy, tự sở hữu mãi mãi."
- "Không cần agency. Không retainer. 16 AI agents làm việc cho brand của bạn từ ngày đầu."

### Descriptions (5 total, 90 chars)

Support whatever headline combination appears. Must all be brand-consistent and complement any headline:
- Include primary keyword in at least 2 descriptions
- One description with urgency/scarcity (if real)
- One description with risk-reversal or guarantee

### Image asset brief

PMax needs images in 3 ratios. Provide brief for each:

**Landscape (1.91:1 — 1200×628 minimum):**
Used in: Search display, YouTube, Gmail, Discovery feed
Brief: [describe what to show — subject, background, text overlay, mood]

**Square (1:1 — 1200×1200 minimum):**
Used in: Display network, Gmail
Brief: [describe]

**Portrait (4:5 — 960×1200 minimum):**
Used in: Discovery, YouTube mastheads
Brief: [describe]

Provide at least 3 images per ratio (9 minimum total). More variety = better performance.

**Marketing image (no text overlay version required):**
Google needs clean images without text for some placements. Include at least 2 no-text versions.

### Video asset brief

If you don't provide video, Google auto-generates from your images and text — quality is usually poor. Always provide video.

PMax video requirements:
- Minimum: 1 video, 10+ seconds
- Recommended: 2–3 videos at different lengths (10s, 30s, 60s)
- Vertical (9:16) for YouTube Shorts placements
- Captions required (many watch muted)

Video brief template:
- **Hook (0–3s):** [First frame description + opening text overlay]
- **Body (3–25s):** [Key message + visual]
- **CTA (last 5s):** [End card design + call to action]

### Audience signals

PMax uses audience signals as suggestions, not hard targeting. Provide:
- Custom intent: keywords your ideal customer searches
- Customer match: upload existing email list
- Website visitors: pixel-based audience
- Similar segments: Google's auto-built from above

Vietnamese PMax signals:
- In-market: "Business software", "Marketing services and tools"
- Custom intent keywords: Vietnamese-language keywords your ICP searches
- Customer list: Even small lists (100+ emails) help PMax find similar users faster

### Sitelinks (4 recommended)

Link to supporting pages that help qualify and convert:
- "[Pricing/Packages]" → pricing page
- "[Case Studies]" → proof page  
- "[Free Consultation]" → booking page
- "[About]" → trust page

### Callouts (10 short phrases, 25 chars max)

Highlight features/benefits that don't fit in headlines:
- "Setup trong 9 ngày"
- "Không retainer"
- "Trả một lần"
- "16 AI agents"
- "Tư vấn miễn phí"

## Step 4 — Write output

Save to `/outputs/assets/ads/google-pmax-brief-[campaign-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Google Performance Max Brief — [Campaign Name]
> Generated: [date] | Conversion goal: [goal] | Budget: [amount/day] | Offer: [offer]

---

## Headlines (15 — 30 chars max each)

### Keyword anchor
1. [headline] ([char count])
2. [headline] ([char count])
3. [headline] ([char count])

### Outcome
4. [headline]
5. [headline]
6. [headline]

### Differentiator
7. [headline]
8. [headline]
9. [headline]

### Social proof
10. [headline]
11. [headline]
12. [headline]

### Offer/CTA
13. [headline]
14. [headline]
15. [headline]

---

## Long Headlines (5 — 90 chars max each)
1. [long headline]
2. [long headline]
3. [long headline]
4. [long headline]
5. [long headline]

---

## Descriptions (5 — 90 chars max each)
1. [description]
2. [description]
3. [description]
4. [description]
5. [description]

---

## Image Brief

### Landscape (1200×628)
1. [description]
2. [description]
3. [description]

### Square (1200×1200)
1. [description]
2. [description]
3. [description]

### Portrait (960×1200)
1. [description]

---

## Video Brief

### Video 1 — 15 seconds
[Hook / Body / CTA breakdown]

### Video 2 — 30 seconds
[Hook / Body / CTA breakdown]

---

## Audience Signals
- Custom intent keywords: [list]
- In-market segments: [list]
- Customer match: [upload instructions]

---

## Sitelinks
1. [text] → [URL]
2. [text] → [URL]
3. [text] → [URL]
4. [text] → [URL]

## Callouts
[list of 10]

---

## Launch Checklist
- [ ] All 15 headlines approved
- [ ] Images created in all 3 ratios
- [ ] At least 1 video asset ready
- [ ] Conversion tracking verified
- [ ] Audience signals uploaded
- [ ] Final URL confirmed (landing page live)
- [ ] Budget set: [amount]/day
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Google PMax brief cho '[Campaign]' đã hoàn chỉnh.**

**Assets briefed:**
- 15 headlines + 5 long headlines + 5 descriptions
- [n] image briefs ([ratios])
- [n] video briefs
- Audience signals: [types]

📁 Đã lưu vào: `/outputs/assets/ads/google-pmax-brief-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Sản xuất image và video assets từ brief này, sau đó launch. Recommend chạy Search campaign song song để capture high-intent traffic trong khi PMax học."

---
