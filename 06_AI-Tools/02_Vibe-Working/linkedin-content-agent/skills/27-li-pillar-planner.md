# Li Pillar Planner — Xây dựng hoặc đánh giá Content Pillars

Content pillars là 3–5 chủ đề cốt lõi mà brand của bạn liên tục chiếm lĩnh trên LinkedIn. Chúng tạo ra sự nhận diện, xây dựng authority, và giúp việc lên kế hoạch content trở nên dễ dàng hơn rất nhiều.

## Cách dùng
```
/li-pillar-planner build    → xây pillar từ đầu (tương tác)
/li-pillar-planner review   → đánh giá pillar hiện tại từ 03-pillars.md
/li-pillar-planner test     → kiểm tra pillar hiện tại có sinh đủ ý tưởng content không
```

---

## Chế độ BUILD — Tạo Pillars từ đầu

### Bước 1: Phỏng vấn khám phá (hỏi người dùng các câu hỏi sau)
1. "Khách hàng/người đọc mục tiêu của bạn gặp phải vấn đề gì mà bạn đã tự mình giải quyết được?"
2. "Bạn thường được hỏi nhiều nhất về chủ đề gì — bởi đồng nghiệp, khách hàng, hay trong các buổi phỏng vấn?"
3. "Bạn có thể viết 20+ bài về chủ đề nào mà không bao giờ cạn ý tưởng?"
4. "Bạn muốn được biết đến vì điều gì trong 2 năm tới?"
5. "Giao điểm giữa điều bạn hiểu sâu + điều người đọc cần + điều ít người khác đề cập là gì?"

### Bước 2: Phác thảo 5 pillar ứng viên
Dựa trên câu trả lời, đề xuất 5 ứng viên. Với mỗi pillar:
- Tên (2–4 từ)
- Câu hỏi cốt lõi pillar này trả lời cho người đọc
- Góc nhìn độc đáo của bạn (điều gì làm quan điểm của bạn khác biệt)
- 5 ý tưởng bài mẫu
- Mục tiêu kinh doanh được phục vụ

### Bước 3: Lọc xuống còn 3–5
Áp dụng các bài kiểm tra sau:
- **Bài kiểm tra 20 bài**: Bạn có thể tạo ra 20+ ý tưởng bài từ pillar này không? Nếu không → quá hẹp
- **Bài kiểm tra sự khác biệt**: Pillar này có thực sự khác với các pillar còn lại không? Có chồng lấp không? → gộp hoặc làm sắc nét hơn
- **Bài kiểm tra bền vững**: Bạn có thể đăng đều về chủ đề này trong 12+ tháng không? → cần lõi evergreen
- **Bài kiểm tra độ phù hợp với người đọc**: Pillar này có trực tiếp giải quyết pain point của người đọc từ 02-audience.md không?
- **Bài kiểm tra authority**: Bạn có kinh nghiệm/hiểu biết thực tế để hỗ trợ pillar này không? (tham chiếu 06-authority.md)

### Bước 4: Định nghĩa từng pillar cuối cùng
Output theo định dạng sẵn sàng lưu vào 03-pillars.md:
```
Pillar [N]: [Tên]
Câu hỏi cốt lõi: [vấn đề này giải quyết gì cho người đọc]
Góc nhìn của bạn: [điều gì làm quan điểm của bạn độc đáo]
Mục tiêu kinh doanh: [pillar này giúp đạt được điều gì]
Bài mẫu:
  1. [ý tưởng chủ đề]
  2. [ý tưởng chủ đề]
  3. [ý tưởng chủ đề]
  4. [ý tưởng chủ đề]
  5. [ý tưởng chủ đề]
```

---

## Chế độ REVIEW — Đánh giá Pillars hiện tại

Đọc 03-pillars.md và chạy các kiểm tra sau:

### Kiểm tra 1: Sự khác biệt
Các chủ đề của từng pillar có thực sự khác nhau rõ ràng không? Chạy bài test chồng lấp đơn giản:
- Lấy một ý tưởng bài ngẫu nhiên — nó có thể thuộc 2+ pillar không? (Nếu có → pillars quá gần nhau)
- Nếu chồng lấp cao: khuyến nghị gộp lại hoặc làm sắc nét với góc nhìn riêng cho từng pillar

### Kiểm tra 2: Liên kết với mục tiêu kinh doanh
Mỗi pillar có phục vụ một mục tiêu kinh doanh rõ ràng không?
Ánh xạ từng pillar vào: brand awareness / lead generation / client retention / authority / community building

Nếu một pillar không có mục tiêu kinh doanh rõ ràng, gắn cờ để xem xét lại.

### Kiểm tra 3: Phân bổ content (nếu có lịch sử bài đăng)
Đọc post-history.json và gán từng bài vào pillar tương ứng.
Bài đăng có trải đều qua các pillar không? Hay một pillar đang thống trị?
Pillar nào không có bài nào trong 30 ngày qua?

### Kiểm tra 4: Độ phù hợp với người đọc
Đối chiếu từng pillar với pain points trong 02-audience.md.
Mỗi pillar có giải quyết ít nhất một pain point chính của người đọc không?

### Kiểm tra 5: Độ tươi mới
Các pillar có còn phù hợp với ngành trong năm 2026 không?
Pillar nào đã lỗi thời hoặc quá đông người làm?

Output: scorecard + khuyến nghị cụ thể cho từng pillar.

---

## Chế độ TEST

Tạo 5 ý tưởng bài mới cho từng pillar hiện tại.
Nếu không tạo được 5 ý tưởng khác biệt, không lặp lại → pillar quá hẹp.

Output: danh sách ý tưởng theo từng pillar + kết luận (Mạnh / Hẹp / Cần làm mới).

---

## Định dạng output (REVIEW)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏛️ PILLAR PLANNER — ĐÁNH GIÁ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Với mỗi pillar:]
Pillar: [tên]
  ✓/✗ Sự khác biệt: [kết quả]
  ✓/✗ Mục tiêu kinh doanh: [mục tiêu + độ rõ ràng]
  ✓/✗ Độ phù hợp với người đọc: [pain point nào được giải quyết]
  ✓/✗ Phân bổ content: [% bài đăng / ngày đăng gần nhất]
  Kết luận: [Giữ / Làm sắc nét / Gộp / Thay thế]

SỨC KHOẺ PILLAR TỔNG THỂ: [Mạnh / Cần điều chỉnh / Cần tái cấu trúc lớn]

KHUYẾN NGHỊ:
  1. [hành động cụ thể + lý do]
  2. [hành động cụ thể + lý do]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
