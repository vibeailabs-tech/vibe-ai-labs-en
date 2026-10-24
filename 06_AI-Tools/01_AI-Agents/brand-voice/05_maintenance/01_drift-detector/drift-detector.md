---
name: drift-detector
description: >
  Chấm điểm bất kỳ nội dung nào theo rubric giọng thương hiệu và gắn cờ vi phạm.
  Đây là skill bảo trì định kỳ — lý do khách hàng trả retainer hàng tháng.
  Dùng khi ai đó chia sẻ content kèm cụm từ "kiểm tra cái này", "cái này nghe có đúng không?",
  "review bài này giúp tôi", "on-brand không?", hoặc "drift check".
  Yêu cầu 05_drift-checker-rubric.json phải tồn tại (được tạo bởi skill-file-generator).
  Cũng kích hoạt theo lịch nếu được cấu hình.
---

# Drift Detector

Ai đó có content cần kiểm tra. Nhiệm vụ của bạn là chấm điểm theo rubric brand voice và đưa ra phản hồi cụ thể, có thể hành động — không phải cảm nhận mơ hồ.

## Lấy rubric

Tìm `05_drift-checker-rubric.json` ở:
1. Đường dẫn người dùng chỉ định
2. Thư mục `brand-voice-output/` — tìm thư mục brand mới nhất
3. Hỏi người dùng cung cấp đường dẫn nếu không tìm thấy

Nếu không có rubric: nói với người dùng cần hoàn thành onboarding brand voice trước.

## Lấy content

Content có thể là:
- Dán trực tiếp vào cuộc trò chuyện
- Trong một file người dùng chỉ đến (đọc bằng Read tool)
- Nhiều bài cần kiểm tra cùng lúc (chấm điểm từng bài riêng)

## Quy trình chấm điểm

Làm việc qua rubric một cách có hệ thống:

**1. Quét từ cấm**
Kiểm tra từng từ/cụm từ trong `rubric.forbidden`. Gắn cờ kết quả khớp chính xác và biến thể gần (ví dụ: nếu "trải nghiệm" bị cấm, cũng gắn cờ "trải nghiệm tuyệt vời").

Mỗi từ cấm tìm thấy: áp dụng `scoring.forbidden_word_penalty` vào điểm.

**2. Kiểm tra sự hiện diện của từ khóa tone**
Kiểm tra các từ signature từ `rubric.tone_keywords`.
Mỗi từ có mặt: áp dụng `scoring.signature_word_bonus`.

**3. Kiểm tra dấu hiệu cá tính**
Với mỗi dấu hiệu `must_have`, đánh giá xem content có phản ánh nó không.
Điều này đòi hỏi phán đoán — một dấu hiệu như "thẳng thắn" có nghĩa là tìm kiếm sự trực tiếp trong cấu trúc câu, không chỉ là từ đó.
Mỗi dấu hiệu có mặt: áp dụng `scoring.personality_marker_bonus`.

**4. Kiểm tra độ dài câu**
Đếm từ trên mỗi câu. Gắn cờ câu dài hơn `rubric.sentence_length_max`.

**5. Quy tắc nền tảng (nếu biết nền tảng)**
Áp dụng quy tắc theo nền tảng cụ thể từ `rubric.platform_rules` nếu người dùng đề cập content này dành cho nền tảng nào.

## Tính điểm cuối cùng

```
điểm = điểm_cơ_sở
       + (số_từ_cấm × hình_phạt_từ_cấm)    [âm]
       + (số_từ_khóa_tone × thưởng_từ_signature)
       + (số_dấu_hiệu_cá_tính × thưởng_dấu_hiệu)

Kẹp trong [0.0, 1.0]
đạt = điểm >= ngưỡng_điểm_tone
```

## Định dạng output

Trình bày kết quả ở định dạng rõ ràng, dễ đọc — không dump JSON ra cho người dùng:

```
DRIFT CHECK — [Tên Thương Hiệu]
═══════════════════════════════

Điểm: 0.62 / 1.00  ❌ Dưới ngưỡng (0.75)

VI PHẠM:
  🚫 Từ cấm: "trải nghiệm" (dòng 2)
     → Thử: mô tả thứ thực sự, không phải "trải nghiệm" về nó
  🚫 Từ cấm: "đam mê" (dòng 4)
     → Thương hiệu này không diễn đam mê — cắt bỏ
  ⚠️  Câu quá dài: "Chúng tôi cam kết..." (38 từ)
     → Tách thành 2 câu

ĐIỂM TỐT:
  ✓ Dùng "thật" đúng cách
  ✓ CTA trực tiếp, không do dự
  ✓ Không lạm dụng dấu chấm than

NHẬN XÉT CHUNG:
Bài viết có cấu trúc đúng nhưng đang để lọt ngôn ngữ thị trường chung
ở dòng 2 và 4. Chỉnh sửa 2 phút để xóa "trải nghiệm" và "đam mê"
sẽ đưa điểm lên trên ngưỡng.

GỢI Ý SỬA DÒNG 2:
[Viết lại câu cụ thể bị gắn cờ theo đúng brand voice]
```

## Gợi ý sửa bài

Với mỗi vi phạm bị gắn cờ, đề xuất một bản viết lại cụ thể của câu đó. Đừng chỉ nói cái gì sai — chỉ ra cái đúng trông như thế nào.

Đây là giá trị: khách hàng không chỉ biết content đang lạc giọng, họ còn nhận được phiên bản đã chỉnh sửa có thể dùng ngay.

## Lưu kết quả (tùy chọn)

Nếu người dùng muốn theo dõi drift theo thời gian, lưu kết quả vào:
`brand-voice-output/[tên-brand]/drift-logs/[ngày]-[tên-file].json`

Điều này cho khách hàng một hồ sơ theo dõi chứng minh chất lượng content trong suốt thời gian retainer.
