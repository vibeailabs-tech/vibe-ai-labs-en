# [27] Skill: fb-review-queue

## Mục đích
Confidence-based routing — quyết định auto-publish, human review, hay auto-reject.
Industry standard 2026: Sprout Social, Hootsuite, Jasper đều có workflow này.

## Input
- `post_package`: toàn bộ output đã qua quality + intelligence layer
- `confidence_scores`: dict confidence từ mỗi skill trước (từ orchestrator)
- `policy_result`: kết quả từ fb-policy-checker
- `save_share_score`: từ fb-save-share-optimizer

## Tính aggregate confidence

```
aggregate_confidence = weighted average của:
  - fb-post-writer confidence:     30%
  - fb-policy-checker result:      25%  (pass=1.0, flag_fixed=0.8, block=0.0)
  - save_share_score:              20%  (max(save,share) / 10)
  - brand_voice_match:             15%  (tự đánh giá tone match)
  - format_fit:                    10%  (format phù hợp goal không)
```

## Routing logic

| Aggregate Confidence | Action |
|---------------------|--------|
| ≥ 0.90 | ✅ **Auto** — chuyển thẳng sang output-validator |
| 0.70 – 0.89 | 👤 **Human review** — pause pipeline, notify reviewer |
| < 0.70 | ❌ **Auto-reject** — bounce về content skill rewrite |

## Human review path (confidence 0.70–0.89)

### Thông tin gửi cho reviewer
- Bài hoàn chỉnh (formatted)
- Lý do cần review: "Confidence 0.82 — [skill nào kéo điểm xuống và tại sao]"
- Proposed edits nếu có (từ policy auto-fix, save/share suggestions)
- Deadline review: 4h cho organic post, 1h cho paid ad

### Reviewer có thể làm
- ✅ **Approve** → pipeline tiếp tục sang output-validator
- ✏️ **Edit** → gửi lại bài đã chỉnh → pipeline tiếp tục
- ❌ **Reject** → bounce về content skill với reviewer notes

### SLA tracking
- Gửi thông báo lần 1 khi vào queue
- Nếu không có response sau SLA/2: gửi reminder
- Nếu không có response sau SLA: notify orchestrator → escalate lên user

### Feedback loop
Decision của reviewer (approve/edit/reject + notes) được ghi vào `performance-memory` để cải thiện confidence model theo thời gian.

## Auto-reject path (confidence < 0.70)

Ghi rõ:
- Skill nào có confidence thấp nhất
- Lý do cụ thể
- Gợi ý rewrite direction

Bounce về skill tương ứng với context đầy đủ. Max 2 lần retry trước khi báo user quyết định.

## Output

```yaml
review_queue_result:
  aggregate_confidence: [0.0–1.0]
  confidence_breakdown:
    post_writer: [score]
    policy_checker: [score]
    save_share: [score]
    brand_voice_match: [score]
    format_fit: [score]
  routing_decision: auto | human_review | auto_reject
  auto_path:
    proceed_to_validator: [true/false]
  human_review_path:
    review_reason: [lý do cần review]
    reviewer_deadline: "Xh kể từ [timestamp]"
    status: pending | approved | edited | rejected
    reviewer_notes: [nếu có]
  reject_path:
    weakest_skill: [tên skill]
    rejection_reason: [lý do]
    rewrite_direction: [gợi ý hướng viết lại]
    retry_count: [0/1/2]
```
