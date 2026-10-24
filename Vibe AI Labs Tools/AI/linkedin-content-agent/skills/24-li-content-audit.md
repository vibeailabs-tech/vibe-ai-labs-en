# Li Content Audit — Kiểm toán Feed

Kiểm toán nội dung LinkedIn hiện có để xác định mất cân đối, thiếu nhất quán và khoảng trống. Chạy hàng tháng hoặc trước khi lên kế hoạch cho giai đoạn nội dung mới.

## Cách dùng
```
/li-content-audit [dán 10-20 bài gần nhất hoặc mô tả]
/li-content-audit [LinkedIn profile URL — sẽ thử scrape nếu truy cập được]
```

---

## Các chiều kiểm toán

### Chiều 1: Pillar Balance
Tải pillars từ brand voice context (03-pillars.md).
Gán mỗi bài đã cung cấp vào một pillar (hoặc "Không khớp").
Tính phần trăm phân phối.

Phân phối mục tiêu: xấp xỉ đều nhau giữa các pillars (±10%).
Flag nếu pillar nào:
- Chiếm trên 50% bài (đăng quá nhiều — độc giả có thể bị nhàm)
- Dưới 10% bài (bị bỏ bê — đang bỏ lỡ cơ hội)
- 0% trong 30 ngày qua (bỏ hẳn — kiểm tra xem có chủ ý không)

### Chiều 2: Tone Consistency
Đọc từng bài và đánh giá tone theo 01-tone.md.
Flag những bài:
- Dùng từ ngữ bị cấm (từ glossary)
- Đổi đại từ xưng hô đột ngột (tôi vs chúng tôi mà không có giải thích)
- Cảm giác khác biệt rõ rệt về văn phong (quá trang trọng/quá thân mật)
- Chứa ngôn ngữ engagement bait

Đánh giá nhất quán tone tổng thể: Strong / Adequate / Inconsistent

### Chiều 3: Authority Signals
Mỗi bài có thiết lập chuyên môn theo cách nào đó không?
Kiểm tra:
- Credibility anchor (theo phong cách trong 06-authority.md)
- Tham chiếu kinh nghiệm cụ thể (dự án, con số, số năm)
- Quan điểm được hỗ trợ bởi bằng chứng (không chỉ là khẳng định)

Bài không có authority signal nào = cơ hội bị bỏ lỡ.
Flag bất kỳ bài nào có thể dễ dàng thêm credibility anchor vào.

### Chiều 4: Format Diversity
Đếm bài theo loại format.
Flag nếu:
- Hơn 60% cùng một format (format fatigue)
- Không có carousel trong 30 ngày qua (format hiệu suất cao nhất đang bị bỏ qua)
- Không có newsletter send trong 4 tuần qua (nếu có newsletter)

### Chiều 5: Hook Pattern Diversity
Phân loại từng loại hook.
Flag nếu:
- Cùng một loại hook được dùng hơn 3 lần trong 7 bài (độc giả thích nghi và ngừng click)
- Tất cả hook đều là câu hỏi (question fatigue)
- Không có hook contrarian nào (đang bỏ lỡ format tạo nhiều tranh luận nhất)

### Chiều 6: CTA Quality and Diversity
Xem lại CTA trong các bài.
Flag nếu:
- Hơn 30% dùng cùng một câu CTA
- CTA chung chung chiếm đa số (kiểu "thoughts?")
- Không có CTA nào mời save (đang bỏ lỡ cơ hội carousel)
- Không có CTA nào mời share (đang bỏ lỡ khuếch đại)

### Chiều 7: Content Freshness Balance
Ước tính tỷ lệ giữa:
- Nội dung evergreen (hữu ích bất cứ lúc nào) vs.
- Nội dung thời sự (news hook, sự kiện, trending)

Mục tiêu: 70% evergreen / 30% thời sự. Feed thiên quá nhiều về thời sự sẽ nhanh lỗi thời.

---

## Phân tích khoảng trống nội dung

Sau khi chạy tất cả các chiều, xác định:
1. Pillar nào đang bị bỏ bê nhất?
2. Format nào chưa được thử hoặc dùng quá ít?
3. Pain point nào của đối tượng (từ 02-audience.md) chưa có bài nào đề cập?
4. Hook type nào chưa được thử gần đây?

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 CONTENT AUDIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Posts audited: [N] | Period: [khoảng thời gian]

SCORECARD:
  Pillar Balance:    [Strong/Adequate/Needs Work]
  Tone Consistency:  [Strong/Adequate/Inconsistent]
  Authority Signals: [Strong/Adequate/Weak]
  Format Diversity:  [Strong/Adequate/Needs Work]
  Hook Diversity:    [Strong/Adequate/Repetitive]
  CTA Quality:       [Strong/Adequate/Generic]
  Content Freshness: [Good mix/Too timely/Too evergreen]

TOP 3 VẤN ĐỀ:
  1. [vấn đề cụ thể + điểm dữ liệu hỗ trợ]
  2. [vấn đề cụ thể + điểm dữ liệu]
  3. [vấn đề cụ thể + điểm dữ liệu]

KHOẢNG TRỐNG NỘI DUNG:
  ▸ Pillar bị bỏ bê: [tên pillar]
  ▸ Format thiếu: [format]
  ▸ Pain point chưa được khai thác: [pain point của đối tượng chưa có bài]
  ▸ Hook type chưa dùng: [loại hook]

GỢI Ý CHO 2 TUẦN TỚI:
  [3-4 ý tưởng nội dung cụ thể giải quyết các khoảng trống hàng đầu]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
