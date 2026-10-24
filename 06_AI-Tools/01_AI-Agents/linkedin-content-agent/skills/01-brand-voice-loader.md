# Brand Voice Loader — Gate Skill

Tải và xác thực ngữ cảnh brand voice trước khi bắt đầu bất kỳ hoạt động tạo nội dung nào.

## Bước 1: Kiểm tra thư mục Brand Voice

Dùng Bash để kiểm tra xem `brand-voice/` có tồn tại trong thư mục hiện tại không:
```bash
ls brand-voice/ 2>/dev/null
```

Nếu thư mục không tồn tại hoặc rỗng:
```
❌ GATE FAILED: Brand voice not found.

Create brand-voice/ with these files:
  01-tone.md       — writing style and what to avoid
  02-audience.md   — reader profile
  03-pillars.md    — core content topics
  04-examples.md   — good/bad post examples
  05-glossary.json — preferred and banned terms
  06-authority.md  — expertise positioning (REQUIRED)

Template files are available at:
brand-voice/ (after running setup)
```

Dừng lại và không tiếp tục tạo nội dung.

## Bước 2: Đọc tất cả các file Brand Voice

Đọc từng file theo thứ tự:

**01-tone.md** — Trích xuất:
- Phong cách viết chính (1-3 gạch đầu dòng)
- 3 quy tắc "tuyệt đối không làm" quan trọng nhất
- Ưu tiên về cấu trúc câu

**02-audience.md** — Trích xuất:
- Mô tả đối tượng độc giả chính (1 câu)
- Điểm đau hàng đầu (2-3 gạch đầu dòng)
- Điều họ muốn nhận được từ nội dung

**03-pillars.md** — Trích xuất:
- Danh sách tất cả tên pillar
- Mô tả ngắn gọn từng pillar (1 dòng mỗi cái)

**04-examples.md** — Trích xuất:
- Ghi nhận điều gì làm cho các ví dụ tốt trở nên tốt (kiểu hook, cấu trúc)
- Ghi nhận điều gì làm cho các ví dụ xấu trở nên xấu (các pattern cần tránh)

**05-glossary.json** — Phân tích JSON:
- Tải mảng `use` (từ/cụm từ ưu tiên)
- Tải mảng `avoid` (từ/cụm từ bị cấm)

**06-authority.md** — Trích xuất (BẮT BUỘC):
- `type`: personal / company / dual
- `name`: tên thương hiệu
- `voice`: đại từ sử dụng
- `can_claim`: danh sách tuyên bố có thể xác minh
- `cannot_claim`: danh sách tuyên bố bị cấm
- `credibility_anchors`: phong cách câu mở đầu

## Bước 3: Xử lý các loại Authority

**Nếu type = personal**:
- Đặt voice = "tôi"
- Hook style = câu chuyện cá nhân hoặc insight chuyên môn
- CTA style = mời bình luận / chia sẻ trải nghiệm

**Nếu type = company**:
- Đặt voice = "chúng tôi"
- Hook style = dẫn dắt bằng dữ liệu hoặc quan sát ngành
- CTA style = mời tìm hiểu thêm / đặt lịch demo / theo dõi

**Nếu type = dual**:
- Ghi nhận cả hai profile (cá nhân và công ty)
- Đánh dấu để li-voice-router hỏi người dùng chọn voice nào
- KHÔNG tự chọn mặc định — luôn hỏi

## Bước 4: Xuất Brand Voice Context

Định dạng và xuất khối thông tin này (sẽ được tham chiếu xuyên suốt pipeline):

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 BRAND VOICE CONTEXT — LOADED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUTHORITY TYPE: [personal/company/dual]
NAME: [name from 06-authority.md]
VOICE PRONOUN: [tôi/chúng tôi]
TITLE: [title/description]

TONE SUMMARY:
  • [key tone point 1]
  • [key tone point 2]
  • Never: [top avoid rule]

AUDIENCE: [1-sentence description]
PAIN POINTS: [2-3 bullets]

CONTENT PILLARS:
  1. [Pillar 1 name] — [brief description]
  2. [Pillar 2 name] — [brief description]
  3. [Pillar 3 name] — [brief description]
  [etc.]

VOCABULARY:
  Preferred: [5 sample terms from use list]
  Banned: [5 sample terms from avoid list]

CREDIBILITY ANCHORS:
  • [anchor 1]
  • [anchor 2]

AUTHORITY LIMITS:
  Can claim: [can_claim summary]
  Cannot claim: [cannot_claim summary]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Bước 5: Cảnh báo Validation

Kiểm tra các vấn đề thường gặp và cảnh báo (không dừng lại, chỉ gắn cờ):
- Nếu 04-examples.md bị thiếu: `⚠️ No examples file found — content will rely on tone/pillar guidelines only`
- Nếu 05-glossary.json rỗng hoặc không parse được: `⚠️ Glossary not loaded — vocabulary guidance unavailable`
- Nếu danh sách credibility_anchors rỗng trong 06-authority.md: `⚠️ No credibility anchors defined — hook quality may be lower`

## Cách dùng

Skill này chạy tự động như bước đầu tiên trong mọi pipeline.
Có thể gọi độc lập: `/brand-voice-loader`

Kết quả của skill này được truyền trực tiếp vào:
- li-voice-router (quyết định loại authority)
- li-post-writer (tone, từ vựng, pillar)
- li-hook-engineer (tuỳ chọn hook style)
- li-policy-checker (kiểm tra tuyên bố authority)
- Tất cả các skill tạo nội dung khác
