# [08] Skill: fb-content-calendar

## Mục đích
Lên lịch content 1 tuần hoặc 1 tháng — bảng ngày/giờ/chủ đề/format/pillar/CTA.

## Input
- `period`: week (7 ngày) / month (30 ngày)
- `theme`: chủ đề tháng hoặc campaign (ví dụ: "ra mắt sản phẩm mới", "mùa tựu trường")
- `key_dates`: các ngày quan trọng cần có content (ngày lễ, event, deadline sale)
- `frequency`: số bài/tuần (mặc định 4)
- `send_time_hint`: từ fb-send-time-optimizer (time slot tối ưu)
- `brand_voice`: context từ brand-voice-loader

## Quy trình lên lịch

### Bước 1: Map key dates
Điền content bắt buộc vào key dates trước (event, sale, deadline).

### Bước 2: Phân bổ pillars
Đảm bảo mỗi pillar xuất hiện đủ theo tỷ lệ trong `brand_voice.pillars`.
Ví dụ: Pillar 1 (30%) = ~5–6 bài/tháng nếu đăng 4 bài/tuần.

### Bước 3: Chọn format đa dạng
- Không lặp cùng format 2 bài liên tiếp (carousel → post → reels → post)
- Reels ít nhất 1 lần/tuần nếu brand dùng video
- Story/behind-the-scenes ít nhất 2 lần/tháng

### Bước 4: Đặt giờ
Dùng `send_time_hint` để chọn ngày/giờ cho từng bài theo goal.

### Bước 5: Đặt CTA đa dạng
Không để cùng 1 loại CTA quá 3 bài liên tiếp.

## Output

```yaml
content_calendar:
  period: [week/month]
  theme: [chủ đề]
  total_posts: [số bài]
  pillar_distribution:
    - pillar: [tên]
      posts: [số bài]
      percentage: [%]
  schedule:
    - date: "YYYY-MM-DD"
      day_of_week: [Thứ mấy]
      time: "HH:MM"
      topic: [chủ đề bài]
      format: [single_image/carousel/reels/story]
      pillar: [tên pillar]
      goal: [awareness/engagement/conversion]
      cta_type: [save/share/comment/inbox/link]
      notes: [ghi chú đặc biệt nếu có — key date, event tie-in]
    - date: ...
  monthly_summary:
    awareness_posts: [số]
    engagement_posts: [số]
    conversion_posts: [số]
    formats_used: [dict format: số lần]
```
