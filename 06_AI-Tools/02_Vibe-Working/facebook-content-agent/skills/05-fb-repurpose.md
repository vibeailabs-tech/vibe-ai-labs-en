# [05] Skill: fb-repurpose

## Mục đích
Chuyển hóa nội dung từ nguồn khác thành native Facebook post.
Ưu tiên insight trực tiếp trên post — không chỉ link out.

## Input
- `source_content`: nội dung gốc (paste text) hoặc `source_url` (link)
- `source_type`: blog / podcast / report / email / youtube / other
- `goal`: mục tiêu bài repurpose
- `brand_voice`: context từ brand-voice-loader

## Quy trình

### Bước 1: Extract core insights
Đọc/phân tích nội dung gốc. Lấy ra:
- 3–5 insight mạnh nhất, có thể đứng độc lập
- 1 số liệu / thống kê đáng chú ý (nếu có)
- 1 quote mạnh (nếu có)

### Bước 2: Viết lại cho Facebook
- Giọng văn = brand voice, không phải giọng nguồn gốc
- Insight được viết lại trực tiếp, không phải tóm tắt ("Theo bài X...") — người đọc không cần biết nguồn
- Nếu insight cần dẫn nguồn: "[Nguồn]" ngắn gọn cuối câu
- Không giữ nguyên cấu trúc bài gốc — reframe cho FB feed

### Bước 3: Xử lý link
- Nếu có link external → KHÔNG đặt trong body bài (FB penalty reach)
- Link sẽ được đặt ở first comment (sẽ được xử lý bởi `fb-first-comment-strategy`)
- Bài body chỉ nói "Link đầy đủ ở comment bên dưới 👇" hoặc tương tự

### Bước 4: Chọn format
Dựa trên lượng insight:
- 1–2 insight mạnh → single image post
- 3–5 insights → carousel (mỗi slide 1 insight)
- Quy trình / how-to → Reels script

## Output

```yaml
repurposed_post:
  source_type: [loại nguồn]
  key_insights:
    - [Insight 1 — viết lại dạng standalone]
    - [Insight 2]
    - [Insight 3]
  recommended_format: [single_image / carousel / reels]
  post_content:
    hook: [3 dòng đầu]
    body: [nội dung chính với insights]
    link_mention: "Link đầy đủ ở comment bên dưới 👇"
    cta: [call-to-action]
    full_post: [bài hoàn chỉnh]
  link_for_first_comment: [URL nếu có, để fb-first-comment-strategy dùng]
  notes: [ghi chú gì cần lưu ý khi đăng]
```
