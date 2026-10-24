# Facebook Content Agent

Hệ thống AI tự động viết, tối ưu và kiểm duyệt nội dung Facebook — chạy hoàn toàn trong Claude Code. Bạn chỉ cần điền thông tin thương hiệu một lần, sau đó gõ lệnh và nhận bài hoàn chỉnh.

---

## Mục lục

1. [Yêu cầu cài đặt](#1-yêu-cầu-cài-đặt)
2. [Cài đặt lần đầu](#2-cài-đặt-lần-đầu)
3. [Điền thông tin thương hiệu](#3-điền-thông-tin-thương-hiệu-bắt-buộc)
4. [Cách dùng](#4-cách-dùng)
5. [Các lệnh hỗ trợ](#5-các-lệnh-hỗ-trợ)
6. [Pipeline hoạt động như thế nào](#6-pipeline-hoạt-động-như-thế-nào)
7. [Output bạn sẽ nhận được](#7-output-bạn-sẽ-nhận-được)
8. [Câu hỏi thường gặp](#8-câu-hỏi-thường-gặp)

---

## 1. Yêu cầu cài đặt

| Yêu cầu | Chi tiết |
|---|---|
| **Claude Code** | App desktop hoặc CLI — tải tại [claude.ai/code](https://claude.ai/code) |
| **Tài khoản Claude** | Plan Pro hoặc Max (cần đủ context window để chạy pipeline) |
| **Hệ điều hành** | macOS, Windows, hoặc Linux |

> **Lưu ý:** Không cần cài thêm bất kỳ phần mềm nào khác. Không có database, không có server, không có API key riêng.

---

## 2. Cài đặt lần đầu

### Bước 1 — Tải Claude Code

Truy cập [claude.ai/code](https://claude.ai/code) và tải app về máy. Đăng nhập bằng tài khoản Claude của bạn.

### Bước 2 — Mở đúng folder

Trong Claude Code, mở folder **Facebook Content Agent** (folder chứa file README này).

> Quan trọng: Claude Code phải được mở tại đúng folder này thì các lệnh `/fb-content-agent` mới hoạt động.

### Bước 3 — Xác nhận hệ thống sẵn sàng

Gõ lệnh sau trong Claude Code để kiểm tra:

```
/fb-content-agent kiểm tra hệ thống
```

Nếu thấy thông báo thiếu brand voice → tiếp tục bước 3 bên dưới.

---

## 3. Điền thông tin thương hiệu (Bắt buộc)

Đây là bước **duy nhất bạn cần làm thủ công**. Mở folder `brand-voice/` và điền vào 5 file sau:

---

### 📄 `brand-voice/01-tone.md` — Giọng văn thương hiệu

Mô tả cách thương hiệu của bạn "nói chuyện" trên mạng xã hội.

**Cần điền:**
- Giọng văn chính (ví dụ: thân thiện, chuyên nghiệp, hài hước nhẹ)
- 3–5 tính từ mô tả tính cách thương hiệu
- Cách xưng hô với khách hàng (bạn / anh / chị / tên riêng)
- Những điều KHÔNG làm (ví dụ: không dùng tiếng lóng, không quá cứng nhắc)
- Ví dụ 2–3 câu mở đầu hay dùng

---

### 👥 `brand-voice/02-audience.md` — Khách hàng mục tiêu

Mô tả người bạn đang viết bài cho họ.

**Cần điền:**
- Tên persona (đặt tên đại diện, ví dụ: "Chị Mai 30 tuổi")
- Độ tuổi, giới tính, địa điểm
- Nghề nghiệp và mức thu nhập
- Pain points (vấn đề họ đang gặp)
- Mong muốn / khát vọng
- Họ lướt Facebook lúc nào trong ngày
- Loại content họ thích (video, bài lưu, câu chuyện...)
- Điều gì trigger họ mua hàng

---

### 🏛️ `brand-voice/03-pillars.md` — Trụ cột nội dung

Định nghĩa 3–5 chủ đề chính bạn sẽ xoay quanh khi đăng bài.

**Cần điền cho mỗi pillar:**
- Tên pillar (ví dụ: "Kiến thức", "Câu chuyện khách hàng", "Sản phẩm")
- Mô tả ngắn chủ đề này nói về gì
- Tỷ lệ % trong tổng content (tổng 5 pillar = 100%)
- Mục tiêu: Awareness / Engagement / Conversion
- Ví dụ 1 tiêu đề bài thuộc pillar này

---

### 📝 `brand-voice/04-examples.md` — Bài mẫu thực tế

Cung cấp ví dụ bài viết thực tế để AI học theo phong cách của bạn.

**Cần điền:**
- 3 bài perform tốt nhất (paste nguyên văn bài vào, kèm loại format và kết quả đạt được)
- 2 bài KHÔNG nên làm (anti-pattern) và lý do vì sao không tốt

> **Mẹo:** Bài mẫu càng thực tế và cụ thể, AI viết ra càng đúng tone của bạn.

---

### 📖 `brand-voice/05-glossary.json` — Từ điển thương hiệu

Danh sách từ được phép dùng và từ bị cấm.

**Cấu trúc file:**
```json
{
  "approved": [
    "từ hoặc cụm từ thương hiệu hay dùng",
    "tên sản phẩm đặc trưng"
  ],
  "banned": [
    "từ vi phạm chính sách Facebook",
    "từ không phù hợp brand"
  ],
  "reasoning": {
    "từ bị cấm": "lý do tại sao bị cấm"
  }
}
```

> **Lưu ý:** File này phải đúng định dạng JSON. Nếu không chắc, dùng [jsonlint.com](https://jsonlint.com) để kiểm tra trước khi lưu.

---

## 4. Cách dùng

Sau khi điền xong brand voice, mở Claude Code tại folder này và gõ:

```
/fb-content-agent [yêu cầu của bạn]
```

### Ví dụ lệnh thực tế

**Viết bài feed:**
```
/fb-content-agent viết bài giới thiệu sản phẩm mới, mục tiêu tăng awareness
```

**Viết carousel:**
```
/fb-content-agent tạo carousel 5 slide về lợi ích của [sản phẩm], tone giáo dục
```

**Viết script Reels:**
```
/fb-content-agent viết script video 30 giây về tips [chủ đề], phong cách hài hước
```

**Lên lịch content:**
```
/fb-content-agent lên kế hoạch content cho tháng tới, tập trung pillar kiến thức và chuyển đổi
```

**Tối ưu bài cũ:**
```
/fb-content-agent tối ưu bài này để tăng save: [paste bài vào đây]
```

**Reply comment:**
```
/fb-content-agent viết reply cho comment này: "[paste comment vào đây]"
```

**Phân tích đối thủ:**
```
/fb-content-agent phân tích fanpage đối thủ và đề xuất cách differentiate
```

**Phân tích cấu trúc bài (chỉ X-ray, không tạo bài mới):**
```
/fb-content-agent brief lại bài này: [paste bài vào đây]
```

**Viết lại bài theo structure của bài mẫu** *(chạy full pipeline → ra file .md)*:
```
/fb-content-agent học theo structure của bài này và viết lại về [chủ đề]: [paste bài mẫu]
```

> ⚠️ Khi yêu cầu **viết lại** hoặc **repurpose** từ bài có sẵn, hệ thống sẽ chạy toàn bộ pipeline (không dừng ở bước phân tích) và xuất file `.md` đầy đủ vào `output/`.

**Tìm pattern từ nhiều bài:**
```
/fb-content-agent phân tích pattern từ 3 bài này: [paste 3 bài vào đây]
```

---

## 5. Các lệnh hỗ trợ

| Lệnh | Tác dụng |
|---|---|
| `/fb-content-agent xem lịch sử bài đã tạo` | Xem các bài AI đã viết trước đó |
| `/fb-content-agent review hiệu suất content` | Phân tích bài nào đang tốt/kém |
| `/fb-content-agent audit toàn bộ content tháng này` | Kiểm tra tổng thể chiến lược |
| `/fb-content-agent nghiên cứu trend hiện tại` | Tìm trend Facebook phù hợp ngành |

---

## 6. Pipeline hoạt động như thế nào

Khi bạn gõ lệnh, hệ thống tự động chạy qua pipeline phù hợp:

```
[01] brand-voice-loader   — Load thông tin thương hiệu (bắt buộc pass)
[02] task-router          — Phân tích yêu cầu, chọn pipeline phù hợp
[03] fb-format-selector   — Chọn format tối ưu (feed / carousel / reel...)
[04] performance-memory   — Đọc lịch sử bài cũ để tránh lặp
[29] fb-content-brief     — (tuỳ chọn) Brief lại nội dung có sẵn nếu bạn cung cấp bài mẫu
     ↓
[Content skill]           — Viết bài theo format đã chọn
     ↓
[15] fb-discussion-architect    — Thiết kế cấu trúc thảo luận
[16] fb-first-comment-strategy  — Lên kế hoạch first comment
[23] fb-readability-formatter   — Tối ưu độ dễ đọc
[24] fb-visual-brief            — Tóm tắt brief cho designer
[25] fb-vietnamese-localizer    — Tối ưu tiếng Việt
[26] fb-policy-checker          — Kiểm tra vi phạm chính sách Facebook
[21] fb-save-share-optimizer    — Tối ưu tỷ lệ save/share
[22] fb-send-time-optimizer     — Đề xuất giờ đăng tối ưu
     ↓
[27] fb-review-queue      — Duyệt tự động hoặc hỏi bạn (tùy confidence)
[28] output-validator     — Kiểm tra 11 tiêu chí trước khi xuất
```

### Cơ chế duyệt tự động

| Độ tin cậy | Hành động |
|---|---|
| ≥ 90% | Tự động xuất bài — không cần bạn can thiệp |
| 70–89% | Dừng lại, hiển thị bài để bạn Approve / Sửa / Reject |
| < 70% | Tự động viết lại từ đầu |

---

## 7. Output bạn sẽ nhận được

Mỗi lần chạy xong, bạn nhận được **1 file duy nhất** lưu tại `output/YYYY_MM_DD-[tên-bài].md` chứa trọn bộ:

```
📝 NỘI DUNG BÀI       — Bài hoàn chỉnh, ready to publish
💬 FIRST COMMENT      — Kế hoạch comment đầu tiên để seed thảo luận
🎨 VISUAL BRIEF       — Mô tả hình ảnh/video cho designer
⏰ GIỜ ĐĂNG           — Top 3 khung giờ tối ưu trong ngày
📊 ĐIỂM SỐ            — Save score, Share score, Confidence %
📋 EXECUTION LOG      — Log từng bước đã chạy
```

> Mỗi bài = đúng 1 file `.md` trong folder `output/`. Hệ thống không tạo file lẻ theo từng section.

---

## 8. Câu hỏi thường gặp

**Q: Tôi cần điền brand voice lại không nếu muốn dùng cho thương hiệu khác?**
A: Có. Mỗi thương hiệu nên có một folder riêng với bộ brand voice riêng. Copy toàn bộ folder này và điền lại 5 file brand voice.

---

**Q: AI có thể tự đăng bài lên Facebook không?**
A: Không. Hệ thống chỉ tạo nội dung — bạn tự copy và đăng. Điều này giúp bạn luôn kiểm soát được những gì được publish.

---

**Q: Bài bị reject ở bước policy-checker thì sao?**
A: Hệ thống tự động yêu cầu viết lại và không thể bypass bước này, kể cả khi bạn yêu cầu. Đây là cơ chế bảo vệ để tránh bài vi phạm chính sách quảng cáo Facebook.

---

**Q: Tôi có thể sửa bài sau khi AI viết xong không?**
A: Hoàn toàn được. Khi hệ thống dừng ở bước review (confidence 70–89%), bạn có thể chọn "Edit" để sửa trực tiếp trước khi xuất.

---

**Q: Lịch sử bài được lưu ở đâu?**
A: Tại `memory/post-history.json`. File này được cập nhật tự động sau mỗi lần tạo bài thành công.

---

**Q: Tôi muốn thêm hoặc chỉnh sửa một skill?**
A: Mở file tương ứng trong folder `skills/` và chỉnh nội dung. Mỗi file là một prompt định nghĩa logic của skill đó. Không cần rebuild hay restart gì cả.

---

**Q: Tại sao khi tôi paste bài mẫu để "viết lại", hệ thống lại chạy lâu hơn chỉ "phân tích"?**
A: Vì đây là hai chế độ khác nhau của skill `fb-content-brief`:
- **Phân tích thuần** (`brief lại bài này`): chỉ X-ray cấu trúc, pipeline ngắn, không tạo bài mới.
- **Viết lại / Repurpose** (`viết lại bài này`, `chuyển bài này thành carousel`...): hệ thống phân tích xong rồi bắt buộc chạy toàn bộ publishing pipeline — ra bài hoàn chỉnh với first comment, visual brief, giờ đăng và lưu file `.md` vào `output/`.

---

## Cấu trúc folder

```
Facebook Content Agent/
├── README.md                          ← File này
├── CLAUDE.md                          ← Hướng dẫn nội bộ cho Claude Code
├── brand-voice/                       ← ⭐ Bạn điền vào đây
│   ├── 01-tone.md                     — Giọng văn thương hiệu
│   ├── 02-audience.md                 — Khách hàng mục tiêu
│   ├── 03-pillars.md                  — Trụ cột nội dung
│   ├── 04-examples.md                 — Bài mẫu thực tế
│   └── 05-glossary.json               — Từ điển thương hiệu
├── skills/                            ← 29 skill AI (không cần chỉnh)
│   ├── 01-brand-voice-loader.md
│   ├── 02-task-router.md
│   ├── 29-fb-content-brief.md
│   └── ... (26 skills khác)
├── memory/
│   ├── post-history.json              — Lịch sử bài đã tạo
│   └── task-state.json                — Checkpoint pipeline
└── .claude/
    └── commands/
        └── fb-content-agent.md        ← Orchestrator chính
```

---

*Facebook Content Agent v3.2 — Powered by Claude*
