# Li Dwell Time Optimizer — Chấm điểm và cải thiện khả năng giữ chân người đọc

Dwell time — thời gian người đọc dừng lại trên một bài — là tín hiệu xếp hạng mạnh nhất của LinkedIn trong năm 2026. Một bài khiến người đọc đọc hơn 30 giây sẽ vượt trội so với bài có 100 like nhưng bị lướt qua nhanh. Hãy chấm điểm và tối ưu cho tín hiệu này.

## Tại sao Dwell Time quan trọng hơn Like

Thuật toán LinkedIn năm 2026 xếp hạng các tín hiệu theo thứ tự:
1. Dwell time (thời gian đọc) — trọng số cao nhất
2. Comment depth (các cuộc hội thoại qua lại)
3. Shares
4. Reactions (like) — trọng số thấp nhất

Một bài khiến người ta dừng lại và đọc, dù không like, vẫn thắng một bài được like nhưng bị lướt qua.

---

## Chấm điểm Dwell Time (7 chiều)

Chấm điểm từng chiều từ 1-10, sau đó tính tổng có trọng số.

### Chiều 1: Hook Strength (trọng số: 20%)
Dòng đầu tiên có khiến người đọc dừng scroll không?
- 1-3: Mở đầu chung chung, dễ bỏ qua
- 4-6: Thú vị nhưng chưa đủ hút
- 7-9: Cụ thể, dừng scroll được
- 10: Ngay lập tức tạo cảm giác "phải đọc"

### Chiều 2: See-More Pull (trọng số: 20%)
Dòng thứ 3 (vách "see more") có thôi thúc người đọc click không?
- 1-3: Dòng 3 có thể là kết — không có lý do để click thêm
- 4-6: Hơi tò mò về phần tiếp theo
- 7-9: Người đọc CẦN click để giải quyết phần setup còn bỏ ngỏ
- 10: Thôi thúc click như bản năng — setup bỏ lửng hoàn hảo

### Chiều 3: Information Density (trọng số: 15%)
Mỗi dòng có mang giá trị — không có câu đệm, không có padding?
- 1-3: Nhiều câu rỗng có thể cắt bỏ
- 4-6: Có một số câu đệm nhưng phần lớn vẫn có giá trị
- 7-9: Mỗi đoạn đều có đóng góp rõ ràng
- 10: Mỗi câu đều xứng đáng có mặt

### Chiều 4: Reading Pace (trọng số: 15%)
Độ dài câu có thay đổi để giữ mắt người đọc di chuyển không?
- 1-3: Tất cả câu cùng độ dài — đơn điệu
- 4-6: Có một chút biến hóa
- 7-9: Nhịp điệu tự nhiên — câu ngắn mạnh mẽ xen kẽ câu dài hơn
- 10: Nhịp hoàn hảo kéo người đọc đi xuyên suốt bài

### Chiều 5: Visual Breaks (trọng số: 10%)
Khoảng trắng và cấu trúc có ngăn người đọc bỏ cuộc không?
- 1-3: Tường chữ — người đọc từ bỏ ngay về mặt thị giác
- 4-6: Có một số ngắt nhưng vẫn còn dày đặc ở vài chỗ
- 7-9: Nhịp thị giác rõ ràng với khoảng trắng nhất quán
- 10: Dễ dàng vừa lướt vừa đọc cùng lúc

### Chiều 6: Narrative Pull (trọng số: 10%)
Mỗi đoạn có dẫn dắt vào đoạn tiếp theo không? (Có cảm giác phải đọc tiếp không?)
- 1-3: Mỗi đoạn đứng độc lập — không có lực kéo về phía trước
- 4-6: Có kết nối nhất định nhưng còn chỗ hổng
- 7-9: Người đọc cảm giác được dẫn qua một hành trình
- 10: Không thể dừng đọc giữa chừng

### Chiều 7: Ending Reward (trọng số: 10%)
Kết bài / CTA có thỏa mãn — có xứng với phần setup không?
- 1-3: Kết đột ngột, CTA chung chung, người đọc cảm thấy bị hụt hẫng
- 4-6: Kết ổn, CTA chấp nhận được
- 7-9: Phần kết thực hiện đúng lời hứa từ hook
- 10: Kết đáng nhớ, CTA tự nhiên và xứng đáng

---

## Công thức tính điểm

```
Dwell Score = (D1×0.20 + D2×0.20 + D3×0.15 + D4×0.15 + D5×0.10 + D6×0.10 + D7×0.10) × 10
```

Kết quả từ 0-100.

### Diễn giải
- **80-100**: Dwell cao — algorithm nhiều khả năng sẽ boost bài này
- **60-79**: Trung bình — một sửa đổi tốt sẽ đẩy vào tier cao
- **40-59**: Yếu — cần chỉnh sửa đáng kể; xác định các chiều điểm thấp nhất
- **<40**: Nên viết lại — có vấn đề cấu trúc cơ bản

---

## Gợi ý cải thiện

Sau khi chấm điểm, xác định HAI chiều điểm thấp nhất và đưa ra sửa đổi cụ thể:

Điểm Hook Strength thấp → gửi sang li-hook-engineer
Điểm See-More Pull thấp → xác định dòng 3 và viết lại
Điểm Information Density thấp → xác định và cắt các câu đệm
Điểm Reading Pace thấp → viết lại một số câu dài thành 2-3 câu ngắn
Điểm Visual Breaks thấp → chạy qua li-readability-formatter
Điểm Narrative Pull thấp → thêm câu cầu nối ở cuối mỗi đoạn
Điểm Ending Reward thấp → viết lại CTA để trực tiếp phản chiếu lời hứa từ hook

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️ DWELL TIME OPTIMIZER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORES:
  Hook Strength:       [1-10] (×20%)
  See-More Pull:       [1-10] (×20%)
  Information Density: [1-10] (×15%)
  Reading Pace:        [1-10] (×15%)
  Visual Breaks:       [1-10] (×10%)
  Narrative Pull:      [1-10] (×10%)
  Ending Reward:       [1-10] (×10%)

DWELL SCORE: [0-100] → [HIGH/AVERAGE/WEAK/REWRITE]

TOP 2 CẢI THIỆN:
  1. [chiều]: [sửa đổi cụ thể]
  2. [chiều]: [sửa đổi cụ thể]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Truyền dwell_score sang li-review-queue để tính confidence và sang performance-memory để ghi lại.
