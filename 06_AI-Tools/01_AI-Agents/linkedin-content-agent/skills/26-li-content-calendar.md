# Li Content Calendar — Lên kế hoạch nội dung

Xây dựng lịch content có cấu trúc cho 1 tuần hoặc 1 tháng. Tích hợp luân phiên pillar, đa dạng format, tối ưu giờ đăng và lịch sử chủ đề gần đây.

## Cách dùng
```
/li-content-calendar week         → kế hoạch 1 tuần
/li-content-calendar month        → kế hoạch 1 tháng
/li-content-calendar week [theme] → kế hoạch tuần theo một chủ đề
/li-content-calendar month [goal] → kế hoạch tháng hướng đến một mục tiêu cụ thể
```

---

## Trước khi lên lịch

### Tải context:
1. Brand voice context (pillars từ 03-pillars.md)
2. Lịch sử bài đăng (memory/post-history.json) — tránh lặp chủ đề trong vòng 14 ngày qua
3. Tần suất đăng bài mục tiêu (từ 06-authority.md nếu có, mặc định: 3 lần/tuần)
4. Bất kỳ sự kiện, chiến dịch, hoặc chủ đề thời sự nào người dùng đề cập

### Ràng buộc:
- Không lặp cùng chủ đề trong vòng 14 ngày
- Không dùng cùng loại hook 3 bài liên tiếp
- Không dùng cùng format 4 bài liên tiếp
- Mỗi tuần phải có ít nhất 2 pillar khác nhau

---

## Template tuần (3 bài)

Phân bổ mặc định:
- **Thứ Hai buổi sáng**: Thought leadership hoặc ý kiến trái chiều (pillar có authority signal mạnh nhất)
- **Thứ Tư buổi sáng**: Framework thực chiến, how-to, hoặc carousel (ngày có tỷ lệ chia sẻ cao nhất)
- **Thứ Sáu buổi sáng**: Câu chuyện, case study, hoặc bài học rút ra (nội dung cảm xúc/suy ngẫm)

Với 5 bài/tuần: thêm poll hoặc bài tương tác vào Thứ Ba, tip chiến thuật vào Thứ Năm.

---

## Template tháng (12–15 bài)

### Tuần 1: Thiết lập & Giáo dục
- Bài 1 (Thứ Hai): Pillar 1 — khái niệm nền tảng hoặc framework
- Bài 2 (Thứ Tư): Pillar 2 — tip thực chiến (carousel là lý tưởng)
- Bài 3 (Thứ Sáu): Câu chuyện gắn với chủ đề cốt lõi

### Tuần 2: Tương tác & Tranh luận
- Bài 4 (Thứ Hai): Ý kiến trái chiều về chuẩn mực ngành
- Bài 5 (Thứ Tư): Poll — câu hỏi thật sự về ngành
- Bài 6 (Thứ Sáu): Case study (thực tế hoặc đã ẩn danh)

### Tuần 3: Bằng chứng & Xác tín xã hội
- Bài 7 (Thứ Hai): Quan sát có số liệu hỗ trợ
- Bài 8 (Thứ Tư): Framework chuyên sâu (carousel)
- Bài 9 (Thứ Sáu): Bài học từ thất bại hoặc sai lầm

### Tuần 4: Chuyển đổi & Tập trung CTA
- Bài 10 (Thứ Hai): Thought leadership — luận điểm lớn
- Bài 11 (Thứ Tư): Gửi newsletter (nếu có)
- Bài 12 (Thứ Sáu): Bài suy ngẫm + CTA rõ ràng hơn (follow, DM, subscribe)

---

## Định dạng lịch

Output ra bảng với các cột sau:
| Ngày | Thứ | Giờ (GMT+7) | Format | Pillar | Ý tưởng chủ đề | Góc hook | Ghi chú |

Điền đầy đủ cho từng bài đã lên kế hoạch. Đánh dấu "NEWSLETTER SEND" vào tuần có gửi newsletter.

---

## Tạo ý tưởng chủ đề

Với mỗi slot trống, tạo một ý tưởng chủ đề cụ thể dựa trên:
1. Pillar nào cần được phủ (kiểm tra cân bằng)
2. Format nào phù hợp (dựa vào loại chủ đề)
3. Góc hook nào chưa dùng gần đây

Định dạng ý tưởng: "[Loại hook]: [góc bài cụ thể]"
Ví dụ: "Contrarian: Tại sao họp 1-1 hàng tuần với team đang lãng phí thời gian của tất cả mọi người"

---

## Định dạng output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 CONTENT CALENDAR — [TUẦN/THÁNG]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kỳ: [ngày bắt đầu] → [ngày kết thúc]
Tần suất đăng: [N] lần/tuần
Pillars phủ: [danh sách]

| Ngày | Thứ | Giờ | Format | Pillar | Chủ đề | Hook | Ghi chú |
|------|-----|-----|--------|--------|--------|------|---------|
[các dòng cho từng bài đã lên kế hoạch]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHỦ ĐỀ DỰ PHÒNG (3 bài bổ sung phòng khi cần thay):
  1. [chủ đề + format]
  2. [chủ đề + format]
  3. [chủ đề + format]

CƠ HỘI THỜI SỰ:
  [Sự kiện, ngày quan trọng trong ngành, hoặc xu hướng có thể gắn content trong kỳ này]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
