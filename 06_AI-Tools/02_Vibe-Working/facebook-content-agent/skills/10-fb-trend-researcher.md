# [10] Skill: fb-trend-researcher

## Mục đích
Tìm trending topics phù hợp ngành + brand, gợi ý angle khai thác phù hợp brand voice.
Dùng web search real-time — không đoán trend từ training data.

## Input
- `industry`: ngành của thương hiệu (ví dụ: skincare, digital marketing, F&B, education)
- `timeframe`: this_week / this_month / next_month
- `brand_voice`: context từ brand-voice-loader
- `existing_pillars`: để filter trend phù hợp pillar

## Quy trình

### Bước 1: Search trends
Dùng web search để tìm:
- Trending topics trên Facebook/social media VN trong ngành
- Hashtag đang tăng reach
- Chủ đề đang được nhiều page cùng ngành đề cập
- Tin tức / sự kiện ngành trong `timeframe`

Search queries:
- "[industry] trending Vietnam Facebook [month/year]"
- "hot topic [industry] mạng xã hội [tháng]"
- Tên các page lớn trong ngành để xem họ đang nói về gì

### Bước 2: Filter theo brand fit
Loại bỏ trend:
- Không phù hợp `brand_voice.pillars`
- Vi phạm `brand_voice.banned_terms` hoặc tone
- Quá controversial cho brand này
- Đã qua đỉnh (trend đang giảm)

### Bước 3: Tạo angle phù hợp brand
Với mỗi trend còn lại, tạo 1–2 angle khai thác phù hợp brand voice — không chỉ "đây là trend", mà "brand mình nên nói về trend này theo hướng nào".

## Output

```yaml
trend_report:
  industry: [ngành]
  timeframe: [tuần/tháng]
  generated_at: [timestamp]
  trends:
    - trend_name: [tên trend]
      description: [trend này về gì]
      evidence: [nơi tìm thấy — page, hashtag, tin tức]
      momentum: rising | peak | declining
      brand_fit_score: [1–5]
      angles:
        - [Angle 1 — cách brand có thể khai thác trend này]
        - [Angle 2 — góc khác]
      suggested_format: [format phù hợp nhất]
      urgency: [high/medium/low — cần đăng trong bao lâu]
  filtered_out:
    - trend_name: [tên]
      reason: [lý do filter]
  recommendation: [1–2 trend nên làm ngay + lý do ưu tiên]
```
