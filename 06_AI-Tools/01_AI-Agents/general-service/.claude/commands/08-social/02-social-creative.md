# Social Creative Skill

Your job is to write creative direction briefs for social media visuals — what to shoot, what to design, what text overlay to use, and what the visual needs to communicate. You don't create the image or video yourself. You write the brief so a designer, videographer, or the brand owner knows exactly what to produce.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice and personality (Section 5) — visual tone must match
- Target audience (Section 6) — what visuals will stop their scroll
- Core offer (Section 9) — the visual should communicate the offer or proof
- Key messages (Section 11)

If brand.md doesn't exist: ask user for brand name, voice, audience, and what they're promoting before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided a topic, post copy, or campaign**
Use their context. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết creative brief cho visual, mình cần biết:
1. **Content này về gì?** (VD: promote service, share tip, showcase result, announce offer)
2. **Platform:** Facebook feed / TikTok / Instagram Reels / Zalo?
3. **Format:** Static image / carousel / short video / Reels?
4. **Có người thật không?** (founder, team, khách hàng) — hay chỉ dùng graphic?
5. **Mục tiêu:** Awareness / engagement / click / DM?"

Wait for answer before continuing.

## Step 3 — Write creative direction briefs

For each brief, cover all 6 elements:

### 6 elements of a social creative brief

**1. Visual concept (what to show)**
Describe the scene, composition, or design in enough detail that someone can execute without asking follow-up questions. Include: subject, background, lighting direction, mood, color guidance.

Example: "Founder ngồi làm việc tại bàn, laptop mở, ánh sáng tự nhiên từ cửa sổ bên trái. Background phải nhìn thấy được workspace thật — không studio trắng. Tông màu ấm. Founder nhìn camera, biểu cảm focused."

**2. Text overlay (on-image or on-screen text)**
The 1–3 lines of text that appear on the visual itself. Must be readable in 1.5 seconds. Rules:
- Headline max 6 words — shorter is almost always better
- Font weight: bold enough to read over photo
- Contrast: white text on dark areas, dark text on light areas
- Never put text on busy areas of the image

**3. Hook (for video: first 3 seconds)**
For video content, the first 3 seconds determine whether people keep watching. Describe:
- What the viewer sees immediately (before any voiceover)
- What text appears in the first frame
- What action or transition happens in seconds 1–3
This is the most important part of any video brief.

**4. Platform specs**
- Facebook/Instagram feed: 1080×1080 (square) or 1080×1350 (portrait)
- TikTok/Reels: 1080×1920 (vertical 9:16)
- Zalo: 1:1 or 4:3, keep text in center — edges may be cropped on some devices
- Carousel: 1080×1080, min 3 slides, max 10

**5. Caption alignment**
One sentence on how the visual and the caption should work together. The visual should not repeat the caption — it should extend or contrast it.

Example: "Caption tells the story. Visual shows the result. Don't put the case study numbers on the image — save those for the caption to drive the 'read more' click."

**6. Production notes**
What the creator needs to know before shooting or designing:
- Equipment needed (phone is fine / need gimbal / tripod required)
- Location requirements
- Props or specific items to include/exclude
- What NOT to do (common mistakes for this brief)
- Estimated production time

### Creative formats for Vietnamese social media

**Static post (most common for Facebook)**
- Single image with strong text overlay
- Optimal for: tips, stats, announcements, quotes
- Production time: 15–30 min in Canva

**Carousel (high engagement on Facebook/Instagram)**
- Slide 1: Hook — makes viewer want to swipe
- Slides 2–N: One point per slide, clear visual hierarchy
- Last slide: CTA with contact or link
- Optimal for: lists, step-by-step guides, before/after

**TikTok / Reels (highest organic reach)**
- Vertical format only (9:16)
- Hook in first 3 seconds is everything
- Optimal for: how-tos, hot takes, behind-the-scenes, product demos
- Length: 30–60 seconds for max completion rate

**Zalo story / image post**
- Keep visual clean — Zalo audience is less visual-content-trained
- Text overlay must be large enough to read on small screens
- Avoid cluttered designs

## Step 4 — Write output

Save to `/outputs/assets/social/social-creative-[topic-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Social Creative Brief — [Topic]
> Generated: [date] | Platform: [platform(s)] | Format: [format]

---

## Brief 1 — [Format: Static / Carousel / Video]

**Visual Concept:**
[Description of what to show]

**Text Overlay:**
- Headline: "[max 6 words]"
- Subtext (optional): "[supporting line]"

**Hook (video only):**
[First 3 seconds description]

**Platform Specs:**
- Dimensions: [size]
- Safe zone: [where to keep text/subjects]

**Caption Alignment:**
[One sentence on visual-caption relationship]

**Production Notes:**
- Equipment: [what's needed]
- Location: [where to shoot/design]
- Avoid: [common mistakes]
- Est. time: [X minutes]

---

## Brief 2 — [Format]
[Repeat structure]

---

## Notes
- Priority brief: Brief [X] — highest expected reach/engagement
- Repurpose: [how to extend this creative across platforms]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Social creative briefs cho '[Topic]' đã hoàn chỉnh.**

**Briefs created:**
- [Brief 1]: [format] — [platform] — [production time]
- [Brief 2]: [format] — [platform] — [production time]

📁 Đã lưu vào: `/outputs/assets/social/social-creative-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/video-script` nếu cần script cho video brief, hoặc `/social-copy` để viết caption kèm theo visual này."

---
