---
name: brand-voice-export
description: >
  Bước cuối của Brand Voice Cloning workflow — biến Brand Voice Card JSON thành file markdown đẹp, đầy đủ để team dùng như brand guideline thực tế.

  Dùng skill này khi đã có Voice Card JSON (từ Skill 4 hoặc load từ file) và cần xuất ra tài liệu. Trigger khi user nói "export", "tạo file markdown", "xuất voice card", "tạo brand guideline", "ra file .md", hoặc sau khi Skill 4 lưu xong và hỏi có muốn export không.
---

# Skill 5 — Export

Nhiệm vụ: biến Voice Card JSON thành file markdown có cấu trúc đẹp để team dùng thực tế. JSON là định dạng cho machine — Export biến nó thành tài liệu thật sự usable.

## Output file

Lưu tại: `brand-voices/{brand_name}_voice_card.md`

## Yêu cầu của file export

File phải phục vụ được 3 mục đích:
1. **Copywriter / account đọc hàng ngày** — ngôn ngữ rõ, ví dụ cụ thể, không dùng JSON key
2. **Paste làm system prompt cho AI tools** — có section riêng dạng instruction ngắn gọn
3. **Share trong team** qua Notion, Google Docs, GitHub — markdown chuẩn, không custom syntax

## Cấu trúc file — theo template

Đọc template tại `references/export_template.md` và điền đầy đủ từng section.

Lưu ý khi render:
- Dùng ngôn ngữ tự nhiên, không dùng key JSON như `brand_purpose`, `core_traits`
- Với `tone_spectrum` → render thành thanh visual: `Funny ←——30%——→ Serious`
- Với `say_this_not_that` → render thành bảng 2 cột rõ ràng
- Với `annotated_sample` → render trong code block kèm chú thích bên dưới
- Nếu có field `"Chưa đủ data để kết luận"` → ghi *(Cần bổ sung)* thay vì để trống

## Sau khi export

Thông báo:

```
✅ Đã tạo: brand-voices/{brand_name}_voice_card.md

File này có thể dùng để:
• Onboard copywriter mới
• Paste vào system prompt ChatGPT / Claude / Jasper
• Share qua Notion hoặc Google Docs
• Input cho Content Generation Agent
```
