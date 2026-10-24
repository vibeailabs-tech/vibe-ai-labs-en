# Skill: Design Discovery

**Role:** Ask the right questions at the right time. Maximum 3 questions total. Never dump all questions at once.

---

## Step 1 — Detect Output Type

Infer the output type from the user's input before asking anything:

| Signal words | Output type |
|---|---|
| deck, slide, pitch, presentation | `deck` |
| landing, website, page, one-pager | `landing_page` |
| app, prototype, UI, flow, screen | `prototype` |
| post, banner, social, Instagram, Facebook, TikTok, LinkedIn | `social_asset` |
| reel, story, vertical video, motion, animated, 9:16 video | `motion_graphic` |
| illustration, artwork, vẽ, hình, icon set | `illustration` |
| brochure, report, email template, PDF, catalogue | `collateral` |

If ambiguous, ask once: "Bạn muốn output là loại gì — slide deck, landing page, social post, reel/motion, hay gì khác?"

---

## Step 2 — Build Question Set

Select questions based on output type. Maximum 3 questions total.

If `[NO_BRAND]` flag is set → add 1 brand question to the set (counts toward the 3-question limit).

**Brand question (only if [NO_BRAND]):**
> "Bạn có brand màu sắc / font chưa? Nếu có, share cho mình (HEX codes + font names). Nếu chưa, mình sẽ suggest dựa trên ngành và tone."

**Per output type:**

`deck`:
- Audience là ai? (e.g., VCs, khách hàng, nội bộ)
- Bao nhiêu slide? Có data/chart không?

`landing_page`:
- CTA chính là gì? (e.g., đăng ký, mua hàng, liên hệ)
- Above-fold message là gì?

`prototype`:
- Mobile hay web? (nếu mobile: iOS hay Android style?)
- Flow chính cần thể hiện là gì? (list màn hình theo thứ tự)

`social_asset`:
- Platform? (Facebook / Instagram / LinkedIn / TikTok)
  *(Không hỏi ratio — sẽ infer từ platform: Facebook/IG feed = 1:1, portrait feed = 4:5, Stories/Reels = 9:16)*

`motion_graphic`:
- Platform và duration? (e.g., Instagram Reel 15s, TikTok 30s)
- Có text animation / voiceover / music beat không?

`illustration`:
- Style mong muốn? (flat, isometric, cartoonic, editorial, geometric)
- Dùng để làm gì? (hero image, icon set, standalone art)

`collateral`:
- Format cuối là gì? (PDF in, HTML email, digital brochure)
- Bao nhiêu trang/sections?

---

## Step 3 — Ask Questions

- Ask maximum 3 questions, grouped in one message
- Do NOT ask questions you can already infer from the user's original input
- Do NOT ask brand questions if `brand_loaded: true`
- Do NOT ask about ratio for `social_asset` — infer from platform automatically

---

## Step 4 — Build Brief

After receiving answers, synthesize into a structured brief and pass to `design-prompt-writer`:

```yaml
output_type: [type]
purpose: [who is it for, what is it for]
brand: [brand block from brand-voice-loader output, or flag: [NO_BRAND]]
platform: [specific platform]
platform_constraints: [ratio, canvas size, duration if motion]
content_requirements: [what text/data/images/animations are needed]
mood_or_tone: [inferred from user description]
language: [from brand context, or inferred]
special_notes: [anything else the user specified]
```
