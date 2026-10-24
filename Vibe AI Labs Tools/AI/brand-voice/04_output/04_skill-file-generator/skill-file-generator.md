---
name: skill-file-generator
description: >
  Tập hợp tất cả output brand voice thành 5 file cuối cùng và ghi ra đĩa.
  Cũng tạo ra hai file chưa được các skill output khác xử lý:
  02_brand-voice-system-prompt.md (system prompt sẵn sàng cho AI) và
  05_drift-checker-rubric.json (rubric chấm điểm để QA content định kỳ).
  Kích hoạt ở Bước 7 của orchestrator, sau khi tất cả skill output đã chạy.
---

# Skill File Generator

Đây là bước lắp ráp cuối cùng. Bạn đã có tất cả các mảnh — giờ đóng gói chúng thành 5 file mà khách hàng thực sự sẽ dùng.

## Bạn tạo ra gì ở đây

Hai file được tạo ở bước này (ba file còn lại đến từ các skill trước):

### `02_brand-voice-system-prompt.md`

Đây là file quan trọng nhất. Nó được dán thẳng vào system prompt của bất kỳ AI agent nào — một người viết mạng xã hội, trợ lý email, chatbot — và ngay lập tức cho agent đó brand voice.

Xây dựng từ `session/voice-dna.json` theo template này:

```markdown
# Brand Voice System Prompt — [Tên Thương Hiệu]

> Dán tất cả nội dung dưới dòng này vào system prompt của AI agent.

---

Bạn đang viết content cho **[Tên Thương Hiệu]**.

**CÁ TÍNH:** [3 tính cách từ voice-dna.personality_traits, ngăn cách bằng dấu phẩy]

**TONE:** Viết như [voice-dna.tone].
Không phải như [voice-dna.tone_not_like].

**KHÔNG BAO GIỜ DÙNG:**
[Mỗi từ cấm trên một dòng riêng, có dấu -]

**HÃY DÙNG NHỮNG TỪ NÀY:**
[Mỗi từ signature trên một dòng riêng, có dấu -]

**PHONG CÁCH CÂU:**
[voice-dna.sentence_rhythm]

**BRAND ARCHETYPE:** [archetype]

**ĐIỀU LÀM CHÚNG TÔI KHÁC BIỆT:**
[differentiation]

---

**VÍ DỤ — Sai:**
> [example_bad]

**VÍ DỤ — Đúng:**
> [example_good]

---

*Khách hàng mục tiêu: [brief.target_audience]*
*Thị trường: [brief.location] | Phân khúc: [brief.price_point]*
```

### `05_drift-checker-rubric.json`

Rubric được dùng bởi skill drift-detector để QA content định kỳ. Xây dựng từ `session/voice-dna.json`:

```json
{
  "brand_name": "",
  "version": "1.0",
  "generated": "[ngày]",
  "must_have": [
    {"type": "personality_marker", "description": "[tính cách 1]"},
    {"type": "personality_marker", "description": "[tính cách 2]"},
    {"type": "personality_marker", "description": "[tính cách 3]"}
  ],
  "forbidden": [
    {"type": "forbidden_word", "value": "[từ]"}
  ],
  "tone_keywords": ["[từ signature 1]", "[từ signature 2]"],
  "tone_score_threshold": 0.75,
  "sentence_length_max": 25,
  "archetype": "[archetype]",
  "scoring": {
    "forbidden_word_penalty": -0.15,
    "signature_word_bonus": 0.05,
    "personality_marker_bonus": 0.10,
    "base_score": 1.0
  },
  "platform_rules": {
    "facebook": {"max_length_words": 150, "emoji_allowed": true},
    "linkedin": {"max_length_words": 300, "hashtag_required": true},
    "email": {"greeting_required": true},
    "chatbot": {"response_length": "short"}
  }
}
```

## Lắp ráp file

Thu thập tất cả output:
- `01_brand-voice-card.md` — từ session hoặc từ output của skill brand-voice-card
- `02_brand-voice-system-prompt.md` — tạo ở trên
- `03_platform-variants.json` — từ output của skill platform-adaptor
- `04_geo-brand-summary.md` — từ output của skill geo-brand-summary
- `05_drift-checker-rubric.json` — tạo ở trên

Ghi tất cả 5 file vào: `brand-voice-output/[tên-brand-an-toàn]-[ngày]/`

Trong đó `tên-brand-an-toàn` là tên thương hiệu viết thường, khoảng trắng thay bằng dấu gạch ngang, bỏ ký tự đặc biệt.

## Thông điệp bàn giao

Sau khi ghi tất cả file, thông báo với người dùng:

```
✅ Brand voice hoàn tất. 5 file đã lưu vào: brand-voice-output/[tên-brand]-[ngày]/

📄 01_brand-voice-card.md      — chia sẻ với team và agency của bạn
🤖 02_brand-voice-system-prompt.md  — dán vào bất kỳ công cụ AI nào
📱 03_platform-variants.json   — quy tắc theo từng nền tảng
🌏 04_geo-brand-summary.md     — dùng trên Google, LinkedIn, trang About
🔍 05_drift-checker-rubric.json — để QA content hàng tháng

Để kiểm tra content mới có phù hợp brand voice không:
→ Chia sẻ content + nói "drift check" và tôi sẽ chấm điểm theo rubric của bạn.
```
