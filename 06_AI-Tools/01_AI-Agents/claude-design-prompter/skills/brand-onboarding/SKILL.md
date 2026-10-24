# Skill: Brand Onboarding

**Role:** First-run experience. Collects brand info in tiers — Tier 1 là bắt buộc (4 rounds), Tier 2 là optional dành cho ai có brand guidelines sẵn (2 rounds). Ghi vào `memory/brand-context.json`.

---

## Trigger Condition

Run this skill when ALL of the following are true:
- `brand-voice-loader` returns `brand_loaded: false`
- User has not yet described a design task in their first message

If user opened with a design request → skip, let `design-discovery` handle brand inline.

---

## Flow Overview

```
Opening
    ↓
Round 1 — Identity (4 câu)
    ↓
Round 2 — Strategy (3 câu)
    ↓
Round 3 — Visual system (4 câu)
    ↓
Round 4 — Rules & constraints (4 câu)
    ↓
Tier 2 gate
    ↓ có          ↓ không
Round 5       → Save & confirm
    ↓
Round 6
    ↓
Save & confirm
```

---

## Tier 1 — Must Have

### Opening message

> Chào! Mình sẽ lưu thông tin brand để không phải hỏi lại mỗi lần. 4 rounds ngắn — bắt đầu nhé.

---

### Round 1 — Identity

> 1. Tên brand là gì? Hoạt động trong ngành nào? (e.g. F&B, fintech, fashion, SaaS)
> 2. Target audience là ai? (e.g. "Gen Z nữ 18–25", "C-level doanh nghiệp vừa")
> 3. Dùng 3–5 tính từ mô tả personality của brand. (e.g. "bold, playful, irreverent" hoặc "calm, trustworthy, minimal")
> 4. Brand muốn trông giống ai? Không muốn bị nhầm với ai? (1–3 tên mỗi loại, bỏ qua nếu không có)

---

### Round 2 — Strategy

> 5. Brand tồn tại để làm gì? (mission — 1–2 câu ngắn)
> 6. Tagline của brand là gì? (câu 1 dòng xuất hiện trên mọi material — bỏ qua nếu chưa có)
> 7. Brand nói chuyện với khách hàng như thế nào?
>    - Nên nói / hay nói: (e.g. "dùng câu ngắn", "xưng 'mình'", "dùng số liệu cụ thể")
>    - Không bao giờ nói: (e.g. "không dùng jargon", "không hứa hẹn quá mức", "không formal quá")

---

### Round 3 — Visual System

> 8. Màu brand: primary, accent, background, text — HEX nếu có. Có màu phụ (secondary) nào không?
> 9. Font đang dùng: heading và body — tên font. Bỏ qua nếu chưa có.
> 10. Imagery style: ảnh chụp thật / illustration / abstract / không dùng ảnh người — hoặc mô tả rule ảnh của brand.
> 11. Platform thiết kế ưu tiên? (e.g. Facebook, Instagram, web, print) — và brand dùng ngôn ngữ nào? (Việt / Anh / song ngữ)

---

### Round 4 — Rules & Constraints

> 12. Tone của brand: một câu mô tả cảm giác brand muốn truyền tải. (e.g. "như người bạn thông minh", "authority nhưng không lạnh lùng")
> 13. Những thứ brand KHÔNG BAO GIỜ làm về mặt visual? (e.g. "không dùng màu đỏ", "không ảnh stock người nước ngoài", "không border radius")
> 14. Logo: có file chưa? Mô tả ngắn logo trông như thế nào.
> 15. Có design rule đặc biệt nào khác không? (bỏ qua nếu không)

---

## Tier 2 Gate

Sau Round 4, hỏi:

> Tier 1 xong — đủ để design được rồi.
>
> Bạn có brand guidelines chi tiết hơn không? (color values đầy đủ RGB/CMYK/Pantone, typography scale, layout grid, logo rules, data viz style, v.v.) Nếu có, mình collect thêm Tier 2 để output chuẩn hơn. Nếu không, mình save và bắt đầu luôn.

- User nói **có / muốn điền thêm** → tiếp tục Round 5–6
- User nói **không / skip / bắt đầu luôn** → nhảy thẳng xuống Save

---

## Tier 2 — Nice to Have

### Round 5 — Extended Strategy & Color

> 16. Brand values là gì? (2–4 giá trị cốt lõi, e.g. "transparency, speed, craft")
> 17. Vision của brand: brand muốn thế giới trông như thế nào sau khi brand thành công?
> 18. Vocabulary — từ brand hay dùng vs. tránh dùng:
>     - Preferred: (e.g. "craft, considered, intentional")
>     - Avoid: (e.g. "cheap, fast, easy, innovative")
> 19. Color values đầy đủ:
>     - RGB: primary, accent (nếu có)
>     - CMYK: primary, accent (nếu in ấn)
>     - Pantone: primary, accent (nếu packaging / branding vật lý)
> 20. Semantic colors: màu cho error, success, warning, info — HEX?
>     Dark mode: background / surface / text?
>     Gradient: brand dùng gradient không? Kiểu gì?

