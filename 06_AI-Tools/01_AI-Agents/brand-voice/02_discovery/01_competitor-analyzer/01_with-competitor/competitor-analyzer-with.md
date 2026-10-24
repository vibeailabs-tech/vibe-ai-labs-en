---
name: competitor-analyzer-with
description: >
  Nghiên cứu brand voice của các đối thủ được nêu tên cụ thể. Dùng skill này khi
  khách hàng đã cung cấp tên đối thủ thực trong brand brief
  (brief.knows_competitor = true). Tạo ra hồ sơ có cấu trúc về tone, cụm từ chính,
  định vị của từng đối thủ — và quan trọng nhất là khoảng trống mà khách hàng có thể chiếm lĩnh.
  Kích hoạt khi orchestrator đến Bước 3 và knows_competitor là true.
---

# Competitor Analyzer — Có Tên Đối Thủ Cụ Thể

Bạn có tên đối thủ cụ thể từ `session/brief.json`. Mục tiêu là hiểu cách mỗi đối thủ nghe như thế nào — không phải họ làm gì, mà **họ nói chuyện như thế nào**.

Kết quả quan trọng nhất ở đây là `gap_opportunity`: vị trí brand voice mà đối thủ này chưa chiếm, khách hàng có thể sở hữu.

## Perplexity API (tùy chọn — dùng thay WebSearch để có kết quả sâu hơn)

Nếu có `PERPLEXITY_API_KEY` trong environment, gọi API bằng Bash:

```bash
curl -s https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": "Phân tích brand voice của [tên đối thủ] tại Việt Nam: tone, cụm từ chính, định vị, chủ đề họ hay nói. Nguồn: website, Facebook, LinkedIn."}]
  }'
```

Nếu không có key → dùng WebSearch bình thường bên dưới.

## Quy trình nghiên cứu cho từng đối thủ

Với mỗi tên trong `competitor_names`, thực hiện:

**1. Tìm kiếm nội dung công khai của họ**

Dùng WebSearch để tìm:
- Website của họ (đặc biệt là trang About, Homepage, Blog)
- Sự hiện diện trên Facebook/LinkedIn
- Bất kỳ bài phỏng vấn hay phát biểu công khai nào của founder

Các câu tìm kiếm hiệu quả:
- `[tên đối thủ] about page brand voice tone`
- `[tên đối thủ] Vietnam [ngành] website`
- `"[tên đối thủ]" site:facebook.com`

**2. Phân tích những gì bạn tìm thấy — tập trung vào voice, không phải tính năng**

Tìm kiếm:
- **Tone**: trang trọng/thân mật, ấm áp/lạnh lùng, nghiêm túc/vui vẻ, chuyên gia/thân thiện
- **Cụm từ chính**: từ ngữ hoặc mẫu câu họ lặp đi lặp lại ("luôn đồng hành", "giải pháp toàn diện", "trải nghiệm tuyệt vời")
- **Chủ đề**: những gì họ nhất quán nói đến
- **Định vị**: họ đặt mình vào thị trường như thế nào
- **Họ nói chuyện với ai**: và cách họ điều chỉnh giọng điệu theo đối tượng đó

**3. Xử lý kết quả mỏng một cách trung thực**

Nếu đối thủ có ít nội dung công khai (thương hiệu nhỏ, ít hiện diện online), nêu rõ điều này trong `notes` và làm tốt nhất với những gì có. Đừng bịa đặt thông tin — dùng ngôn ngữ như "nội dung công khai hạn chế; có thể dùng tone [trang trọng/thân mật] dựa trên chuẩn ngành."

## Output

Lưu vào `session/competitor-analysis.json`:

```json
{
  "type": "named_competitors",
  "profiles": [
    {
      "competitor": "Tên Thương Hiệu",
      "tone": "mô tả tone trong một câu",
      "key_phrases": ["cụm từ 1", "cụm từ 2", "cụm từ 3"],
      "topics": ["chủ đề họ hay nói đến"],
      "positioning": "cách họ định vị mình trên thị trường",
      "gap_opportunity": "điều họ KHÔNG nói mà khách hàng có thể sở hữu",
      "notes": "mọi lưu ý về chất lượng dữ liệu hoặc kết quả mỏng"
    }
  ],
  "collective_gap": "khoảng trắng tổng thể — điều không ai trong ngành này đang nói"
}
```

## Thế nào là một `gap_opportunity` tốt

Yếu: *"Họ không nói nhiều về chất lượng"*
Mạnh: *"Mọi đối thủ trong ngành này đều đang biểu diễn sự ấm áp — không ai thực sự thẳng thắn hoặc trung thực về đánh đổi. Một thương hiệu nói thẳng và thừa nhận những gì mình không làm được sẽ thực sự khác biệt."*

Khoảng trống phải có thể hành động được và đặc thù cho voice/tone — không phải tính năng sản phẩm.
