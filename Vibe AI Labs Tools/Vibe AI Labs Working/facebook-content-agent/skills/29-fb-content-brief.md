# [29] Skill: fb-content-brief

## Mục đích
Reverse-engineer nội dung có sẵn thành một content brief có cấu trúc.
Phân tích bộ khung bên trong bài (hook type, structure, tone, emotion trigger, engagement target)
để dùng làm đầu vào cho các skill viết bài — thay vì bắt đầu từ zero.

Không viết lại bài. Chỉ X-ray và brief.

## Input
- `source_content`: bài viết cần phân tích (paste text trực tiếp)
- `mode`: `analyze` / `brief-for-rewrite` / `brief-for-repurpose` / `series`
- `target_skill`: (tuỳ chọn) skill sẽ nhận output — `fb-post-writer` / `fb-carousel-architect` / `fb-repurpose` / `fb-pillar-planner`
- `series_posts`: (chỉ khi mode=series) mảng 3–5 bài cần tìm pattern
- `brand_voice`: context từ brand-voice-loader

## Chế độ hoạt động

### Mode: `analyze`
Phân tích đầy đủ 1 bài. Không tạo brief để forward — chỉ trả insight.
Dùng khi user muốn hiểu tại sao bài hoạt động tốt hoặc kém.

### Mode: `brief-for-rewrite`
Phân tích rồi tạo brief chuẩn để feed vào `fb-post-writer mode=iterate`.
Output brief chứa đủ: hook formula, structure pattern, tone markers, CTA type.
`fb-post-writer` sẽ giữ nguyên structure nhưng viết lại nội dung đúng brand voice.

### Mode: `brief-for-repurpose`
Phân tích rồi tạo brief cho `fb-repurpose` hoặc `fb-carousel-architect`.
Output brief chứa thêm: format recommendation, số slides nếu chuyển carousel,
beat structure nếu chuyển Reels.

### Mode: `series`
Nhận 3–5 bài, phân tích từng bài, sau đó tổng hợp pattern chung.
Output là một formula sheet: hook formula nào lặp, CTA style nào consistent,
emotion trigger nào luôn xuất hiện. Feed vào `fb-pillar-planner` hoặc `fb-post-writer`.

## Quy trình phân tích (áp dụng cho mọi mode)

### Bước 1: Đọc bài và xác định cấu trúc
Chia bài thành 3 phần: Hook (trước "Xem thêm" / 3 dòng đầu), Body, CTA.
Nếu không có CTA rõ ràng → ghi `cta_type: implicit`.

### Bước 2: Phân tích Hook
Xác định hook type:
- `question`: đặt câu hỏi trực tiếp cho người đọc
- `bold_statement`: tuyên bố gây tranh cãi hoặc bất ngờ
- `statistic`: dùng số liệu gây sốc hoặc gây tò mò
- `story`: mở đầu bằng tình huống / câu chuyện ngắn
- `pain_point`: chỉ thẳng vào vấn đề người đọc đang gặp
- `controversy`: đi ngược quan niệm thông thường
- `how_to`: hứa hẹn chỉ cách làm ngay từ đầu

Đánh giá hook score 1–10 theo:
- Tốc độ tạo tò mò (1–3 giây đọc đầu)
- Độ cụ thể (tránh hook mơ hồ)
- Khớp với audience từ brand_voice

### Bước 3: Phân tích Body
- Value delivery: bài cho đi insight / story / how-to hay chỉ nói chung chung?
- Pacing: ngắn gọn / dài hơi / có pattern interrupt không (số liệu, câu hỏi giữa bài)?
- Emotional arc: cảm xúc nào được kéo qua bài (tò mò → aha → muốn thử)?

### Bước 4: Phân tích CTA
Phân loại:
- `save_bait`: "Lưu lại để dùng", checklist, tip có thể áp dụng
- `share_bait`: "Tag người bạn cần biết", relatable situation
- `comment_bait`: câu hỏi mở, poll, "Bạn nghĩ sao?"
- `click_bait`: "Link ở comment", "DM mình để nhận"
- `soft`: không có CTA rõ, dừng lại ở story

### Bước 5: Đánh giá brand voice alignment
So sánh tone, từ ngữ, cách xưng hô của bài với `brand_voice` context.
Ghi điểm 1–10 và liệt kê gaps nếu có.

### Bước 6 (chỉ mode series): Tổng hợp pattern
Sau khi phân tích từng bài, tìm:
- Hook formula lặp lại >= 2/3 bài
- CTA type nhất quán
- Emotion trigger xuất hiện nhiều nhất
- Độ dài trung bình, pacing chung

## Rules bắt buộc
- Không viết lại bài gốc trong bất kỳ mode nào — đây là skill phân tích, không phải viết
- Không tự thêm hashtag hoặc emoji vào brief
- Nếu bài gốc vi phạm `brand_voice.banned_terms` → ghi vào `brand_voice_alignment.gaps`, không bỏ qua
- Giữ nguyên ngôn ngữ phân tích bằng tiếng Việt dù bài gốc là tiếng Anh

## ⚠️ PIPELINE RULE — bắt buộc với brief-for-rewrite và brief-for-repurpose

Khi mode là `brief-for-rewrite` hoặc `brief-for-repurpose`:

