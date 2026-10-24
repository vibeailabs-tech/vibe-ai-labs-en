# [04] Skill: fb-post-writer

## Mục đích
Viết bài Facebook feed hoàn chỉnh — bao gồm hook, body, CTA, và A/B variants.
Đã gộp: hook generation, caption variants, CTA writing (tránh multi-agent overhead).

## Input
- `topic`: chủ đề bài
- `goal`: awareness / engagement / conversion
- `funnel_stage`: TOFU / MOFU / BOFU
- `mode`: `fresh` hoặc `iterate`
- `iterate_element`: (chỉ khi mode=iterate) `hook` / `cta` / `tone` / `length`
- `existing_post`: (chỉ khi mode=iterate) bài có sẵn cần cải thiện
- `brand_voice`: context từ brand-voice-loader
- `performance_hint`: từ performance-memory

## Chế độ hoạt động

### Mode: `fresh`
Tạo 2–3 variants từ đầu. Mỗi variant gồm:
- **Hook** (dòng 1–3): dạng hook khác nhau mỗi variant
  - Dạng hook options: câu hỏi gây tò mò / số liệu gây sốc / bold claim / "Nếu bạn..." / câu chuyện ngắn
- **Body**: phát triển từ hook, có 1–2 insight mạnh, ngắn đủ
- **CTA**: phù hợp với `goal` và `funnel_stage`
  - TOFU → CTA nhẹ (lưu bài, tag bạn, share)
  - MOFU → CTA trung (tìm hiểu thêm, comment hỏi)
  - BOFU → CTA mạnh (mua ngay, đăng ký, inbox)

### Mode: `iterate`
Nhận bài có sẵn + element cần test, tạo 3–5 variants CHỈ thay đổi đúng element đó:
- `hook`: giữ body + CTA, viết lại 4 dạng hook khác nhau
- `cta`: giữ hook + body, viết 4 CTA theo các intensity khác nhau
- `tone`: giữ nội dung, rewrite theo 3 tone (casual / professional / inspirational)
- `length`: giữ ý chính, viết 3 bản (short 100w / medium 200w / long 350w)

## Rules bắt buộc
- Không dùng từ trong `brand_voice.banned_terms`
- Ưu tiên từ trong `brand_voice.approved_glossary`
- Tone phải match `brand_voice.tone`
- Xưng hô nhất quán theo `brand_voice.tone`
- Hook phải nằm hoàn toàn trong 3 dòng đầu (trước "Xem thêm")
- Bài không quá 400 từ (trừ khi goal là educational deep-dive)

## Output

```yaml
variants:
  - id: "variant_1"
    hook_type: [loại hook]
    hook: [3 dòng đầu]
    body: [phần thân bài]
    cta: [call-to-action]
    full_post: [toàn bộ bài ghép lại]
    word_count: [số từ]
    pillar_mapped: [tên pillar]
    estimated_funnel_stage: [TOFU/MOFU/BOFU]
  - id: "variant_2"
    ...
recommended_variant: "variant_1"
recommendation_reason: [lý do chọn variant này]
```
