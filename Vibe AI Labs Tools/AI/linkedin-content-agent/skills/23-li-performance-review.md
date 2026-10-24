# Li Performance Review — Phân tích số liệu LinkedIn

Phân tích dữ liệu hiệu suất LinkedIn để hiểu điều gì đang hoạt động và cần thay đổi gì. Input có thể là số liệu người dùng cung cấp thủ công hoặc dữ liệu từ memory/post-history.json.

## Cách dùng
```
/li-performance-review                    → phân tích từ memory file
/li-performance-review [dán số liệu]      → phân tích dữ liệu được cung cấp
/li-performance-review period=30d         → phân tích 30 ngày gần nhất
/li-performance-review period=90d         → phân tích 90 ngày gần nhất
```

---

## Các số liệu cần phân tích

### Số liệu cấp bài đăng
- **Impressions**: Tổng lượt xem. Benchmark: 500-2000 với tài khoản <5K follower; 2000+ với 5K+ follower
- **Engagement rate**: (Reactions + Comments) / Impressions. Benchmark: 2-5% = tốt; >5% = xuất sắc
- **Comment depth**: Comment 1 dòng hay hội thoại nhiều đoạn? Nhiều đoạn = chất lượng cao
- **Dwell time / avg read**: Nếu có từ LinkedIn Analytics — mục tiêu >30 giây
- **Saves**: Saves cao = nội dung có giá trị cao (chỉ số của carousel)
- **Reposts**: Thể hiện insight có thể chia sẻ được

### Số liệu cấp profile/trang
- **Follower growth**: Tăng trưởng mỗi tuần. Đăng đều đặn nên kéo thêm 50-200+ follower mới/tuần
- **Profile views**: Tăng đột biến sau bài viral là bình thường; tăng trưởng bền vững = brand awareness đang được xây dựng
- **Newsletter open rate**: 30-60% = tốt; <20% = vấn đề ở subject line; >60% = xuất sắc

### Tổng hợp cấp nội dung
- Format nào kéo nhiều impressions nhất trung bình?
- Hook type nào kéo comment depth nhiều nhất?
- Pillar nào được save nhiều nhất?

---

## Khung phân tích

### 1. TOP PERFORMERS
3-5 bài hàng đầu theo từng chỉ số là gì? Tìm pattern chung:
- Hook type
- Format
- Thời điểm đăng
- Pillar
- Cấu trúc nội dung (story vs. framework vs. opinion)

### 2. BÀI HIỆU SUẤT KÉM
3-5 bài thấp nhất là gì? Tại sao chúng có thể kém hiệu quả?
- Hook quá mơ hồ?
- Chủ đề không liên quan đến đối tượng?
- Sai format cho nội dung đó?
- Đăng vào giờ không tối ưu?

### 3. PHÂN TÍCH XU HƯỚNG
Hiệu suất đang cải thiện, giảm sút hay đi ngang trong giai đoạn này?
Tính toán:
- Impressions trung bình: giai đoạn này vs. giai đoạn trước
- Xu hướng engagement rate
- Xu hướng tốc độ tăng follower

### 4. PHÁT HIỆN BẤT THƯỜNG
Bài nào hiệu suất cao hoặc thấp hơn đáng kể so với trung bình?
Với mỗi bất thường: đề xuất giả thuyết về nguyên nhân (và cách nhân rộng thành công hoặc tránh thất bại).

### 5. SO SÁNH FORMAT
Lập bảng đơn giản:
| Format | Avg Impressions | Avg Engagement Rate | Avg Comment Depth | Verdict |
|--------|----------------|--------------------|--------------------|---------|

### 6. KHUYẾN NGHỊ
Dựa trên dữ liệu, đưa ra đúng 3 khuyến nghị cụ thể và có thể hành động cho giai đoạn tiếp theo:
- Một về format/loại nội dung
- Một về hook hoặc hướng tiếp cận nội dung
- Một về tần suất đăng hoặc thời điểm

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 PERFORMANCE REVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Period: [khoảng thời gian] | Posts analyzed: [N]

TỔNG QUAN:
  Avg impressions: [N] | Trend: [↑/↓/→ X%]
  Avg engagement rate: [%] | Benchmark: [trên/dưới/đạt]
  Follower growth: [+N trong giai đoạn này]
  Newsletter open rate: [% nếu có]

TOP 3 HIỆU QUẢ NHẤT:
  1. "[chủ đề/ngày]" — [chỉ số chính] — Tại sao hiệu quả: [giả thuyết]
  2. "[chủ đề/ngày]" — [chỉ số chính] — Tại sao hiệu quả: [giả thuyết]
  3. "[chủ đề/ngày]" — [chỉ số chính] — Tại sao hiệu quả: [giả thuyết]

BÀI KÉM HIỆU QUẢ:
  1. "[chủ đề/ngày]" — [chỉ số chính] — Nguyên nhân có thể: [giả thuyết]

SO SÁNH FORMAT:
  [bảng]

XU HƯỚNG: [cải thiện/giảm sút/đi ngang] — [phân tích 1-2 câu]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3 KHUYẾN NGHỊ CHO GIAI ĐOẠN TIẾP THEO:
  1. [khuyến nghị format/loại + lý do]
  2. [khuyến nghị hook/nội dung + lý do]
  3. [khuyến nghị thời điểm/tần suất + lý do]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
