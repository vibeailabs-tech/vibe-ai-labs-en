# Li Policy Checker — Cổng kiểm duyệt tuân thủ

Kiểm tra nội dung theo LinkedIn Community Policy và luật quảng cáo Việt Nam trước khi đăng. Đây là hard gate — kết quả FAIL đồng nghĩa bài không thể đăng nguyên bản.

## Check 1: LinkedIn Community Policy

### 1a. Thông tin sai lệch hoặc gây hiểu nhầm
Flag nếu bài chứa:
- Số liệu thống kê không có nguồn trích dẫn ("70% startup thất bại vì X" — cần nguồn)
- Chức danh hoặc kinh nghiệm mâu thuẫn với nội dung trong 06-authority.md
- Cam kết về kết quả không thể kiểm chứng ("guaranteed results", "always works")
- Trước/sau khi dùng mà không có ngữ cảnh rõ ràng

Hành động: Flag câu cụ thể và yêu cầu cung cấp nguồn hoặc viết lại.

### 1b. Tín hiệu spam
Flag nếu bài chứa:
- Cụm từ lặp lại có chủ đích để thao túng algorithm
- Yêu cầu tương tác giả tạo: "comment bất cứ gì để nhận template", "like để lưu"
- Tag quá nhiều người (tag hơn 3 người không thực sự liên quan)
- Nội dung trùng hoặc gần giống bài đã đăng trước đó

### 1c. Hành vi lừa dối
Flag nếu:
- Nội dung quảng cáo được trình bày như ý kiến cá nhân không có disclosure
- Thông tin tuyển dụng hoặc hợp tác với điều khoản mơ hồ hoặc gây hiểu nhầm
- Link dẫn đến landing page không được mô tả trong bài

### 1d. Hành xử chuyên nghiệp
Flag nếu:
- Bài đề cập tên cá nhân cụ thể trong ngữ cảnh tiêu cực mà không có sự đồng ý
- Nội dung có thể bị hiểu là quấy rối hoặc tấn công có chủ đích
- Thông tin bảo mật của khách hàng bị tiết lộ (dù không nêu tên — ngành + vai trò + chi tiết vẫn có thể nhận dạng được)

---

## Check 2: Luật Quảng cáo Việt Nam (Luật Quảng cáo 2012, sửa đổi 2024)

### 2a. Ngôn ngữ so sánh tuyệt đối
Flag bất kỳ cụm nào sau đây nếu không có chứng nhận chính thức:
- "số 1", "hàng đầu", "tốt nhất", "duy nhất tại Việt Nam"
- "leading", "best", "#1" — bất kể ngôn ngữ nào
Hành động: Xóa bỏ hoặc thêm "theo kinh nghiệm của tôi" / "theo đánh giá của [nguồn được chứng nhận]"

### 2b. Quy định theo ngành
- **Y tế / thuốc**: Bất kỳ tuyên bố về sức khỏe nào đều cần disclaimer. "Tham khảo ý kiến bác sĩ" là bắt buộc với mọi lời khuyên sức khỏe.
- **Dịch vụ tài chính**: Tư vấn đầu tư cần disclaimer "Đây không phải là tư vấn đầu tư" nếu bài đề cập đến lợi nhuận tài chính.
- **Giáo dục**: Cam kết về kết quả học tập cần được làm rõ điều kiện đi kèm.

### 2c. Disclosure nội dung AI
Khuyến nghị (chưa bắt buộc nhưng nên làm): Nếu phần lớn bài được AI tạo ra mà không qua chỉnh sửa/cá nhân hóa, nên ghi "Hỗ trợ bởi AI, đã chỉnh sửa bởi [tên]."
Skill này không tự động thêm disclosure — chỉ flag như một advisory recommendation.

### 2d. Testimonial và case study
- Testimonial bịa đặt là hành vi bất hợp pháp. Mọi kết quả của khách hàng được đề cập phải là thật.
- Nếu khách hàng đã cho phép: dùng trực tiếp. Nếu chưa: ẩn danh + thêm "một khách hàng trong ngành X"
- Số liệu phải thật. Làm tròn là được ("khoảng 30%") nhưng số liệu bịa đặt thì không.

---

## Hệ thống phán quyết

| Kết quả | Ý nghĩa | Hành động |
|---------|---------|-----------|
| ✅ PASS | Không phát hiện vấn đề | Tiếp tục bước tiếp theo trong pipeline |
| ⚠️ NEEDS_REVISION | Có vấn đề nhưng có thể sửa | Hiển thị vấn đề + gợi ý sửa; người dùng tự quyết |
| ❌ FAIL | Vi phạm nghiêm trọng | Chặn output; yêu cầu viết lại trước khi tiếp tục |

Điều kiện FAIL (chặn tự động):
- Số liệu thống kê bịa đặt
- Tuyên bố so sánh tuyệt đối về sản phẩm/dịch vụ đang quảng bá mà không có chứng nhận
- Tấn công cá nhân được nêu tên
- Nguy cơ lộ thông tin bảo mật của khách hàng

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛡️ POLICY CHECKER — RESULT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Verdict: [✅ PASS / ⚠️ NEEDS_REVISION / ❌ FAIL]
Risk level: [LOW / MEDIUM / HIGH]

ISSUES FOUND: [N]
[Nếu không có: "Không phát hiện vi phạm policy nào."]

Issue 1: [mô tả]
  Location: "[trích dẫn đoạn text từ bài]"
  Rule: [quy tắc nào bị vi phạm]
  Fix: [gợi ý sửa cụ thể]

Issue 2: [nếu có]
  ...

ADVISORY NOTES:
  • [các khuyến nghị best practice, dù chưa phải vi phạm]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Nếu FAIL: dừng pipeline và yêu cầu người dùng viết lại trước khi tiếp tục.
Nếu NEEDS_REVISION: hiển thị vấn đề, đề nghị tự động áp dụng các sửa đổi, rồi kiểm tra lại.
Nếu PASS: tiếp tục bước tiếp theo trong pipeline.