---

### Round 6 — Design System

> 21. Typography scale: size của H1, H2, H3, H4, body, caption — px hoặc rem.
>     Font display (hero headline)? Font caption (label nhỏ)?
>     Weights, line height, letter spacing có rule không?
> 22. Logo đầy đủ:
>     - Variants: có bao nhiêu version? (primary / horizontal / icon-only / reversed)
>     - File formats có sẵn: SVG / PNG / EPS / PDF?
>     - Minimum size: nhỏ nhất logo có thể hiển thị (px cho digital, mm cho print)?
>     - Don'ts: những điều không được làm với logo?
>     - Safe zone: khoảng cách tối thiểu quanh logo?
>     - Logo có animated version không? Nếu có: duration bao lâu? Easing kiểu gì?
> 23. Photography direction chi tiết:
>     - Lighting: natural / studio / golden hour / harsh / backlit?
>     - Composition: centered / rule of thirds / overhead / close-up / wide?
>     - Color grading: warm film / cool editorial / desaturated / vivid / high contrast?
> 24. Brand pattern / texture: brand có graphic element riêng không? (pattern, texture, illustration system)
>     Data visualization: chart dùng màu gì? Style gì? (e.g. "flat bars, brand colors, no grid lines")
> 25. Document templates: brand có spec cho những loại tài liệu nào không?
>     - Business card: layout, size, thông tin nào bắt buộc?
>     - Letterhead: margin, vị trí logo, footer?
>     - Presentation master: slide layout, header/footer rule?
> 26. Layout system: grid mấy columns? Spacing scale? Border radius? Shadow/elevation?
> 27. Iconography style: filled / outline / duotone / custom?
>     Motion: animation principles? (e.g. "ease-out, max 300ms, không bounce")
>     Accessibility: min contrast ratio? Min font size?
>     Print specs: CMYK hay RGB? Bleed và margin?

---

## Parsing Rules

**Tier 1:**

| Trường | Parse |
|---|---|
| `name`, `industry`, `target_audience` | Lấy trực tiếp |
| `brand_personality` | Array of adjectives |
| `mission` | String, 1–2 câu |
| `tagline` | String hoặc `""` |
| `reference_brands`, `avoid_brands` | Array, `[]` nếu không có |
| `colors.*` | HEX. Tên màu → convert + báo lại |
| `colors.secondary` | Array of HEX |
| `typography.heading`, `.body` | Font name hoặc `""` |
| `tone` | String |
| `voice_dos`, `voice_donts` | Array of strings |
| `imagery_style` | `"photography"` / `"illustration"` / `"abstract"` / `"no humans"` / mô tả tự do |
| `never_do` | Array of strings |
| `platform_priority` | Array lowercase: `["facebook", "instagram", "web"]` |
| `language` | `"vi"` / `"en"` / `"vi+en"` |
| `logo` | String mô tả hoặc `""` |
| `design_notes` | String |

**Tier 2:**

| Trường | Parse |
|---|---|
| `brand_values` | Array |
| `vision` | String |
| `positioning_statement` | String |
| `vocabulary.preferred`, `.avoid` | Array of strings |
| `colors.rgb.*` | `"rgb(r, g, b)"` format |
| `colors.cmyk.*` | `"C% M% Y% K%"` format |
| `colors.pantone.*` | `"PMS XXXX C"` format |
| `colors.semantic.*` | HEX |
| `colors.dark_mode.*` | HEX |
| `colors.gradient` | Mô tả ngắn |
| `typography.display`, `.caption` | Font name |
| `typography.scale.*` | Size values, e.g. `"48px"` |
| `typography.weights`, `.line_height`, `.letter_spacing` | String |
| `logo.variants` | Array of strings |
| `logo.safe_zone` | String, e.g. `"1x logo height"` |
| `logo.min_size` | e.g. `"24px digital, 10mm print"` |
| `logo.file_formats` | Array: `["SVG", "PNG", "EPS"]` |
| `logo.dont` | Array of strings |
| `logo.animated.has_animation` | Boolean |
| `logo.animated.duration` | e.g. `"600ms"` |
| `logo.animated.easing` | e.g. `"ease-out"` |
| `photography.lighting` | `"natural"` / `"studio"` / `"golden hour"` / `"harsh"` / `"backlit"` |
| `photography.composition` | `"centered"` / `"rule of thirds"` / `"overhead"` / `"close-up"` / `"wide"` |
| `photography.color_grading` | `"warm film"` / `"cool editorial"` / `"desaturated"` / `"vivid"` / `"high contrast"` |
| `brand_pattern` | Mô tả hoặc `""` |
| `data_viz_style` | Mô tả hoặc `""` |
| `document_templates.business_card` | Mô tả layout hoặc `""` |
| `document_templates.letterhead` | Mô tả layout hoặc `""` |
| `document_templates.presentation_master` | Mô tả layout hoặc `""` |
| `layout.*` | String values |
| `iconography_style` | `"filled"` / `"outline"` / `"duotone"` / `"custom"` |
| `motion_principles` | String |
| `accessibility.*` | e.g. `"4.5:1"`, `"14px"` |
| `print_specs.*` | String values |

