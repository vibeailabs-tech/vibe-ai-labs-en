# Agent 13 — Distribution Agent: Deep Dive

## What this agent does

The Distribution Agent's job is **reach multiplication**. Every piece of content created by upstream agents passes through here before it ships. One blog post becomes 12+ platform assets. One announcement becomes a press release, podcast pitch, and partnership brief. This agent ensures nothing is created once and published once — everything gets maximum mileage.

---

## Why this agent exists

Most Vietnamese businesses create content and post it on one platform. The Distribution Agent changes that default. A single well-researched blog post contains at least 10 social posts, 3 email angles, and 5 quote cards — the atomizer finds them all. Platform formatter ensures each asset matches the technical requirements of its destination so it actually performs.

---

## Skills (5)

### Skill 1 — Content Atomizer (`/content-atomizer`)

**What it does:** Takes one long-form piece and breaks it into every smaller asset it contains.

**Input:** Blog post, video script, webinar, or case study (file path or pasted text)

**Output:** `/outputs/distribution/atomized-[slug].md` with minimum 12 assets

**3-tier atomization framework:**
- **Tier 1 — Direct extracts:** Pull quotes, statistics, key arguments, numbered lists
- **Tier 2 — Light adaptation:** Same idea, reformatted (problem section → Facebook pain post; solution → Zalo broadcast)
- **Tier 3 — Repurposed angle:** Contrarian take, "what I got wrong" version, behind-the-scenes

**Output per content type:**
- Blog post (2,000 words) → minimum 12 assets: 3 Facebook posts, 2 TikTok captions, 1 Zalo broadcast, 1 LinkedIn post, 3 pull quotes, 1 email teaser, 1 video hook
- Video script → minimum 8 assets
- Case study → minimum 10 assets

**Vietnamese rules:**
- Numbers survive atomization exactly — "45 phút/tuần" stays "45 phút/tuần" everywhere
- Register stays consistent — bạn/mình source = bạn/mình atoms
- Facebook version is always longest; Zalo always shortest
- TikTok caption supports the video — it's not a standalone post

---

### Skill 2 — Platform Formatter (`/platform-formatter`)

**What it does:** Takes any content and formats it to exact platform technical specifications.

**Input:** Any text content + target platforms

**Output:** `/outputs/distribution/formatted-[slug].md` with platform-ready versions

**Platform specs it applies:**

| Platform | Character limit | Link handling | Hashtags | Image |
|---|---|---|---|---|
| Facebook | 63,206 (hook before 480) | End of post | 3–5 at end | 1200×630 |
| TikTok | 2,200 (practical: 150 words) | Bio link only | 5–8 at end | 9:16 video |
| Zalo OA | 1,000 recommended | Full URL own line | None | 800×400 |
| LinkedIn | 3,000 (hook before 210) | First comment | 3–5 at end | 1200×627 |

