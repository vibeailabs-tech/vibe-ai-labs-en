---
name: brand-voice-platform-intake
description: >
  Bước đầu tiên của Brand Voice Cloning workflow — hỏi context brand và platform trước khi nhận bất kỳ content nào để phân tích giọng văn.

  Dùng skill này khi user muốn: bắt đầu phân tích brand voice, clone giọng văn brand mới, tạo brand voice card, hoặc nói bất cứ điều gì như "phân tích brand này", "tôi muốn clone voice của X", "bắt đầu brand voice", "tạo guideline viết content cho brand". Đây luôn là skill đầu tiên cần chạy nếu chưa có platform_map.
---

# Skill 0 — Platform Intake

Nhiệm vụ của skill này là hỏi đúng 2 thứ trước khi nhận content: **tên brand** và **content đến từ platform nào**.

Lý do quan trọng: cùng 1 brand nhưng Facebook vs Email vs Ads viết hoàn toàn khác nhau. Nếu không biết trước, Skill 2 (Analyze) sẽ không phân biệt được đâu là brand voice thật và đâu là convention của platform — ví dụ brand dùng emoji vì thật sự thích hay vì tất cả Facebook post đều vậy.

## Cách thực hiện

### Bước 1 — Hỏi brand name và platform

Hỏi user:

```
Brand này tên gì?

Content bạn sẽ paste thuộc platform nào? (chọn một hoặc nhiều)

  SHORT-FORM SOCIAL    → Facebook, Instagram, TikTok, X, Threads
  LONG-FORM OWNED      → Blog, Email, Landing page, Website copy
  PAID & CONVERSION    → Ads, Banner, Advertorial
  CONVERSATIONAL       → Chatbot, CS script, Auto-reply
```

### Bước 2 — Nếu user chọn nhiều platform

Yêu cầu label rõ từng đoạn content trước khi paste:

```
Vì bạn chọn nhiều platform, hãy label rõ từng đoạn khi paste:
[FACEBOOK], [BLOG], [EMAIL], [ADS], [LANDING], v.v.
```

Nếu user chọn 1 platform duy nhất → không cần label, ghi nhận luôn.

## Output — platform_map

Sau khi có đủ thông tin, tóm tắt lại để confirm với user trước khi chuyển sang Skill 1:

```
Brand: {brand_name}
Platform(s): {danh sách platform}
Label scheme: {cần label / không cần label}

→ Sẵn sàng nhận content. Bạn muốn paste ngay bây giờ không?
```

Khi user confirm → chuyển sang **Skill 1 (Ingest + Quality Gate)**.
