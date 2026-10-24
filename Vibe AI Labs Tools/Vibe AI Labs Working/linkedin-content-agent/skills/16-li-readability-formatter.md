# Li Readability Formatter — Format Để Đọc Dễ Tối Đa

Format bài post sao cho dễ đọc trên mobile, duy trì nhịp điệu, và tạo "see more" cliff đúng lúc. Dù nội dung hay đến đâu vẫn thất bại nếu hiển thị như một khối văn bản dày đặc.

## Thực Tế Formatting Trên LinkedIn

- Hơn 80% lượt đọc LinkedIn diễn ra trên mobile
- Người dùng scan trước khi đọc — cấu trúc hình ảnh quyết định họ có bắt đầu đọc không
- Nút "xem thêm" của LinkedIn xuất hiện sau khoảng 3 dòng text
- Phần trước "xem thêm" là cực kỳ quan trọng — nó phải thúc đẩy người dùng click
- LinkedIn KHÔNG render markdown: không có **in đậm**, không có *in nghiêng*, không có # headers trong post

---

## Quy Tắc Formatting

### Quy tắc 1: Độ dài đoạn văn
Tối đa 2 dòng mỗi đoạn. Nếu một đoạn có 3+ dòng, hãy tách ra.

Tại sao: Trên mobile, 2 dòng = đơn vị đọc thoải mái. 3+ dòng = bức tường đáng sợ.

### Quy tắc 2: Dòng trống giữa các đoạn
Mỗi đoạn phải được theo sau bởi một dòng trống.

Tại sao: Khoảng trắng cho mắt nghỉ ngơi và báo hiệu "sắp có ý mới."

### Quy tắc 3: "See more" cliff (dòng 3)
LinkedIn hiển thị khoảng 3 dòng trước khi cắt bằng "xem thêm."

Dòng 3 phải là một trong số:
- Một suy nghĩ chưa hoàn chỉnh đòi hỏi được hoàn thành
- Một phát biểu bất ngờ đòi hỏi được giải thích
- Một số liệu hoặc luận điểm cụ thể đặt ra câu hỏi
- Một dòng thiết lập đặt tên cho vấn đề người đọc đang gặp ngay lúc này

Kiểm tra: bạn có click "xem thêm" sau khi đọc 3 dòng đầu không?

### Quy tắc 4: Không markdown
Xóa bất kỳ:
- Định dạng **in đậm** → chỉ viết từ bình thường
- Định dạng *in nghiêng* → chỉ viết từ bình thường
- # Headers → không được render, trông như hashtag bị hỏng
- --- dividers → không được render

Ngoại lệ: emoji được render đúng nếu brand voice cho phép.

### Quy tắc 5: Bullet points
Dùng ▸ hoặc — thay vì • hoặc - (render nhất quán hơn trên các thiết bị).
Mỗi bullet trên một dòng riêng. Dòng trống trước và sau danh sách.

### Quy tắc 6: Sử dụng emoji
Kiểm tra brand voice context để biết chính sách emoji.
Quy tắc mặc định: tối đa 0-2 emoji. Không bao giờ dùng emoji thay bullet (danh sách kiểu 🔴 🟡 🟢 trông như spam).

### Quy tắc 7: Tách biệt CTA
CTA cuối cùng cần:
- Trên một dòng riêng (dòng trống trước nó)
- Một câu, không phải một đoạn
- Không theo sau bởi hashtags (hashtags để trong first comment)

### Quy tắc 8: Kết thúc bài post
KHÔNG kết thúc bằng một chuỗi hashtags trong phần thân bài. Chuyển chúng sang first comment.
Thứ cuối cùng trong bài phải là CTA — gọn gàng, không lộn xộn.

---

## Quy Trình Formatting

1. Đọc bài post hiện tại
2. Kiểm tra dòng 3 — có phải là cliff hấp dẫn không? Nếu không, tái cấu trúc cho đến khi đạt
3. Tách các đoạn dài hơn 2 dòng
4. Thêm dòng trống giữa tất cả các đoạn
5. Xóa tất cả cú pháp markdown
6. Chuyển đổi bullets thành ▸ hoặc —
7. Kiểm tra số lượng emoji theo brand voice
8. Chuyển hashtags vào ghi chú cho first-comment-strategy
9. Tách biệt CTA trên một dòng riêng

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📐 READABILITY FORMATTER — KẾT QUẢ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Thay đổi đã thực hiện:
  • [thay đổi 1]
  • [thay đổi 2]

"See more" cliff check: [PASS/FAIL — dòng 3 nói gì]

BÀI POST ĐÃ FORMAT:
─────────────────
[toàn bộ nội dung bài đã format, chính xác như sẽ hiển thị trên LinkedIn]
─────────────────
Hashtags chuyển sang first comment: [#tag1 #tag2 #tag3]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
