# Thought Leadership Skill

Your job is to write opinion articles and industry commentary that position this brand as the sharpest, most trustworthy voice in the space. Not content marketing dressed as opinion. Real perspective. A clear point of view. Something worth disagreeing with.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — bold, pragmatic, trustworthy — this is where bold matters most
- Positioning and competitive angle (Section 7) — what does this brand genuinely believe?
- Key messages (Section 11) — each thought leadership piece should reinforce one of these
- Content pillars (Section 12) — which pillar does this piece serve?
- USP (Section 8) — the mechanism and belief system behind the brand

If `/outputs/research/trend-monitoring-*.md` exists: read it — use current trends as the hook or counterpoint.
If `/outputs/research/market-research-*.md` exists: use market data to support the argument.

If brand.md doesn't exist: ask user for brand info before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User has a topic or angle**
Use their angle. Go to Step 3.

**Path B — No direction provided**
Ask:
"Bài thought leadership này muốn nói điều gì?
1. Quan điểm về ngành (industry commentary — điều mà mọi người đang làm sai)
2. Dự đoán (prediction — điều sắp xảy ra mà ít người thấy)
3. Phản biện (contrarian take — quan điểm ngược với số đông)
4. Bài học rút ra (lessons from experience — điều mình học được)
5. Framework / mental model (cách nhìn mới về vấn đề quen thuộc)

Và topic cụ thể?"

Wait for answer before continuing.

## Step 3 — Write the thought leadership piece

### What makes thought leadership different from a blog post

A blog post informs. Thought leadership challenges.

A blog post answers "how to." Thought leadership answers "why this matters" or "why everyone else is wrong."

A blog post is safe. Thought leadership has a point of view someone can disagree with.

**Test:** If you removed the author's name and replaced it with any other brand in the space — would it still make sense? If yes, it's not thought leadership. It's content.

### Structure for a thought leadership piece

**Opening: The provocation (100–150 words)**
Start with the controversial claim, the uncomfortable truth, or the prediction. Don't bury the lede.

Not: "Trong thời đại AI phát triển nhanh chóng, doanh nghiệp cần thích ứng..."
Yes: "73% doanh nghiệp Việt Nam đã dùng AI — và phần lớn trong số đó đang làm sai hoàn toàn."

**The argument (body)**
- H2s as arguments, not topics
- Each section advances the central thesis
- Use: personal observation, market data, specific examples, logical consequence
- Acknowledge the strongest counterargument — then refute it. This builds credibility.
- Avoid: vague claims, unverifiable statements, generic advice

**The implication**
What does this mean for the reader specifically? If the argument is true — what should they do differently starting today?

**The close**
- Restate the central claim — stronger, with more evidence behind it now
- One specific, actionable conclusion
- CTA that flows naturally from the argument

### Tone calibration for Vietnamese B2B thought leadership
- Direct, but not arrogant — "Mình tin rằng..." not "Rõ ràng là..."
- Back every claim with a specific example or number
- Acknowledge uncertainty where it exists — "Dữ liệu chưa đủ để chắc chắn, nhưng mình thấy pattern này..."
- Vietnamese readers respond to: concrete stories, specific numbers, honest admission of limits
- Avoid: moralizing, lecturing, overpromising

### Formats
- **Long form (1,000–1,500 words):** LinkedIn article, blog post, Medium
- **Short form (400–600 words):** Facebook long post, newsletter section
- **Thread format:** 8–12 points, each 2–3 sentences — for Facebook/LinkedIn

## Step 4 — Write output

Save to `/outputs/assets/content/thought-leadership/[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# [Title — The Claim, Not the Topic]
> Generated: [date] | Format: [long/short/thread] | Pillar: [content pillar] | Platform: [primary platform]

---

[Full article content]

---

## Repurposing Notes
- TikTok angle: [how to turn this into a 60s video]
- Zalo version: [shortened 150-word version for broadcast]
- Facebook short version: [hook + 3 key points + CTA]

## Follow-up content ideas
1. [Related piece this argument leads to]
2. [Counterargument piece to write next]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Thought leadership piece '[Title]' đã hoàn chỉnh.**

**Central claim:** [one sentence — the argument]
**Format:** [long/short/thread]
**Content pillar:** [pillar]
**Strongest point:** [the section that will generate most discussion]

📁 Đã lưu vào: `/outputs/assets/content/thought-leadership/[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/social-copy` để atomize bài này thành Facebook post + TikTok script + Zalo message."

---
