# [24] Skill: fb-visual-brief

## Mục đích
Tạo brief hình/video cho designer — brief cho người, không phải AI image prompt.

## Input
- `post_content`: bài đã viết
- `format_type`: single_image / carousel / reels
- `slide_count`: số slide nếu carousel
- `brand_voice`: context từ brand-voice-loader (tone, audience)
- `goal`: mục tiêu bài

## Output theo format

### Single Image Brief

```yaml
visual_brief:
  format: single_image
  aspect_ratio: "4:5 (portrait, tối ưu feed) hoặc 1:1 (square)"
  concept: [Mô tả ý tưởng hình ảnh chính — 2–3 câu]
  main_subject: [Chủ thể chính của hình]
  text_overlay:
    headline: [Text lớn chính — tối đa 5 từ]
    subtext: [Text nhỏ phụ nếu cần]
    text_placement: [top / center / bottom]
  color_direction:
    primary: [màu chính — hex hoặc mô tả]
    mood: [energetic / calm / professional / playful]
    avoid: [màu/phong cách cần tránh]
  photography_direction: [nếu dùng ảnh thật — góc chụp, model nếu có, bối cảnh]
  design_notes: [ghi chú thêm cho designer]
```

### Carousel Brief

```yaml
visual_brief:
  format: carousel
  slide_count: [số]
  aspect_ratio: "4:5 hoặc 1:1 — nhất quán tất cả slides"
  overall_style:
    color_palette: [bộ màu — primary + accent + background]
    typography: [font style: bold/light/mixed]
    template_style: [minimalist / vibrant / data-driven / storytelling]
  slides:
    - slide_number: 1
      purpose: "Cover — phải wow ngay"
      layout: [mô tả bố cục]
      text_overlay: [text chính trên slide]
      visual_element: [icon / photo / illustration / pattern]
    - slide_number: 2
      purpose: "Value slide"
      layout: ...
      text_overlay: ...
      visual_element: ...
  consistency_rules:
    - [Rule 1 về nhất quán giữa các slide]
    - [Rule 2]
```

### Reels Visual Brief

```yaml
visual_brief:
  format: reels
  aspect_ratio: "9:16 (vertical — bắt buộc)"
  duration: [giây]
  hook_visual: [Mô tả cảnh 0–3s — phải strong ngay frame đầu]
  key_scenes:
    - timestamp: "0–3s"
      visual: [mô tả cảnh]
      text_overlay: [text nếu có]
    - timestamp: "3–10s"
      visual: ...
      text_overlay: ...
  color_and_style:
    mood: [energetic / educational / inspirational / entertaining]
    lighting: [natural / studio / outdoor]
    editing_style: [fast-cut / slow / documentary]
  text_overlay_style: [font, màu, vị trí trên màn hình]
  b_roll_suggestions: [danh sách cảnh phụ có thể dùng]
  production_notes: [thiết bị cần, setup quay, lưu ý khi dựng]
```
