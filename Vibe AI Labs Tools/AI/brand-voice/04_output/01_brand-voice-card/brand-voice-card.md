---
name: brand-voice-card
description: >
  Tạo ra 01_brand-voice-card.md — tài liệu tham khảo brand voice dành cho con người.
  Dùng để khách hàng xem xét và bàn giao cho agency. Nó chuyển Voice DNA thành
  một tài liệu rõ ràng, đầy ví dụ mà bất kỳ copywriter hay marketer nào cũng có thể làm theo.
  Kích hoạt khi orchestrator đến Bước 6, hoặc khi ai đó hỏi về
  "bộ brand voice guide", "tài liệu brand voice", hoặc "voice reference card".
---

# Brand Voice Card Generator

Đọc `session/voice-dna.json` và `session/brief.json`, sau đó tạo ra `01_brand-voice-card.md`.

Tài liệu này dành cho con người — khách hàng, copywriter của agency, social media manager vừa được onboard. Nó phải đọc được mà không cần bất kỳ ngữ cảnh nào, đủ cụ thể để ai đó có thể áp dụng ngay lập tức, và đủ cụ thể để loại trừ các bài viết tệ một cách rõ ràng.

## Cấu trúc tài liệu

Tạo file theo đúng cấu trúc này:

---

```markdown
# Brand Voice Card — [Tên Thương Hiệu]
*Tạo ngày: [ngày] | Xác nhận và ký duyệt trước khi phân phối*

---

## 3 Tính Cách Cốt Lõi

### 1. [Tên Tính Cách]
[2-3 câu giải thích điều này có nghĩa gì trong thực tế. Không trừu tượng — đặt nó vào hành vi cụ thể.
Ví dụ: "Thẳng thắn không có nghĩa là thô lỗ. Có nghĩa là nếu sản phẩm của chúng tôi không phải lựa chọn tốt nhất cho bạn, chúng tôi sẽ nói thẳng. Không có sales pitch."]

### 2. [Tên Tính Cách]
[Cùng định dạng]

### 3. [Tên Tính Cách]
[Cùng định dạng]

---

## Tone — Chúng Tôi Nghe Giống Ai

**Chúng tôi viết như:** [Mô tả người/nhân vật cụ thể — KHÔNG phải người nổi tiếng, mà là một archetype người đọc sẽ hình dung ngay]

**Chúng tôi KHÔNG viết như:** [Ngược lại — cũng cụ thể như vậy]

**Trong một câu:** [Tone của thương hiệu trong một cụm từ đáng nhớ]

---

## Những Từ Chúng Tôi Không Bao Giờ Dùng

| Từ / Cụm Từ | Tại sao tránh |
|-------------|---------------|
| "[từ]" | [Lý do cụ thể — không chỉ "bị dùng nhiều" mà TẠI SAO sai cho thương hiệu này] |
| "[từ]" | [Lý do] |
[8-12 hàng]

---

## Những Từ Nghe Giống Chúng Tôi

| Từ / Cụm Từ | Cách sử dụng |
|-------------|--------------|
| "[từ]" | [Ngữ cảnh hoặc ví dụ sử dụng đúng] |
[8-12 hàng]

---

## Phong Cách Câu

[3-5 gạch đầu dòng mô tả cụ thể phong cách viết:
- Ưu tiên độ dài câu
- Có dùng câu hỏi, câu không đầy đủ, em-dash không
- Luôn/không bao giờ kết thúc bằng gì
- Xử lý thông tin kỹ thuật như thế nào]

---

## Đúng vs. Sai — Cùng Thông Điệp, Hai Giọng Khác Nhau

**Tình huống:** [Một kịch bản thực tế thương hiệu này đối mặt — ra mắt sản phẩm, khoảnh khắc dịch vụ khách hàng, bài đăng quảng cáo]

❌ **Sai:**
> [example_bad từ voice DNA — hoặc ví dụ mới viết theo giọng sai]
*Tại sao sai: [một câu]*

✅ **Đúng:**
> [example_good từ voice DNA — hoặc ví dụ mới theo giọng đúng]
*Tại sao hiệu quả: [một câu]*

---

## Brand Archetype

**[Tên Archetype]**
[2-3 câu về điều này có nghĩa gì cho cách thương hiệu thể hiện trong văn bản. Tại sao archetype này được chọn thay vì các lựa chọn thay thế rõ ràng hơn.]

---

## Điều Làm Chúng Tôi Khác Biệt

[Sự khác biệt từ voice-dna.json, mở rộng thành 3-4 câu. Đây là "vậy thì sao" — tại sao vị trí voice cụ thể này quan trọng trong thị trường này.]

---

*Tài liệu này là tài liệu tham khảo sống. Cập nhật khi brand voice phát triển hoặc thêm nền tảng mới.*
```

---

## Kiểm tra chất lượng

Trước khi lưu, xác nhận:
- Mỗi tính cách có ví dụ hành vi cụ thể, không chỉ là định nghĩa
- Các ví dụ đúng/sai minh họa rõ sự khác biệt
- Bảng từ cấm có lý do thực sự, không chỉ "bị dùng nhiều"
- Một copywriter chưa từng gặp thương hiệu này có thể viết theo giọng đó sau khi đọc xong

Lưu markdown hoàn chỉnh vào `brand-voice-output/[tên-brand]/01_brand-voice-card.md`.
Cũng trả nội dung về orchestrator dưới dạng chuỗi để file-generator đóng gói.
