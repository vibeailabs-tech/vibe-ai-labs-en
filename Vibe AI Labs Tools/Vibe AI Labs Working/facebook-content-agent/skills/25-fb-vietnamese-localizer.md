# [25] Skill: fb-vietnamese-localizer

## Mục đích
Localize sâu cho thị trường Việt Nam — register, idiom, văn hoá.
Không chỉ dịch — phải viết như người Việt đang viết cho người Việt.

## Input
- `post_content`: bài cần localize
- `brand_voice`: context từ brand-voice-loader (đặc biệt cách xưng hô và tone)

## Rules localization

### 1. Xưng hô nhất quán
Chọn 1 kiểu xưng hô và dùng xuyên suốt:
- **bạn/mình**: thân thiện, peer-to-peer, phù hợp lifestyle/education brands
- **anh/chị**: tôn trọng, phù hợp B2B, dịch vụ chuyên nghiệp
- **em**: brand trẻ, thương hiệu thời trang/beauty nhắm đến Gen Z
- **cô/chú**: brands nhắm đến 40+

Lỗi phổ biến: trộn "bạn" và "anh/chị" trong cùng 1 bài → flag và sửa.

### 2. Idiom và cụm từ
- Flag idiom dịch gượng từ tiếng Anh ("take it to the next level" → gượng)
- Thay bằng idiom/cụm từ Việt tương đương có cảm xúc tương tự
- Tránh Việt hoá bằng tiếng lóng nếu brand voice trang trọng

### 3. Reference văn hoá VN theo mùa
Kiểm tra xem trong 2 tuần tới có dịp lễ/sự kiện VN nào không:
- Tết Nguyên Đán (tháng 1–2)
- Quốc tế Phụ nữ 8/3
- Giỗ Tổ Hùng Vương 10/3 âm lịch
- 30/4 — 1/5
- Ngày của Mẹ (chủ nhật thứ 2 tháng 5)
- Trung Thu (15/8 âm lịch)
- Ngày Nhà giáo 20/11
- Mùa thi (tháng 6–7 và tháng 11–12)
- Giáng sinh 24–25/12

Nếu có dịp phù hợp: gợi ý 1 câu tie-in tự nhiên (không ép buộc phải thêm).

### 4. Cảm xúc và văn hoá
- Người Việt phản hồi mạnh với: gia đình, cộng đồng, sự tự hào, vượt khó
- Tránh: quá individualistic ("chỉ cần tin vào bản thân") — thêm yếu tố cộng đồng/gia đình nếu phù hợp
- CTA "chia sẻ cho bạn bè" hoạt động tốt hơn "share with your network"

### 5. Số và đơn vị
- Tiền: triệu/tỷ (không dùng "M" hay viết số nhiều chữ số)
- Thời gian: thứ 2–6 (không Monday–Friday)
- Địa danh: tên tiếng Việt (TP.HCM không phải HCMC)

## Output

```yaml
localized_post:
  original: [bài gốc]
  localized: [bài đã localize]
  changes_made:
    - type: [xung_ho / idiom / cultural_ref / number_format / other]
      original_text: [text gốc]
      new_text: [text mới]
      reason: [lý do thay]
  cultural_opportunity:
    has_upcoming_event: [true/false]
    event_name: [tên dịp lễ nếu có]
    suggested_tie_in: [câu gợi ý tie-in — để người dùng tự quyết có dùng không]
  xung_ho_used: [bạn/anh-chị/em/cô-chú/mình]
  consistency_check: [pass/fail — có xưng hô nhất quán không]
```
