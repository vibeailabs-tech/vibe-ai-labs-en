---
name: platform-adaptor
description: >
  Tạo ra 03_platform-variants.json — các quy tắc brand voice theo từng nền tảng cho
  Facebook, LinkedIn, Email và Chatbot. Voice DNA cốt lõi không thay đổi,
  nhưng độ mạnh tone, định dạng, dùng emoji và kiểu CTA thích nghi theo từng nền tảng.
  Kích hoạt khi orchestrator đến Bước 6, hoặc khi ai đó hỏi về
  "quy tắc nền tảng", "bộ hướng dẫn voice mạng xã hội", hoặc "cách thích nghi giọng theo từng kênh".
---

# Platform Adaptor

Đọc `session/voice-dna.json` và `session/brief.json`, sau đó tạo ra `03_platform-variants.json`.

Brand Voice DNA không thay đổi theo nền tảng — cá tính là bất biến. Điều thay đổi là **cách cá tính đó thể hiện** theo định dạng, kỳ vọng khán giả và chuẩn mực của từng nền tảng. Một thương hiệu "thẳng thắn và không vòng vo" vẫn thẳng thắn trên Facebook, nhưng Facebook cho phép câu ngắn hơn và chút ấm áp hơn. LinkedIn đòi hỏi nhiều nội dung thực chất hơn.

## Tạo 4 hồ sơ nền tảng

Với mỗi nền tảng, suy nghĩ về:
1. Cá tính của thương hiệu trông như thế nào *ở đây cụ thể*?
2. Nền tảng này đặt ra ràng buộc định dạng gì?
3. Khán giả trên nền tảng này kỳ vọng gì — và thương hiệu này đáp ứng/phá vỡ kỳ vọng đó như thế nào?
4. Viết một bài đăng/tin nhắn ví dụ thực tế theo giọng của thương hiệu cho nền tảng này

### Facebook
- Ngắn hơn là tốt hơn — 50-150 từ cho hầu hết bài đăng
- Kết nối cảm xúc trực tiếp hơn LinkedIn
- Emoji: quyết định dựa trên cá tính thương hiệu (B2B nghiêm túc → không; quán cà phê → có thể, ít thôi)
- CTA nên cảm thấy như lời mời, không phải mệnh lệnh

### LinkedIn
- 150-300 từ cho bài đăng thông thường; dài hơn cho thought leadership
- Thực chất hơn — chia sẻ quan điểm, không chỉ sản phẩm
- Hashtag: 2-4 cái liên quan ở cuối
- Mặt "chuyên môn" của thương hiệu thể hiện rõ hơn ở đây

### Email
- Lời chào và ký tên thiết lập tone ngay lập tức — đây là quyết định thương hiệu không thể thương lượng
- Phong cách tiêu đề: câu hỏi / phát biểu mạnh / khoảng trống tò mò — chọn cái phù hợp với giọng
- Nội dung phải cảm thấy như do người viết, không phải template

### Chatbot / Dịch Vụ Khách Hàng
- Định dạng hội thoại nhất — gần nhất với cách thương hiệu nói chuyện trực tiếp
- Độ dài trả lời: ngắn (1-3 câu mỗi tin nhắn) trừ khi giải thích điều gì đó phức tạp
- Cá tính thương hiệu phải tồn tại kể cả trong những lúc "Tôi xin lỗi khi nghe điều đó"

## Định dạng output

```json
{
  "brand_name": "",
  "generated_date": "",
  "facebook": {
    "tone_note": "cách giọng cốt lõi thích nghi cho Facebook",
    "max_length_words": 150,
    "emoji": false,
    "hashtag": false,
    "cta_style": "mô tả cách tiếp cận CTA",
    "opening_hook_style": "cách bài đăng thường mở đầu",
    "example": "Bài đăng ví dụ đầy đủ theo giọng thương hiệu"
  },
  "linkedin": {
    "tone_note": "cách giọng cốt lõi thích nghi cho LinkedIn",
    "max_length_words": 300,
    "emoji": false,
    "hashtag": true,
    "hashtag_count": 3,
    "cta_style": "",
    "opening_hook_style": "",
    "example": "Bài đăng ví dụ đầy đủ theo giọng thương hiệu"
  },
  "email": {
    "tone_note": "",
    "greeting": "Cụm từ chào cụ thể (ví dụ: 'Chào [tên],' không phải 'Kính gửi Quý Khách')",
    "sign_off": "Cụm từ ký tên cụ thể",
    "subject_line_style": "mô tả kèm ví dụ",
    "example": "Email ví dụ đầy đủ theo giọng thương hiệu (tiêu đề + nội dung)"
  },
  "chatbot": {
    "tone_note": "",
    "response_length": "short",
    "personality_notes": "cách duy trì brand voice trong ngữ cảnh hỗ trợ",
    "greeting": "Tin nhắn mở đầu khi người dùng bắt đầu chat",
    "error_response_style": "cách xử lý khi bot không làm được điều gì đó",
    "example": "Ví dụ trao đổi (tin nhắn người dùng + phản hồi thương hiệu)"
  }
}
```

## Kiểm tra chất lượng

Các ví dụ là phần quan trọng nhất. Ví dụ yếu là: "Xin chào! Chúng tôi có thể giúp gì cho bạn?" — đó là generic.

Ví dụ mạnh cho chatbot thương hiệu cà phê thẳng thắn, không vòng vo: "Chào. Bạn cần gì?" — 3 từ đã nói lên tất cả về thương hiệu.

Làm cho mỗi ví dụ thực sự nghe như thương hiệu, không phải như chỗ điền template.

Lưu vào `brand-voice-output/[tên-brand]/03_platform-variants.json`.
