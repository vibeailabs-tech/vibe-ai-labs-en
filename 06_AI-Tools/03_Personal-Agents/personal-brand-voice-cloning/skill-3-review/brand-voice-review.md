---
name: brand-voice-review
description: >
  Bước 4 của Brand Voice Cloning workflow — hiển thị Brand Voice Card cho user đọc, chỉnh sửa, và confirm trước khi lưu.

  Dùng skill này sau khi Skill 2 đã xuất ra Brand Voice Card JSON. Đây là human checkpoint bắt buộc. Trigger khi user được hỏi "xem lại Voice Card", "chỉnh sửa Voice Card", "review brand voice", hoặc khi cần confirm trước khi lưu.
---

# Skill 3 — User Review

Nhiệm vụ: hiển thị Brand Voice Card để user đọc và chỉnh trực tiếp trước khi lưu. AI đôi khi miss nuance — đặc biệt `emotional_signature` và `brand_identity_foundation` là những thứ không đọc được hoàn toàn từ text. User là người biết brand thật hơn bất kỳ AI nào.

**Đây là hard checkpoint** — không tự động đi sang Skill 4 khi chưa được user xác nhận.

## Cách thực hiện

### Bước 1 — Hiển thị Voice Card

Trình bày Voice Card theo định dạng dễ đọc (không phải raw JSON) — từng nhóm một với heading rõ ràng. Dùng format markdown gọn, không quá dài.

Với mỗi nhóm, highlight những điểm AI **không chắc chắn** hoặc ghi `"Chưa đủ data"` để user chú ý kiểm tra kỹ hơn.

### Bước 2 — Hỏi feedback

Sau khi hiển thị xong, hỏi:

```
Bạn muốn chỉnh gì không?
Có điểm nào tôi phân tích sai hoặc thiếu không?

(Gõ "ok" hoặc "lưu" nếu mọi thứ đúng)
```

### Bước 3 — Áp dụng chỉnh sửa

Nếu user chỉnh sửa:
- Áp dụng ngay vào Voice Card JSON
- Hiển thị lại phần đã chỉnh để confirm
- Hỏi xem còn gì cần chỉnh không

### Bước 4 — Confirm lần cuối

Khi user nói ok / xong / lưu:

```
Xác nhận lưu Voice Card cho brand "{brand_name}"?
(Trả lời "có" để lưu và chuyển sang Skill 4)
```

Khi có xác nhận → chuyển sang **Skill 4 (Store/Load)** với Voice Card đã confirmed.
