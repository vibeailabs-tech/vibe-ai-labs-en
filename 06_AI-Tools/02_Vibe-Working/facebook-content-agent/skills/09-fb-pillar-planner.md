# [09] Skill: fb-pillar-planner

## Mục đích
Xây mới hoặc rà soát 3–5 content pillars cho thương hiệu.

## Input
- `mode`: build_new / audit_existing
- `brand_info`: thông tin thương hiệu (sản phẩm/dịch vụ, target market, USP)
- `marketing_goals`: mục tiêu marketing (brand awareness / lead gen / sales / community)
- `existing_pillars`: (chỉ khi mode=audit_existing) list pillars đang dùng
- `brand_voice`: context từ brand-voice-loader

## Mode: build_new

### Framework xây pillars
Mỗi pillar phải trả lời được 3 câu hỏi:
1. **Audience**: Pillar này phục vụ pain point / desire nào của audience?
2. **Brand**: Pillar này thể hiện thế mạnh / góc nhìn nào của thương hiệu?
3. **Business**: Pillar này dẫn đến conversion / loyalty như thế nào?

### Tỷ lệ phân bổ gợi ý
- 40% Educational / Value content (build trust)
- 30% Storytelling / Behind-the-scenes (build connection)
- 20% Promotional / Product (convert)
- 10% Community / UGC / Interaction (build loyalty)

Điều chỉnh theo goal thực tế của thương hiệu.

## Mode: audit_existing

Đánh giá từng pillar hiện tại:
- Có đủ rộng để tạo content lâu dài không?
- Có quá chồng chéo với pillar khác không?
- Tỷ lệ phân bổ có cân bằng không?
- Có pillar nào đang thiếu (gap) không?

## Output

```yaml
pillar_plan:
  mode: [build_new / audit_existing]
  pillars:
    - id: 1
      name: [Tên pillar ngắn gọn]
      description: [Mô tả — pillar này về gì, phục vụ audience thế nào]
      ratio: [% tổng content]
      primary_goal: [awareness / engagement / conversion / loyalty]
      content_types: [list dạng bài phù hợp]
      example_topics:
        - [Ví dụ tiêu đề bài 1]
        - [Ví dụ tiêu đề bài 2]
        - [Ví dụ tiêu đề bài 3]
      why_this_pillar: [lý do pillar này quan trọng với brand]
    - id: 2
      ...
  audit_notes: (chỉ khi mode=audit_existing)
    gaps_found: [list gap nếu có]
    overlap_issues: [list chồng chéo nếu có]
    recommended_changes: [danh sách thay đổi gợi ý]
  implementation_tip: [1–2 câu gợi ý cách bắt đầu dùng pillars này]
```
