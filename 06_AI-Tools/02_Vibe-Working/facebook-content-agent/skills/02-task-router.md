# [02] Skill: task-router

## Mục đích
Phân loại intent của user → chọn đúng skill và branch pipeline.

## Input
- `user_request`: yêu cầu gốc của user
- `brand_voice`: context từ brand-voice-loader

## Quy trình phân loại

### Bước 1: Detect intent
Phân loại vào một trong các category:

| Intent | Skill chính | Branch |
|--------|-------------|--------|
| Viết bài feed thường | fb-post-writer | publishing |
| Viết carousel | fb-carousel-architect | publishing |
| Viết script Reels/video | fb-reels-script | publishing |
| Repurpose nội dung từ nguồn khác | fb-repurpose | publishing |
| Lên kế hoạch content | fb-content-calendar | strategy |
| Xây content pillars | fb-pillar-planner | strategy |
| Tìm trending topics | fb-trend-researcher | strategy |
| Chiến lược hashtag | fb-hashtag-strategy | strategy |
| Reply comment | fb-comment-reply | engagement-lite |
| Kể chuyện thương hiệu | fb-story-arc | publishing |
| Viết quảng cáo | fb-ad-copy | publishing |
| Phân tích hiệu quả | fb-performance-review | analytics |
| Audit feed | fb-content-audit | analytics |
| Quét đối thủ | fb-competitor-scan | analytics |
| Phân tích / brief lại nội dung có sẵn | fb-content-brief | content-brief |
| Viết lại bài cũ / học theo bài mẫu | fb-content-brief → [content skill] | publishing |
| Tìm pattern từ nhiều bài | fb-content-brief (mode=series) | content-brief |

### Bước 2: Xử lý intent mơ hồ
Nếu không chắc chắn ≥ 80% intent là gì → KHÔNG đoán, hỏi user:

```
Tôi hiểu bạn muốn [paraphrase yêu cầu]. Bạn muốn:
A) [Option phù hợp nhất]
B) [Option phù hợp thứ 2]
C) [Option khác]
```

### Bước 3: Extract thông tin bổ sung
Từ yêu cầu, extract nếu có:
- Chủ đề / sản phẩm cần viết
- Mục tiêu (awareness / engagement / conversion)
- Funnel stage (TOFU / MOFU / BOFU)
- Format cụ thể nếu user đề cập
- Số slide / thời lượng nếu có

## Output

```yaml
routing:
  intent: [tên intent đã detect]
  skill: [skill chính sẽ chạy]
  branch: [publishing / strategy / analytics / engagement-lite]
  confidence: [0.0 – 1.0]
  extracted_params:
    topic: [chủ đề nếu có]
    goal: [mục tiêu nếu có]
    funnel_stage: [TOFU/MOFU/BOFU nếu rõ]
    format_hint: [format nếu user đề cập]
  clarification_needed: [true/false]
  clarification_question: [câu hỏi nếu cần]
```

## Ghi chú
- Branch `publishing` → chạy full pipeline (format-selector → content → distribution → quality → intelligence → review → validator)
- Branch `strategy` / `analytics` → chạy lightweight pipeline (loader → router → skill → validator)
- Branch `engagement-lite` (reply comment) → loader → router → comment-reply → localizer + policy → validator
- Branch `content-brief` (chỉ phân tích) → loader → router → fb-content-brief → output-validator
- Trigger `fb-content-brief` trong publishing pipeline khi user: paste nội dung vào, nói "viết lại bài này", "học theo bài này", "làm theo kiểu này", "brief lại bài này"
