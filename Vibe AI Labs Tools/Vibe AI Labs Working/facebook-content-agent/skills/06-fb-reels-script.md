# [06] Skill: fb-reels-script

## Mục đích
Viết script Reels tối ưu completion rate — không chỉ tối ưu length.
FB 2026: 15s xem hết > 60s bị lướt. UTIS model survey khớp interest → must align với audience.

## Input
- `topic`: chủ đề video
- `goal`: awareness / engagement / conversion
- `duration_seconds`: 15 / 30 / 60 (mặc định 30)
- `brand_voice`: context từ brand-voice-loader

## Cấu trúc script theo thời lượng

### 15 giây
- 0–3s: Hook visual + voiceover
- 3–12s: 1 insight mạnh, không phí chữ
- 12–15s: Loop close + micro-CTA

### 30 giây
- 0–3s: Hook
- 3–8s: Setup (vấn đề / bối cảnh)
- 8–20s: Core value (2 beats)
- 20–27s: Resolution / payoff
- 27–30s: Loop close + CTA

### 60 giây
- 0–3s: Hook
- 3–10s: Setup
- 10–45s: Core value (4–5 beats, pattern interrupt mỗi 5–7s)
- 45–55s: Resolution
- 55–60s: Loop close + CTA

## Retention engineering (bắt buộc áp dụng)

### Pattern interrupt mỗi 5–7 giây
Chỉ định loại interrupt tại từng điểm trong script:
- Cut nhanh (jump cut)
- Zoom in / out
- Text pop xuất hiện đột ngột
- Sound shift (nhạc nền thay đổi)
- Camera angle thay đổi

### Hook 0–3s
- Visual quan trọng hơn voiceover (nhiều người xem không bật âm)
- Hook phải gây tò mò hoặc gây sốc trong 1 frame
- Text overlay phải đọc được trong 1 giây

### Loop close
- Câu cuối kết nối lại câu đầu → người xem bị kéo xem lại
- Ví dụ: Mở đầu "Tại sao bài tôi không có reach?" → Kết thúc "Và đó là lý do bài của bạn đang mất reach mỗi ngày."

## Output

```yaml
reels_script:
  duration: [15/30/60]
  hook:
    visual: [mô tả cảnh đầu tiên]
    voiceover: [lời nói 0–3s]
    text_overlay: [text hiển thị trên màn hình]
  beats:
    - timestamp: "3–8s"
      voiceover: [lời thoại]
      visual: [mô tả cảnh quay]
      text_overlay: [text overlay nếu có]
      pattern_interrupt: [loại interrupt tại điểm này]
    - timestamp: "8–15s"
      ...
  loop_close:
    voiceover: [câu kết nối lại mở đầu]
    visual: [cảnh visual cuối]
  cta:
    in_video: [CTA nói trong video]
    text_overlay: [CTA text trên màn hình]
  caption:
    hook: [3 dòng đầu caption]
    body: [mô tả ngắn]
    cta: [hành động mong muốn]
    hashtags_placeholder: "[hashtag-strategy sẽ thêm vào]"
  production_notes: [gợi ý quay/dựng ngắn gọn]
```
