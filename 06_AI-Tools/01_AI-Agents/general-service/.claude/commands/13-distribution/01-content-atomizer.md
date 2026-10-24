# Content Atomizer Skill

Your job is to take one piece of long-form content — blog post, video script, webinar, case study — and break it into all the smaller assets it contains. One input, maximum output. A 2,000-word blog post contains at least 10 social posts, 3 email angles, 2 video hooks, and 5 quote cards. This skill finds them all.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — all atomized pieces stay in brand voice
- Content pillars (Section 12) — confirm which pillar this content falls under
- Target audience (Section 6) — who each atomized piece is for

Read the source content from `/outputs/assets/content/blog/` or wherever the user points to.

If brand.md doesn't exist: ask user for brand voice and source content before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided source content or file path**
Use their input. Go to Step 3.

**Path B — No source provided**
Ask:
"Để atomize content, mình cần:
1. **Source content:** Paste bài blog / video script / case study bạn muốn atomize
2. **Platforms cần:** Facebook / TikTok / Zalo / LinkedIn / Email / tất cả?
3. **Priority:** Bạn muốn mình ưu tiên format nào nhất?"

Wait for answer before continuing.

## Step 3 — Atomize the content

### The atomization framework

Every piece of long-form content contains these extractable assets:

**Tier 1 — Direct extracts (no rewriting needed)**
- Pull quotes: 3–5 sentences that stand alone as insights
- Statistics or numbers: every specific data point becomes a stat card
- Key argument: the central thesis = LinkedIn thought leadership post
- List items: any numbered list = carousel or thread

**Tier 2 — Light adaptation (same idea, new format)**
- Hook sentences: first paragraph → TikTok hook text
- Problem section → Facebook pain post
- Solution section → Zalo broadcast summary
- Case study or proof → email story sequence
- FAQ section → Twitter/X thread or community FAQ post

**Tier 3 — Repurposed angle (same topic, new entry point)**
- Contrarian take on the main argument
- "What I got wrong" version (builds trust through vulnerability)
- "The one thing most people miss" angle
- Behind-the-scenes of how the content was created

### Output map per content type

**Blog post (2,000 words) → minimum 12 assets:**
- 3 Facebook posts (different hooks: stat / story / question)
- 2 TikTok captions (hook-led, short)
- 1 Zalo broadcast
- 1 LinkedIn post (insight angle)
- 3 pull quotes (for graphic design)
- 1 email teaser (drive traffic to blog)
- 1 short video script hook (15–30 seconds)

**Video script (60 seconds) → minimum 8 assets:**
- 1 TikTok caption
- 1 Facebook post (expand the argument)
- 1 Zalo broadcast
- 3 pull quotes from spoken lines
- 1 thumbnail headline
- 1 email subject line (using video hook)

**Case study → minimum 10 assets:**
- 1 Facebook story post (before/after narrative)
- 1 LinkedIn post (professional insight)
- 1 TikTok caption (result-first hook)
- 1 Zalo broadcast (social proof)
- 3 quote cards (client direct quotes)
- 1 email subject line ("How [name] went from X to Y")
- 1 ad headline (result stat)
- 1 cold email proof line

### Vietnamese atomization rules

- Keep register consistent — if source is bạn/mình, all atoms stay bạn/mình
- Numbers survive atomization: "45 phút/tuần", "$80/tháng" stay exact in every version
- Facebook version is always longest; Zalo always shortest
- TikTok caption must work as caption (video does the work) not standalone post
- LinkedIn: adapt to professional context — same data, more analytical framing

## Step 4 — Write output

Save to `/outputs/distribution/atomized-[source-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Content Atomization — [Source Title]
> Generated: [date] | Source: [file path] | Total assets: [n]

---

## Facebook Posts

### Post 1 — [Angle: stat/story/question]
[Full post with hashtags]

### Post 2 — [Angle]
[Full post]

### Post 3 — [Angle]
[Full post]

---

## TikTok Captions

### Caption 1
[Caption + hashtags]

### Caption 2
[Caption + hashtags]

---

## Zalo Broadcast
[Message text — no hashtags]

---

## LinkedIn Post
[Full post + hashtags]

---

## Pull Quotes (for graphic design)
1. "[Quote]" — [Source]
2. "[Quote]"
3. "[Quote]"

---

## Email Teaser
**Subject:** [Subject line]
**Preview:** [Preview text]
**Body:** [2–3 sentences + link CTA]

---

## Video Script Hook (15–30 sec)
VISUAL: [description]
SPOKEN: "[hook line]"
TEXT OVERLAY: "[text]"

---

## Ad Assets
**Headline:** [result-led headline]
**Proof line:** [for cold email use]

---

## Asset Inventory
| Asset | Platform | Status |
|---|---|---|
| Facebook Post 1 | Facebook | Ready |
| TikTok Caption 1 | TikTok | Ready |
[etc.]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Content atomization cho '[Source]' hoàn chỉnh.**

**Total assets produced:** [n]
**Platforms covered:** [list]
**Highest priority to publish first:** [asset + reason]

📁 Đã lưu vào: `/outputs/distribution/atomized-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/platform-formatter` để format từng asset đúng spec của từng platform, hoặc schedule qua `/social-calendar`."

---
