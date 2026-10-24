# Brand Voice Agent

Một AI agent hoàn chỉnh để xây dựng brand voice cho doanh nghiệp vừa và nhỏ (SMB). Agent phỏng vấn khách hàng, nghiên cứu đối thủ, tổng hợp Brand Voice DNA, và xuất ra 5 file sẵn sàng sử dụng — bao gồm system prompt có thể dán thẳng vào bất kỳ AI nào.

**Không cần code. Không cần cài đặt. Chỉ cần Claude Code.**

---

## Bắt đầu

Mở project trong Claude Code và gõ:

```
xây dựng brand voice
```

Để kiểm tra content đã có đúng giọng thương hiệu chưa:

```
drift check [dán nội dung vào đây]
```

---

## Kết quả sau khi chạy

5 file được lưu vào `brand-voice-output/{tên-brand}-{ngày}/`:

| File | Mục đích |
|------|----------|
| `01_brand-voice-card.md` | Tài liệu tham khảo cho team, agency, copywriter |
| `02_brand-voice-system-prompt.md` | Dán vào system prompt của bất kỳ AI agent nào |
| `03_platform-variants.json` | Quy tắc riêng cho Facebook, LinkedIn, Email, Chatbot |
| `04_geo-brand-summary.md` | Copy chuẩn cho Google Business, LinkedIn, trang About |
| `05_drift-checker-rubric.json` | Rubric chấm điểm để kiểm tra content định kỳ |

---

## Cấu trúc Agent

Agent được xây dựng hoàn toàn bằng file markdown. Mỗi skill là một file `.md` với hướng dẫn cho Claude thực hiện một nhiệm vụ cụ thể. Các skill giao tiếp với nhau thông qua các file JSON trong thư mục `session/`.

```
brand-voice/
├── 00_orchestrator/
│   └── brand-voice-agent.md        ← Điểm vào, điều phối toàn bộ quy trình
│
├── 01_intake/
│   └── 01_brand-brief/
│       └── brand-brief.md          ← Thu thập thông tin nền tảng
│
├── 02_discovery/
│   ├── 01_competitor-analyzer/
│   │   ├── 01_with-competitor/
│   │   │   └── competitor-analyzer-with.md    ← Nghiên cứu đối thủ có tên
│   │   └── 02_without-competitor/
│   │       └── competitor-analyzer-without.md ← Phân tích toàn ngành
│   ├── 02_content-scanner/
│   │   └── content-scanner.md      ← Quét content hiện có của thương hiệu
│   └── 03_interview/
│       └── brand-interview.md      ← Phỏng vấn brand DNA chuyên sâu
│
├── 03_extraction/
│   └── 01_voice-synthesizer/
│       └── voice-synthesizer.md    ← Tổng hợp tất cả → Brand Voice DNA
│
├── 04_output/
│   ├── 01_brand-voice-card/
│   │   └── brand-voice-card.md     → 01_brand-voice-card.md
│   ├── 02_platform-adaptor/
│   │   └── platform-adaptor.md     → 03_platform-variants.json
│   ├── 03_geo-brand-summary/
│   │   └── geo-brand-summary.md    → 04_geo-brand-summary.md
│   └── 04_skill-file-generator/
│       └── skill-file-generator.md → 02_system-prompt + 05_rubric
│
├── 05_maintenance/
│   └── 01_drift-detector/
│       └── drift-detector.md       ← Chấm điểm và kiểm tra content định kỳ
│
├── session/                        ← Dữ liệu trung gian giữa các skill
├── brand-voice-output/             ← File kết quả cuối cùng
├── .env                            ← Perplexity API key (tùy chọn)
└── README.md
```

---

## Cách Agent Hoạt Động

### Tổng quan quy trình

