# Li Carousel Architect — LinkedIn Carousel PDF

Thiết kế LinkedIn Carousel PDF. Đây là format có hiệu suất cao nhất trên LinkedIn năm 2026 nhờ tỷ lệ save cao và dwell time tối đa.

## Tại Sao Carousel Hiệu Quả

- Người dùng vuốt qua nhiều slide = tín hiệu dwell time đáng kể
- Tỷ lệ save cao gấp 3-5 lần so với text post = reach dài hạn
- Format PDF tạo cảm giác chuyên nghiệp và "đáng lưu lại"
- Mỗi slide hoạt động như một mini-post — tạo ra nhiều điểm dừng cuộn

---

## Cấu Trúc Carousel (10-15 slides)

### Slide 1: COVER (quan trọng nhất)
Phải khiến người dùng dừng lại. Bao gồm:
- Tiêu đề in đậm (cam kết về điều người đọc sẽ học được)
- Tên/handle của bạn ở chữ nhỏ (branding)
- Tùy chọn: hình ảnh minh họa cho tiêu đề

Mẫu tiêu đề cover:
- "[N] [điều] giúp bạn [kết quả]" — list promise
- "Cách [kết quả cụ thể] trong [thời gian/bối cảnh]"
- "Tại sao [niềm tin phổ biến] là sai"
- "[Tên framework]: [nó làm gì]"

### Slides 2-3: ĐẶT VẤN ĐỀ
- Tại sao chủ đề này quan trọng?
- Người đọc đang gặp phải vấn đề gì?
- Thiết lập nhu cầu cho nội dung tiếp theo
- Giữ tính gần gũi — người đọc nên nghĩ "đúng rồi, đây là mình"

### Slides 4-9: NỘI DUNG CỐT LÕI (1 insight mỗi slide)
Mỗi slide:
- MỘT tiêu đề in đậm (điểm chính) — tối đa 5-10 từ
- 2-4 bullet points hỗ trợ hoặc 2-3 câu ngắn
- Tối đa 50 từ toàn bộ mỗi slide
- Visual hierarchy: tiêu đề lớn, body text nhỏ hơn

Các dạng nội dung:
- **Framework slides**: "Bước 1: [hành động]", "Bước 2: [hành động]"
- **Insight slides**: "[Luận điểm chính]" + bằng chứng hoặc ví dụ
- **Comparison slides**: "Trước: [X] → Sau: [Y]"
- **Checklist slides**: các mục hành động cần kiểm tra

### Slides 10-11: TỔNG HỢP
- Tập hợp các takeaway chính lại
- Một "summary framework" hoặc "one-liner" người đọc có thể ghi nhớ
- Câu "vậy thì sao" — điều này thay đổi cách họ hành động như thế nào?

### Slides 12-13: MINH CHỨNG (tùy chọn nhưng rất mạnh)
- Ví dụ cá nhân áp dụng framework
- Kết quả hoặc số liệu cụ thể (với authority claims phù hợp theo 06-authority.md)
- Tham chiếu từ khách hàng hoặc dự án (ẩn danh nếu cần)

### Slide 14: SLIDE CTA
Các lựa chọn CTA mạnh cho carousel:
- "Save bài này để dùng khi cần" (hiệu quả nhất cho carousel giáo dục)
- "Follow [tên] để xem thêm về [chủ đề]"
- "Nhắn tin '[từ khóa]' để nhận [tài nguyên]"
- "Chia sẻ với một [vai trò cụ thể] cần đọc bài này"

Chỉ một CTA. Làm cho nó cụ thể.

### Slide 15: SLIDE GIỚI THIỆU (tùy chọn)
- Tên, chức danh, 1-2 credentials
- Cách tìm thêm nội dung của bạn
- Tùy chọn: preview chủ đề carousel tiếp theo

---

## Design Brief (dành cho designer hoặc AI tools)

Với mỗi slide, xuất ra:
1. Số thứ tự và loại slide
2. Nội dung văn bản chính xác (tiêu đề + body)
3. Định hướng hình ảnh (hình ảnh/đồ họa nào sẽ bổ sung tốt)

Sau đó xuất ra design brief tổng thể:

```
🎨 DESIGN BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT: [1:1 square (1080x1080) / 4:5 portrait (1080x1350)]
Rationale: [lý do chọn tỷ lệ này cho nội dung này]

COLOR PALETTE:
  Primary: [màu + hex nếu có brand colors]
  Secondary: [màu]
  Background: [màu]
  Text: [màu]

TYPOGRAPHY:
  Headline: [Bold sans-serif khuyến nghị / editorial serif nếu brand yêu cầu]
  Body: [Regular weight, độ tương phản cao với background]
  Min size: 24px (để đọc được trên mobile)

STYLE: [minimal / illustrated / data-viz / photography + text]

MOOD: [professional / warm / bold / academic]

SLIDE-BY-SLIDE VISUAL NOTES:
  Slide 1: [concept hình ảnh cụ thể]
  Slide 4-9: [phong cách iconography hoặc diagram nhất quán]
  Slide 14: [xử lý CTA nổi bật]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Output Format

Xuất ra cả nội dung lẫn design brief:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 CAROUSEL CONTENT — [N] SLIDES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SLIDE 1 (Cover):
  Headline: [tiêu đề]
  Subtext: [tùy chọn]
  Visual: [định hướng hình ảnh]

SLIDE 2 (Problem):
  Headline: [tiêu đề]
  Body: [2-3 dòng]

[...tiếp tục cho tất cả slides...]

SLIDE [N] (CTA):
  CTA: [nội dung]
  Secondary: [hướng dẫn follow/save]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[DESIGN BRIEF — xem format ở trên]

📊 Metadata:
  Slides: [N] | Format: [ratio] | Estimated dwell: [X-Y sec]
  Pillar: [tên pillar] | Hook type: [loại hook]
```
