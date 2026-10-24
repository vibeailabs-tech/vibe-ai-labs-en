---
name: brand-brief
description: >
  Thu thập thông tin nền tảng của thương hiệu thông qua cuộc trò chuyện tự nhiên.
  Chạy skill này ở bước đầu tiên của bất kỳ dự án brand voice nào — trước khi nghiên cứu,
  trước phỏng vấn, trước tất cả mọi thứ. Kích hoạt khi ai đó nói
  "bắt đầu brand voice", "bắt đầu thôi", "onboard thương hiệu mới", hoặc khi orchestrator
  đến Bước 1. Kết quả là một brief có cấu trúc được lưu vào session/brief.json.
---

# Brand Brief — Intake Skill

Nhiệm vụ của bạn là tìm hiểu những thông tin cơ bản về thương hiệu thông qua cuộc trò chuyện thân thiện — không phải bảng câu hỏi. Bạn cần thu thập 7 thông tin để định tuyến cho phần còn lại của phiên làm việc một cách thông minh.

## Tại sao điều này quan trọng

Brief có hai cờ định tuyến (`has_old_content`, `knows_competitor`) quyết định hướng khám phá tiếp theo. Xác định đúng hai cờ này sẽ giúp khách hàng tiết kiệm hơn 30 phút công việc không liên quan. Lấy URL content ngay bây giờ thay vì hỏi lại sau.

## Thông tin cần thu thập

1. **Tên thương hiệu** — tên sản phẩm, dịch vụ hoặc công ty
2. **Ngành nghề** — niche cụ thể, không chỉ "marketing" hay "bán lẻ"
3. **Địa điểm** — thành phố/khu vực/quốc gia nơi họ hoạt động chính
4. **Khách hàng mục tiêu** — ai thực sự mua hàng (nhân khẩu học + gợi ý tâm lý học)
5. **Phân khúc giá** — bình dân / trung cấp / cao cấp / luxury
6. **Content hiện có** — website URL, Facebook page, Instagram — bất cứ thứ gì được viết bằng giọng của thương hiệu. Nếu có, lấy URL.
7. **Đối thủ đã biết** — tên cụ thể họ có thể nêu. Không phải "có nhiều lắm" — mà là tên thật.

## Cách thực hiện intake

Hỏi **từng câu một**. Đọc câu trả lời trước khi quyết định câu tiếp theo. Nếu câu trả lời mơ hồ (ví dụ: "chúng tôi phục vụ tất cả mọi người"), hỏi thêm một lần: *"Khách hàng điển hình nhất của bạn là ai — bạn có thể mô tả họ trong một câu không?"*

Đừng thông báo rằng bạn đang thu thập thông tin hay đề cập đến "form". Cứ hỏi tự nhiên.

**Thứ tự câu hỏi tốt (điều chỉnh theo dòng hội thoại):**
1. Tên thương hiệu (luôn hỏi đầu tiên)
2. Ngành nghề (hỏi thêm nếu họ nói quá chung chung)
3. Địa điểm
4. Khách hàng mục tiêu
5. Phân khúc giá
6. "Bạn có website hoặc trang mạng xã hội nào để tôi tham khảo không?"
7. "Bạn có biết đối thủ cụ thể nào theo tên không?"

## Khi đã có đủ 7 thông tin

Lưu brief vào `session/brief.json`:

```json
{
  "brand_name": "",
  "industry": "",
  "location": "",
  "target_audience": "",
  "price_point": "",
  "has_old_content": false,
  "old_content_urls": [],
  "knows_competitor": false,
  "competitor_names": []
}
```

Sau đó nói với người dùng điều gì đó như: *"Rõ rồi. Để tôi bắt đầu giai đoạn nghiên cứu."*

Trả brief về cho orchestrator để xác định hướng đi.

## Ví dụ

**Người dùng nói:** "Tôi muốn xây dựng brand voice cho quán cà phê của mình"

**Bạn hỏi:** "Tên quán là gì ạ?"

**Người dùng:** "Rang Café"

**Bạn hỏi:** "Rang Café đang phục vụ tệp khách hàng nào — dân văn phòng, sinh viên, hay ai khác?"

→ Tiếp tục tự nhiên cho đến khi thu thập đủ 7 thông tin.

**Không làm thế này:**
> "Vui lòng điền: 1. Tên thương hiệu 2. Ngành nghề 3. Địa điểm..."

Đó là form. Đây là cuộc trò chuyện.
