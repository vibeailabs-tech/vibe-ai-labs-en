# Claude Design Prompter

Một agent chạy trên Claude, giúp bạn viết prompt chuẩn cho Claude Design.

**Vấn đề nó giải quyết:** Bạn có ý tưởng design nhưng không biết cách mô tả đúng để Claude Design hiểu. Agent này hỏi đúng câu, đúng lúc — rồi tự viết prompt hoàn chỉnh cho bạn paste vào.

---

## Cách dùng

### Bước 1 — Load agent

Mở Claude, paste toàn bộ nội dung file `ORCHESTRATOR.md` vào đầu conversation.

### Bước 2 — Bắt đầu

Nói bất cứ thứ gì. Agent sẽ tự biết phải làm gì tiếp theo.

**Nếu chưa có brand:**
> Agent sẽ hỏi thông tin brand của bạn qua 4 rounds ngắn (Tier 1).
> Sau đó lưu lại — lần sau không hỏi nữa.

**Nếu đã có brand:**
> Agent load brand context tự động và bắt đầu hỏi về design task luôn.

### Bước 3 — Mô tả design bạn muốn

Nói tự nhiên, không cần format:

> *"Làm social post Facebook về cà phê Việt Nam, vintage style"*
> *"Cần pitch deck cho startup fintech, 12 slides"*
> *"Vẽ illustration cánh đồng lúa cartoonic"*

Agent sẽ hỏi tối đa 3 câu để làm rõ — rồi tự viết prompt.

### Bước 4 — Lấy prompt

Copy prompt output → paste vào Claude Design → done.

---

## 6 loại output được hỗ trợ

| Loại | Dùng khi |
|---|---|
| `deck` | Pitch deck, presentation, slide |
| `landing_page` | Landing page, one-pager, website |
| `prototype` | App prototype, UI flow, màn hình mobile/web |
| `social_asset` | Facebook post, Instagram, banner quảng cáo |
| `illustration` | Artwork, illustration, icon set |
| `collateral` | Brochure, report, email template, PDF |

---

## Brand Memory

Lần đầu dùng, agent hỏi thông tin brand của bạn và lưu vào `memory/brand-context.json`. Từ lần sau, brand được tự động inject vào mọi prompt — bạn không cần nhắc lại.

**Brand system gồm 2 tier:**

**Tier 1 — Must have** (4 rounds, ~15 câu)
Đủ để design được ngay. Gồm: tên, ngành, audience, personality, mission, tagline, màu sắc, font, tone, voice, imagery style, platform, logo, constraints.

**Tier 2 — Nice to have** (2 rounds, ~12 câu)
Dành cho ai có brand guidelines chi tiết. Gồm: typography scale, color system đầy đủ (RGB/CMYK/Pantone), logo system, layout grid, photography direction, data viz style, document templates, motion principles, accessibility specs.

**Update brand bất kỳ lúc nào:**
> *"Đổi màu primary thành #FF5733"*
> *"Thêm font Inter cho body"*
> *"Update tone: bớt formal hơn"*

Agent sẽ ghi đè đúng trường, không chạy lại toàn bộ flow.

---

## Cấu trúc thư mục

```
claude-design-prompter/
│
├── ORCHESTRATOR.md                        ← Load file này vào Claude
│
├── skills/
│   ├── brand-voice-loader/SKILL.md        ← Đọc & inject brand context
│   ├── brand-onboarding/SKILL.md          ← Thu thập brand info lần đầu
│   ├── design-discovery/SKILL.md          ← Hỏi về design task
│   └── design-prompt-writer/
│       ├── SKILL.md                       ← Viết prompt hoàn chỉnh
│       └── references/
│           ├── output-types.md            ← Template cho 6 loại output
│           ├── vocabulary.md              ← Từ điển design language
│           └── prompt-examples.md         ← Before/after examples
│
└── memory/
    └── brand-context.json                 ← Brand data được lưu ở đây
```

---

## Ví dụ output

**Input:**
> "Làm Facebook post về cà phê sữa đá, vintage style, nền đỏ"

**Output:**
```
Create a Facebook post visual for a Vietnamese iced coffee brand.

FORMAT: 1:1 ratio, 1080x1080px.

VISUAL DIRECTION:
Vintage poster aesthetic — aged, textured, warm. Distressed grain overlay
(15% opacity). Background: aged brick red (#A63224), full bleed.
Central composition: oval badge/emblem frame in dark brown (#2C1A0E)...

COPY ON VISUAL:
"CAFE SỮA ĐÁ" — Playfair Display 700, 52px, cream (#F5ECD7)...

CONSTRAINTS:
80px safe zone. No modern sans-serif fonts. PNG export.
```

---

## Những gì agent không làm

- Không tự design — nó chỉ viết prompt
- Không generate ảnh — paste prompt vào Claude Design để làm việc đó
- Không hỏi lại brand nếu đã lưu
- Không dùng từ vague: "đẹp", "hiện đại", "chuyên nghiệp" — luôn dùng HEX, font name, layout cụ thể
