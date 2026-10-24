# [18] Skill: fb-content-audit

## Mục đích
Rà soát feed hiện tại — pillar balance, tone consistency, content gap, Save:Like và Share:Like ratio.

## Input
- `posts_data`: danh sách bài gần nhất (paste text, CSV, hoặc mô tả từng bài)
  - Mỗi bài cần: topic, format, pillar (nếu biết), metrics cơ bản
- `audit_period`: số ngày muốn audit (mặc định 30 ngày)
- `brand_voice`: context từ brand-voice-loader

## Audit checklist

### 1. Pillar balance
- Tính tỷ lệ % mỗi pillar trong tổng số bài
- So sánh với tỷ lệ mục tiêu trong `brand_voice.pillars`
- Flag pillar nào đang over/under-represented

### 2. Format diversity
- Tỷ lệ từng format (carousel / single image / reels / story)
- Flag nếu 1 format chiếm > 60% — thiếu đa dạng
- Format nào có metrics tốt nhất?

### 3. Tone consistency
- Đọc 5–10 bài ngẫu nhiên — có nhất quán với brand_voice.tone không?
- Flag bài nào lạc tone
- Xưng hô có nhất quán không?

### 4. Content gap
- Pillar nào chưa có bài?
- Topic nào audience hay hỏi mà chưa có bài?
- Format nào chưa thử hoặc ít thử?

### 5. Save:Like ratio và Share:Like ratio
Đây là chỉ số quality signal quan trọng nhất:
- **Save:Like ratio** = saves / likes — tốt nếu ≥ 0.1 (10 saves mỗi 100 likes)
- **Share:Like ratio** = shares / likes — tốt nếu ≥ 0.05

Tính average ratio và identify outlier (bài nào có ratio đặc biệt cao/thấp).

### 6. Posting consistency
- Tần suất đăng có đều không?
- Có gaps dài không (> 5 ngày không đăng)?
- Giờ đăng có consistent không?

## Output

```yaml
content_audit:
  period: [số ngày]
  total_posts_reviewed: [số]
  pillar_balance:
    current_distribution:
      - pillar: [tên]
        count: [số bài]
        percentage: [%]
        target_percentage: [% mục tiêu]
        status: on_track | over | under
    gaps: [list pillar thiếu bài]
  format_diversity:
    distribution:
      carousel: [%]
      single_image: [%]
      reels: [%]
      story: [%]
    dominant_format: [format chiếm nhiều nhất]
    recommendation: [nên thêm format nào]
  tone_consistency:
    consistent: [true/false]
    inconsistent_posts: [list bài lạc tone nếu có]
    issues_found: [list vấn đề]
  save_share_ratios:
    avg_save_like_ratio: [số]
    avg_share_like_ratio: [số]
    best_ratio_posts: [top 3 bài có ratio cao nhất]
    benchmark_comparison: above / at / below
  content_gaps:
    - gap: [mô tả gap]
      suggested_content: [gợi ý bài cụ thể]
  posting_consistency:
    avg_posts_per_week: [số]
    longest_gap_days: [số ngày gap dài nhất]
    recommendation: [nếu cần điều chỉnh]
  priority_actions:
    - [Action 1 — cụ thể nhất, tác động lớn nhất]
    - [Action 2]
    - [Action 3]
```
