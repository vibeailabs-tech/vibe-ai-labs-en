# Li Content Brief — X-Ray & Tạo Brief cho Nội dung Hiện có

Phân tích nội dung sẵn có để trích xuất pattern, tạo brief viết lại, hoặc xây dựng chiến lược repurpose.

## Cách dùng
```
/li-content-brief mode=analyze [paste content here]
/li-content-brief mode=brief-for-rewrite [paste content here]
/li-content-brief mode=brief-for-repurpose [paste content here]
/li-content-brief mode=series [paste 3+ posts here]
```

Mặc định mode = analyze nếu không chỉ định.

---

## MODE: analyze

Thực hiện X-ray toàn diện cho nội dung được cung cấp.

**Phân tích cấu trúc**:
- Hook: Kiểu gì? (story / number / question / contrarian / statement) — Mạnh không?
- "See more" cliff: Có điểm dừng hấp dẫn ở dòng 3 không? (có/không + lý do)
- Cấu trúc body: Được tổ chức như thế nào? (list / narrative / framework / Q&A)
- CTA: Kiểu gì và cụ thể đến đâu? (generic/specific/none)
- Độ dài: Số từ + thời gian đọc ước tính

**Phân tích tone**:
- Voice: personal (tôi) / company (chúng tôi) / unclear
- Cung bậc cảm xúc: confident / vulnerable / authoritative / neutral
- Mức độ khớp brand voice: So sánh với brand voice đã tải (nếu có)
- Chất lượng từ vựng: Có dùng từ bị cấm không? Có bỏ lỡ cơ hội dùng từ ưu tiên không?

**Chất lượng nội dung**:
- Điểm cụ thể (1-10): Có dùng số liệu, tên người, ngày tháng cụ thể không, hay chỉ mơ hồ?
- Chiều sâu insight (1-10): Có điểm không hiển nhiên không, hay chỉ đang nói điều ai cũng biết?
- Khớp pillar: Phục vụ pillar nào? (đối chiếu với pillars đã tải)
- Dwell potential (1-10): Khả năng người đọc đọc đến cuối cao không?

**Cơ chế tương tác**:
- Bài có kích thích tranh luận hay chỉ tạo đồng thuận?
- CTA có được đặt vị trí để tạo ra bình luận chất lượng không?
- Có expertise trigger nào khiến thought leader muốn phản hồi không?

**Định dạng đầu ra**:
```
📊 CONTENT X-RAY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hook type: [type] | Hook strength: [1-10]
See-more cliff: [yes/no] — [why]
Body structure: [type]
CTA: [type] | Specificity: [generic/specific]
Word count: [N] | Est. read time: [X sec]

Tone: [voice] | Register: [emotional register]
Specificity score: [1-10]
Insight depth: [1-10]
Pillar: [pillar name or "no match"]
Dwell potential: [1-10]

TOP STRENGTH: [what works best]
TOP WEAKNESS: [what to fix first]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## MODE: brief-for-rewrite

Phân tích nội dung VÀ tạo brief để viết lại.

Đầu tiên, chạy mode analyze ở trên. Sau đó:

**Brief viết lại**:
1. **Giữ lại**: Những yếu tố nào đang hoạt động tốt? (ngôn ngữ cụ thể, một ví dụ hay, một luận điểm mạnh)
2. **Cải thiện**: Phần yếu nhất là gì? (thường là hook hoặc CTA)
3. **Hook mới**: Gợi ý 2 biến thể hook mạnh hơn (dùng kiểu contrarian + số cụ thể)
4. **Góc độ mới**: Có góc nhìn khiêu khích hơn hoặc không hiển nhiên hơn về cùng chủ đề không?
5. **Điều chỉnh tone**: Thay đổi tone nào sẽ cải thiện engagement?
6. **Nâng cấp CTA**: Thay CTA chung chung bằng câu hỏi cụ thể, nhắm đúng audience

**Định dạng đầu ra**:
```
📝 REWRITE BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KEEP:
  • [element 1]
  • [element 2]

IMPROVE:
  • [specific issue + why]

NEW HOOK OPTIONS:
  A (contrarian): "[hook text]"
  B (specific number): "[hook text]"

NEW ANGLE: [1-2 sentences on a sharper take]

TONE: [what to adjust]
CTA: "[specific replacement CTA]"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Truyền brief này sang li-post-writer (mode=iterate).

---

## MODE: brief-for-repurpose

Phân tích format gốc của nội dung và tạo kế hoạch repurpose cho LinkedIn.

**Phân tích nguồn**:
- Format gốc là gì? (blog / podcast / report / email / tweet / presentation)
- Insight cốt lõi là gì? (điều có giá trị nhất trong nội dung)
- Đối tượng mục tiêu của bản gốc so với audience LinkedIn là ai?

**Ánh xạ repurpose**:
- Format LinkedIn phù hợp nhất cho nội dung này (và tại sao)
- Cần trích xuất gì (1-3 insight gần gũi nhất với LinkedIn)
- Cần bỏ gì (những gì không hoạt động trên LinkedIn)
- Cần đóng khung lại như thế nào (cách tái ngữ cảnh hoá cho audience chuyên nghiệp)
- Góc độ cá nhân cần thêm vào (nếu là personal brand: gắn với kinh nghiệm của bạn)

**Định dạng đầu ra**:
```
🔄 REPURPOSE BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Source: [format]
Core insight: [1 sentence]

Best LinkedIn format: [text post / carousel / newsletter / article]
Why: [1-2 sentences]

EXTRACT:
  • [key insight 1]
  • [key insight 2]
  • [key insight 3 if applicable]

DROP: [what doesn't work on LinkedIn and why]

NEW FRAMING: [how to re-angle for LinkedIn context]
PERSONAL HOOK: [how to tie to your experience]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Truyền brief này sang li-repurpose hoặc li-carousel-architect.

---

## MODE: series

Phân tích 3+ bài viết để tìm pattern và trích xuất brief cho content series.

**Trích xuất pattern**:
- Kiểu hook lặp lại (hook nào xuất hiện nhiều nhất?)
- Pattern cấu trúc (các bài mạnh tổ chức nội dung như thế nào?)
- Cụm chủ đề (sub-topic nào xuất hiện nhiều lần?)
- Tương quan hiệu suất (nếu có số liệu: điều gì tương quan với hiệu suất cao?)
- Nhất quán voice (tone có nhất quán qua các bài không?)

**Phân tích khoảng trống**:
- Pillar nào đang bị thiếu hoặc ít đại diện?
- Kiểu hook nào chưa được thử?
- Chủ đề nào sẽ bổ sung tốt cho series hiện tại?

**Định dạng đầu ra**:
```
📈 SERIES ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Posts analyzed: [N]

PATTERNS FOUND:
  Hook: [most common type] ([X]% of posts)
  Structure: [most common structure]
  Strong performers: [what they have in common]

CONTENT GAPS:
  • [gap 1]
  • [gap 2]

SERIES RECOMMENDATIONS:
  1. [next post idea — fills gap 1]
  2. [next post idea — continues strong pattern]
  3. [experimental post — different hook type]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