```
[Khách hàng] → Brand Brief → Phân tích đối thủ → Quét Content → Phỏng vấn
                                                                      ↓
                                                             Voice Synthesizer
                                                                      ↓
                              Brand Voice Card ←─────────── Voice DNA ─────────→ Platform Adaptor
                              System Prompt   ←─────────────────────────────────→ Geo Summary
                              Drift Rubric    ←────────────────────────────────────────────────
                                                                      ↓
                                                              5 File Output
```

### Luồng dữ liệu giữa các skill

Các skill không gọi trực tiếp nhau — chúng giao tiếp qua file JSON trong `session/`:

| File | Được tạo bởi | Được đọc bởi |
|------|-------------|--------------|
| `session/brief.json` | brand-brief | interview, voice-synthesizer |
| `session/competitor-analysis.json` | competitor skills | interview, voice-synthesizer |
| `session/content-scan.json` | content-scanner | interview, voice-synthesizer |
| `session/interview.json` | brand-interview | voice-synthesizer |
| `session/voice-dna.json` | voice-synthesizer | tất cả output skills |

---

## Chi Tiết Từng Skill

### 00 · Brand Voice Agent (Orchestrator)
**File:** `00_orchestrator/brand-voice-agent.md`

Điểm vào duy nhất của toàn bộ hệ thống. Đọc trạng thái session hiện tại, quyết định skill nào cần chạy tiếp theo, và dẫn dắt người dùng qua từng bước. Không tự thực hiện bất kỳ phân tích nào — nhiệm vụ duy nhất là điều phối.

Ở bước đầu tiên, orchestrator kiểm tra `.env` để xem có Perplexity API key không. Nếu có, phân tích đối thủ sẽ sâu hơn. Nếu không, tự động dùng WebSearch thay thế.

---

### 01 · Brand Brief
**File:** `01_intake/01_brand-brief/brand-brief.md`

Thu thập 7 thông tin nền tảng của thương hiệu qua cuộc trò chuyện tự nhiên — không phải bảng câu hỏi. Hỏi từng câu một, đọc câu trả lời trước khi hỏi tiếp.

**7 thông tin cần có:**
1. Tên thương hiệu
2. Ngành nghề (cụ thể)
3. Địa điểm hoạt động
4. Khách hàng mục tiêu
5. Phân khúc giá
6. URL content hiện có (nếu có)
7. Tên đối thủ cụ thể (nếu biết)

**Output:** `session/brief.json` với hai cờ định tuyến:
- `has_old_content` — có content cũ để quét không?
- `knows_competitor` — có tên đối thủ cụ thể không?

Hai cờ này quyết định hướng đi của toàn bộ phần discovery.

---

### 02 · Competitor Analyzer — Có Tên Đối Thủ
**File:** `02_discovery/01_competitor-analyzer/01_with-competitor/competitor-analyzer-with.md`

Chạy khi `knows_competitor = true`. Nghiên cứu từng đối thủ được nêu tên — không phải họ làm gì, mà **họ nói chuyện như thế nào**.

Dùng Perplexity API (nếu có key) hoặc WebSearch để tìm website, Facebook, LinkedIn của từng đối thủ. Phân tích tone, cụm từ lặp lại, chủ đề và định vị.

Kết quả quan trọng nhất là `gap_opportunity`: khoảng trắng trong brand voice mà đối thủ đã bỏ ngỏ — và khách hàng có thể chiếm lĩnh.

**Output:** `session/competitor-analysis.json`

---

### 03 · Competitor Analyzer — Không Có Tên Đối Thủ
**File:** `02_discovery/01_competitor-analyzer/02_without-competitor/competitor-analyzer-without.md`

Chạy khi `knows_competitor = false`. Dùng kiến thức của Claude để lập bản đồ toàn ngành dựa trên `industry`, `location` và `price_point` từ brief.

Xác định: các mẫu tone chiếm ưu thế, cụm từ bị dùng nhiều đến mức vô nghĩa, các nhóm định vị trong ngành, và quan trọng nhất — vị trí brand voice chưa ai chiếm.

**Output:** `session/competitor-analysis.json`

---

