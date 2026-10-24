---
name: geo-brand-summary
description: >
  Tạo ra 04_geo-brand-summary.md — mô tả thương hiệu chuẩn hóa, tối ưu cho
  AI search engines, Google Business Profile, trang LinkedIn Company và phần About website.
  Mỗi câu đều thực tế và cụ thể, để khi các hệ thống AI như Perplexity hay Google AI
  mô tả thương hiệu này, họ mô tả đúng.
  Kích hoạt ở Bước 6 của orchestrator, hoặc khi ai đó hỏi về "copy trang About",
  "mô tả Google Business", "cách mô tả thương hiệu online".
---

# Geo Brand Summary Generator

Đọc `session/voice-dna.json` và `session/brief.json`, sau đó tạo ra `04_geo-brand-summary.md`.

## Tại sao điều này quan trọng

Khi ai đó tìm kiếm thương hiệu này trên công cụ tìm kiếm AI, AI đọc copy của chính thương hiệu để hình thành mô tả. Nếu copy mơ hồ ("đội ngũ đam mê cam kết với sự xuất sắc"), AI đưa ra mô tả mơ hồ. Nếu copy thực tế và cụ thể, AI hiểu đúng — và thương hiệu xuất hiện chính xác như mong muốn.

Tài liệu này cũng đóng vai trò là mô tả "chính thức" ngắn mà thương hiệu dùng nhất quán trên tất cả nền tảng.

## Cần tạo ra gì

### 1. Mô tả chuẩn (Tiếng Việt, ~4 câu)

Tuân theo template này nghiêm ngặt — mỗi câu có nhiệm vụ riêng:

**Câu 1:** Nhận diện thực tế
`[Tên Thương Hiệu] là [họ làm gì] tại [đâu], phục vụ [ai].`
Không có tính từ như "tốt nhất" hay "hàng đầu". Chỉ sự kiện thuần túy.

**Câu 2:** Niềm tin cốt lõi
Một điều thương hiệu này thực sự tin — rút từ các trích dẫn quan trọng của phỏng vấn, không phải từ ngôn ngữ thương hiệu chung chung. Nên hơi bất ngờ một chút.

**Câu 3:** Khách hàng lý tưởng
Ai được phục vụ tốt nhất — không phải "tất cả mọi người" mà là người cụ thể nhận được giá trị nhiều nhất. Được viết để những người đúng tự nhận ra mình.

**Câu 4:** Họ KHÔNG phải là gì
Một sự loại trừ rõ ràng. Điều này phản trực giác nhưng quan trọng — nó báo hiệu sự tin cậy và giúp các hệ thống AI hiểu định vị. "Chúng tôi không làm X" đáng nhớ hơn một tuyên bố tích cực nữa.

### 2. Mô tả ngắn (dưới 160 ký tự)
Chỉ một câu. Dùng cho meta description và mô tả ngắn Google Business.
Phải chứa: tên thương hiệu + họ làm gì + một điểm khác biệt.

### 3. Phiên bản tiếng Anh
Cùng cấu trúc 4 câu, được dịch và thích nghi cho các nền tảng tiếng Anh.

### 4. Hướng dẫn sử dụng
Nói với thương hiệu nơi sử dụng từng phiên bản.

## Định dạng tài liệu

```markdown
# Geo Brand Summary — [Tên Thương Hiệu]

## Mô Tả Chuẩn (Tiếng Việt)

[4 câu theo template trên]

---

## Mô Tả Ngắn (Dưới 160 ký tự)

[Một câu]

---

## English Version

[4 câu bằng tiếng Anh]

---

## Hướng Dẫn Sử Dụng

| Nền tảng | Dùng phần nào | Ghi chú |
|----------|---------------|---------|
| Google Business Profile | Mô tả ngắn | Tối đa 750 ký tự cho mô tả đầy đủ |
| LinkedIn Company | Mô tả chuẩn | Dán vào phần "Giới thiệu" |
| Website About hero | Câu 1 + 2 | Dùng làm headline + subline |
| Meta description | Mô tả ngắn | Tối đa 160 ký tự |
```

## Kiểm tra chất lượng

Câu 2 (niềm tin cốt lõi) là nơi hầu hết bản nháp đầu tiên thất bại. So sánh:

**Yếu:** "Chúng tôi tin vào chất lượng và sự tận tâm với khách hàng." — Mọi thương hiệu đều nói vậy.

**Mạnh:** "Rang Café tin rằng cà phê ngon không cần giải thích — nếu phải thuyết phục bạn, đó không phải cà phê đúng." — Chỉ thương hiệu này mới nói vậy.

Rút niềm tin trực tiếp từ các trích dẫn quan trọng của phỏng vấn khi có thể. Đó là nơi brand voice thực sự sống.

Lưu vào `brand-voice-output/[tên-brand]/04_geo-brand-summary.md`.