1. **Skill này KHÔNG phải điểm kết thúc.** Sau khi tạo xong brief, orchestrator PHẢI tiếp tục chạy toàn bộ publishing pipeline:
   ```
   [content skill nhận brief] → fb-discussion-architect → fb-first-comment-strategy
   → fb-readability-formatter → fb-visual-brief → fb-vietnamese-localizer → fb-policy-checker
   → fb-save-share-optimizer → fb-send-time-optimizer → fb-review-queue → output-validator
   ```

2. **Output cuối PHẢI là file `.md`** được lưu vào `output/YYYY_MM_DD-[slug].md` theo format chuẩn (Bước 7 của orchestrator). Tuyệt đối không dừng lại ở bước phân tích hoặc brief.

3. Output của skill này phải kèm theo flag rõ ràng:
   ```yaml
   pipeline_continue: full_publishing
   handoff_to: [fb-post-writer nếu brief-for-rewrite / fb-carousel-architect hoặc fb-repurpose nếu brief-for-repurpose]
   ```

Chỉ mode `analyze` và `series` mới được kết thúc mà không chạy tiếp publishing pipeline.

## Output

### Mode `analyze`
```yaml
analysis:
  core_message: "1 câu — bài đang nói gì"
  hook:
    type: [loại hook]
    text: "[hook gốc trích nguyên văn]"
    why_it_works: "[lý do hiệu quả — hoặc tại sao không hiệu quả]"
    score: 1–10
  structure:
    hook_section: "[đoạn mở]"
    body_summary: "[body làm gì — deliver value kiểu gì]"
    cta_type: [save_bait / share_bait / comment_bait / click_bait / soft]
    cta_text: "[CTA gốc trích nguyên văn nếu có]"
  tone:
    style: "[thân thiện / chuyên nghiệp / hài hước / truyền cảm hứng]"
    emotion_triggers: ["[cảm xúc 1]", "[cảm xúc 2]"]
    pacing: "[ngắn gọn / dài hơi / có pattern interrupt]"
  funnel_stage: TOFU | MOFU | BOFU
  pillar_match: "[pillar phù hợp nhất từ brand_voice]"
  engagement_target: save | share | comment | click
  brand_voice_alignment:
    score: 1–10
    gaps: ["[điểm nào chưa khớp brand voice — nếu có]"]
  verdict: "[1–2 câu tổng kết: bài này mạnh ở đâu, yếu ở đâu]"
```

### Mode `brief-for-rewrite`
Output gồm `analysis` (như trên) + `rewrite_brief`:
```yaml
rewrite_brief:
  instruction_for_post_writer:
    keep: ["hook formula: [loại hook] + [pattern cụ thể]", "CTA type: [loại]", "pacing: [ngắn/dài]"]
    change: ["tone → match brand_voice", "từ ngữ → dùng approved_glossary", "xưng hô → [theo brand_voice]"]
    topic: "[core message cần giữ nguyên hoặc điều chỉnh]"
    goal: "[awareness / engagement / conversion — infer từ funnel_stage]"
    funnel_stage: "[TOFU / MOFU / BOFU]"
    mode: "iterate"
    iterate_element: "[element nào cần thay đổi nhiều nhất]"
```

### Mode `brief-for-repurpose`
Output gồm `analysis` (như trên) + `repurpose_brief`:
```yaml
repurpose_brief:
  format_recommendation: carousel | reels | single_image
  format_reason: "[tại sao format này phù hợp với nội dung này]"
  carousel_plan:                         # chỉ nếu format=carousel
    slide_count: [số slide đề xuất]
    slide_structure:
      - slide: 1
        role: "cover — hook"
        content_hint: "[gợi ý nội dung slide 1]"
      - slide: 2
        role: "body — [tên phần]"
        content_hint: "..."
      - slide: "[n]"
        role: "CTA"
        content_hint: "..."
  reels_plan:                            # chỉ nếu format=reels
    duration: "15s | 30s | 60s"
    hook_0_3s: "[gợi ý visual + voiceover]"
    beat_structure: ["[0–5s]", "[5–10s]", "[10–15s]"]
    loop_close: "[gợi ý kết nối cuối với đầu]"
  source_type: "facebook_post"
  link_for_first_comment: null
```

### Mode `series`
```yaml
series_analysis:
  posts_analyzed: [số bài]
  individual_scores:
    - post: 1
      hook_type: "..."
      hook_score: 7
      cta_type: "..."
      engagement_target: "..."
  pattern_report:
    dominant_hook_formula: "[hook type xuất hiện nhiều nhất + pattern cụ thể]"
    dominant_cta_type: "[CTA type nhất quán]"
    recurring_emotion_triggers: ["[trigger 1]", "[trigger 2]"]
    avg_word_count: [số từ trung bình]
    pacing_pattern: "[ngắn gọn / dài hơi / mixed]"
    funnel_stage_mix: "[TOFU-heavy / MOFU-heavy / balanced]"
  formula_sheet:
    hook_template: "[template có thể áp dụng lại — ví dụ: '[Số] điều về [chủ đề] mà [audience] chưa biết']"
    body_pattern: "[pattern body lặp lại]"
    cta_template: "[template CTA nhất quán]"
  recommendation: "[1–2 câu gợi ý dùng formula này thế nào]"
```
