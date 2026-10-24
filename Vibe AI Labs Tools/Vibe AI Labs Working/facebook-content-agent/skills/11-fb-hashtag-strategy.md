# [11] Skill: fb-hashtag-strategy

## Mục đích
Tạo bộ hashtag theo mục tiêu reach — branded, niche, trending.

## Input
- `topic`: chủ đề bài
- `industry`: ngành
- `goal`: branded_awareness / niche_reach / trending_boost / mixed
- `brand_voice`: context từ brand-voice-loader
- `post_language`: vi / en / mixed

## 3 nhóm hashtag

### Nhóm 1: Branded (1–3 hashtag)
Hashtag riêng của thương hiệu — mục tiêu build brand awareness và community.
- #TênThươngHiệu
- #Slogan hoặc #CampaignName
- Nếu chưa có: gợi ý tạo branded hashtag

### Nhóm 2: Niche (5–8 hashtag)
Hashtag chuyên ngành — reach đúng audience, ít cạnh tranh hơn hashtag đại trà.
- Cụ thể hơn broad hashtag: #skincarevietnam tốt hơn #skincare
- Audience của hashtag này phù hợp với brand_voice.audience_persona
- Volume: không quá nhỏ (< 1k post) và không quá lớn (> 10M post)

### Nhóm 3: Trending/Broad (3–5 hashtag)
Hashtag đang có volume cao — mục tiêu reach rộng, khám phá mới.
- Phù hợp chủ đề bài
- Đang được dùng nhiều (không phải hashtag đã lỗi thời)
- Không nên dùng hashtag quá generic (#life, #love) trừ khi có lý do

## Rules Facebook hashtag 2026
- Facebook hashtag kém hiệu quả hơn Instagram — dùng ít và có chọn lọc
- Tổng: 5–10 hashtag là đủ (Instagram có thể 20+, Facebook không)
- Đặt cuối bài hoặc trong first comment — không trộn vào body
- Hashtag tiếng Việt: viết liền không dấu (#skincarevietnam) hoặc CamelCase (#SkincareVietNam)

## Output

```yaml
hashtag_strategy:
  total_count: [số hashtag tổng]
  branded:
    hashtags: [list]
    note: [ghi chú — nếu cần tạo branded hashtag mới]
  niche:
    hashtags: [list]
    reasoning: [lý do chọn các hashtag này]
  trending:
    hashtags: [list]
    reasoning: [lý do chọn]
  placement_recommendation: [body / first_comment / end_of_post]
  full_set: [toàn bộ hashtag ghép lại, ready to paste]
  alternative_set: [bộ hashtag thay thế nếu muốn A/B test]
```
