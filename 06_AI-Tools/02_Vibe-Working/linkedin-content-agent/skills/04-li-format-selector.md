# Li Format Selector — Chọn Format Nội dung

Chọn format LinkedIn tối ưu dựa trên task, chủ đề và lịch sử hiệu suất.

## Các Format Có sẵn

| Format | Phù hợp nhất cho | Hiệu suất trung bình 2026 |
|--------|----------|---------------------|
| text_post | Ý kiến, câu chuyện, insight, mẹo nhanh | Trung bình — reach phụ thuộc nhiều vào độ sâu engagement |
| carousel_pdf | Từng bước, framework, danh sách, hướng dẫn trực quan | Cao nhất — save rate + dwell time rất mạnh |
| article | SEO, phân tích sâu, case study, thought leadership | Reach tức thì thấp hơn, lưu lượng Google dài hạn |
| newsletter | Cập nhật định kỳ cho audience, series, thông báo | Push notification đến TẤT CẢ followers — open rate cao |
| poll | Nghiên cứu audience, tăng engagement, kiểm chứng chủ đề | Reach cao nhờ hiệu ứng mạng lưới người bình chọn |
| video_script | Hướng dẫn, demo, behind-the-scenes | Format đang tăng trưởng — algorithm đang ưu tiên native video |
| live | Q&A thời gian thực, sự kiện | Reach tức thì cao nhất, cần chuẩn bị kỹ |

## Logic Lựa chọn

### Bước 1: Kiểm tra xem người dùng có chỉ định format không
- Nếu người dùng nói "carousel" hoặc "slide" → carousel_pdf
- Nếu người dùng nói "video" hoặc "script" → video_script
- Nếu người dùng nói "newsletter" → newsletter
- Nếu người dùng nói "poll" hoặc "khảo sát" → poll
- Nếu người dùng nói "article" hoặc "bài dài" → article
- Nếu đã xác định format, bỏ qua và chuyển sang Bước 3

### Bước 2: Đề xuất format dựa trên chủ đề + lịch sử

Đọc `memory/post-history.json` để xem hiệu suất theo format:
- Format nào có dwell_score cao nhất trong lịch sử?
- Format nào đang bị lạm dụng quá (cùng format 3+ lần trong 7 ngày gần nhất)?

Áp dụng đối chiếu nội dung — format:

**Chọn carousel_pdf khi**:
- Nội dung có 5+ điểm hoặc bước riêng biệt
- Chủ đề là "cách thực hiện", framework, checklist, hoặc quy trình
- Mục tiêu là save và reach dài hạn
- Ví dụ: "5 bước onboard khách hàng SaaS"

**Chọn text_post khi**:
- Nội dung là câu chuyện cá nhân, quan sát, hoặc một insight duy nhất
- Chủ đề dựa trên ý kiến cá nhân hoặc ngược chiều
- Độ dài 150-300 từ
- Ví dụ: "Điều tôi học được sau 3 năm build B2B SaaS"

**Chọn newsletter khi**:
- Nội dung là series định kỳ hoặc cập nhật thường xuyên
- Chủ đề cần format dài hơn (800+ từ)
- Mục tiêu là giữ chân audience và xây dựng quan hệ

**Chọn poll khi**:
- Chủ đề thực sự có hai luồng ý kiến trái chiều hoặc chưa chắc chắn
- Mục tiêu là nghiên cứu audience + tăng engagement
- Đã có kế hoạch bài follow-up với kết quả

**Chọn article khi**:
- Chủ đề cần 1500+ từ để trình bày đầy đủ
- Có cơ hội từ khoá SEO
- Mục tiêu là thought leadership + lưu lượng Google

**Chọn video_script khi**:
- Chủ đề phù hợp để trình bày bằng hình ảnh hơn là văn bản (hướng dẫn, demo)
- Có khả năng quay video
- Mục tiêu là watch time và tiếp cận audience mới

### Bước 3: Xử lý xung đột format
Nếu carousel được đề xuất nhưng người dùng muốn text post:
- Tôn trọng lựa chọn của người dùng
- Ghi chú: "Carousel có thể perform tốt hơn cho topic này — bạn muốn thử không?"

## Đầu ra

```
━━━━━━━━━━━━━━━━━━━━━━━━━━
📐 FORMAT SELECTED
━━━━━━━━━━━━━━━━━━━━━━━━━━
Format: [selected format]
Reasoning: [1-2 sentences why]
Historical performance: [if data available: "Your [format] posts avg dwell score: X"]
Alternative: [second best format and why]
━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Truyền format đã chọn sang skill tạo nội dung phù hợp:
- text_post → li-post-writer
- carousel_pdf → li-carousel-architect
- newsletter → li-newsletter-architect
- article → li-article-writer
- video_script → li-video-script
- poll → li-poll-strategist
