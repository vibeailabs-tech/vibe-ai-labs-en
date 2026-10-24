# Task Router — Phân loại Intent

Phân loại intent của người dùng và định tuyến đến pipeline phù hợp.

## Đầu vào

Phân tích: $ARGUMENTS (yêu cầu thô của người dùng) + nội dung họ đã dán vào + ngữ cảnh cuộc hội thoại.

## Ma trận Phân loại

Ánh xạ đầu vào thành một loại task:

| Task Type | Vietnamese signals | English signals |
|-----------|-------------------|-----------------|
| PUBLISH_TEXT | "viết bài", "post về", "chia sẻ về", "đăng bài", "tạo bài" | "write post", "post about", "share about" |
| PUBLISH_CAROUSEL | "carousel", "slide", "PDF", "dạng slide" | "carousel", "slides", "PDF post" |
| PUBLISH_NEWSLETTER | "newsletter", "bản tin", "email newsletter LinkedIn" | "newsletter", "email blast" |
| PUBLISH_ARTICLE | "article", "bài dài", "viết dài", "long-form", "SEO" | "article", "long-form", "in-depth" |
| PUBLISH_VIDEO | "script video", "video LinkedIn", "kịch bản video" | "video script", "LinkedIn video" |
| PUBLISH_POLL | "poll", "khảo sát", "bình chọn", "hỏi audience" | "poll", "survey", "vote" |
| REPURPOSE | "chuyển từ", "repurpose", "từ blog", "từ podcast", "từ báo cáo" | "repurpose", "convert from", "turn into LinkedIn" |
| ANALYZE | "phân tích bài này", "x-ray", "học từ bài", "tìm pattern" | "analyze this post", "x-ray", "what makes this work" |
| REPLY | "reply comment", "trả lời", "phản hồi comment" | "reply to", "respond to comment" |
| PLAN_CALENDAR | "kế hoạch tháng", "lịch content", "calendar", "plan tuần" | "content calendar", "monthly plan", "schedule" |
| AUDIT | "kiểm tra feed", "audit", "rà soát content" | "audit feed", "review my content" |
| STRATEGY | "xây pillar", "chiến lược", "brand strategy", "content strategy" | "build pillars", "strategy", "brand positioning" |
| COMPETITOR | "phân tích đối thủ", "competitor", "đối thủ làm gì" | "competitor analysis", "what is X posting" |
| TREND | "trending", "xu hướng", "topic nóng", "chủ đề hot" | "trending topics", "what's hot", "industry trends" |
| HASHTAG | "hashtag", "tag", "hashtag cho bài" | "hashtags", "which tags" |

## Tính điểm Confidence

Tính confidence (0-100%) dựa trên:
- Khớp từ khoá rõ ràng → 90-100%
- Intent ngầm hiểu (ví dụ: người dùng dán nội dung mà không có chỉ dẫn) → 60-75%
- Yêu cầu mơ hồ (có thể là 2+ loại) → 50-65%

**Nếu confidence < 70%**: Hỏi để làm rõ:
```
Bạn muốn làm gì với nội dung này?

1. Viết bài text post mới
2. Tạo carousel / slide
3. Phân tích bài này để học pattern
4. Repurpose thành dạng LinkedIn khác
5. Lên kế hoạch content

Chọn 1-5 hoặc mô tả thêm:
```

## Trích xuất Topic

Từ yêu cầu của người dùng, trích xuất:
- **Topic**: Bài viết về điều gì? (1-3 từ)
- **Target pillar**: Bài viết này thuộc pillar nội dung nào? (đối chiếu với pillars trong brand voice)
- **Detected format preference**: Người dùng có đề cập format cụ thể không?
- **Urgency**: Đây có phải nội dung nhạy cảm về thời gian không? (tin tức mới, sự kiện, deadline)

## Đầu ra

```
📌 TASK CLASSIFICATION
━━━━━━━━━━━━━━━━━━━━━
Task type: [TYPE]
Topic: [extracted topic]
Pillar match: [pillar name or "no match — may need pillar check"]
Format: [detected or "TBD by format-selector"]
Urgency: [none / moderate / high]
Confidence: [%]
Pipeline: [pipeline name]
━━━━━━━━━━━━━━━━━━━━━
```

Truyền kết quả phân loại này sang skill tiếp theo trong pipeline.

## Các trường hợp ngoại lệ

- **Nhiều task trong một yêu cầu**: Xử lý task chính, sau đó liệt kê các task phụ như lựa chọn tiếp theo ở cuối
- **Tín hiệu xung đột**: "viết newsletter về topic X như một carousel" → làm rõ: newsletter HAY carousel, không phải cả hai
- **Không có topic rõ ràng**: Trích xuất những gì có thể, sau đó hỏi: "Topic cụ thể bạn muốn viết về là gì?"
