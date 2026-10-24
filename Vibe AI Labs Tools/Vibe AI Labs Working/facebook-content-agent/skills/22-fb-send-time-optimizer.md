# [22] Skill: fb-send-time-optimizer

## Mục đích
Recommend giờ publish tối ưu dựa trên audience activity pattern.
Standard feature của Hootsuite/Sprout — thiếu là thiếu sót cơ bản so với pro tools.

## Input
- `audience`: từ brand-voice-loader (độ tuổi, nghề nghiệp, địa điểm)
- `performance_hint`: từ performance-memory (engagement pattern của bài cũ)
- `format_type`: single_image / carousel / reels / story
- `post_goal`: awareness / engagement / conversion
- `day_preference`: (tuỳ chọn) user muốn đăng ngày nào trong tuần

## Logic tính toán

### Bước 1: Baseline theo audience persona
| Audience | Peak giờ | Lý do |
|---------|---------|-------|
| Nhân viên văn phòng (25–40) | 12:00–13:00, 20:00–22:00 | Giờ nghỉ trưa + sau giờ làm |
| Sinh viên / Gen Z (18–24) | 22:00–00:00, 10:00–11:00 | Tối muộn + buổi sáng trễ |
| Phụ huynh (30–45) | 21:00–22:30 | Sau khi con ngủ |
| Doanh nhân / freelancer | 07:00–08:30, 20:00–21:00 | Sáng sớm + tối |
| Người nội trợ | 10:00–11:30, 14:00–15:30 | Giữa buổi sáng/chiều |

### Bước 2: Điều chỉnh theo format
- **Reels**: +30 phút vào tối (thuật toán push Reels tốt hơn vào tối)
- **Carousel**: không đổi — phù hợp mọi giờ
- **Story**: 08:00–09:00 (xem story buổi sáng) hoặc 21:00–22:00

### Bước 3: Điều chỉnh theo goal
- **Awareness**: đăng lúc peak — nhiều người thấy nhất
- **Engagement**: đăng 30–60 phút trước peak — comment build up trước khi peak đến
- **Conversion**: đăng giờ người ta có tâm trí mua sắm (tối thứ 6, cuối tuần)

### Bước 4: Override từ performance-memory
Nếu `performance_hint` có dữ liệu engagement pattern thực tế → ưu tiên data này hơn baseline.

### Bước 5: Best days
| Goal | Ngày tốt nhất | Ngày tránh |
|------|--------------|-----------|
| Awareness | Thứ 3, Thứ 4 | Thứ 7, Chủ nhật (organic reach thấp hơn) |
| Engagement | Thứ 4, Thứ 5 | Thứ 2 (mọi người bận đầu tuần) |
| Conversion | Thứ 6, Thứ 7 | Thứ 2, Thứ 3 |

## Output

```yaml
send_time_recommendation:
  top_slots:
    - rank: 1
      day: [Thứ mấy]
      time_range: "HH:MM – HH:MM"
      reasoning: [lý do cụ thể cho slot này]
      confidence: [high/medium/low]
    - rank: 2
      day: ...
      time_range: ...
      reasoning: ...
      confidence: ...
    - rank: 3
      day: ...
      time_range: ...
      reasoning: ...
      confidence: ...
  data_source: [performance_memory / baseline_persona / combined]
  note: [ghi chú thêm nếu có — ví dụ: "Tránh đăng ngày 30/4 vì mọi người offline"]
```