### 04 · Content Scanner
**File:** `02_discovery/02_content-scanner/content-scanner.md`

Chạy khi `has_old_content = true`. Dùng WebFetch để tải URL từ brief, hoặc nhận text được dán trực tiếp. Phân tích để tìm các mẫu vô thức trong văn bản hiện tại của thương hiệu.

Tìm kiếm: cấu trúc lặp lại, tone thực sự (thường khác tone họ nghĩ họ đang có), từ ngữ thường dùng, nhịp câu, điểm mạnh và điểm yếu.

Đây thường là bước tiết lộ nhất — khách hàng hay nói "wow, tôi không nhận ra mình đang làm vậy."

**Output:** `session/content-scan.json`

---

### 05 · Brand Interview
**File:** `02_discovery/03_interview/brand-interview.md`

Skill quan trọng nhất trong toàn bộ quy trình. Tiến hành phỏng vấn chuyên sâu với founder để kéo ra những điều chỉ họ mới có thể nói — cụ thể, có chính kiến, không đối thủ nào dám nhận.

**8 câu hỏi cốt lõi** xoay quanh 4 chủ đề:
- Khách hàng nói gì về thương hiệu
- Thương hiệu không muốn bị nhầm với ai
- Cá tính của thương hiệu nếu là người
- Điều thương hiệu tin mà đối thủ không tin

**Cơ chế follow-up:** Khi câu trả lời mơ hồ ("chuyên nghiệp", "thân thiện", "đam mê"), skill tự động đặt câu hỏi khai thác sâu hơn để biến tính từ chung thành đặc điểm cụ thể.

**Output:** `session/interview.json` — bản ghi đầy đủ và danh sách trích dẫn quan trọng.

---

### 06 · Voice Synthesizer
**File:** `03_extraction/01_voice-synthesizer/voice-synthesizer.md`

Đọc tất cả 4 file session và tổng hợp thành Brand Voice DNA — nguồn sự thật duy nhất cho toàn bộ phần output.

**4 bước tổng hợp:**
1. Chiết xuất tín hiệu chân thực từ trích dẫn phỏng vấn
2. Đối chiếu với content scan (tone thực tế vs. tone họ nghĩ họ có)
3. Định vị so với thị trường (khác biệt thực sự là gì)
4. Chuyển tính cách thành quy tắc viết cụ thể

Trước khi lưu, kiểm tra: mô tả này có áp dụng được cho đối thủ không? Nếu có, chưa đủ cụ thể.

**Output:** `session/voice-dna.json`

---

### 07 · Brand Voice Card
**File:** `04_output/01_brand-voice-card/brand-voice-card.md`

Tạo tài liệu tham khảo dành cho con người từ Voice DNA. Đối tượng: copywriter, social media manager, agency partner — những người cần hiểu giọng thương hiệu mà không cần qua phỏng vấn.

Bao gồm: 3 tính cách cốt lõi với ví dụ hành vi, bảng từ cấm có lý do cụ thể, từ signature và cách dùng, phong cách câu, và ví dụ đúng/sai cho cùng một tình huống.

**Output:** `brand-voice-output/{brand}/01_brand-voice-card.md`

---

### 08 · Platform Adaptor
**File:** `04_output/02_platform-adaptor/platform-adaptor.md`

Tạo quy tắc voice theo từng nền tảng. Cá tính cốt lõi không thay đổi — chỉ có cách thể hiện thích nghi theo định dạng và kỳ vọng của từng nền tảng.

**4 nền tảng:** Facebook (ngắn, cảm xúc), LinkedIn (thực chất, chuyên môn), Email (lời chào + ký tên thiết lập tone), Chatbot (hội thoại, ngắn, giữ cá tính kể cả khi xin lỗi).

Mỗi nền tảng đi kèm một ví dụ thực tế — không phải placeholder.

**Output:** `brand-voice-output/{brand}/03_platform-variants.json`

---

### 09 · Geo Brand Summary
**File:** `04_output/03_geo-brand-summary/geo-brand-summary.md`

