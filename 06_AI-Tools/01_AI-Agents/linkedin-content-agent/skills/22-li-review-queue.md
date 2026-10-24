# Li Review Queue — HITL: Định tuyến theo điểm tin cậy

Tính điểm tin cậy tổng thể cho nội dung và định tuyến tương ứng. Điểm cao = tự động phê duyệt. Điểm thấp = cần người xem xét hoặc viết lại.

## Tính điểm tin cậy

Thu thập điểm từ các bước pipeline đã chạy:

### Yếu tố 1: Brand Voice Match (trọng số: 25%)
Bài đăng khớp với brand voice đã tải đến mức nào?
- Kiểm tra tone theo 01-tone.md: phong cách viết có đúng không?
- Kiểm tra từ ngữ: có từ bị cấm nào từ glossary không?
- Kiểm tra đại từ xưng hô: có khớp với authority type đã chọn không?
- Điểm 0-100

### Yếu tố 2: Hook Strength (trọng số: 20%)
Dùng điểm từ li-hook-engineer nếu đã chạy, hoặc đánh giá lại:
- 80-100: Mạnh (contrarian/số cụ thể/story, dưới 150 ký tự, không có cliché)
- 50-79: Đủ dùng (cụ thể nhưng chưa dừng scroll được)
- 0-49: Yếu (mơ hồ, cliché, hoặc quá dài)

### Yếu tố 3: Policy Compliance (trọng số: 25%)
Dùng kết quả từ li-policy-checker:
- PASS → 100
- NEEDS_REVISION → 50
- FAIL → 0

### Yếu tố 4: Dwell Score (trọng số: 15%)
Dùng điểm từ li-dwell-time-optimizer nếu đã chạy:
- ≥80 → đóng góp 100 vào confidence
- 60-79 → 75
- 40-59 → 50
- <40 → 25

### Yếu tố 5: Pillar Alignment (trọng số: 15%)
Bài này có phục vụ rõ ràng một trong các pillar đã định nghĩa không?
- Phục vụ rõ ràng một pillar → 100
- Có thể gắn vào một pillar nhưng lỏng lẻo → 60
- Không khớp rõ ràng với pillar nào → 20

### Điểm tin cậy tổng thể
```
Confidence = (F1×0.25) + (F2×0.20) + (F3×0.25) + (F4×0.15) + (F5×0.15)
```

---

## Logic định tuyến

### ≥90: TỰ ĐỘNG PHÊ DUYỆT ✅
Xuất nội dung ngay với nhãn đã phê duyệt.
Không cần người xem xét.

### 70-89: NÊN XEM XÉT 🔶
Hiển thị nội dung kèm:
- Danh sách những gì cần kiểm tra lại (các yếu tố điểm thấp nhất)
- Câu hỏi cụ thể cần xác nhận trước khi đăng
- Tùy chọn phê duyệt ngay ("đăng như hiện tại") hoặc yêu cầu cải thiện

Định dạng checklist cho người xem xét:
```
🔶 NÊN XEM XÉT — [điểm]% tin cậy

Hãy kiểm tra trước khi đăng:
  □ [yếu tố thấp nhất 1]: [mối lo ngại cụ thể]
  □ [yếu tố thấp nhất 2]: [mối lo ngại cụ thể]

Để đạt trên 90%: [cần cải thiện gì]

→ Phê duyệt và đăng? hoặc → Yêu cầu chỉnh sửa?
```

### <70: TỪ CHỐI VÀ VIẾT LẠI ❌
KHÔNG xuất bài cuối. Thay vào đó:
- Hiển thị phân tích điểm confidence
- Xác định yếu tố điểm thấp nhất
- Tự động kích hoạt skill xử lý vấn đề đó:
  - Hook thấp → chạy lại li-hook-engineer
  - Policy thấp → chạy lại li-policy-checker với các vấn đề cụ thể
  - Brand voice thấp → chỉ ra sự không khớp cụ thể và hỏi hướng xử lý
  - Dwell thấp → chạy lại li-dwell-time-optimizer với các gợi ý sửa
  - Pillar thấp → hỏi người dùng bài này phục vụ pillar nào

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👥 REVIEW QUEUE — ĐỊNH TUYẾN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHÂN TÍCH ĐIỂM TIN CẬY:
  Brand Voice Match: [điểm]/100 (×25%)
  Hook Strength:     [điểm]/100 (×20%)
  Policy Compliance: [điểm]/100 (×25%)
  Dwell Score:       [điểm]/100 (×15%)
  Pillar Alignment:  [điểm]/100 (×15%)

TỔNG THỂ: [điểm]%
ĐỊNH TUYẾN: [✅ AUTO / 🔶 REVIEW / ❌ REJECT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Khối output theo từng hướng định tuyến — xem phần trên]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
