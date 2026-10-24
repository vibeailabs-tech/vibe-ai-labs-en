# [16] Skill: fb-first-comment-strategy

## Mục đích
Tối ưu first comment — đòn bẩy reach.
FB penalize bài có outbound link trong body → chuyển link xuống first comment giữ reach.

## Input
- `post_content`: bài đã viết (sau discussion-architect)
- `has_external_link`: true / false
- `external_link`: URL nếu có
- `desired_interaction`: comment / share / save / inbox
- `brand_voice`: context từ brand-voice-loader

## Output cần tạo

### 1. First comment của page/admin
Nội dung post ngay lập tức sau khi bài được đăng:
- Nếu có link: "🔗 Link đầy đủ: [URL]\n\n[1 câu giá trị bổ sung]"
- Nếu không có link: tạo "seed comment" mở đầu discussion — tự trả lời câu hỏi trong bài hoặc share góc nhìn thêm
- Tone phải khác với body bài (casual hơn, như đang nói chuyện)

### 2. Comment "mồi" cho team (2–3 cái)
Comment mà team/cộng sự post trong 30 phút đầu để kick-start discussion.
- Mỗi comment theo 1 angle khác nhau
- Không được copy tone nhau — phải như nhiều người khác nhau
- Không được sounding like a bot

**Dạng comment mồi:**
- Người chia sẻ trải nghiệm liên quan
- Người hỏi câu hỏi cụ thể về nội dung
- Người tag bạn bè với lý do rõ ràng

### 3. Câu hỏi pin (nếu phù hợp)
Câu hỏi pin lên top để trigger comment từ audience rộng hơn.
- Ngắn (1 câu)
- Ai đọc cũng có thể trả lời
- Liên quan trực tiếp đến topic

## Rules
- Comment mồi phải thật, không robotic
- Không spam links nhiều lần trong comment
- Câu hỏi pin không trùng với trigger points đã có trong bài

## Output

```yaml
first_comment_strategy:
  admin_first_comment:
    content: [nội dung comment đầu tiên]
    timing: "Đăng ngay sau khi post bài"
    includes_link: [true/false]
  seed_comments:
    - author_persona: [ví dụ: "team member A"]
      content: [nội dung comment]
      timing: "Trong 15 phút đầu"
      angle: [trải nghiệm / câu hỏi / tag bạn]
    - author_persona: ...
      content: ...
      timing: "Trong 30 phút đầu"
      angle: ...
  pin_question:
    content: [câu hỏi pin]
    applicable: [true/false]
    reason: [lý do pin câu này]
```
