---
name: competitor-analyzer-without
description: >
  Lập bản đồ brand voice của cả ngành khi khách hàng không biết tên đối thủ cụ thể.
  Dùng khi brief.knows_competitor = false.
  Sử dụng kiến thức của Claude để xác định các mẫu tone chiếm ưu thế, các cụm từ cần tránh,
  và cơ hội whitespace khách hàng có thể chiếm lĩnh. Kích hoạt khi orchestrator
  đến Bước 3 và knows_competitor là false.
---

# Competitor Analyzer — Bức Tranh Thị Trường (Không Có Tên Đối Thủ)

Khách hàng không biết tên đối thủ cụ thể, nhưng bạn biết ngành, địa điểm và phân khúc giá của họ từ `session/brief.json`. Vậy là đủ để lập bản đồ lãnh thổ.

## Tại sao điều này vẫn có giá trị

Hầu hết chủ SMB không biết đối thủ cụ thể là ai — họ chỉ biết "có những người khác ngoài kia". Bạn có thể cho họ thấy bức tranh toàn cảnh thị trường hơn những gì họ tự biết. Quan trọng hơn, bạn có thể chỉ ra các mẫu brand voice họ vô thức hấp thu từ thị trường, và cho họ thấy điều gì chưa được chiếm lĩnh.

## Cần tạo ra gì

Dựa trên `industry`, `location`, và `price_point` từ brief, phân tích:

**1. Các mẫu tone chiếm ưu thế**
Thương hiệu điển hình trong ngành này nghe như thế nào? Hãy cụ thể về *giọng điệu*, không phải danh mục sản phẩm. Ví dụ:
- Thương hiệu F&B Việt Nam phân khúc trung cấp → nhiều "chill", "không gian ấm cúng", "trải nghiệm", copy thiên về lifestyle
- B2B SaaS Việt Nam → trang trọng, nặng thuật ngữ, tập trung danh sách tính năng, không có cá tính
- Skincare cao cấp → đầy hy vọng nhưng mơ hồ, nhiều "hành trình", "glow", "ritual"

Đặt tên cho mẫu đó để khách hàng nhận ra (và tránh) nó.

**2. Các cụm từ cần tránh**
Xác định 8-12 từ hoặc cụm từ bị dùng nhiều đến mức mất hết ý nghĩa trong thị trường này. Chúng phải cảm thấy quen thuộc ngay lập tức với bất kỳ ai đã dành thời gian trong ngành.

**3. Các nhóm định vị**
Có những "phe" nào khác nhau? Hầu hết thị trường có 2-3 nhóm:
- Ví dụ: Cà phê Việt Nam → "specialty nghiêm túc" vs "lifestyle chill" vs "bình dân địa phương"

**4. Cơ hội whitespace**
Output quan trọng nhất: vị trí brand voice nào hiện chưa được chiếm lĩnh hoặc còn hiếm? Cách nói nào sẽ cảm thấy thực sự khác biệt trong thị trường này?

Hãy cụ thể. "Hãy authentic hơn" không phải whitespace. "Là thương hiệu duy nhất trong không gian này dám nói 'cái này không phải dành cho tất cả mọi người'" — đó mới là whitespace.

**5. Kỳ vọng vs. mong muốn của khách hàng**
Người mua trong phân khúc này kỳ vọng gì từ giao tiếp thương hiệu? Họ sẽ thực sự thích điều gì nếu thấy nó?

## Output

Lưu vào `session/competitor-analysis.json`:

```json
{
  "type": "market_landscape",
  "industry": "",
  "location": "",
  "price_point": "",
  "dominant_tone_patterns": ["mẫu 1", "mẫu 2"],
  "phrases_to_avoid": ["chill", "không gian ấm cúng", "trải nghiệm"],
  "positioning_clusters": [
    {"name": "tên nhóm", "description": "họ nghe như thế nào"}
  ],
  "whitespace_opportunity": "mô tả cụ thể về vị trí voice chưa được chiếm lĩnh",
  "audience_expectation": "họ kỳ vọng gì",
  "audience_desire": "họ thực sự muốn thấy gì thay thế"
}
```

## Giọng điệu của bản phân tích này

Viết như một tài liệu briefing sắc bén, không phải sách giáo khoa. Khách hàng đọc xong phải ngay lập tức nói "đúng rồi, tôi đã thấy chính xác cái đó" về các mẫu, và "tôi muốn là CÁI ĐÓ" về whitespace.
