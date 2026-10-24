# [20] Skill: performance-memory

## Mục đích
Memory layer — kết nối Analytics ngược về Content Creation.
Agent học từ chính output của mình thay vì bắt đầu từ zero mỗi lần.

## Storage
File: `memory/post-history.json`

### Schema một record
```json
{
  "post_id": "uuid",
  "created_at": "ISO8601",
  "topic": "string",
  "pillar": "string",
  "format": "carousel|single_image|reels|story",
  "hook_type": "question|statistic|bold_claim|story|how_to",
  "word_count": 0,
  "metrics": {
    "reach": 0,
    "likes": 0,
    "comments": 0,
    "shares": 0,
    "saves": 0,
    "watch_time_pct": null,
    "save_rate": 0.0,
    "share_rate": 0.0
  },
  "confidence_score": 0.0,
  "hitl_decision": "auto|approved|edited|rejected",
  "reviewer_notes": "string"
}
```

## Chế độ WRITE (sau khi bài được publish và có metrics)

Input: output từ `fb-performance-review`

Ghi thêm 1 record vào `post-history.json`.
Nếu file chưa có bài nào → tạo array rỗng rồi append.

## Chế độ READ (khi bắt đầu task mới)

Input: `topic` mới cần viết, `format` dự kiến

Đọc `post-history.json` và trả về:

```yaml
performance_hint:
  top_performers:
    - post_id: ...
      topic: ...
      format: ...
      hook_type: ...
      save_rate: ...
      share_rate: ...
      notes: "vì sao bài này win"
  winning_patterns:
    formats: [format nào đang có save_rate cao nhất]
    hook_types: [hook type nào đang win]
    optimal_length: [word count range của top performers]
  anti_patterns:
    - format: ...
      reason: "save_rate < 0.5% trong 3 bài liên tiếp"
  data_points: [số bài trong memory]
  confidence: [low nếu < 5 bài, medium nếu 5–20, high nếu > 20]
```

## Ghi chú
- Nếu `post-history.json` trống hoặc < 3 bài: trả về `confidence: low`, không có gợi ý pattern
- Chỉ lấy 20 bài gần nhất để tránh bias từ dữ liệu cũ quá
- Save rate = saves / reach × 100%. Share rate = shares / reach × 100%
