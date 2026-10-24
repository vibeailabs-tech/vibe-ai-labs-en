# Newsletter Skill

Your job is to write a single broadcast newsletter — educational, valuable, and with a natural CTA. Not a promotional blast. A newsletter people actually read.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5)
- Target audience (Section 6)
- Content pillars (Section 12)
- Core offer (Section 9) — for the CTA

Check if `/outputs/assets/content/` has recent blog posts or thought leadership — these can be repurposed or linked in the newsletter.

If brand.md doesn't exist: ask user for brand, audience, and newsletter topic before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified topic or content to include**
Use their direction. Go to Step 3.

**Path B — No direction**
Ask:
"Để viết newsletter, mình cần biết:
1. **Chủ đề số này:** Topic hoặc insight chính bạn muốn share với subscribers
2. **Có content gốc không?** Bài blog, case study, hay research nào bạn muốn link vào?
3. **CTA:** Bạn muốn reader làm gì sau khi đọc? (Book call / đọc bài full / reply email / xem sản phẩm)
4. **Tone số này:** Giáo dục / storytelling / behind-the-scenes / contrarian opinion?"

Wait for answer.

## Step 3 — Write the newsletter

### Newsletter formats (choose based on content)

**Format 1 — The Insight Letter**
One idea, explored deeply. 300–500 words. Best for thought leadership brands.
Structure: Hook → The insight → Why it matters → One actionable takeaway → CTA

**Format 2 — The Curation Letter**
3–5 curated items (articles, tools, observations) + brief commentary on each. 250–400 words.
Structure: Intro (1 sentence) → 3–5 items with 2–3 sentence commentary each → CTA

**Format 3 — The Story Letter**
A story from behind the scenes, a client situation (anonymized), or a personal experience. 400–600 words.
Structure: Scene-setting opening → The conflict or tension → The lesson → Application to reader → CTA

**Format 4 — The Number Letter**
Lead with a surprising stat or data point, unpack it, connect to reader's situation. 300–450 words.
Structure: The number (bold) → Context → What most people miss → What this means for you → CTA

### Vietnamese newsletter standards

**Subject line for newsletters (different from sequences):**
- Can be more personal/curious than sales emails
- Works well: "[số thứ tự] | [topic]" format (e.g., "#12 | Tại sao 86% doanh nghiệp dùng AI sai cách")
- Or direct value: "3 điều mình học được từ khách hàng tuần này"

**Opening:**
- For newsletters: can open with a personal observation or story — readers subscribed to hear *your* perspective
- Still keep it short: context in 2–3 sentences, then into the substance

**Length:**
- Vietnamese newsletter sweet spot: 300–500 words
- Mobile read time: 2–3 minutes max
- If longer: use headers to let skimmers navigate

**The "one thing" rule:**
Every newsletter should leave the reader with one thing they can think about or do differently. If there are 5 takeaways, pick the best one and cut the rest.

**CTA for newsletters:**
- Softer than sales emails: "Đọc full tại đây", "Reply và cho mình biết bạn nghĩ gì", "Book tư vấn nếu điều này relevant với bạn"
- Never: "MUA NGAY" in a newsletter — it breaks trust

### Brand voice check:
- Does it sound like a person writing to another person?
- Would the reader feel this was written for them specifically?
- Is there one original insight — something they wouldn't get from a generic AI newsletter?

## Step 4 — Write output

Save to `/outputs/assets/email/newsletter-[topic-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Newsletter — [Title/Topic]
> Generated: [date] | Format: [format type] | Issue: #[n if known]

**Subject:** [subject line]
**Preview:** [preview text]
**Send date:** [recommended send day/time]

---

[Full newsletter content]

---

## Newsletter Notes
- Format used: [format name + why]
- CTA: [what action + where it goes]
- Repurpose opportunity: [can this become a LinkedIn post / Facebook post / blog section?]
```

## Step 5 — Confirm

After writing:

---
"✅ **Newsletter '[Topic]' hoàn chỉnh.**

**Format:** [format name]
**Subject:** [subject line]
**Word count:** ~[n] từ (~[x] phút đọc)
**CTA:** [CTA text]

📁 Đã lưu: `/outputs/assets/email/newsletter-[topic-slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/subject-line-ab` để test subject line, hoặc `/social-copy` để atomize newsletter thành posts."

---
