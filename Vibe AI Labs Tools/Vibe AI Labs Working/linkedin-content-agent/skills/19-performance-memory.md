# Performance Memory — Lớp trí tuệ nội dung

Đọc và ghi lịch sử hiệu suất để việc tạo nội dung ngày càng thông minh hơn. Skill này có ba chế độ: READ (trước khi tạo nội dung), WRITE (sau khi tạo nội dung), và UPDATE (khi có số liệu thực từ LinkedIn).

## Cách dùng
```
/performance-memory           → chế độ READ (hiển thị insights)
/performance-memory write     → chế độ WRITE (ghi bài mới vào log)
/performance-memory update [date] impressions=N dwell=N.NN comments=N
```

---

## Chế độ READ

Được gọi ở đầu mỗi pipeline để định hướng việc tạo nội dung.

### Bước 1: Tải lịch sử
Đọc file `memory/post-history.json`.

Nếu file rỗng hoặc có 0 bài:
```
🧠 Memory: Chưa có lịch sử. Bắt đầu từ đầu.
Vài bài đầu tiên sẽ thiết lập baseline cho bạn — cứ tiếp tục viết.
```

Nếu file đã có bài, tiến hành phân tích.

### Bước 2: Trích xuất insights

**Hiệu suất hook**:
- Nhóm bài theo hook_type (contrarian / number / story / question / other)
- Với mỗi loại: tính dwell_score trung bình
- Xác định loại hook hiệu quả nhất

**Hiệu suất format**:
- Nhóm theo format (text / carousel / newsletter / article / poll / video)
- Với mỗi loại: dwell_score trung bình và comment_depth trung bình
- Xác định format hiệu quả nhất

**Hiệu suất pillar** (nếu trường pillar đã được điền):
- Pillar nào có engagement cao nhất?
- Pillar nào đang đăng ít quá?

**Kiểm tra độ mới** (tránh lặp chủ đề):
- Liệt kê chủ đề trong 14 ngày gần nhất
- Flag nếu có trùng lặp với chủ đề đang lên kế hoạch

**Xu hướng thời gian** (nếu dữ liệu date trải qua nhiều tuần):
- Ngày nào có số bài cao nhất? (tần suất đăng)
- Ghi chú các pattern trong ngày/giờ của bài hiệu quả cao

### Bước 3: Xuất Memory Insights

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 PERFORMANCE MEMORY — INSIGHTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Posts tracked: [N]
Date range: [đầu] → [cuối]

HIỆU QUẢ NHẤT:
  Hook type: [loại] (dwell trung bình: [điểm])
  Format: [format] (dwell trung bình: [điểm])
  Pillar: [pillar] (engagement trung bình)

NÊN TRÁNH HÔM NAY:
  Chủ đề gần đây: [danh sách chủ đề 14 ngày qua]
  Hook dùng quá nhiều: [loại hook dùng 3+ lần trong 7 ngày qua]

GỢI Ý:
  → Dùng hook [loại] — hiệu quả cao nhất của bạn
  → Thử [format] — chưa dùng trong [N] ngày
  → Pillar [tên] đã đến lúc — lần cuối đăng [N] ngày trước
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Chế độ WRITE

Được gọi sau khi nội dung hoàn thiện, trước khi người dùng đăng bài. Thêm bản ghi mới vào post-history.json.

### Định dạng bản ghi mới:
```json
{
  "date": "YYYY-MM-DD",
  "topic": "[chủ đề 2-4 từ được trích xuất]",
  "format": "[text/carousel/newsletter/article/poll/video]",
  "hook_type": "[contrarian/number/story/question/other]",
  "authority_type": "[personal/company]",
  "pillar": "[tên pillar từ 03-pillars.md]",
  "impressions": 0,
  "comment_depth": 0,
  "dwell_score": [điểm từ li-dwell-time-optimizer, hoặc 0 nếu chưa chạy]
}
```

Đọc file `memory/post-history.json` hiện tại, thêm bản ghi mới vào mảng `posts`, rồi ghi lại.

Xác nhận: `✅ Đã ghi bài vào memory. Tổng [N] bài đang theo dõi.`

**Bảo trì**: Nếu mảng posts vượt quá 200 bản ghi, xóa 50 bản cũ nhất (lưu trữ vào `memory/post-history-archive.json` trước).

---

## Chế độ UPDATE

Được gọi khi người dùng cung cấp số liệu LinkedIn thực tế cho bài đã đăng.

Lệnh: `/performance-memory update [date] impressions=1200 dwell=0.73 comments=45`

Quy trình:
1. Tìm bản ghi bài khớp với ngày đã cho
2. Cập nhật các trường: impressions, comment_depth (dùng giá trị comments), dwell_score
3. Nếu giá trị dwell nằm trong khoảng 0 đến 1, lưu nguyên (tỷ lệ). Nếu >1, xem như điểm thô (0-100).
4. Ghi lại vào file
5. Xác nhận: `✅ Đã cập nhật bài từ [date]: impressions=[N], dwell=[N], comments=[N]`

---

## Sức khỏe dữ liệu

Định kỳ (khi được gọi với `/performance-memory health`), kiểm tra:
- Có bao nhiêu bài có 0 impressions? (chưa được cập nhật số liệu thực)
- dwell_score có đang được theo dõi không? (cho thấy dwell-time-optimizer có đang chạy không)
- Đã đủ dữ liệu để có insights có ý nghĩa chưa? (cần ít nhất 10 bài)

Xuất báo cáo health ngắn gọn kèm các khuyến nghị.
