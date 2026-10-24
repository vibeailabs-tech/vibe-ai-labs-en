# [23] Skill: fb-readability-formatter

## Mục đích
Format trình bày bài — KHÔNG sửa nội dung, chỉ sửa cách hiển thị.

## Input
- `post_content`: bài cần format
- `format_type`: single_image / carousel_caption / reels_caption
- `brand_voice`: context từ brand-voice-loader

## Rules format

### Ngắt dòng
- Mỗi đoạn tối đa 2 câu → xuống dòng
- Câu đơn ngắn (impact statement) → đứng một mình 1 dòng
- Không để block text dài 4+ câu liên tục

### "Xem thêm" cliff (điểm gập Facebook)
- Facebook hiển thị ~3 dòng đầu trước khi cắt "Xem thêm"
- Hook phải nằm hoàn toàn trong 3 dòng này
- Dòng 3 phải tạo câu hỏi/tò mò để người ta bấm "Xem thêm"
- Không để dòng 3 là câu kết thúc ý

### Emoji làm visual anchor
- Dùng emoji để đánh dấu đầu ý (📌, ✅, 💡, ⚡, 🔑) — không lạm dụng
- Emoji phải phù hợp tone: trang trọng → dùng ít; casual → có thể nhiều hơn
- Không dùng emoji ngay đầu bài nếu brand voice serious/professional
- Không dùng emoji trong mọi câu — chỉ tại điểm cần highlight

### Rhythm xen kẽ
- Xen kẽ câu ngắn (5–10 từ) và câu dài (15–25 từ)
- Tránh nhiều câu dài liên tiếp — gây nặng nề khi đọc trên mobile
- Câu ngắn đứng sau insight mạnh → nhấn mạnh

### Khoảng trắng
- Giữa các section lớn: 1 dòng trống
- Giữa các đoạn thường: xuống dòng (không trống hẳn)

## Output

```yaml
formatted_post:
  original: [bài gốc]
  formatted: [bài đã format — đây là output dùng để đăng]
  changes_made:
    - [Mô tả thay đổi 1]
    - [Mô tả thay đổi 2]
  see_more_cliff_check:
    line_3_content: [nội dung dòng 3]
    creates_tension: [true/false]
    note: [ghi chú nếu cần điều chỉnh hook]
```
