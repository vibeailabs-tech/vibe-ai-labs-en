# Li Send Time Optimizer — Thời điểm đăng bài tối ưu

Gợi ý ngày và giờ đăng bài tốt nhất cho loại nội dung cụ thể này để đạt lượt tiếp cận tối đa với đối tượng mục tiêu.

## Baseline: Đối tượng chuyên nghiệp Việt Nam (GMT+7)

Khung giờ tối ưu cho LinkedIn B2B tại Việt Nam, dựa trên dữ liệu nghiên cứu:

| Ngày | Khung giờ tốt nhất | Ghi chú |
|------|-------------------|---------|
| Thứ Hai | 8:00-9:30 sáng | Tâm thế đầu tuần, intent cao |
| Thứ Ba | 7:30-8:30 sáng, 12:00-1:00 trưa | Ngày mạnh nhất nhìn chung |
| Thứ Tư | 7:30-8:30 sáng, 12:00-1:00 trưa | Mạnh thứ hai — đà giữa tuần |
| Thứ Năm | 8:00-9:00 sáng, 5:00-6:30 chiều | Tốt cho thought leadership |
| Thứ Sáu | 8:00-9:00 sáng (chỉ buổi sáng) | Buổi chiều giảm mạnh |
| Thứ Bảy | 9:00-11:00 sáng | Reach thấp hơn nhưng founder/freelancer thường online |
| Chủ Nhật | Tránh | Engagement chuyên nghiệp rất thấp |

**Khung sáng** (7:30-9:30 sáng): Lướt trước giờ làm trên xe buýt hoặc với cà phê — intent đọc cao nhất.
**Khung trưa** (12:00-1:00 trưa): Đọc nhanh giờ nghỉ — phù hợp nội dung ngắn và mạnh mẽ.
**Khung chiều tối** (5:00-6:30 chiều): Thư giãn sau giờ làm — phù hợp bài kể chuyện và nội dung nhẹ nhàng hơn.

---

## Điều chỉnh theo loại nội dung

Áp dụng thêm vào baseline trên:

**Newsletter**: Chỉ sáng Thứ Ba hoặc Thứ Tư. Không bao giờ phát hành vào Thứ Sáu.

**Poll**: Thứ Hai 8:00 sáng. Cho 7 ngày chạy xuyên suốt chu kỳ tuần làm việc.

**Thought leadership / bài quan điểm**: Sáng Thứ Ba-Tư.

**How-to thực hành / framework**: Bất kỳ khung sáng nào trong giờ cao điểm. Trưa Thứ Tư cũng tốt (người ta hành động theo trong buổi chiều).

**Story / bài founder**: Sáng Thứ Năm hoặc Thứ Sáu (nội dung cảm xúc phù hợp tâm trạng cuối tuần).

**Carousel PDF**: Sáng Thứ Ba-Tư (lưu bài diễn ra trong lúc đọc tập trung).

**Phản ứng với trending topic / tin tức**: Đăng càng sớm càng tốt sau sự kiện. Với nội dung thời sự, tốc độ quan trọng hơn thời điểm tối ưu.

---

## Điều chỉnh theo lịch sử

Kiểm tra `memory/post-history.json` để tìm pattern:
- Có ngày nào impressions tăng vọt không? Ghi nhận ngày/giờ đó.
- Có ngày nào liên tục hiệu suất kém không?
- Ngày/giờ nào 3 bài có dwell_score cao nhất được đăng?

Nếu đã theo dõi từ 10+ bài, cân bằng 50% dữ liệu lịch sử và 50% baseline.
Nếu <10 bài, dựa chủ yếu vào khuyến nghị baseline.

---

## Kiểm tra độ khẩn cấp

Nếu nội dung có tính thời sự (hook tin tức, gắn với sự kiện, trending topic):
```
⚡ KHẨN: Nội dung này có giới hạn thời gian.
Khuyến nghị: Đăng trong vòng [X tiếng] để nắm bắt cửa sổ relevance.
Khung tối ưu trong giới hạn khẩn cấp: [giờ cụ thể]
```

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ SEND TIME OPTIMIZER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Content type: [loại nội dung]
Audience: Chuyên nghiệp Việt Nam (GMT+7)

KHUNG GIỜ CHÍNH:
  [Ngày], [giờ] GMT+7
  Lý do: [1-2 câu giải thích]

KHUNG GIỜ DỰ PHÒNG:
  [Ngày], [giờ] GMT+7
  Dùng khi: [điều kiện]

NÊN TRÁNH:
  [Ngày/giờ cần tránh và lý do]

[Nếu có dữ liệu lịch sử:]
Lịch sử: Bài [format] của bạn đạt reach cao hơn trung bình [X]% khi đăng vào [ngày/giờ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
