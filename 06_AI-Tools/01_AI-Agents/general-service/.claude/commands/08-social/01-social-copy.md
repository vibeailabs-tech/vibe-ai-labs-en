# Social Copy Skill

Your job is to take one piece of content or topic and produce platform-specific social posts — Facebook, TikTok caption, Zalo broadcast, and LinkedIn. One input, four outputs. Every post written in the brand's voice, optimized for each platform's format and audience behavior.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5) — every post must sound like this brand
- Target audience (Section 6) — Vietnamese SMB owners, marketers, founders
- Key messages (Section 11) — weave in naturally
- Content pillars (Section 12) — confirm topic fits a pillar

If a blog post or brief exists in `/outputs/assets/content/`: read it — atomize from the source content.
If `/outputs/strategy/content-calendar-*.md` exists: check if this topic is scheduled and what angle to use.

If brand.md doesn't exist: ask user for brand name, voice, and audience before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided content to atomize (blog post, brief, article)**
Extract the key argument, 3 best proof points, and the CTA. Go to Step 3.

**Path B — User provided a topic or keyword only**
Ask:
"Để viết social posts, mình cần biết thêm:
1. **Topic cụ thể:** Bạn muốn post về gì? (VD: 'Claude Design là gì', 'cách giảm chi phí marketing', '5 lỗi AI thường gặp')
2. **Mục tiêu:** Bài này để làm gì? (tăng awareness / drive traffic / generate leads / build trust)
3. **Có link không:** Bạn muốn include link đến bài blog hay landing page không?"

Wait for answer before continuing.

## Step 3 — Write all 4 platform versions

### Platform rules

**Facebook (primary platform for Vietnamese SMBs)**
- Length: 150–300 words — long enough to tell a story, short enough to not lose them
- Format: Hook line → 2–3 short paragraphs → CTA + link
- Hook: First line must stop the scroll. Options: bold claim, specific number, relatable scenario, or direct question
- Paragraphs: 2–3 sentences max. Use line breaks generously — wall of text kills Facebook reach
- Emoji: 1–2 max, only if they add meaning. Never decorative.
- CTA: One action — comment, click link, or tag someone. Never more than one.
- Hashtags: 3–5 niche hashtags, end of post

**TikTok caption**
- Length: 100–150 words — the video does the work, caption supports
- Hook: First sentence = video hook restatement (what the viewer just saw / is about to see)
- Format: 1–2 sentences context → CTA → hashtags
- Hashtags: 5–8, mix trending (#AI, #marketing) + niche (#AIviệtnam, #doanhnghiepviet)
- No long explanations — the caption is a supplement, not the content
- Tone: Casual, direct, no corporate speak

**Zalo broadcast**
- Length: 80–120 words — Zalo is messaging, not scrolling. Short wins.
- Format: Greeting (optional, 1 line) → core message → one clear action (link or reply keyword)
- No hashtags — Zalo doesn't use them
- Register: Warm but direct. "Bạn" register. Can open with "Chào [Tên]," if personalized
- CTA: Always one — "Nhắn 'TƯ VẤN' để mình gửi thêm" or "Đọc đầy đủ tại: [link]"
- Avoid: Multiple links, long lists, anything that looks like spam

**LinkedIn**
- Length: 200–400 words — longer is accepted here, especially for insight posts
- Format: Hook → insight or argument → evidence or story → takeaway → CTA
- Tone: More professional than Facebook but still direct. Same "bạn/mình" if Vietnamese, "you/I" if English
- Structure: Use line breaks every 2–3 sentences. Avoid bullet lists unless they add clarity
- CTA: Subtle — "Curious what you think" / "What's your experience?" — LinkedIn rewards engagement over clicks
- Hashtags: 3–5 professional hashtags at end

### Vietnamese social writing rules
- Lead with specifics: "93%", "7 ngày", "$500/tháng" — not "nhiều", "rất nhanh", "hiệu quả"
- Short sentences for impact. Medium sentences for explanation. Never long compound sentences.
- Bạn/mình register throughout — never "quý khách", never corporate distance
- Pain points > features: "Bạn đang tốn 3 giờ/ngày viết content" hits harder than "tiết kiệm thời gian"
- Vietnamese context: Use Vietnamese examples, Vietnamese market references, Vietnamese price points

## Step 4 — Write output

Save to `/outputs/assets/social/social-copy-[topic-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Social Copy — [Topic]
> Generated: [date] | Source: [blog post / topic] | Platforms: Facebook, TikTok, Zalo, LinkedIn

---

## Facebook

[Full Facebook post]

---

## TikTok Caption

[Full TikTok caption with hashtags]

---

## Zalo Broadcast

[Full Zalo message]

---

## LinkedIn

[Full LinkedIn post]

---

## Notes
- Best posting time: [platform-specific recommendation]
- Repurpose tip: [how to extend the life of this content]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Social copy cho '[Topic]' đã hoàn chỉnh — 4 platform versions.**

**Summary:**
- Facebook: [hook preview — first 10 words]
- TikTok: [hook preview]
- Zalo: [opening line preview]
- LinkedIn: [hook preview]

📁 Đã lưu vào: `/outputs/assets/social/social-copy-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/video-script` để viết TikTok script cho topic này, hoặc `/social-calendar` để lên lịch đăng."

---
