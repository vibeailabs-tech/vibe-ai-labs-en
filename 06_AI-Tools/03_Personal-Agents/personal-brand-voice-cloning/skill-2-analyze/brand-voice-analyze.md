---
name: brand-voice-analyze
description: >
  Bước 3 của Brand Voice Cloning workflow — phân tích toàn bộ content mẫu và extract ra Brand Voice Card JSON đầy đủ 10 nhóm.

  Đây là skill nặng nhất trong workflow. Dùng khi đã có content đã clean từ Skill 1 và cần phân tích giọng văn, tone, vocabulary, storytelling pattern của brand. Trigger khi user nói "phân tích đi", "analyze brand voice", "extract voice card", hoặc sau khi Skill 1 đã confirm quality gate.
---

# Skill 2 — Analyze

Nhiệm vụ: đọc toàn bộ content theo `platform_map`, extract ra Brand Voice Card JSON. Kết quả ở đây quyết định Voice Card có đủ sâu để reproduce giọng văn hay không.

## Nguyên tắc phân tích 2 lớp

Phân tích song song 2 lớp — đừng trộn lẫn:

- **Cross-platform constants** → xuất hiện nhất quán ở mọi kênh → đây là **brand voice thật**
- **Per-platform variations** → thay đổi theo kênh → đây là **tone adaptation**, không phải core voice

## 10 nhóm cần extract

### 1. brand_identity_foundation
- `brand_purpose`: Brand tồn tại để làm gì, giải quyết vấn đề gì cho ai
- `core_values`: 3–5 giá trị cốt lõi + cách chúng thể hiện cụ thể trong ngôn ngữ
- `brand_persona`: Nếu brand là một người — nghề nghiệp, tính cách, cách nói chuyện
- `market_position`: premium / mass / rebel / expert / challenger / friendly-neighbor
- `target_audience`: Brand đang nói chuyện với ai, mô tả cụ thể

### 2. tone_and_personality
- `core_traits`: 3–5 tính cách dùng "but not" method — *Confident but not arrogant*
- `tone_spectrum`: % trên 4 trục:
  - Funny (0%) ↔ Serious (100%)
  - Formal (0%) ↔ Casual (100%)
  - Respectful (0%) ↔ Irreverent (100%)
  - Enthusiastic (0%) ↔ Matter-of-fact (100%)
- `tone_by_context`: Tone khi bán hàng / educate / crisis / celebrate
- `emotional_target`: Cảm xúc brand muốn người đọc có sau khi đọc xong
- `humor_style`: none / wry / self-deprecating / absurd / wordplay — kèm ví dụ
- `vulnerability_level`: Mức độ brand chia sẻ thật, behind-the-scenes, admit mistakes

### 3. vocabulary_and_language
- `signature_words`: Từ / cụm từ đặc trưng hay xuất hiện — trích dẫn thực tế
- `forbidden_words`: Từ brand tránh hoàn toàn (từ chứng cứ trong text, không đoán)
- `english_mix_ratio`: 0% / thỉnh thoảng / ~30% / ~50%+
- `self_reference`: Brand tự xưng thế nào
- `audience_address`: Gọi người đọc thế nào
- `jargon_level`: none / dùng có giải thích / dùng tự do — kèm ví dụ
- `inclusive_language`: Mức độ và cách áp dụng

### 4. sentence_and_rhythm
- `sentence_length`: Ngắn / Trung bình / Dài / Mix — với ví dụ thực tế
- `uses_fragments`: Có / Không — ví dụ nếu có
- `signature_patterns`: Pattern câu lặp lại — contrast, nhịp ba, câu hỏi tự trả lời, anaphora
- `opening_rhythm`: Pattern mở đầu bài điển hình
- `closing_rhythm`: Pattern kết thúc bài điển hình
- `punctuation_style`: Cách dùng dash (—), ellipsis (...), chấm than (!)

### 5. formatting_dna
- `emoji_usage`: none / sparingly / heavy — dùng ở đâu, loại nào
- `structure_style`: Headers+sections / Pure prose / Mixed
- `list_vs_paragraph`: Ưu tiên list hay paragraph
- `avg_length_by_platform`: Ước tính độ dài theo từng kênh
- `whitespace_style`: Cách dùng khoảng trắng và xuống dòng
- `text_emphasis`: Bold/italic — có dùng không, dùng để làm gì

### 6. storytelling_and_angles
- `preferred_angles`: Góc quen thuộc — trái chiều / data-driven / story-first / how-to / behind-scenes
- `opening_hooks`: Cách mở vấn đề — câu hỏi / quan sát / số liệu / cảnh quen thuộc / bold claim
- `uses_personal_stories`: Có / Không — mức độ
- `data_usage`: Có dùng không, dùng thế nào, nguồn loại gì
- `handles_controversy`: Cách xử lý chủ đề nhạy cảm
- `self_promotion_level`: Thấp / Vừa / Cao — và cách thể hiện

### 7. channel_adaptation
- `voice_constants`: Thứ tuyệt đối không đổi dù ở kênh nào
- `per_platform_rules`: Quy tắc riêng từng platform quan sát được
- `adaptation_logic`: Mô tả ngắn logic thay đổi tone theo kênh

### 8. emotional_signature
- `reader_emotion`: inspired / empowered / informed / entertained / challenged / comforted
- `energy_level`: High / Medium / Low-key / Varies
- `empathy_style`: Cách brand thể hiện empathy — có không, kiểu gì

### 9. dos_and_donts
- `say_this_not_that`: 5–7 cặp cụ thể — "Thay vì [X], viết [Y]"
- `common_mistakes`: Lỗi hay gặp khi viết cho brand này
- `red_lines`: Thứ tuyệt đối không được xuất hiện

### 10. sample_fingerprints
- `signature_sentences`: 5–7 câu "chỉ brand này mới viết thế này" — trích trực tiếp hoặc reconstruct sát nhất
- `opening_patterns`: 1–2 ví dụ pattern mở bài điển hình
- `closing_patterns`: 1–2 ví dụ pattern kết bài điển hình
- `annotated_sample`: 1 đoạn văn mẫu hoàn chỉnh kèm annotation từng phần giải thích tại sao đúng brand voice

## Quy tắc quan trọng

- Không bỏ nhóm nào dù thiếu data
- Nếu không đủ bằng chứng để kết luận → ghi `"Chưa đủ data để kết luận"`, không đoán
- Mọi nhận xét cần có ít nhất 1 ví dụ trích dẫn từ content thực tế
- Nếu brand chỉ có 1 platform → bỏ qua per-platform analysis ở nhóm 7, ghi rõ lý do

## Output

Brand Voice Card dạng JSON đầy đủ 10 nhóm → chuyển sang **Skill 3 (User Review)**.
