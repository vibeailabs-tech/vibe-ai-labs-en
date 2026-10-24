# Social Calendar Skill

Your job is to build a 30-day social media posting calendar — specific posts planned by day, platform, format, topic, hook, and CTA. Not a template. A real calendar tied to the brand's content pillars, campaign dates, and platform best practices for the Vietnamese market.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — tone determines content mix
- Target audience (Section 6) — their platform habits and peak times
- Content pillars (Section 12) — one calendar column per pillar
- Core offer (Section 9) — how often to include promotional posts

If `/outputs/strategy/content-calendar-*.md` exists: read it — align this calendar to the existing campaign plan.
If `/outputs/assets/social/hashtag-research-*.md` exists: use the hashtag clusters for each post.
If `/outputs/strategy/campaign-brief-*.md` exists: note any campaign dates or launch events.

If brand.md doesn't exist: ask user for brand name, content topics, platforms, and any upcoming events before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified platforms, frequency, and any key dates**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để build social calendar, mình cần biết:
1. **Platforms:** Bạn đang post ở đâu? (Facebook / TikTok / Zalo / LinkedIn)
2. **Tần suất:** Bạn muốn post bao nhiêu lần/tuần trên mỗi platform?
3. **Ngày bắt đầu:** Calendar bắt đầu từ ngày nào?
4. **Sự kiện đặc biệt:** Có launch, sale, campaign, hay holiday nào trong 30 ngày tới không?
5. **Content hiện có:** Bạn đã có blog post, case study, hay email nào có thể atomize không?"

Wait for answer before continuing.

## Step 3 — Build the 30-day calendar

### Vietnamese social media best practices

**Posting frequency by platform:**
- Facebook: 4–5x/week — consistency beats frequency
- TikTok: 5–7x/week — TikTok algorithm rewards volume
- Zalo OA: 2–3x/week — don't spam, Zalo users mute aggressive broadcasters
- LinkedIn: 2–3x/week — quality over quantity, longer form performs

**Best posting times (Vietnamese audience, GMT+7):**
- Facebook: 8–9am (morning commute) / 12–1pm (lunch) / 7–9pm (evening wind-down)
- TikTok: 7–9am / 12–2pm / 8–10pm
- Zalo: 8–9am / 12–1pm / 5–6pm (end of workday)
- LinkedIn: 7–9am Tuesday–Thursday (avoid Monday mornings and Fridays)

**Content mix formula (weekly):**
- 40% Education / tips / insight — builds authority, gets saved and shared
- 30% Social proof / case study / results — builds trust
- 20% Behind-the-scenes / personal / founder story — builds connection
- 10% Promotional / offer / CTA — converts

**Vietnamese social media calendar rules:**
- Never post 2 promotional posts back-to-back — always sandwich between value content
- Monday is poor for Facebook in Vietnam — people scroll less, engage less
- Tết period (January/February): shift content toward celebration, reflection, new year goals
- Major Vietnamese holidays: 30/4 (Liberation Day), 1/5 (Labor Day), 2/9 (National Day) — content should acknowledge or tie in
- Vietnamese audiences engage heavily in comment sections — build in "question posts" to seed discussion

### Calendar structure per post

Each entry in the calendar must include:
- **Day + Date:** Day X — DD/MM
- **Platform:** Facebook / TikTok / Zalo / LinkedIn
- **Format:** Static image / Carousel / Short video / Text post / Reels
- **Content pillar:** Which pillar this post belongs to
- **Topic:** Specific topic (not "marketing tips" — "3 lý do ChatGPT không thay thế được hệ thống AI thật")
- **Hook:** First line or opening 3 seconds (the scroll-stopper)
- **Angle:** Education / Social proof / Behind-the-scenes / Promotional
- **CTA:** What action you want (comment / click / DM / save)
- **Assets needed:** What needs to be created (photo, graphic, video)
- **Status:** To create / Ready / Scheduled / Posted

### Campaign tie-ins
If there are launches, promotions, or events in the 30-day window:
- Build a 3–5 post "campaign arc" around the event: Tease → Build → Launch → Social proof → Last call
- Space campaign posts 2–3 days apart
- Surround campaign posts with value content so the promotional posts don't feel isolated

## Step 4 — Write output

Save to `/outputs/assets/social/social-calendar-[month-year].md`:

```markdown
# Social Calendar — [Month Year]
> Generated: [date] | Platforms: [list] | Frequency: [posts/week]

## Content Mix Target
- Education: 40% ([n] posts)
- Social proof: 30% ([n] posts)
- Behind-the-scenes: 20% ([n] posts)
- Promotional: 10% ([n] posts)

---

## Week 1 — [Date range]

### Day 1 — [Date]
**Platform:** [platform]
**Format:** [format]
**Pillar:** [pillar]
**Topic:** [specific topic]
**Hook:** "[first line or 3-second opener]"
**Angle:** [Education / Proof / BTS / Promo]
**CTA:** [specific action]
**Assets needed:** [what to create]
**Status:** To create

---

### Day 2 — [Date]
[Repeat structure]

---

[Continue through all 30 days]

---

## Campaign Arc: [Campaign Name if applicable]
| Post | Date | Platform | Hook | Goal |
|---|---|---|---|---|
| Tease | [date] | [platform] | [hook] | [goal] |
| Build | [date] | [platform] | [hook] | [goal] |
| Launch | [date] | [platform] | [hook] | [goal] |
| Proof | [date] | [platform] | [hook] | [goal] |
| Last call | [date] | [platform] | [hook] | [goal] |

---

## Notes
- Key dates this month: [holidays, events]
- Content to repurpose: [existing blog posts, emails to atomize]
- Assets to prepare in advance: [list of images/videos needed]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Social calendar tháng [month] đã hoàn chỉnh.**

**Summary:**
- Total posts: [n] posts over 30 days
- Platforms: [list]
- Content mix: [40/30/20/10 or actual split]
- Campaign arcs: [n] — [names]

📁 Đã lưu vào: `/outputs/assets/social/social-calendar-[month-year].md`

**Bước tiếp theo:** Chạy `/social-copy` để viết copy cho từng post, hoặc `/social-creative` để brief visual cho tuần đầu."

---
