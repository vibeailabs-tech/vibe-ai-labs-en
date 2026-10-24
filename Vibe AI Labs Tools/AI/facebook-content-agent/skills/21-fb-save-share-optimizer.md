# [21] Skill: fb-save-share-optimizer

## Mục đích
Chấm bài theo "save-worthiness" và "share-worthiness" trước khi publish.
FB 2026: 1 Save = 50 Likes, 1 Share to Story = 50 Likes — metric quan trọng nhất.

## Input
- `post_content`: bài đã qua quality layer
- `format_type`: single_image / carousel / reels
- `brand_voice`: context từ brand-voice-loader

## Scoring framework

### Save Score (0–10)
Bài có đáng lưu lại để xem sau không?

| Signal | Điểm |
|--------|------|
| Có checklist / framework / bước rõ ràng | +2 |
| Có số liệu / data cụ thể đáng reference | +2 |
| Là "evergreen" — đọc lại 3 tháng sau vẫn còn giá trị | +2 |
| Giải quyết pain point thực tế của audience | +2 |
| Ngắn gọn, dễ scan lại | +1 |
| Carousel dễ swipe lại | +1 |
| Quá dài, khó đọc lại | -1 |
| Nội dung mang tính thời điểm (trend 1 tuần) | -2 |

### Share Score (0–10)
Share bài này có làm người share trông tốt hơn không?

| Signal | Điểm |
|--------|------|
| Hot take / góc nhìn khác biệt đáng chia sẻ | +2 |
| Insight hữu ích có thể giúp bạn bè | +2 |
| Nội dung khiến người share trông "smart" hoặc "caring" | +2 |
| Story cảm xúc, dễ share cho người thân | +2 |
| Có "tag bạn bè" trigger tự nhiên | +1 |
| Nhẹ nhàng chia sẻ được mọi lúc | +1 |
| Quá promotional — chia sẻ bài này làm mình trông đang bán hàng | -3 |
| Nội dung quá niche, chỉ 1 nhóm nhỏ quan tâm | -1 |

## Gợi ý cải thiện

Nếu Save Score < 6: gợi ý cụ thể để tăng save-worthiness:
- Thêm checklist / bullet list có thể screenshot
- Thêm 1 framework / model có tên
- Thêm số liệu cụ thể
- Rút ngắn để dễ scan lại

Nếu Share Score < 6: gợi ý cụ thể để tăng share-worthiness:
- Làm mềm promotional angle
- Thêm 1 insight có thể giúp người khác
- Thêm "tag ai đang cần điều này" ở cuối
- Reframe từ "về sản phẩm của mình" sang "hữu ích cho ai đó"

## Threshold
Output-validator yêu cầu: Save Score ≥ 6 HOẶC Share Score ≥ 6 (không cần cả hai).

## Output

```yaml
save_share_score:
  save_score: [0–10]
  save_signals:
    positive: [list signal tốt tìm thấy]
    negative: [list signal kéo điểm xuống]
  share_score: [0–10]
  share_signals:
    positive: [list signal tốt tìm thấy]
    negative: [list signal kéo điểm xuống]
  passes_threshold: [true/false — save≥6 OR share≥6]
  improvement_suggestions:
    for_save: [list gợi ý nếu save < 6]
    for_share: [list gợi ý nếu share < 6]
  recommended_action: [publish_as_is / apply_suggestions_then_publish / rewrite]
```
