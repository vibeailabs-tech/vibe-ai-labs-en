# [19] Skill: fb-competitor-scan

## Mục đích
Phân tích content đối thủ → pattern content, cơ hội differentiation, benchmark engagement rate.

## Input
- `competitors`: list tên page hoặc link Facebook page đối thủ (tối đa 5)
- `scan_depth`: recent_posts (7 ngày) / monthly (30 ngày)
- `brand_voice`: context từ brand-voice-loader

## Quy trình

### Bước 1: Thu thập data
Dùng web search để tìm thông tin công khai về page đối thủ:
- Bài gần đây (dạng text, chủ đề, format)
- Engagement pattern (bài nào nhiều tương tác)
- Tone và style content
- Hashtag thường dùng
- Tần suất đăng

### Bước 2: Phân tích pattern
Với mỗi đối thủ:
- Format nào họ hay dùng nhất?
- Chủ đề nào họ cover?
- Hook style của họ là gì?
- Điểm mạnh rõ ràng nhất trong content?
- Điểm yếu / gap rõ ràng nhất?

### Bước 3: Benchmark engagement
Ước tính engagement rate từ data công khai (like/comment/share visible).
So sánh với benchmark ngành.

### Bước 4: Tìm differentiation opportunity
Câu hỏi quan trọng nhất: "Brand mình có thể làm gì mà đối thủ KHÔNG làm hoặc làm kém?"
- Chủ đề nào đối thủ bỏ qua?
- Format nào đối thủ chưa khai thác?
- Tone/angle nào đối thủ không có?
- Audience segment nào đối thủ không serve?

## Output

```yaml
competitor_scan:
  scan_date: [ngày scan]
  competitors_analyzed: [số]
  competitor_profiles:
    - name: [tên page]
      url: [link nếu có]
      posting_frequency: [số bài/tuần ước tính]
      dominant_formats: [list format hay dùng]
      top_topics: [list chủ đề hay cover]
      content_strengths: [điểm mạnh]
      content_weaknesses: [điểm yếu / gap]
      estimated_engagement_rate: [% ước tính]
      hook_style: [loại hook họ hay dùng]
      notable_patterns: [pattern đặc biệt nếu có]
  competitive_landscape:
    market_avg_engagement: [% trung bình ngành ước tính]
    most_common_format: [format phổ biến nhất trong ngành]
    oversaturated_topics: [chủ đề đối thủ đều làm — nên tránh hoặc differentiate]
  differentiation_opportunities:
    - opportunity: [cơ hội cụ thể]
      why_it_works: [lý do đây là gap thực sự]
      suggested_approach: [cách brand mình khai thác]
      priority: high / medium / low
  recommended_moves:
    - [Move 1 — action cụ thể brand nên làm ngay]
    - [Move 2]
    - [Move 3]
```
