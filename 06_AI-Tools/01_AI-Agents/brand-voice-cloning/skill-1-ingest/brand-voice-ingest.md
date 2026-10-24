---
name: brand-voice-ingest
description: >
  Bước 2 của Brand Voice Cloning workflow — nhận content mẫu của brand, clean và đánh giá chất lượng sample trước khi phân tích.

  Dùng skill này khi user đã có platform_map từ Skill 0 và đang paste hoặc upload content mẫu của brand để phân tích giọng văn. Trigger khi user paste nhiều đoạn text/bài viết, upload file txt/md, hoặc nói "đây là content của brand", "tôi paste nội dung vào đây", "nhận content brand".
---

# Skill 1 — Ingest + Quality Gate

Nhiệm vụ: nhận content, làm sạch, và đánh giá xem sample có đủ chất lượng để phân tích chính xác không. Không để user nộp 3 bài rồi ra Voice Card như thể đủ data.

## Cách nhận content

Nhắc user:
```
Paste content trực tiếp vào đây, hoặc upload file (.txt, .md).
Nếu nhiều platform thì nhớ label [FACEBOOK], [BLOG], [EMAIL]... trước mỗi đoạn.
```

Khi nhận được content:
1. Tách và đếm số lượng bài/đoạn riêng biệt
2. Gắn platform tag theo `platform_map` từ Skill 0
3. Loại bỏ content trùng lặp hoặc không liên quan (navigation text, footer boilerplate, v.v.)

## Quality Gate

Sau khi nhận xong, đánh giá và **báo rõ cho user** trước khi sang Skill 2:

| Tình trạng | Hành động |
|---|---|
| < 10 bài | Cảnh báo rõ, đề nghị bổ sung. Nếu user vẫn muốn tiếp → cho phép, ghi rõ **Draft tier** |
| Tất cả cùng 1 topic | Yêu cầu thêm bài đa dạng topic để tránh bias |
| Chỉ 1 loại context (toàn sale hoặc toàn educate) | Gợi ý thêm bài từ context khác |
| 10–14 bài | **Draft tier** — kết quả sơ bộ, cần user verify kỹ ở Skill 3 |
| 15–25 bài | **Reliable tier** — đủ để ra Voice Card tốt |
| 30–50+ bài | **Deep tier** — Voice Card rất chính xác |

## Output

Báo cáo ngắn gọn cho user:

```
✅ Đã nhận: {N} bài từ {platform(s)}
📊 Quality tier: {Draft / Reliable / Deep}
{Cảnh báo nếu có — topic bias, context bias, v.v.}

→ Sẵn sàng phân tích. Chuyển sang Skill 2 (Analyze)?
```

Chờ user confirm → chuyển sang **Skill 2 (Analyze)**.