**Vietnamese specifics:**
- Facebook "Xem thêm" fires at ~480 chars — entire hook must land before this
- Zalo renders rich link previews — always put URL on its own line
- TikTok: mix English + Vietnamese hashtags (#AImarketing + #AIvietnam) for dual discovery paths
- LinkedIn Vietnam: bilingual posts or pure Vietnamese both work; match the language to the audience tier

**Output includes:** A formatting checklist with 6 checkboxes the human verifies before posting.

---

### Skill 3 — Press Release (`/press-release`)

**What it does:** Writes journalistic press releases for Vietnamese media — product launches, milestones, partnerships, research.

**Input:** Announcement details, spokesperson quote, target publications

**Output:** `/outputs/distribution/press-release-[slug].md`

**Structure:**
1. Headline — newsworthy, not promotional "("[Brand] Giúp SMB Giảm 80% Chi Phí" ✓ vs "Ra Mắt Sản Phẩm Đột Phá" ✗)
2. Dateline — TP. Hồ Chí Minh, [Date] —
3. Lead paragraph — who, what, when, where, why it matters in 2–3 sentences
4. Body (2–3 paragraphs) — context, data, evidence
5. Quote — must add insight, not repeat the headline
6. Boilerplate — what the company does, who it serves, where, founding year
7. Contact — name, title, email, Zalo for media follow-up

**Target publications:**
- Tech/business: VnExpress Kinh doanh, CafeF, Báo Đầu Tư, Nhịp Cầu Đầu Tư
- Startup/innovation: Startup Vietnam, e27 Vietnam, Tech in Asia Vietnam
- General: Thanh Niên, Tuổi Trẻ (significant news only)

**What kills a Vietnamese press release:**
- Promotional language: "giải pháp toàn diện", "đột phá" — editors delete on sight
- No numbers — vague claims without data
- Quote that says nothing: "Chúng tôi rất vui khi ra mắt sản phẩm này"

---

### Skill 4 — Podcast Pitch (`/podcast-pitch`)

**What it does:** Writes cold pitches to podcast hosts for the brand founder to appear as a guest. Three versions per pitch.

**Input:** Target podcast(s), speaker details, topic angle

**Output:** `/outputs/distribution/podcast-pitch-[slug].md`

**5-element pitch structure:**
1. **Subject line** — reference show by name, hint at audience value, under 8 words
2. **Opening** — specific episode or guest referenced (never generic "I love your podcast")
3. **Topic angle** — specific, counterintuitive, timely, actionable (not "AI marketing in Vietnam")
4. **Credibility** — one specific result, any prior appearances, unique vantage point
5. **Easy CTA** — one ask: "Có phù hợp không nếu mình gửi thêm thông tin?"

**3 pitch versions:**
- **Version A:** Cold pitch to specific show (referencing their actual content)
- **Version B:** Template for similar shows (with [SHOW NAME], [RECENT EPISODE] placeholders)
- **Version C:** LinkedIn DM version (150 words max)

**Topic angle formulas:**
- Contrarian: "Lý do AI tool của bạn không tiết kiệm thời gian (và cách fix)"
- Behind-the-scenes: "Mình setup 50+ AI marketing systems — đây là điều hầu hết bài hướng dẫn không nói"
- Data-driven: "93% dùng AI nhưng chỉ 13.8% thấy kết quả — data từ thị trường Việt Nam"

**Vietnamese podcast targets:**
- Business/startup: Startup Vietnam Podcast, The Coffee House Talks, Wisdom Talks
- Marketing: Marketing Arena, Brand Camp
- Tech/AI: Technically Vietnam, The Vietnamese Podcast

**Follow-up plan included:** Day 0 email → Day 1 LinkedIn DM → Day 7 follow-up → Day 14 final or move on

---

### Skill 5 — Partnership Brief (`/partnership-brief`)

**What it does:** Writes partnership proposals — co-marketing, referral programs, content collaborations, distribution partnerships, tech integrations.

**Input:** Partner type or specific company, what you offer, what you want, deal structure

**Output:** `/outputs/distribution/partnership-brief-[slug].md`

**6-section brief:**
1. **The match** — why you, why them, why now (market trend, audience overlap)
2. **Audience overlap** — side-by-side table: your audience vs. theirs, shared characteristics
3. **What you bring** — concrete assets, unique angle, one credibility proof point
4. **Proposed structure** — specific deal (not "let's explore") — type, duration, what happens step by step, revenue/value split
5. **What they get** — quantified + qualitative value, low-risk framing
6. **Next step** — one specific ask, timeline, Zalo + email contact

**5 partnership types with value frames:**
- **Co-marketing:** "Cả hai audience đều cần điều này — và mình + bạn cùng reach được nhiều hơn riêng lẻ"
- **Referral:** "Mỗi client bạn refer sang mình = 20% trên mỗi deal thành công"
- **Content collab:** "Mình bring AI marketing angle. Bạn bring [their expertise]. Output: content cả hai publish"
- **Distribution:** "Bạn có [audience]. Mình có [product they need]. Revenue share: [structure]"
- **Tech integration:** "Khách của bạn đang dùng mình. Khách của mình đang dùng bạn"

**Vietnamese business culture notes:**
- Trust first, deal second — a cold brief may need LinkedIn warm-up or mutual introduction first
- Revenue share: 15–30% is B2B standard in Vietnam — be specific, not vague
- Reciprocal framing: "Mình giúp bạn distribute, bạn làm tương tự" lands better than one-sided proposals
- Community partnerships (Startup Vietnam, YBA) = distribution to thousands of SMB owners directly

**Output includes 3 proposals:** Main proposal + Option B (simpler) + Option C (content collab only, lowest commitment)

---

## Workflow position

```
Agent 05 (Content) → Agent 13 (Distribution) → Agent 14 (Performance)
Agent 06 (SEO)     ↗
```

Distribution Agent reads outputs from Content, SEO, Video & Creative agents. It feeds formatted, published assets into the Performance Agent's tracking system.

---

## No APIs required

All 5 skills are pure writing and formatting. No external API calls needed. The agent works from:
- `brand.md` (voice, audience, offer)
- Source content files (from `/outputs/assets/content/`)
- User-provided announcement or partnership details

When APIs are available (Meta Insights, GA4), the Performance Agent picks up from here to measure what Distribution puts out.

---

## File naming conventions

| Skill | Output file |
|---|---|
| content-atomizer | `atomized-[source-slug].md` |
| platform-formatter | `formatted-[topic-slug].md` |
| press-release | `press-release-[announcement-slug].md` |
| podcast-pitch | `podcast-pitch-[speaker-topic-slug].md` |
| partnership-brief | `partnership-brief-[partner-slug].md` |

All files land in `/outputs/distribution/`.
