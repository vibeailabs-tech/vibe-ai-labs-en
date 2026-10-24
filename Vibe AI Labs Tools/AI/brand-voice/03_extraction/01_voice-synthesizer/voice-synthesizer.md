---
name: voice-synthesizer
description: >
  Tổng hợp tất cả dữ liệu khám phá thành Brand Voice DNA hoàn chỉnh — tài sản cốt lõi
  mà mọi skill output đều sử dụng. Chạy sau khi phỏng vấn hoàn tất.
  Đây là bước đòi hỏi phân tích nhiều nhất: bạn đang hòa giải các tín hiệu có thể
  mâu thuẫn từ phỏng vấn, nghiên cứu đối thủ và quét content thành
  một brand identity nhất quán, cụ thể, có thể hành động.
  Kích hoạt khi orchestrator đến Bước 5, hoặc khi ai đó nói
  "tổng hợp brand voice", "tạo voice DNA", "ghép tất cả lại".
---

# Voice Synthesizer

Bạn đã thu thập tất cả: brand brief, bức tranh đối thủ, content scan (nếu có), bản ghi phỏng vấn với các trích dẫn quan trọng. Bây giờ tổng hợp tất cả thành Brand Voice DNA — nguồn sự thật duy nhất về cách thương hiệu này nghe như thế nào.

## Đọc tất cả dữ liệu session trước

Trước khi tổng hợp, đọc:
- `session/brief.json`
- `session/competitor-analysis.json`
- `session/content-scan.json` (nếu tồn tại)
- `session/interview.json`

## Bạn đang tổng hợp hướng đến gì

Voice DNA phải **cụ thể** và **khác biệt**. Nó thất bại nếu:
- Các tính cách có thể áp dụng cho bất kỳ thương hiệu nào ("chuyên nghiệp, thân thiện, đáng tin")
- Danh sách từ cấm không làm ai bất ngờ
- Mô tả tone không vẽ ra hình ảnh tâm trí rõ ràng

Nó thành công nếu:
- Đọc xong, bạn ngay lập tức biết một bài đăng của thương hiệu này nghe như thế nào
- Các từ cấm cảm thấy rõ ràng là sai *đặc biệt với thương hiệu này*
- Các ví dụ làm cho cái trừu tượng trở nên cụ thể

## Logic tổng hợp

**Bước 1 — Xác định các tín hiệu chân thực**
Từ các trích dẫn quan trọng của phỏng vấn, chiết xuất giọng thô: founder thực sự nói gì, không được gợi ý, tiết lộ họ là ai? Đây là dữ liệu sơ cấp của bạn.

**Bước 2 — Đối chiếu với content scan**
Tone vô thức trong content hiện có của họ có phù hợp hay mâu thuẫn với phỏng vấn không? Nếu họ nói họ "trang trọng và nghiêm túc" nhưng bài Facebook lại thân mật và hài hước, hãy đặt tên cho khoảng cách đó. Tổng hợp phải phản ánh họ thực sự là ai, không chỉ là ai họ nghĩ họ là.

**Bước 3 — Định vị so với thị trường**
Dùng phân tích đối thủ để làm sắc nét sự khác biệt. Nếu mọi người trong thị trường đều dùng "ấm áp và thân thiện", và thương hiệu này thực sự ấm áp và thân thiện, họ cần phải ấm áp và thân thiện *theo cách khác* — cụ thể hơn phiên bản của thị trường.

**Bước 4 — Chuyển thành quy tắc có thể hành động**
Các tính cách không hữu ích cho đến khi chúng được chuyển thành quy tắc viết:
- "Thẳng thắn" → câu ngắn, không vòng vo, không dùng ngôn ngữ xin lỗi
- "Tự tin" → không dấu hỏi trong câu khẳng định, không giải thích thừa
- "Không làm màu" → cấm: "trải nghiệm", "hành trình", "đam mê", "chill"

## Định dạng output

Lưu vào `session/voice-dna.json`:

```json
{
  "brand_name": "",
  "personality_traits": [
    "thẳng thắn — nói thẳng, không vòng vo, không xin lỗi thừa",
    "tự tin — không giải thích thừa, không cần validation từ khách",
    "không làm màu — không dùng ngôn ngữ lifestyle khi nói về sản phẩm thực tế"
  ],
  "tone": "Như người bạn nói thật — không phải nhân viên bán hàng, không phải lifestyle blogger",
  "tone_not_like": "Không phải: nhân viên phục vụ lịch sự, không phải: influencer chill",
  "sentence_rhythm": "Câu ngắn. Tự tin. Không giải thích thừa. Nếu có sự kiện thì nói thẳng sự kiện.",
  "forbidden_words": [
    "chill", "sống chậm", "trải nghiệm", "không gian ấm cúng",
    "hành trình", "đam mê", "tận tâm", "chuyên nghiệp"
  ],
  "signature_words": [
    "thật", "đúng vị", "không phải ngẫu nhiên", "thẳng thắn"
  ],
  "archetype": "Người Nói Thẳng — thương hiệu trung thực trong thị trường đầy sự ấm áp giả tạo",
  "differentiation": "Trung thực và thẳng thắn trong thị trường mà mọi thương hiệu đều đang diễn sự ấm áp. Không cần khách thích mình — chỉ cần khách đúng.",
  "example_good": "Batch Ethiopia vừa về. Rang light, chua thanh, hậu ngọt. Ghé thử trước khi hết.",
  "example_bad": "Không gian chill để bạn sống chậm lại với ly cà phê ấm áp~ ☕✨"
}
```

## Kiểm tra chất lượng trước khi lưu

Trước khi lưu, tự hỏi:
- Mô tả cá tính này có thể áp dụng cho một đối thủ trong cùng thị trường không? Nếu có, nó chưa đủ cụ thể.
- Một người viết đọc xong có biết KHÔNG viết gì không? Danh sách từ cấm quan trọng ngang với những gì được phép.
- example_good có thực sự phản ánh các tính cách, nhịp câu và từ signature không?

Nếu bất kỳ điều nào yếu, hãy sửa lại trước khi lưu.

## Sau khi lưu

Thông báo với orchestrator: "Voice DNA hoàn tất. Sẵn sàng tạo output."
Trả về tóm tắt Voice DNA cho người dùng ở định dạng ngắn gọn, dễ đọc — đừng chỉ nói "đã lưu vào file". Cho họ xem các tính cách chính và một ví dụ đúng vs. sai để họ có thể phản hồi trước khi bạn tạo 5 file output.
