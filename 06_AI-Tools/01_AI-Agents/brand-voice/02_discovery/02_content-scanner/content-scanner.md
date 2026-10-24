---
name: content-scanner
description: >
  Phân tích content hiện có của thương hiệu (website, Facebook, bất kỳ bản copy nào) để phát hiện
  các mẫu voice vô thức — cách họ đang nghe mà không hay biết.
  Chạy khi brief.has_old_content = true và có old_content_urls.
  Khách hàng thường có brand voice tiềm ẩn chưa bao giờ được diễn đạt; skill này tìm ra nó.
  Kích hoạt khi orchestrator xác định has_old_content là true.
---

# Content Scanner — Phân Tích Brand Voice Hiện Tại

Khách hàng có content đã viết trước đây. Dù họ chưa bao giờ nghĩ về brand voice, văn bản của họ có các mẫu — lựa chọn từ vựng, nhịp câu, giọng cảm xúc — tiết lộ họ thực sự là ai so với họ nghĩ họ là ai.

Nhiệm vụ của bạn là bộc lộ các mẫu vô thức đó. Đây thường là bước tiết lộ nhất — khách hàng thường nói "wow, tôi không nhận ra mình đang làm vậy."

## Lấy content

Kiểm tra `session/brief.json` để tìm `old_content_urls`. Sau đó:

**Nếu có URL:**
Dùng WebFetch để tải từng URL. Tập trung vào các trang có nhiều chữ: About, văn bản hero Homepage, Blog posts, phần "Giới thiệu" của Facebook page. Bỏ qua menu điều hướng, link footer và văn bản pháp lý.

Tải tối đa 3 URL. Ưu tiên các trang mà thương hiệu nói bằng giọng của chính mình (không phải thông số kỹ thuật hay bảng giá).

**Nếu URL không có hoặc không tải được:**
Hỏi khách hàng: *"Bạn có thể dán một vài đoạn copy bạn đã viết cho thương hiệu không? Có thể là bài Facebook, phần About website, bất cứ thứ gì."*

Chờ họ dán xong, rồi tiếp tục.

## Cần phân tích gì

Đọc kỹ toàn bộ content thu thập được. Tìm kiếm:

**1. Các mẫu hiện tại**
Những mẫu cấu trúc hoặc phong cách nào lặp đi lặp lại? Ví dụ:
- Luôn bắt đầu bài đăng bằng câu hỏi
- Kết thúc mỗi bài bằng dấu chấm than
- Dùng bullet points nhiều
- Luôn gọi người đọc là "bạn" vs "quý khách"

**2. Tone vô thức**
Đây là phát hiện quan trọng nhất. Tone thực sự của họ là gì — *không phải* tone họ nghĩ họ đang có? Một thương hiệu nói họ "chuyên nghiệp" có thể thực sự rất ấm áp và thân mật trong văn bản. Hãy đặt tên trung thực.

**3. Từ ngữ thường dùng**
Liệt kê 10-15 từ hoặc cụm từ xuất hiện nhiều nhất. Không đếm giới từ và liên từ. Tìm kiếm lựa chọn từ vựng có ý nghĩa.

**4. Nhịp câu**
Câu ngắn gọn súc tích hay dài và giải thích? Họ có dùng câu hỏi tu từ không? Em-dash? Câu không đầy đủ để nhấn mạnh?

**5. Điểm mạnh và điểm yếu đáng chú ý**
Cái gì đang hiệu quả? Cái gì không nhất quán hoặc đang làm hại thương hiệu?

## Output

Lưu vào `session/content-scan.json`:

```json
{
  "sources_analyzed": ["url1", "url2"],
  "existing_patterns": [
    "Luôn mở đầu bằng câu hỏi",
    "Dùng nhiều dấu chấm than",
    "Gọi người đọc là 'bạn' (thân mật)"
  ],
  "unconscious_tone": "Ấm áp và thân mật hơn họ có thể nghĩ. Cảm giác như người bạn có kiến thức, không phải chuyên gia.",
  "frequently_used_words": ["thật", "chất lượng", "tận tâm", "đam mê"],
  "sentence_rhythm": "Câu ngắn gọn súc tích. Đôi khi dùng câu không đầy đủ để nhấn mạnh. Không có mệnh đề phức tạp.",
  "strengths": ["Sự ấm áp chân thực toát ra", "Giữ nhất quán giọng thân mật"],
  "weaknesses": ["Dùng 'chất lượng' quá nhiều đến mức mất ý nghĩa", "Không có sự khác biệt so với đối thủ"],
  "notes": "Content được scan từ homepage và 3 bài Facebook đăng năm 2024."
}
```

## Xử lý trường hợp đặc biệt

- **Content quá ít** (chỉ một bài Facebook): Làm hết sức nhưng ghi chú kích thước mẫu hạn chế
- **Nhiều ngôn ngữ pha trộn**: Ghi chú ngôn ngữ nào cảm thấy tự nhiên hơn cho thương hiệu
- **Tone không nhất quán** trong các bài khác nhau: Nêu rõ điều này — sự không nhất quán tự nó là một phát hiện
