---
name: brand-voice
description: Extracts and defines brand voice, tone, vocabulary, and writing style for a Vietnamese business. Use this skill when the user wants to define how their brand sounds, set up their brand personality, extract voice from existing content, or fill the Brand Voice section of brand.md. Trigger whenever the user mentions brand voice, tone, writing style, how their brand should sound, or wants to start setting up their brand.
---

# Brand Voice Skill

Your job is to extract the authentic voice of this business and document it clearly enough that any piece of content — a Facebook post, a TikTok caption, a Zalo message — sounds unmistakably like them.

Brand voice is not about being fancy. It's about being consistent. A cafe that always feels warm and local. A coaching brand that always feels direct and encouraging. The goal is to capture that consistency in writing.

## Step 1 — Check if brand.md exists

Read the file `/profiles/brand.md`.

- If it exists: note what's already filled in. You will only update Section 5 (Brand Voice & Tone) and Sections 1–4 (Brand Name, Industry, Location, Language) if they are empty.
- If it does not exist: you will create it using the schema from `.claude/commands/brand-foundation/references/brand-md-schema.md`.

## Step 2 — Collect input

Look at what the user has already provided in their message. Then choose the right path:

**Path A — User pasted existing content (posts, captions, website copy)**
Skip the questions. You have enough to work with. Go to Step 3.

**Path B — No content provided**
Ask these questions. Ask all of them at once — don't send one at a time:

---
"Để xây dựng giọng nói thương hiệu cho bạn, mình cần biết thêm một chút:

1. **Tên và lĩnh vực:** Tên doanh nghiệp của bạn là gì? Bạn kinh doanh trong lĩnh vực nào?
2. **Địa điểm:** Bạn hoạt động ở đâu? (TP.HCM, Hà Nội, toàn quốc...)
3. **Tính cách thương hiệu:** Nếu thương hiệu của bạn là một người, họ sẽ như thế nào? Chọn 3 từ mô tả: (vui vẻ / nghiêm túc / ấm áp / chuyên nghiệp / trẻ trung / đáng tin / táo bạo / thân thiện / truyền cảm hứng...)
4. **Nội dung mẫu:** Dán 2–3 bài đăng Facebook/TikTok hoặc đoạn nội dung bạn đã viết trước đây. Nếu chưa có, mô tả ngắn cách bạn thường nói chuyện với khách hàng.
5. **Ngôn ngữ:** Bạn muốn nội dung bằng tiếng Việt, tiếng Anh, hay cả hai?"

*(To build your brand voice, I need to know a bit more: 1. Business name and industry? 2. Location? 3. If your brand was a person, what would they be like — pick 3 words? 4. Paste 2–3 existing posts, or describe how you talk to customers. 5. Vietnamese, English, or both?)*

---

Wait for the user's answers before continuing.

## Step 3 — Analyze and extract

Based on what the user provided, extract the following. Think carefully — you're trying to capture something real about this business, not apply a generic template.

**Personality:** What 3 traits genuinely describe this brand? Look for evidence in the language they use, the examples they give, the way they describe their customers. Don't just reflect their words back — synthesize what you observe.

**Tone dimensions:**
- How formal or casual? (look at pronoun choices: bạn/mình vs anh/chị vs quý khách)
- How serious or playful? (look at emoji use, humor, energy)
- How direct or story-driven? (do they explain or do they show?)

**Vocabulary:**
- Words and phrases that feel natural for this brand
- Words that would feel off — too corporate, too cold, too generic, or simply not "them"
- Emojis: which ones fit, which ones don't

**Writing style:**
- Do they write short punchy sentences or longer flowing ones?
- How do their posts typically open? (a question, a bold claim, a scene, a fact?)
- How do their posts typically close? (a CTA, a question to the audience, a soft reflection?)

**Vietnamese register — this matters a lot:**
- `bạn/mình` → casual, peer-to-peer, most F&B, youth, lifestyle brands
- `anh/chị` → respectful, professional services, healthcare, real estate, education
- `quý khách` → very formal, luxury, high-end hospitality

**Platform adaptation:**
- Facebook: usually longer, more storytelling, ends with a question for comments
- TikTok: punchy, hook in first 3 words, energy matches the scroll speed
- Zalo: short, personal, direct — like a message from a friend

**Write 3 example sentences** that sound exactly like this brand. These are the clearest test of whether you've captured the voice correctly.

## Step 4 — Write to brand.md

Write the output to `/profiles/brand.md`.

If the file doesn't exist, create it using the full 12-section schema from `.claude/commands/brand-foundation/references/brand-md-schema.md`. Fill Sections 1–5. Leave Sections 6–12 as `[To be filled]`.

If the file exists, update only:
- Section 1 (Brand Name) — if empty
- Section 2 (Industry) — if empty
- Section 3 (Location) — if empty
- Section 4 (Language) — if empty
- Section 5 (Brand Voice & Tone) — always rewrite this section

Never touch Sections 6–12 if they already have content.

Always update the `Last updated` date at the top.

## Step 5 — Confirm

After writing, reply to the user with:

---
"✅ **Giọng nói thương hiệu của [Brand Name] đã được lưu.**

**Tóm tắt:**
- Tính cách: [3 traits]
- Giọng điệu: [one sentence]
- Xưng hô: [bạn/mình | anh/chị | quý khách]
- Ví dụ câu nói đúng tone:
  1. "[example 1]"
  2. "[example 2]"
  3. "[example 3]"

📁 Đã lưu vào: `/profiles/brand.md` — Mục 5

**Bước tiếp theo:** Chạy `/audience-profile` để xây dựng hồ sơ khách hàng mục tiêu."

*(Brand voice saved. Summary: personality, tone, register, 3 example sentences. Saved to brand.md Section 5. Next step: run /audience-profile)*

---
