# [12] Skill: fb-comment-reply

## Mục đích
Soạn reply comment phù hợp brand voice — tự nhiên, không robotic.

## Input
- `original_comment`: nội dung comment cần reply
- `comment_type`: question / negative_feedback / compliment / spam / viral_crisis
- `context`: (tuỳ chọn) bài gốc để hiểu ngữ cảnh
- `brand_voice`: context từ brand-voice-loader

## Xử lý theo từng loại comment

### Câu hỏi (question)
- Trả lời đúng và đủ — không vòng vo
- Nếu câu hỏi cần tư vấn riêng: mời inbox, không reply công khai thông tin nhạy cảm
- Thêm 1 câu mở rộng conversation nếu phù hợp
- Kết bằng CTA nhẹ nếu liên quan sản phẩm

### Feedback tiêu cực (negative_feedback)
- Không phòng thủ, không tranh luận
- Acknowledge cảm xúc trước, giải thích sau
- Nếu lỗi của brand: nhận trách nhiệm rõ ràng, nêu action sẽ làm
- Mời inbox để giải quyết cụ thể — không để drama trên bình luận công khai
- Tone: bình tĩnh, chuyên nghiệp, empathetic

### Khen (compliment)
- Cảm ơn chân thành — không quá formal, không sáo rỗng
- Personalize nếu comment có chi tiết cụ thể
- Có thể mời share trải nghiệm hoặc tag bạn bè nếu tự nhiên

### Spam
- Không reply (phần lớn trường hợp)
- Nếu phải reply (ví dụ spam trong bài viral): 1 câu lịch sự, không engage
- Gợi ý: hide comment hoặc report thay vì reply

### Khủng hoảng viral (viral_crisis)
- Ưu tiên de-escalation — không phòng thủ, không attack lại
- Reply nhanh (trong 1h) — để lâu càng tệ
- Công nhận vấn đề, nêu bước xử lý cụ thể
- Mời contact private để giải quyết
- Nếu có sai sót nghiêm trọng: cân nhắc post bài riêng xin lỗi thay vì chỉ reply comment
- KHÔNG: xóa comment tiêu cực (trừ vi phạm standards), cãi lại, dùng template nghe có vẻ PR

## Output

```yaml
comment_reply:
  comment_type: [loại comment]
  suggested_reply: [nội dung reply hoàn chỉnh]
  tone_check: [có đúng brand voice không]
  escalation_needed: [true/false — có cần leo thang lên quản lý không]
  additional_action: [hide/report/post_apology/inbox_followup/none]
  alternative_reply: [phiên bản reply thứ 2 nếu muốn A/B]
  notes: [ghi chú đặc biệt nếu có]
```
