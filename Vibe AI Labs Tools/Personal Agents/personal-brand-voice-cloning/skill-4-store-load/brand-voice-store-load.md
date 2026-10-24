---
name: brand-voice-store-load
description: >
  Bước 5 của Brand Voice Cloning workflow — lưu Brand Voice Card đã confirmed vào file, hoặc load lại Voice Card của brand đã có sẵn.

  Dùng skill này khi: user vừa confirm xong ở Skill 3 và cần lưu Voice Card; hoặc user muốn load lại brand đã phân tích trước đó để dùng lại mà không cần analyze từ đầu. Trigger khi user nói "lưu brand voice", "load brand X", "dùng lại voice card của X", "xem brand đã lưu", hoặc khi bắt đầu session mới và user nhắc đến brand đã có.
---

# Skill 4 — Store / Load

Nhiệm vụ: lưu Voice Card theo tên brand, hoặc load lại khi cần. Đây là bộ nhớ dài hạn của agent — lần sau không cần analyze lại từ đầu.

Tất cả file được lưu trong thư mục `brand-voices/` của project.

## Thao tác STORE

Chạy sau khi user confirm ở Skill 3.

1. Tạo filename: `brand-voices/{brand_name}_voice_card.json`
   - Lowercase, spaces thành dấu gạch dưới, bỏ ký tự đặc biệt
   - Ví dụ: "Vibe AI Labs" → `vibe_ai_labs_voice_card.json`

2. Kiểm tra file đã tồn tại chưa:
   - Nếu chưa có → lưu luôn
   - Nếu đã có → hỏi: `"File đã tồn tại. Overwrite hay lưu thành version mới (v2, v3...)?"

3. Lưu JSON với metadata:
```json
{
  "brand_name": "...",
  "created_at": "YYYY-MM-DD",
  "quality_tier": "Draft / Reliable / Deep",
  "sample_count": N,
  "platforms": [...],
  "voice_card": { ...10 nhóm... }
}
```

4. Xác nhận đã lưu:
```
✅ Đã lưu: brand-voices/{filename}.json
→ Chuyển sang Skill 5 (Export) để tạo file .md?
```

## Thao tác LOAD

Chạy khi user muốn dùng lại brand đã có.

1. List tất cả file `.json` trong `brand-voices/`
2. Hiển thị danh sách:
```
Brand đã lưu:
  1. Vibe AI Labs (Reliable tier, 18 bài, 2024-01-15)
  2. ...

Bạn muốn load brand nào?
```

3. Load file → parse JSON → hỏi:
```
Đã load Voice Card của "{brand_name}".
Bạn muốn:
  A. Export ra file .md luôn (Skill 5)
  B. Xem lại / update trước (Skill 3)
```

## Kiểm tra khi mở session mới

Khi skill này được gọi lần đầu trong session, tự động kiểm tra `brand-voices/` có file nào không. Nếu có → thông báo:

```
Tôi thấy bạn đã có Voice Card cho: {danh sách brand}.
Bạn muốn load brand cũ hay phân tích brand mới?
```