**Nếu user cung cấp màu dạng tên** → convert sang HEX gần nhất và confirm:
> *"Mình đã convert 'xanh navy' → #0A1628, bạn có thể đổi lại nếu cần."*

---

## Save to Memory

Ghi vào `memory/brand-context.json` theo đúng cấu trúc JSON sau. Set `brand_loaded: true` ngay khi Tier 1 hoàn thành — không cần đợi Tier 2.

**Cấu trúc JSON bắt buộc:**

```json
{
  "brand_loaded": true,
  "tier1": {
    "name": "...",
    "industry": "...",
    "target_audience": "...",
    "brand_personality": [],
    "mission": "...",
    "tagline": "...",
    "reference_brands": [],
    "avoid_brands": [],
    "colors": {
      "primary": "#HEX",
      "accent": "#HEX",
      "background": "#HEX",
      "text": "#HEX",
      "secondary": []
    },
    "typography": { "heading": "...", "body": "..." },
    "tone": "...",
    "voice_dos": [],
    "voice_donts": [],
    "imagery_style": "...",
    "never_do": [],
    "platform_priority": [],
    "language": "...",
    "logo": "...",
    "design_notes": "..."
  },
  "tier2": {
    "brand_values": [],
    "vision": "...",
    "positioning_statement": "...",
    "vocabulary": { "preferred": [], "avoid": [] },
    "colors": {
      "rgb": { "primary": "", "accent": "" },
      "cmyk": { "primary": "", "accent": "" },
      "pantone": { "primary": "", "accent": "" },
      "semantic": { "error": "", "success": "", "warning": "", "info": "" },
      "dark_mode": { "background": "", "surface": "", "text": "" },
      "gradient": "",
      "usage_rules": ""
    },
    "typography": {
      "display": "", "caption": "",
      "scale": { "h1": "", "h2": "", "h3": "", "h4": "", "body": "", "caption": "" },
      "weights": "", "line_height": "", "letter_spacing": ""
    },
    "logo": {
      "variants": [], "safe_zone": "", "min_size": "", "file_formats": [],
      "dont": [],
      "animated": { "has_animation": false, "duration": "", "easing": "" }
    },
    "photography": { "lighting": "", "composition": "", "color_grading": "" },
    "brand_pattern": "",
    "data_viz_style": "",
    "document_templates": { "business_card": "", "letterhead": "", "presentation_master": "" },
    "layout": { "grid": "", "spacing_scale": "", "border_radius": "", "shadow": "" },
    "iconography_style": "",
    "motion_principles": "",
    "accessibility": { "min_contrast_ratio": "", "min_font_size": "" },
    "print_specs": { "color_mode": "", "bleed": "", "margin": "" }
  }
}
```

Khi chỉ hoàn thành Tier 1: ghi đúng vào `tier1`, để `tier2` với tất cả trường là `""` / `[]` / `false`.

---

## Confirmation Message

> Brand đã được lưu. Từ giờ mình sẽ tự động enforce brand này vào mọi design output.
>
> Bạn muốn làm design gì đầu tiên?

---

## Edge Cases

**User skip brand setup:**
> Ghi `brand_loaded: false`, `tier1.design_notes: "no_brand_skip"`. Không hỏi lại trong session này.

**User chỉ điền một phần:**
> Ghi những gì có, `""` / `[]` cho phần còn lại. Không ép điền đủ. Set `brand_loaded: true` nếu đã có ít nhất tên brand + màu primary.

**User muốn update sau:**
> Nếu user nói "đổi brand", "update màu", "thêm font" → hỏi lại chỉ round liên quan, ghi đè trường tương ứng trong đúng `tier1` hoặc `tier2`. Không chạy lại toàn bộ flow.

**User paste brand guidelines document:**
> Parse trực tiếp từ document, map vào các trường Tier 1 + Tier 2 theo đúng cấu trúc JSON trên, confirm với user trước khi save.
