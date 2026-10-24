# Agent 1 — Brand Foundation Agent ✅

> AI Marketing Agent Team · Agent 1 of 16

**Purpose:** Xây dựng `/profiles-output/brand.md` — file nền tảng mà tất cả 16 agents đọc trước khi thực thi.
**APIs/MCPs required:** None — pure Claude reasoning.
**Status:** Complete and tested.

---

## Overview

The Brand Foundation Agent is always built and run first. No other agent can operate without `brand.md`. It contains 5 skills that collectively fill all 12 sections of the master brand file.

---

## 5 Skills

### `/brand-setup` — Master Onboarding Command
**Purpose:** Runs all 4 skills in sequence. Builds the complete brand profile in one session.
**Input:** 18 questions across 4 parts (Brand & Voice / Audience / Positioning & Competitors / USP & Proof)
**Output:** All 12 sections of brand.md
**Use when:** New client starting from zero. Recommended entry point.

---

### `/brand-voice` — Brand Voice & Tone
**Purpose:** Extracts brand personality, tone, vocabulary, and writing style.
**Input:** Existing content (posts, captions) — or 5 questions if nothing exists.
**Output:** Sections 1–5 (Brand Name, Industry, Location, Language, Voice & Tone)

**Analyzes:**
- Personality traits (3 từ đặc trưng)
- Tone: formal/casual, serious/playful
- Vietnamese register: `bạn/mình` · `anh/chị` · `quý khách`
- Platform adaptation: Facebook · TikTok · Zalo
- 3 example sentences in brand voice

**5 câu hỏi:**
1. Tên doanh nghiệp và lĩnh vực?
2. Địa điểm hoạt động?
3. Tính cách thương hiệu (chọn 3 từ)?
4. Nội dung mẫu hoặc cách nói chuyện với khách?
5. Ngôn ngữ: Việt / Anh / Cả hai?

---

### `/audience-profile` — Target Audience & ICP
**Purpose:** Builds a detailed target audience profile and Ideal Customer Profile.
**Input:** 5 questions about customers.
**Output:** Section 6 (Target Audience) + Section 12 (Content Pillars)

**Analyzes:**
- Demographics: tuổi, giới tính, thu nhập, nghề nghiệp
- Psychographics: giá trị, lối sống, kỳ vọng, áp lực xã hội
- Top 5 pain points
- Buying triggers
- Online behavior: Facebook · TikTok · Zalo patterns
- ICP as a real Vietnamese person (tên, ngày thường, thói quen)
- 3–5 Content Pillars derived from audience interests

**5 câu hỏi:**
1. Mô tả khách hàng tốt nhất của bạn?
2. Họ gặp khó khăn gì trước khi tìm đến bạn?
3. Tại sao họ chọn bạn và nói gì khi giới thiệu?
4. Mạng xã hội họ dùng nhiều nhất và vào lúc nào?
5. Điều gì khiến họ do dự trước khi mua?

---

### `/positioning` — Competitive Positioning
**Purpose:** Defines where the brand sits in the market relative to competitors.
**Input:** 5 questions about competitors and differentiation.
**Output:** Section 7 (Positioning) + Section 9 (Core Offer) + Section 10 (Competitors)

**Positioning formula:**
> "For [audience], [brand] is the only [category] that [benefit] — unlike [competitors] who [weakness]."

**Analyzes:**
- Competitive landscape in Vietnam
- Gaps no competitor is claiming
- Trust signals specific to Vietnamese buyers
- Core offer: sản phẩm + giá + outcome + what makes it safe to buy
- Competitor table: strengths, weaknesses, how this brand differs

**5 câu hỏi:**
1. Kể tên 2–3 đối thủ chính — điểm mạnh và yếu?
2. Bạn làm được gì mà đối thủ không làm được?
3. Sản phẩm/dịch vụ chủ lực và mức giá?
4. Khách hàng nói gì khi giới thiệu bạn?
5. Muốn được nhớ đến như thế nào trong 3 năm tới?

---

### `/USP-definition` — Unique Selling Point & Key Messages
**Purpose:** Names the unique mechanism, builds the transformation story, and creates 5 headline directions.
**Input:** 5 questions about proof and unique advantage.
**Output:** Section 8 (USP) + Section 11 (Key Messages)

**Analyzes:**
- Unique mechanism: the specific, nameable thing only this brand does
- Before → After transformation (emotional, specific)
- Proof points: số liệu, giải thưởng, testimonials
- 5 headline directions in Vietnamese:
  1. Outcome (kết quả khách nhận được)
  2. Mechanism (cách bạn làm)
  3. Before/After (tương phản)
  4. Social proof (số liệu)
  5. Challenge (gọi ra vấn đề, định vị là giải pháp)
- 3 key messages the brand always comes back to

**5 câu hỏi:**
1. Có quy trình, phương pháp, hay cam kết đặc biệt nào không?
2. Khách hàng trông như thế nào TRƯỚC và SAU?
3. Có con số, giải thưởng, hay review nổi bật không?
4. Điều khách hay tự khen nhất là gì?
5. Lời hứa bạn tự tin 100% có thể thực hiện là gì?

---

## brand.md — 12 Sections Ownership

| Section | Name | Owned by |
|---|---|---|
| 1 | Brand Name | `/brand-voice` |
| 2 | Industry | `/brand-voice` |
| 3 | Location | `/brand-voice` |
| 4 | Language | `/brand-voice` |
| 5 | Brand Voice & Tone | `/brand-voice` |
| 6 | Target Audience | `/audience-profile` |
| 7 | Positioning | `/positioning` |
| 8 | USP | `/USP-definition` |
| 9 | Core Offer | `/positioning` |
| 10 | Competitors | `/positioning` |
| 11 | Key Messages | `/USP-definition` |
| 12 | Content Pillars | `/audience-profile` |

---

## Workflow Paths

**Full setup (recommended for new clients):**
```
/brand-setup → /brand-voice → /audience-profile → /positioning → /USP-definition → brand.md ✓
```

**Individual skill (update specific sections):**
```
Run any skill standalone → updates only its own sections → other sections untouched
```

---

## Key Rules

1. **Section ownership is strict** — each skill only writes its own sections, never overwrites others.
2. **brand.md is the single source of truth** — all 16 agents read this file before executing anything.
3. **`/brand-setup` is the recommended entry point** — builds all 12 sections in one session.
4. **No APIs or MCPs needed** — this entire agent runs on pure Claude reasoning.
