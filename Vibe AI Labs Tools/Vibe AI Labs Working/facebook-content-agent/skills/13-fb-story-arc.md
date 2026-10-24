# [13] Skill: fb-story-arc

## Mục đích
Viết bài kể chuyện theo cung bậc cảm xúc rõ ràng: setup → conflict → resolution.
Storytelling là format có share rate cao nhất trên Facebook.

## Input
- `story_type`: founder / behind_the_scenes / customer / product / team
- `key_message`: điều muốn người đọc nhớ hoặc cảm nhận sau khi đọc
- `story_facts`: những sự thật/chi tiết thực tế cần include (không được bịa)
- `brand_voice`: context từ brand-voice-loader

## Story frameworks theo loại

### Founder story
Arc: Tôi bắt đầu từ đâu → Tôi đã sai/khó khăn thế nào → Tôi học được gì → Giờ tôi đang làm gì
- Authentic hơn nếu có moment yếu đuối / thất bại thật
- Kết nối với mission của thương hiệu, không chỉ success story

### Behind-the-scenes
Arc: Mọi người thấy kết quả cuối → Ít ai biết quá trình → Đây là góc khuất thật
- Tạo cảm giác "được nhìn hậu trường" — exclusive
- Humanize thương hiệu — team, quy trình, nỗ lực thật

### Customer story
Arc: Khách hàng ở đâu trước → Vấn đề / pain point cụ thể → Hành trình thay đổi → Kết quả thật
- KHÔNG dùng kết quả cụ thể nếu vi phạm policy (đặc biệt ngành y tế/giảm cân)
- Focus vào cảm xúc và hành trình, không chỉ outcome

### Product story
Arc: Tại sao sản phẩm này được tạo ra → Vấn đề nó giải quyết → Sản phẩm ra đời như thế nào
- Origin story > feature list — người đọc kết nối với "tại sao" hơn "cái gì"

### Team story
Arc: Gặp nhau như thế nào → Thách thức team đã vượt qua → Điều gắn kết team

## Nguyên tắc viết story

### Cảm xúc trước, logic sau
Mở đầu bằng cảm xúc hoặc khoảnh khắc cụ thể, không phải facts.
❌ "Chúng tôi thành lập năm 2020 với mục tiêu..."
✅ "Hôm đó tôi nhìn vào tài khoản ngân hàng và thấy số dư là 0."

### Chi tiết cụ thể > nói chung chung
Chi tiết cụ thể tạo credibility và khả năng đồng cảm.
❌ "Giai đoạn đó rất khó khăn"
✅ "3 tháng liên tiếp không đủ tiền trả lương cho nhân viên"

### Conflict là trái tim của story
Không có conflict = không có story. Đừng skip khó khăn để kể thành công.

## Output

```yaml
story_post:
  story_type: [loại]
  arc_structure:
    setup: [đoạn mở — bối cảnh, nhân vật, thời điểm]
    conflict: [vấn đề / thách thức / khoảnh khắc khó]
    resolution: [giải quyết, bài học, kết quả]
  full_post:
    hook: [3 dòng đầu — kéo người đọc vào story]
    body: [thân bài theo arc]
    cta: [CTA phù hợp — thường là share hoặc comment trải nghiệm]
    full_text: [toàn bộ bài]
  emotional_journey: [cảm xúc chính muốn reader trải qua: đồng cảm → inspired / surprised → moved]
  word_count: [số từ]
  share_trigger: [điểm nào trong bài khiến người ta muốn share]
```
