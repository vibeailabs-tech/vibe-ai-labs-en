# [26] Skill: fb-policy-checker

## Mục đích
Gate kiểm duyệt: FB Community Standards + Ad Policies + luật VN 2026.
Block = không qua review queue, bắt rewrite bắt buộc — không bypass.

## Input
- `post_content`: bài cần kiểm tra
- `post_type`: organic / paid_ad
- `industry`: general / cosmetics / supplement / finance / healthcare / weightloss
- `brand_voice`: context từ brand-voice-loader (lấy `banned_terms`)

## Rule modules

### Module 1: FB General Policy
Scan cho các vi phạm phổ biến:

| Pattern | Mức độ | Thay thế |
|---------|--------|---------|
| "đảm bảo", "cam kết", "chắc chắn" | Flag | "có thể giúp bạn", "nhiều người đã..." |
| "100%", "tuyệt đối", "hoàn toàn" | Flag | "phần lớn", "hầu hết", "trong nhiều trường hợp" |
| Before/after ngầm ý y tế | Flag → Block nếu ngành nhạy cảm | Mô tả trải nghiệm, không kết quả |
| Từ y khoa: "điều trị", "chữa", "khỏi bệnh" | Block | "hỗ trợ", "cải thiện", "giúp" |
| "giảm cân X kg trong Y ngày" | Block | "hỗ trợ quá trình..." |
| Thu nhập cụ thể: "kiếm X triệu" | Flag | "mức lương thị trường", "thu nhập tương xứng" |
| Claim tỷ lệ thành công: "95% thành công" | Block | Không dùng % thành công |

### Module 2: Luật VN 15/2/2026 (Quảng cáo online)
Chỉ áp dụng khi `post_type = paid_ad`:
- Video ad ≥ 5s phải có nút skip rõ ràng, 1-click close
- Không được tự động phát với âm thanh mà không có user action
- Flag nếu script video không đề cập đến skip mechanism

### Module 3: Nghị định Mỹ phẩm VN 1/7/2026
Chỉ áp dụng khi `industry = cosmetics`:
- Không claim hiệu quả lâm sàng nếu không có chứng nhận
- Không so sánh "tốt hơn X%" mà không có data
- Không dùng ảnh before/after trong ad
- Tên thành phần phải viết đúng INCI name nếu đề cập

### Module 4: Brand-specific banned terms
Scan `brand_voice.banned_terms` — flag bất kỳ từ nào trong danh sách.

## Kết quả có thể

| Kết quả | Ý nghĩa |
|---------|---------|
| ✅ Pass | Không có vi phạm |
| ⚠️ Flag — auto-fix | Vi phạm nhẹ, có câu thay thế rõ ràng → tự sửa + ghi log |
| ❌ Block — rewrite required | Vi phạm nghiêm trọng → dừng pipeline, bắt buộc rewrite |

## Output

```yaml
policy_check:
  result: pass | flag_auto_fixed | block_rewrite_required
  violations:
    - location: [đoạn text vi phạm]
      rule: [module + rule cụ thể]
      severity: warning | block
      original_text: [text gốc]
      suggested_fix: [câu thay thế]
      was_auto_fixed: [true/false]
  post_after_autofix: [bài sau khi auto-fix, nếu có]
  block_reason: [lý do block nếu result = block_rewrite_required]
  modules_checked: [list modules đã chạy]
```

## Ghi chú
- Nếu result = block: pipeline dừng hoàn toàn, không tiếp tục sang intelligence layer hay review queue
- Nếu result = flag_auto_fixed: log rõ những gì đã sửa, tiếp tục pipeline với `post_after_autofix`
- Không bao giờ bypass policy check dù orchestrator yêu cầu
