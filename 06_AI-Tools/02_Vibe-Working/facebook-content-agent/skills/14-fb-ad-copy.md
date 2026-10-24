# [14] Skill: fb-ad-copy

## Mục đích
Viết copy cho paid Facebook post / quảng cáo.
Built-in compliance check theo luật VN 15/2/2026 (5s skip rule).

## Input
- `ad_format`: image / video / carousel / collection
- `campaign_objective`: awareness / traffic / engagement / leads / conversions / catalog_sales
- `product_or_service`: sản phẩm / dịch vụ cần quảng cáo
- `offer`: ưu đãi nếu có (giảm giá, quà tặng, thời hạn)
- `target_audience_note`: audience cụ thể của ad set này (có thể khác audience chung)
- `brand_voice`: context từ brand-voice-loader

## Cấu trúc ad copy Facebook

### Primary Text (phần bên trên hình/video)
- 125 ký tự đầu hiển thị trước "Xem thêm" — hook phải nằm đây
- Tối đa 3–5 dòng cho hầu hết campaign
- Clarity > cleverness với paid ad — người ta scroll nhanh hơn organic

### Headline (bên dưới hình/video, in đậm)
- Tối đa 40 ký tự (truncate trên mobile)
- Rõ value proposition hoặc offer
- Đây là dòng người ta đọc thứ 2 sau hình

### Description (bên dưới headline, nhỏ hơn)
- Tối đa 30 ký tự
- Reinforce headline hoặc thêm urgency/detail
- Nhiều placement không hiển thị description

### CTA Button
Chọn 1 phù hợp campaign_objective:
- Awareness: Tìm hiểu thêm
- Traffic: Tìm hiểu thêm / Xem thêm
- Leads: Đăng ký / Liên hệ
- Conversions: Mua ngay / Đặt hàng
- Engagement: Thích trang / Theo dõi

## Compliance check tích hợp

### FB Ad Policy (luôn check)
- Không claim không được phép (health, finance, income)
- Text trên hình ≤ 20% diện tích (nếu có note về design)
- Không before/after với ngành nhạy cảm

### Luật VN 15/2/2026 (áp dụng với video ad)
- Video ≥ 5 giây phải có nút skip rõ ràng, 1-click close
- Ghi rõ trong production note: "Cần có nút skip sau 5s — bắt buộc theo luật VN hiệu lực 15/2/2026"
- Không tự động phát với âm thanh bật sẵn

## Output

```yaml
ad_copy:
  ad_format: [loại ad]
  campaign_objective: [mục tiêu]
  primary_text:
    full: [toàn bộ primary text]
    hook_125_chars: [125 ký tự đầu — phần hiển thị trước "Xem thêm"]
  headline: [tối đa 40 ký tự]
  description: [tối đa 30 ký tự]
  cta_button: [text nút CTA]
  compliance_notes:
    fb_policy: [pass / issues found]
    vn_law_2026: [applicable/not_applicable — ghi note nếu applicable]
    issues: [list vi phạm nếu có + cách fix]
  variants:
    - variant: A
      primary_text: [...]
      headline: [...]
    - variant: B
      primary_text: [...]
      headline: [...]
  production_note: [ghi chú cho team creative — đặc biệt về compliance visual]
```
