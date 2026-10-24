# [01] Skill: brand-voice-loader

## Mục đích
Đọc brand voice folder, extract context có cấu trúc, inject vào tất cả skill phía sau.
Đây là HARD GATE — nếu không load được brand voice, toàn bộ pipeline dừng lại.

## Input
- `brand_voice_path`: đường dẫn tới brand voice folder (mặc định: `./brand-voice/`)

## Quy trình thực hiện

1. Đọc 5 file trong brand voice folder:
   - `01-tone.md` — giọng văn, tính cách thương hiệu
   - `02-audience.md` — persona khách hàng mục tiêu
   - `03-pillars.md` — content pillars và tỷ lệ phân bổ
   - `04-examples.md` — bài mẫu tốt và anti-pattern
   - `05-glossary.json` — từ ngữ approved/banned có cấu trúc

2. Nếu bất kỳ file nào thiếu:
   - Báo rõ file nào thiếu
   - Dừng pipeline: "❌ Brand voice folder thiếu file [tên file]. Vui lòng thêm file này vào thư mục [path] trước khi tiếp tục."

3. Parse `05-glossary.json` thành danh sách có thể query:
   - `approved_terms`: list từ được dùng
   - `banned_terms`: list từ bị cấm
   - `ban_reasoning`: dict giải thích lý do từng ban

4. Tổng hợp thành brand voice context object

## Output (structured context object)

```yaml
brand_voice:
  tone: [nội dung từ 01-tone.md]
  audience_persona: [nội dung từ 02-audience.md]
  pillars:
    - name: [tên pillar]
      description: [mô tả]
      ratio: [tỷ lệ %]
      goal: [Awareness/Engagement/Conversion]
  approved_glossary: [list từ approved]
  banned_terms: [list từ banned]
  ban_reasoning: [dict giải thích]
  approved_examples: [list bài mẫu tốt]
  anti_patterns: [list anti-pattern]
```

## Ghi chú quan trọng
- Skills phía sau KHÔNG được tự đọc brand voice folder — chỉ dùng context object từ skill này
- Nếu 05-glossary.json không tồn tại, dùng danh sách banned mặc định: ["đảm bảo", "100%", "cam kết", "chắc chắn"]
- Log kết quả: `[timestamp] brand-voice-loader ✅ [duration]ms — loaded: [brand name]`
