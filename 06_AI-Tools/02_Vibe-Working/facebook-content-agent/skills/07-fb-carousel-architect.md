# [07] Skill: fb-carousel-architect

## Mục đích
Thiết kế multi-slide carousel — engagement gấp 1.5–3 lần single image.

## Input
- `topic`: chủ đề carousel
- `goal`: mục tiêu bài
- `slide_count`: số slide (5–10, mặc định 7)
- `brand_voice`: context từ brand-voice-loader

## Nguyên tắc thiết kế carousel

### Cover slide (Slide 1) — Hook
- Phải kéo người ta swipe ngay
- Công thức: [Con số / Câu hỏi gây tò mò] + [Promise rõ ràng sẽ học được gì]
- Ví dụ: "7 lỗi làm bài Facebook của bạn chết reach" hoặc "Framework giúp mình tăng save 3x"
- Text ngắn, readable trên mobile

### Slide giữa (2 đến N-1) — Value reveal
- Mỗi slide = 1 idea / 1 tip / 1 step — không nhồi nhiều
- Mỗi slide phải đứng được một mình nếu ai screenshot
- Tạo open loop sang slide tiếp: "Nhưng đây không phải điều quan trọng nhất..."
- Slide cuối value phải là strong insight, không phải filler

### Slide cuối (Slide N) — CTA
- 1 hành động rõ ràng (save / share / comment / inbox / link)
- Không quá 2 CTA trong cùng 1 slide
- Nhắc lại promise từ cover: "Bạn đã có [X], giờ hãy [action]"

### Caption đi kèm
- Hook mạnh (3 dòng đầu mô tả carousel này cho ai)
- Không spoil toàn bộ nội dung slide
- CTA nhắc swipe: "Swipe để xem đủ [X] bước →"

## Output

```yaml
carousel:
  cover:
    slide_number: 1
    headline: [tiêu đề chính]
    subtext: [mô tả ngắn nếu cần]
    design_note: [gợi ý visual ngắn]
  slides:
    - slide_number: 2
      title: [tiêu đề slide]
      content: [nội dung chính — 1 idea]
      open_loop: [câu kéo sang slide tiếp, nếu cần]
      design_note: [gợi ý visual]
    - slide_number: 3
      ...
  cta_slide:
    slide_number: [N]
    headline: [tiêu đề CTA]
    action: [hành động cụ thể]
    design_note: [gợi ý visual]
  caption:
    hook: [3 dòng đầu]
    body: [mô tả ngắn nội dung carousel]
    cta: [swipe prompt + action]
    full_caption: [toàn bộ caption]
```
