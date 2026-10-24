# [15] Skill: fb-discussion-architect

## Mục đích
Thiết kế bài để invite multi-thread comment — nhiều nhóm audience comment vì lý do khác nhau.
FB 2026: 10 comment ý nghĩa > 100 likes. Multi-thread comment được boost reach mạnh hơn single-thread.

## Input
- `post_draft`: bài đã viết (từ content creation skill)
- `brand_voice`: context từ brand-voice-loader

## 3 loại trigger points cần tích hợp vào bài

### 1. Identity Trigger
Câu hỏi hoặc statement khiến người đọc phải tự nhận mình thuộc nhóm nào.
- Tạo 2 camp rõ ràng → 2 luồng comment khác nhau
- Ví dụ: "Bạn là người lên kế hoạch hay người làm theo cảm hứng?"
- Ví dụ: "Team dậy sớm hay team ngủ muộn làm việc?"

### 2. Opinion Trigger
Hot take hoặc góc nhìn khác biệt → audience muốn đồng ý hoặc phản đối.
- Phải đủ "cứng" để gây phản ứng, nhưng không gây tranh cãi toxic
- Ví dụ: "Tôi không tin vào 'content is king' nữa — distribution mới là king"
- Ví dụ: "Posting nhiều không bằng posting đúng — 3 bài/tuần làm tốt hơn 7 bài/tuần cẩu thả"

### 3. Experience Trigger
Câu hỏi mời share trải nghiệm cá nhân — người đọc thấy được hỏi, không phải bị dạy.
- Phải liên quan trực tiếp đến chủ đề bài
- Ví dụ: "Bạn đã thử cách nào rồi? Comment cho mình biết với!"
- Ví dụ: "Case của bạn là gì? Có ai đang gặp tình huống này không?"

## Quy trình

### Bước 1: Phân tích bài gốc
Xác định điểm nào trong bài có thể tự nhiên trigger discussion.

### Bước 2: Tích hợp trigger points
- Không thêm trigger một cách gượng ép — phải flow tự nhiên trong bài
- Tối đa 2–3 trigger points (thêm sẽ loãng, bài thành bài hỏi)
- Nên có ít nhất 1 experience trigger ở cuối bài (trước hoặc thay CTA)
- Identity / opinion trigger nên ở giữa bài hoặc sau hook

### Bước 3: Kiểm tra
- Bài sau khi chỉnh có đọc tự nhiên không, hay bị đứt mạch?
- Trigger có phù hợp với brand voice không?

## Output

```yaml
discussion_optimized_post:
  original_post: [bài gốc]
  trigger_points_added:
    - type: identity | opinion | experience
      location: [vị trí trong bài: đầu/giữa/cuối]
      trigger_text: [đoạn text được thêm/sửa]
      expected_response: [dạng comment mong muốn từ audience]
  revised_post: [bài đã chỉnh với trigger points tích hợp]
  changes_summary: [mô tả ngắn đã thay đổi gì]
```