Tạo mô tả thương hiệu chuẩn hóa cho các nền tảng AI search (Perplexity, Google AI) và directory (Google Business, LinkedIn).

**Template 4 câu cố định:**
1. Nhận diện thực tế (không tính từ hoa mỹ)
2. Niềm tin cốt lõi (rút từ trích dẫn phỏng vấn — phải bất ngờ)
3. Khách hàng lý tưởng (cụ thể để người đúng tự nhận ra)
4. Điều thương hiệu KHÔNG là (tăng tính tin cậy)

Kèm phiên bản tiếng Anh và hướng dẫn nền tảng nào dùng phần nào.

**Output:** `brand-voice-output/{brand}/04_geo-brand-summary.md`

---

### 10 · Skill File Generator
**File:** `04_output/04_skill-file-generator/skill-file-generator.md`

Bước lắp ráp cuối cùng. Tạo 2 file chưa được skill nào xử lý:

**`02_brand-voice-system-prompt.md`** — File quan trọng nhất. Lấy Voice DNA và đóng gói thành system prompt sẵn sàng dán vào ChatGPT, Claude, Gemini, hay bất kỳ AI agent nào. Người dùng không cần hiểu prompt engineering — copy và paste là xong.

**`05_drift-checker-rubric.json`** — Rubric máy tính được để drift-detector chấm điểm content. Bao gồm: danh sách từ cấm, từ signature, ngưỡng điểm, hệ số trừ/cộng, và quy tắc theo từng nền tảng.

Sau đó ghi tất cả 5 file ra đĩa và thông báo bàn giao cho người dùng.

**Output:** Toàn bộ thư mục `brand-voice-output/{brand}-{ngày}/`

---

### 11 · Drift Detector
**File:** `05_maintenance/01_drift-detector/drift-detector.md`

Skill bảo trì — dùng sau khi onboarding xong để kiểm tra content mới có đúng giọng thương hiệu không. Đây là lý do khách hàng trả retainer hàng tháng.

**Cách dùng:** Chia sẻ bất kỳ nội dung nào kèm "drift check". Agent tự tìm rubric, chấm điểm từ 0-1, và báo cáo:
- Điểm tổng và có vượt ngưỡng không
- Từng vi phạm với vị trí cụ thể
- Bản viết lại đề xuất cho từng câu bị gắn cờ
- Những điểm đang làm đúng

Kết quả có thể lưu vào `drift-logs/` để theo dõi chất lượng content theo thời gian.

---

## Định Tuyến Theo 4 Hướng

Sau khi Brand Brief hoàn tất, orchestrator định tuyến theo 4 hướng dựa trên 2 cờ:

| Hướng | `has_old_content` | `knows_competitor` | Discovery chạy |
|-------|-------------------|--------------------|----------------|
| A | ✅ | ✅ | Content Scanner + Competitor (có tên) |
| B | ✅ | ❌ | Content Scanner + Competitor (toàn ngành) |
| C | ❌ | ✅ | Competitor (có tên) |
| D | ❌ | ❌ | Competitor (toàn ngành) |

Content Scanner và Competitor Analyzer chạy song song ở hướng A và B.

---

## Tùy Chọn: Perplexity API

Mặc định, agent dùng WebSearch tích hợp sẵn trong Claude Code để nghiên cứu đối thủ. Nếu muốn kết quả sâu hơn, thêm Perplexity API key:

1. Lấy key tại [perplexity.ai/settings/api](https://www.perplexity.ai/settings/api)
2. Mở file `.env` trong project
3. Dán key vào: `PERPLEXITY_API_KEY=your_key_here`

Agent tự phát hiện key khi chạy và dùng Perplexity thay cho WebSearch.

---

## Yêu Cầu

- [Claude Code](https://claude.ai/code) (CLI hoặc desktop app)
- Không cần cài thêm gì — không có dependencies, không có build step
- Perplexity API key là tùy chọn, không bắt buộc
