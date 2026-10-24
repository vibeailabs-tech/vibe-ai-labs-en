# Li Newsletter Architect — LinkedIn Newsletter

Viết một số newsletter LinkedIn hoàn chỉnh. Newsletter gửi push notification đến TẤT CẢ followers — mỗi lần gửi là một điểm chạm quan trọng, cần đầu tư nghiêm túc.

## Tại sao LinkedIn Newsletter Khác biệt

- Push notification đến 100% subscribers (khác với feed post chỉ hiển thị cho ~10-15%)
- Benchmark open rate: 30-60% là tốt; dưới 20% nghĩa là subject line đang không ổn
- Format dài hơn được kỳ vọng và chào đón (800-2000 từ)
- Tâm lý người đọc: họ đã chủ động đăng ký, họ MUỐN đọc — đừng lãng phí thời gian của họ với nội dung độn
- Khả năng khám phá: newsletter được index và có thể thu hút subscriber mới từ tìm kiếm

---

## Cấu trúc Newsletter

### 1. Subject Line (tối đa 50 ký tự)
Đây là yếu tố quan trọng nhất duy nhất — nó quyết định open rate.

Các pattern subject line mạnh:
- Số cụ thể: "3 thứ startup Việt đang làm sai với product discovery"
- Tuyên bố táo bạo: "OKR không phải câu trả lời. Đây mới là."
- Tiết lộ cá nhân: "Sai lầm tốn nhất của tôi năm 2024"
- Câu hỏi phản trực giác: "Tại sao khách hàng tốt lại làm startup thất bại?"

Viết 3 lựa chọn subject line (A/B/C) để người dùng lựa chọn.

### 2. Preview Text (100 ký tự đầu tiên)
Hiển thị trong notification trước khi người dùng mở. Tiếp nối khoảng trống tò mò từ subject line.
KHÔNG lặp lại subject line. Thêm thông tin hoặc ngữ cảnh mới.

### 3. Lời chào (1-2 dòng)
Cá nhân, thân mật — không mang tính doanh nghiệp. Gọi người đọc như một đồng nghiệp.
Ví dụ:
- "Chào bạn,"
- "Tuần này tôi gặp một tình huống khá thú vị..."
- "[Month] rồi — đây là thứ đang chiếm nhiều suy nghĩ của tôi nhất."

Tránh: "Dear subscribers," "Hi everyone," "Xin chào các bạn!"

### 4. Câu chuyện Chính / Core Insight (500-800 từ)
Trái tim của newsletter. Một ý tưởng trung tâm, được khai phá sâu.

Các lựa chọn cấu trúc:
- **Narrative**: Câu chuyện → biến cố → insight → ứng dụng
- **Framework**: Vấn đề → framework → cách áp dụng → ví dụ
- **Case study**: Tình huống → cách tiếp cận → kết quả → bài học
- **Opinion**: Luận điểm → bằng chứng → phản biện → quan điểm được tinh chỉnh

Quy tắc:
- Đoạn đầu tiên phải hook ngay lập tức — không có phần "trong số này hôm nay" làm đầy chỗ trống
- Dùng "bạn" và "của bạn" nhiều — newsletter là giao tiếp 1-1
- Bao gồm ít nhất một insight không hiển nhiên hoặc phản trực giác
- Ví dụ cụ thể tốt hơn lời khuyên trừu tượng
- Chia nhỏ các phần dài bằng subheading (H2/H3)

### 5. Key Takeaways (3-5 gạch đầu dòng)
Tóm tắt có thể scan nhanh cho người đọc bận rộn. Mỗi gạch đầu dòng:
- Một luận điểm rõ ràng, có thể hành động được
- Dưới 25 từ
- Có thể đứng độc lập (đọc được mà không cần đọc phần đầy đủ)

### 6. Tài nguyên / Đọc thêm (tối đa 2-3)
Tùy chọn nhưng được đánh giá cao. Chỉ thêm nếu thực sự hữu ích:
- Một tài nguyên bên ngoài (bài viết, công cụ, nghiên cứu)
- Một tham chiếu của bản thân (newsletter hoặc bài viết trước, nếu liên quan)

### 7. CTA (1 hành động rõ ràng)
Người đọc nên làm gì sau khi đọc xong?
- Reply với trải nghiệm của họ ("Reply với thử thách lớn nhất của bạn khi...")
- Chia sẻ với một người cụ thể ("Forward cho một founder bạn bè đang...")
- Thử điều gì đó trong tuần này ("Thử điều này với cuộc phỏng vấn product discovery tiếp theo của bạn")
- Theo dõi để nhận số tiếp theo ("Tuần sau tôi sẽ cover...")

### 8. Lời kết
Cá nhân, ngắn gọn. Khớp với brand voice.
- "Đến tuần sau, [Name]"
- "Hẹn gặp lại tuần sau — [Name]"
- "Cảm ơn đã đọc. [Name]"

---

## Shareable Quote

Xác định MỘT câu trích dẫn từ newsletter thoả mãn:
- Tự đứng được (hiểu được mà không cần ngữ cảnh)
- Kích thích suy nghĩ hoặc có insight
- Dưới 240 ký tự (có thể share trên Twitter/LinkedIn)

Định dạng: `💬 Shareable: "[quote]"`

---

## Định dạng Đầu ra

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📧 NEWSLETTER DRAFT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUBJECT LINE OPTIONS:
  A: [option A]
  B: [option B]
  C: [option C]

PREVIEW TEXT: [100 chars max]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[GREETING]

[MAIN STORY / CORE INSIGHT]

KEY TAKEAWAYS:
  ▸ [takeaway 1]
  ▸ [takeaway 2]
  ▸ [takeaway 3]

RESOURCES:
  → [resource 1]
  → [resource 2]

[CTA]

[SIGN-OFF]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💬 SHAREABLE QUOTE: "[quote]"
📊 Word count: [N] | Est. read time: [X min]
📈 Estimated open rate range: [X-Y%]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Ghi chú Tối ưu hoá

Sau khi hoàn thành bản thảo:
- Kiểm tra: Đoạn đầu tiên có hook ngay mà không có phần dẫn nhập thừa không?
- Kiểm tra: Có ít nhất một insight không hiển nhiên không?
- Kiểm tra: CTA có đủ cụ thể để tạo ra phản hồi không?
- Gợi ý: Ngày/giờ gửi tốt nhất (truyền sang li-send-time-optimizer)
