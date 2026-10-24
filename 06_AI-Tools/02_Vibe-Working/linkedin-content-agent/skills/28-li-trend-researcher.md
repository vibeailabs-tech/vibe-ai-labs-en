# Li Trend Researcher — Tìm kiếm chủ đề đang trending

Nghiên cứu các chủ đề đang trending trong ngành của người dùng và lọc qua lăng kính brand voice để tìm ra những cơ hội content tốt nhất.

## Cách dùng
```
/li-trend-researcher              → nghiên cứu dựa trên brand voice context
/li-trend-researcher [industry]   → override với ngành cụ thể
/li-trend-researcher [topic]      → nghiên cứu trend trong một chủ đề cụ thể
```

---

## Quy trình nghiên cứu

### Bước 1: Xác định ngành và chủ đề từ brand voice
Đọc brand voice context:
- Ngành/niche là gì? (từ 02-audience.md và 03-pillars.md)
- Phân khúc người đọc là gì? (startup founders, PM, v.v.)
- Các content pillar là gì? (để lọc trend phù hợp)

### Bước 2: Tìm kiếm web để nắm trend hiện tại
Dùng web search để tìm các cuộc thảo luận đang trending gần đây (30 ngày qua):

Các câu query cần chạy:
1. "[industry] LinkedIn trending [tháng năm hiện tại]"
2. "top [industry] discussions [tháng hiện tại]"
3. "[primary pillar topic] debate [năm hiện tại]"
4. "[industry] controversy OR debate OR opinion [tháng hiện tại]"
5. "[audience role] LinkedIn viral [tháng hiện tại]"

Cũng kiểm tra thêm:
- Các báo cáo nghiên cứu hoặc nghiên cứu mới nhất trong ngành
- Hội nghị hoặc sự kiện diễn ra trong tháng này (cơ hội tie-in thời sự)
- Tin tức ngành hoặc thông báo lớn từ các công ty
- Báo cáo học thuật hoặc phân tích được phát hành gần đây

### Bước 3: Lọc theo độ phù hợp brand voice
Với mỗi trend tìm được, chạy các bộ lọc sau:

**Bộ lọc độ liên quan**: Chủ đề này có khớp với ít nhất 1 content pillar không?
- Liên quan cao (chủ đề cốt lõi của pillar) → ưu tiên 1
- Liền kề với pillar → ưu tiên 2
- Thú vị nhưng ngoài pillar → ưu tiên 3

**Bộ lọc sự khác biệt**: Bạn có thể mang đến góc nhìn độc đáo không?
- Mọi người đang nói cùng một điều → chỉ tiến hành nếu bạn có quan điểm phản biện thực sự
- Chủ đề có tính phân cực → lý tưởng cho góc nhìn trái chiều
- Nghiên cứu/dữ liệu mới → lý tưởng cho kiểu "đây là ý nghĩa thực sự với [người đọc]"

**Bộ lọc authority**: Bạn có kinh nghiệm hoặc insight thực tế để bổ sung không? (kiểm tra 06-authority.md)
- Có thể claim dựa trên kinh nghiệm thực tế → tiến hành
- Chỉ có thể nhắc lại quan điểm của người khác → ưu tiên thấp hơn (thêm góc cá nhân hoặc bỏ qua)

**Bộ lọc độ bền**: Câu chuyện một tuần hay cuộc trò chuyện kéo dài nhiều tuần?
- Tin tức nóng → đăng trong vòng 24–48h hoặc bỏ qua
- Tranh luận rộng hơn → có thể đăng trong tuần này
- Xu hướng dài hạn → có thể xây thành chuỗi bài

### Bước 4: Tạo concept bài đăng
Với 2–3 trend hàng đầu, tạo brief concept bài đăng:
- Hướng headline/hook
- Góc nhìn độc đáo của bạn
- Khuyến nghị format
- Cửa sổ thời gian phù hợp (chủ đề này còn timely bao lâu?)

---

## Định dạng output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 TREND RESEARCHER — [Ngành]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ngày nghiên cứu: [hôm nay]
Ngành: [ngành đã xác định]

TREND TÌM ĐƯỢC: [N]

[Với mỗi trend:]
━━ Trend [N] ━━
Chủ đề: [tên]
Lý do trending: [giải thích ngắn]
Độ phù hợp pillar: [tên pillar hoặc "liền kề"]
Có góc nhìn độc đáo: [có/không + là gì]
Cửa sổ thời gian: [X ngày/tuần]
Ưu tiên: [1/2/3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOP 2 ĐỂ ƯU TIÊN TUẦN NÀY:

LỰA CHỌN 1: [chủ đề]
  Hướng hook: "[hook đề xuất]"
  Format: [format khuyến nghị]
  Góc của bạn: [điều gì làm góc nhìn của bạn khác biệt]
  Đăng trước: [ngày — cửa sổ khẩn cấp]

LỰA CHỌN 2: [chủ đề]
  Hướng hook: "[hook đề xuất]"
  Format: [format khuyến nghị]
  Góc của bạn: [điều gì làm góc nhìn của bạn khác biệt]
  Đăng trước: [ngày]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
