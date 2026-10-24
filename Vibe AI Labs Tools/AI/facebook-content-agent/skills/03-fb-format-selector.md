# [03] Skill: fb-format-selector

## Mục đích
Quyết định format tối ưu trước khi viết — tránh viết xong mới biết sai format.

## Input
- `topic`: chủ đề bài
- `goal`: mục tiêu (awareness / engagement / conversion)
- `audience`: từ brand-voice-loader
- `performance_hint`: gợi ý từ performance-memory (format nào đang win)

## Logic chọn format

### Bảng quyết định chính

| Tình huống | Format khuyến nghị | Lý do |
|-----------|-------------------|-------|
| Ra mắt sản phẩm mới, nhiều thông tin | Carousel 6–8 slides | Nhiều thông tin → nhiều swipe → engagement cao |
| Tip / checklist / how-to | Carousel 5–7 slides | Dạng list → save-worthy |
| Câu chuyện cảm xúc, ngắn | Single image + long caption | Story không cần nhiều hình |
| Tutorial video, quy trình | Reels 30–60s | Video > image cho hướng dẫn |
| Hook / attention ngắn | Reels 15s | Short-form = completion rate cao |
| Promotion / offer | Single image hoặc Carousel | Rõ ràng, ít slide |
| Behind the scenes | Reels hoặc Story | Casual, thật |
| Tổng hợp kiến thức sâu | Carousel 7–10 slides | Reference content = nhiều save |
| Link bài blog / podcast | Link post — NHƯNG đặt link xuống first comment | Body sạch tránh bị giảm reach |
| Quảng cáo trả phí | Theo mục tiêu campaign |  |

### Rules bổ sung (FB 2026)
- Mid-2025 Meta gộp tất cả video vào Reels feed — format video = Reels
- Reels 15s completion > Reels 60s bị lướt → ưu tiên 15–30s nếu không cần giải thích sâu
- Carousel swipe rate tính là engagement → tốt hơn single image về MSI

### Override rule
Nếu `performance_hint` cho thấy format X đang underperform với audience này → tránh X, suggest format đang win.

## Output

```yaml
format_decision:
  recommended_format: [single_image / carousel / reels / story / link_post]
  slide_count: [số slide nếu carousel, null nếu không]
  duration_seconds: [thời lượng nếu reels, null nếu không]
  reasoning: [giải thích ngắn lý do chọn format này]
  alternative_format: [format thứ 2 nếu muốn thử A/B]
```
