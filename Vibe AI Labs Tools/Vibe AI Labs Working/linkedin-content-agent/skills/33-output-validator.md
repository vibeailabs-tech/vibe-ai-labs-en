# Output Validator — Cổng kiểm soát chất lượng cuối cùng

Chạy kiểm tra 11 điểm cuối cùng trên toàn bộ output trước khi giao cho người dùng. Đây là cổng cuối trong mọi pipeline. Chặn output nếu bất kỳ kiểm tra critical nào thất bại.

## Danh sách kiểm tra 11 điểm

### CRITICAL (phải pass — chặn nếu có điểm nào thất bại)

**Kiểm tra 1: POLICY**
li-policy-checker đã được chạy chưa? Kết quả có là PASS không?
- Nếu chưa chạy: chạy ngay bây giờ
- Nếu NEEDS_REVISION hoặc FAIL: chặn output và xử lý vấn đề trước
- Điều kiện pass: kết quả policy-checker = PASS

**Kiểm tra 2: GIỌNG ĐIỆU BRAND VOICE**
Bài đăng có khớp với hướng dẫn tone trong 01-tone.md không?
- Kiểm tra: đại từ đúng (tôi/chúng tôi)?
- Kiểm tra: không có từ vựng bị cấm từ 05-glossary.json?
- Kiểm tra: cấu trúc câu khớp với hướng dẫn tone?
- Kiểm tra: không có cách mở đầu sáo rỗng trong danh sách tránh?
- Điều kiện pass: tone nhất quán với brand voice xuyên suốt

**Kiểm tra 3: KHỚP AUTHORITY**
Giọng văn có khớp với loại authority đã chọn trong li-voice-router không?
- personal được chọn → bài dùng "tôi", hook câu chuyện cá nhân, chỉ claim dựa trên kinh nghiệm
- company được chọn → bài dùng "chúng tôi", dẫn dắt bằng dữ liệu, claim phù hợp với công ty
- Kiểm tra: có claim nào vi phạm danh sách cannot_claim từ 06-authority.md không?
- Điều kiện pass: loại authority nhất quán, không có claim bị cấm

**Kiểm tra 4: KHỚP PILLAR**
Bài đăng có rõ ràng phục vụ ít nhất một content pillar được định nghĩa từ 03-pillars.md không?
- Xác định pillar nào bài này phục vụ
- Nếu không khớp pillar nào: gắn cờ để người dùng xác nhận (tiếp tục với cảnh báo, không chặn)
- Điều kiện pass: xác định được pillar khớp rõ ràng

---

### IMPORTANT (nên pass — gắn cờ nếu thất bại, nhưng không chặn)

**Kiểm tra 5: CHẤT LƯỢNG HOOK**
Hook có cụ thể, đủ sức dừng thumb lại, và dưới 150 ký tự không?
- Cụ thể (số / tên / ngày / luận điểm)?
- Không có cách mở đầu sáo rỗng?
- Dưới 150 ký tự?
- Điểm: STRONG / ADEQUATE / WEAK

**Kiểm tra 6: ĐỊNH DẠNG**
Bài đăng có được định dạng đúng không?
- Đoạn văn ≤ 2 dòng?
- Dòng trống giữa các đoạn?
- Không dùng markdown bold/italic?
- Không quá nhiều emoji?
- Điểm: CLEAN / NEEDS_CLEANUP

**Kiểm tra 7: CHẤT LƯỢNG CTA**
Có đúng một CTA không? CTA có cụ thể không?
- Một CTA (không phải hai, không phải không có)?
- Câu hỏi hoặc hành động cụ thể (không chung chung)?
- Điểm: STRONG / GENERIC / MISSING

**Kiểm tra 8: DWELL SCORE**
Dwell score đã được tính chưa? Có ≥60 không?
- Nếu li-dwell-time-optimizer đã chạy: dùng điểm đó
- Nếu chưa chạy: ước tính từ các tín hiệu chất lượng rõ thấy
- Điểm: ≥80 EXCELLENT / 60–79 ADEQUATE / <60 LOW

---

### ADVISORY (best practice — ghi chú nếu thiếu, không gắn cờ)

**Kiểm tra 9: GIỜ ĐĂNG**
Đã có khuyến nghị giờ đăng chưa?
- Trạng thái: PROVIDED / NOT PROVIDED

**Kiểm tra 10: VISUAL BRIEF**
Đã có visual brief nếu bài có hoặc được hưởng lợi từ ảnh không?
- Bài chỉ có text: NOT NEEDED
- Bài có ảnh/carousel: NEEDED / PROVIDED / NOT PROVIDED

**Kiểm tra 11: FIRST COMMENT**
Đã chuẩn bị chiến lược first comment chưa?
- Trạng thái: PROVIDED / NOT PROVIDED

---

## Chấm điểm và Điều hướng

**Tất cả 4 kiểm tra CRITICAL pass**: Tiến hành output.
**Bất kỳ kiểm tra CRITICAL nào thất bại**: Chặn output, hiển thị kiểm tra nào thất bại, kích hoạt sửa.
**Kiểm tra IMPORTANT thất bại**: Hiển thị trong output kèm cảnh báo — người dùng có thể chọn override.
**Mục ADVISORY thiếu**: Ghi chú trong output — người dùng có thể thêm nếu muốn.

---

## Lắp ráp Output cuối cùng

Khi tất cả kiểm tra critical pass, lắp ráp output cuối cùng:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ OUTPUT ĐÃ ĐƯỢC XÁC NHẬN — SẴN SÀNG ĐĂNG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 BÀI ĐĂNG:
─────────────────────────────────────────────
[Toàn bộ nội dung bài — copy và paste trực tiếp]
─────────────────────────────────────────────

💬 FIRST COMMENT:
─────────────────────────────────────────────
[Nội dung first comment — đăng trong vòng 60 giây sau khi publish]
─────────────────────────────────────────────

🎨 VISUAL BRIEF:
[Visual brief HOẶC "Bài chỉ có text — không cần ảnh"]

⏰ GIỜ ĐĂNG: [Ngày, giờ, GMT+7]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 BÁO CÁO CHẤT LƯỢNG
  Độ tự tin: [điểm]%
  Kiểm tra pass: [N/11]
  Policy: ✅ PASS
  Brand voice: ✅ PASS
  Authority: ✅ PASS
  Pillar: ✅ [tên pillar]
  Hook: [STRONG/ADEQUATE/WEAK]
  Format: [CLEAN/NEEDS_CLEANUP]
  CTA: [STRONG/GENERIC]
  Dwell score: [điểm]/100

📋 PIPELINE ĐÃ CHẠY:
  [Danh sách các skill đã chạy theo thứ tự]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Khi kiểm tra Critical thất bại

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ OUTPUT BỊ CHẶN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kiểm tra thất bại: [tên kiểm tra]
Vấn đề: [mô tả cụ thể]
Sửa cần thiết: [cần thay đổi gì]

Để tiếp tục: [hành động cụ thể cần thực hiện]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
