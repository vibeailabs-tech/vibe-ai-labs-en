# [17] Skill: fb-performance-review

## Mục đích
Phân tích hiệu quả content → nhận xét + gợi ý điều chỉnh.
Output feed vào performance-memory để agent học theo thời gian.

## Input
- `metrics_data`: dữ liệu metrics (paste từ Facebook Insights hoặc nhập tay)
  - reach, impressions, likes, comments, shares, saves, link_clicks
  - watch_time_completion (nếu có Reels)
  - follower_change
- `period`: 7_days / 30_days / custom
- `posts`: list bài kèm metrics cá nhân (tuỳ chọn — phân tích chi tiết từng bài)
- `brand_voice`: context từ brand-voice-loader

## Metrics hierarchy 2026

Ưu tiên đọc metrics theo tầm quan trọng (FB algorithm 2026):

1. **Save rate** = saves / reach × 100% → signal mạnh nhất
2. **Share rate** = shares / reach × 100% → signal mạnh thứ 2
3. **Comment quality** → comment dài, multi-thread > comment emoji
4. **Watch time completion** (Reels) → % xem hết video
5. **Engagement rate** = (likes + comments + shares + saves) / reach × 100%
6. **Reach** → chỉ có ý nghĩa khi kèm engagement rate cao

## Benchmarks ngành (tham khảo)

| Metric | Dưới trung bình | Trung bình | Tốt | Rất tốt |
|--------|----------------|-----------|-----|---------|
| Engagement rate | < 1% | 1–3% | 3–6% | > 6% |
| Save rate | < 0.3% | 0.3–1% | 1–3% | > 3% |
| Share rate | < 0.2% | 0.2–0.8% | 0.8–2% | > 2% |
| Reels completion | < 20% | 20–40% | 40–70% | > 70% |

## Phân tích

### Level 1: Tổng quan kỳ
- Metrics tổng so với kỳ trước
- Trend tăng/giảm + nguyên nhân suy đoán

### Level 2: Top performers
- 3 bài save rate cao nhất → điểm chung là gì?
- 3 bài share rate cao nhất → điểm chung là gì?
- Pattern: format, topic, hook type, độ dài

### Level 3: Underperformers
- Bài nào dưới benchmark → vì sao?
- Format nào đang underperform → cần điều chỉnh?

### Level 4: Gợi ý điều chỉnh
Cụ thể, actionable — không chung chung:
- ❌ "Nên cải thiện engagement"
- ✅ "Carousel 5–7 slides có save rate 2.3% cao hơn single image 0.4% — tăng tần suất carousel lên 3/tuần"

## Output

```yaml
performance_review:
  period: [khoảng thời gian]
  overall_metrics:
    total_reach: [số]
    avg_engagement_rate: [%]
    avg_save_rate: [%]
    avg_share_rate: [%]
    top_format_by_save: [format]
    top_format_by_share: [format]
  vs_previous_period:
    reach_change: [+/-% ]
    engagement_change: [+/-%]
    save_change: [+/-%]
  top_performers:
    - post_topic: [chủ đề]
      format: [format]
      save_rate: [%]
      share_rate: [%]
      why_it_worked: [phân tích ngắn]
  underperformers:
    - post_topic: [chủ đề]
      format: [format]
      issue: [vấn đề chính]
      recommendation: [gợi ý cụ thể]
  insights:
    - [Insight 1 — cụ thể, có số]
    - [Insight 2]
    - [Insight 3]
  action_items:
    - priority: high/medium/low
      action: [hành động cụ thể]
      expected_impact: [kỳ vọng]
  memory_write:
    should_update: true
    records_to_add: [list record để write vào performance-memory]
```
