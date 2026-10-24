# Facebook Content Agent — Skill Structure (v3.2)

> **v3 thay đổi gì?** Đối chiếu với 2026 SOTA (Microsoft Agent Framework, Sprout Social Trellis, Hootsuite OwlyWriter, Jasper Social) + FB algorithm 2026 + luật quảng cáo VN có hiệu lực 15/2/2026 và 1/7/2026. Xem **Changelog** ở cuối file.
> **v3.1 thêm gì?** `fb-content-agent` — orchestrator trung tâm, entry point duy nhất, quản lý toàn bộ 28 skill còn lại.
> **v3.2 thêm gì?** `fb-content-brief` — reverse-engineer nội dung có sẵn thành content brief có cấu trúc. 4 modes: analyze / brief-for-rewrite / brief-for-repurpose / series.

---

## Architecture Overview

```
[User Input]
     │
     ▼
╔═══════════════════════════════════════════════════════════════╗
║              fb-content-agent  (ORCHESTRATOR)                 ║
║                                                               ║
║  ┌──────────────────────────────────────────────────────┐    ║
║  │ 1. Parse intent + clarify nếu mơ hồ                 │    ║
║  │ 2. Tạo execution plan → show user trước khi chạy    │    ║
║  │ 3. Dispatch skill theo branch (publishing / strategy)│    ║
║  │ 4. Pipe output N → input N+1                        │    ║
║  │ 5. PAUSE tại review-queue nếu cần human approval    │    ║
║  │ 6. Handle lỗi: retry / fallback / stop              │    ║
║  │ 7. Checkpoint state sau mỗi skill                   │    ║
║  │ 8. Aggregate output → trả về user                   │    ║
║  └──────────────────────────────────────────────────────┘    ║
║                                                               ║
║  ┌──────────────────────┐                                     ║
║  │ brand-voice-loader   │ 🔒 GATE                             ║
║  └──────────────────────┘                                     ║
║           │                                                   ║
║           ▼                                                   ║
║  ┌──────────────────────┐                                     ║
║  │ task-router          │                                     ║
║  └──────────────────────┘                                     ║
║           │                                                   ║
║     ┌─────┴──────────────────────────────┐                   ║
║     ▼ (Publishing)       ▼ (Strategy /   ║                   ║
║  format-selector          Analytics)     ║                   ║
║     │                         │          ║                   ║
║     ▼                         │          ║                   ║
║  performance-memory (read)    │          ║                   ║
║     │                         │          ║                   ║
║     ▼                         │          ║                   ║
║  Content Creation skill       │          ║                   ║
║     │                         │          ║                   ║
║     ▼                         │          ║                   ║
║  DISTRIBUTION DESIGN LAYER    │          ║                   ║
║     │                         │          ║                   ║
║     ▼                         │          ║                   ║
║  QUALITY & COMPLIANCE LAYER   │          ║                   ║
║     │                         │          ║                   ║
║     ▼                         │          ║                   ║
║  INTELLIGENCE LAYER           │          ║                   ║
║     │                         │          ║                   ║
║     ▼                         │          ║                   ║
║  fb-review-queue (HITL)       │          ║                   ║
║  ≥90% auto / 70–89% pause     │          ║                   ║
║  <70% reject+bounce           │          ║                   ║
║     │                         │          ║                   ║
║     ▼ ◄───────────────────────┘          ║                   ║
║  output-validator ✅ GATE                ║                   ║
║                                          ║                   ║
╚══════════════════════════════════════════╝                   ║
     │
     ▼
[Final Output: bài + visual brief + send time + confidence score + execution log]

         ┌──────────────────────────────────┐
         │ ASYNC: post performance →        │
         │ feedback vào performance-memory  │
         └──────────────────────────────────┘
```

---

## 🎛️ Orchestrator — Entry point duy nhất

### `fb-content-agent` 🆕
- **Mục đích**: Điểm tiếp nhận duy nhất — user chỉ nói chuyện với skill này. Nó dispatch, pipe, pause, retry, và aggregate toàn bộ 28 skill còn lại.
- **Input**: Raw user message (bất kỳ ngôn ngữ, bất kỳ format)
- **Output**: Final content package gồm: bài đã validate + visual brief + send time + confidence score + execution log

#### 3 chế độ hoạt động

| Confidence | Mode | Orchestrator làm gì |
|-----------|------|---------------------|
| ≥ 90% | Auto | Chạy toàn pipeline → trả output ngay |
| 70–89% | Semi-auto | Pause tại `fb-review-queue` → notify Gmail → chờ approve/edit/reject → tiếp tục |
| < 70% | Manual | Auto-reject → báo skill nào fail + lý do → hỏi user muốn rewrite không |

#### Plan-first approach
Trước khi chạy, orchestrator tạo execution plan và xác nhận với user:
```
User: "viết bài ra mắt serum vitamin C, mục tiêu convert"

fb-content-agent:
  Tôi sẽ thực hiện:
  1. Load brand voice Lana Skin
  2. Format: Carousel 7 slides (lý do: product launch + nhiều thông tin)
  3. Viết bài → thêm discussion triggers → quality check → policy check
  4. Score save/share → gợi ý đăng lúc 20:00–21:00 (peak audience)
  Bắt đầu không?
```

#### Error handling

| Tình huống | Xử lý |
|---|---|
| `brand-voice-loader` không tìm thấy folder | Stop toàn bộ, báo path lỗi, hỏi user |
| `policy-checker` Block | Dừng pipeline, không bypass, bắt rewrite bắt buộc |
| Skill không bắt buộc fail | Log lỗi + tiếp tục với degraded output, note rõ trong log |
| `output-validator` fail | Bounce về skill fail tương ứng, max 2 lần retry rồi báo user |
| HITL timeout (reviewer không reply sau SLA) | Gửi Gmail lần 2 → nếu vẫn không có → notify user tự quyết định |

#### State & checkpoint
```json
{
  "task_id": "uuid",
  "status": "running | paused_hitl | completed | failed",
  "current_step": "fb-policy-checker",
  "completed_steps": ["brand-voice-loader", "task-router", "..."],
  "outputs": { "fb-post-writer": "...", "fb-visual-brief": "..." },
  "confidence_scores": { "fb-post-writer": 0.87 },
  "hitl_decision": null
}
```
Lưu tại `memory/task-state.json`. Nếu pipeline bị ngắt giữa chừng → resume từ bước cuối đã xong, không chạy lại từ đầu.

#### Execution log (observability)
```
[10:32:01] brand-voice-loader       ✅  234ms
[10:32:02] task-router              ✅   89ms  → publishing/carousel
[10:32:03] fb-format-selector       ✅  120ms  → carousel 7 slides
[10:32:05] fb-carousel-architect    ✅  3.2s   confidence: 0.91
[10:32:06] fb-discussion-architect  ✅  1.1s
[10:32:07] fb-policy-checker        ⚠️  890ms  2 flags → auto-fix
[10:32:09] fb-save-share-optimizer  ✅  560ms  save: 8/10  share: 7/10
[10:32:10] fb-review-queue          ✅   —     confidence 0.91 → auto-publish
[10:32:11] output-validator         ✅   —     11/11 ✓
```

---

## 🔒 Gate — Bắt buộc (chạy trước mọi skill)

### `brand-voice-loader` (refactored output)
- **Mục đích**: Đọc brand voice folder, extract context, inject vào tất cả skill phía sau
- **Input**: Path tới brand voice folder
- **Output (v3 structured)**:
  ```yaml
  tone: ...
  audience_persona: ...
  pillars: [...]
  approved_glossary: [...]   # 🆕 từ ngữ ưu tiên dùng
  banned_terms: [...]        # 🆕 từ tuyệt đối tránh (knowledge graph style)
  approved_examples: [...]
  ```
- **Ghi chú v3**: Tách `donts.md` thành cấu trúc query được — agent có thể check `if word in banned_terms` thay vì scan free-form text. Khớp approach của Writer/Jasper.

**Brand voice folder structure (cập nhật):**
- `01-tone.md`, `02-audience.md`, `03-pillars.md`, `04-examples.md` (giữ nguyên)
- `05-glossary.json` 🆕 — `{ approved: [...], banned: [...], reasoning: {...} }`

---

## 🧭 Router & Format

### `task-router`
- **Mục đích**: Phân loại intent → chọn category skill
- **Output**: Category + skill cụ thể + branch (publishing path / non-publishing path)
- **Lưu ý**: Intent mơ hồ → hỏi user, không đoán

### `fb-format-selector`
- **Mục đích**: Quyết định format trước khi viết
- **Input**: Chủ đề + mục tiêu + audience + recommendation từ `performance-memory`
- **Output**: Format khuyến nghị (single image / carousel / Reel / live / story / link post) + lý do
- **Lưu ý**: Mid-2025 Meta gộp tất cả video → Reels. Format selector phải biết khi nào pick Reel thay vì video post.

---

## ✍️ Content Creation (5 skills)

### `fb-content-brief` 🆕
- **Mục đích**: Reverse-engineer nội dung có sẵn thành content brief có cấu trúc — X-ray bài để thấy hook formula, structure pattern, tone, emotion trigger, engagement target
- **Input**: `source_content` (bài paste vào) + `mode` + `brand_voice`
- **Modes**:
  - `analyze`: chỉ phân tích, không tạo brief forward — trả insight đầy đủ
  - `brief-for-rewrite`: phân tích + tạo brief cho `fb-post-writer mode=iterate`
  - `brief-for-repurpose`: phân tích + tạo brief kèm cấu trúc carousel/reels cho `fb-repurpose` hoặc `fb-carousel-architect`
  - `series`: phân tích 3–5 bài, tổng hợp pattern chung → formula sheet cho `fb-pillar-planner` hoặc `fb-post-writer`
- **Output**: `analysis` (hook type + score, structure, tone, funnel stage, brand voice alignment) + `rewrite_brief` hoặc `repurpose_brief` hoặc `formula_sheet` tuỳ mode
- **Trigger tự động**: khi user paste nội dung vào, nói "viết lại bài này", "học theo bài này", "brief lại bài này", "tìm pattern từ nhiều bài"
- **Vị trí pipeline**: optional step sau `fb-format-selector`, trước content skill (publishing branch) — hoặc standalone (content-brief branch)
- **Lưu ý**: Không viết lại bài gốc trong bất kỳ mode nào. Chỉ phân tích và brief. Giữ brand_voice alignment check để phát hiện gap khi học theo bài đối thủ.

### `fb-post-writer` (mở rộng)
- **Mục đích**: Viết bài Facebook feed hoàn chỉnh — gộp luôn hook generation, CTA writing, và A/B variant iteration
- **Input**: Chủ đề + mục tiêu + funnel stage (TOFU/MOFU/BOFU) + mode (`fresh` / `iterate`)
- **Modes**:
  - `mode=fresh`: tạo 2–3 variants từ đầu, mỗi variant có hook + body + CTA khác nhau
  - `mode=iterate`: nhận bài có sẵn + element cần test (`hook` / `cta` / `tone` / `length`) → output 3–5 variants chỉ thay đổi đúng element đó
- **Output**: Variant(s) gồm hook, body, CTA, đã map vào pillar
- **Lưu ý v3**: Đã hấp thụ `fb-hook-generator`, `fb-caption-variants`, `fb-cta-writer` của v2. Gộp lại để tránh multi-agent overhead (Princeton NLP 2026: multi-agent thêm 2.1% accuracy nhưng gấp 10–30× latency).

### `fb-repurpose`
- **Mục đích**: Chuyển hóa nội dung từ nguồn khác thành native FB post
- **Input**: Link / nội dung gốc (blog, podcast, báo cáo, email, video YouTube)
- **Output**: Bài FB viết lại đúng tone mạng xã hội
- **Lưu ý**: Ưu tiên insight trực tiếp trên post, không chỉ link out. Nếu có link external → chuyển xuống first comment (phối hợp với `fb-first-comment-strategy`).

### `fb-reels-script` (nâng cấp với retention engineering)
- **Mục đích**: Viết script cho Reels — tối ưu **completion rate**, không chỉ length
- **Input**: Chủ đề + thời lượng mục tiêu (15s / 30s / 60s)
- **Output**:
  - **Hook 0–3s**: visual + voiceover (visual quan trọng hơn chữ)
  - **Retention curve plan**: pattern interrupt mỗi 5–7s (cut, zoom, text pop, sound shift)
  - **Voiceover script** chia theo beat (timestamp)
  - **On-screen text overlays**
  - **Loop close**: kết nối kết thúc với mở đầu để user xem lại (replay = watch time gấp đôi)
  - **CTA cuối + caption đăng kèm**
- **Lưu ý v3**: FB algorithm 2026 — 15s xem hết > 60s bị lướt. UTIS model (Meta, 1/2026) survey "video này có khớp interest không" → must align với audience persona từ `brand-voice-loader`.

### `fb-carousel-architect`
- **Mục đích**: Thiết kế multi-slide carousel (engagement gấp 1.5–3 lần single image)
- **Input**: Chủ đề + số slide (5–10)
- **Output**: Cover slide (hook), từng slide reveal value, slide CTA cuối, caption đi kèm
- **Lưu ý**: Mỗi slide phải đứng được một mình + tạo open loop sang slide sau

---

## 🧭 Strategy (4 skills — không đổi)

### `fb-content-calendar`
- **Mục đích**: Lên lịch content 1 tuần / 1 tháng
- **Input**: Chủ đề tháng + key dates + tần suất (3–5 bài/tuần) + recommendation từ `fb-send-time-optimizer`
- **Output**: Bảng ngày – giờ – chủ đề – format – pillar – CTA

### `fb-pillar-planner`
- **Mục đích**: Xây / rà soát 3–5 content pillars
- **Input**: Thông tin thương hiệu + mục tiêu marketing
- **Output**: Pillars + mô tả + tỷ lệ phân bổ + ví dụ bài cho mỗi pillar

### `fb-trend-researcher`
- **Mục đích**: Tìm trending topics phù hợp ngành + brand
- **Input**: Ngành + khoảng thời gian
- **Output**: Trend list + angle gợi ý phù hợp brand voice
- **Lưu ý**: Web search real-time

### `fb-hashtag-strategy`
- **Mục đích**: Hashtag theo mục tiêu reach
- **Input**: Chủ đề + mục tiêu (branded / niche / trending)
- **Output**: 3 nhóm hashtag + lý do

---

## 💬 Engagement (3 skills — gọn hơn v2)

### `fb-comment-reply`
- **Mục đích**: Soạn reply phù hợp brand voice
- **Input**: Comment gốc + loại (câu hỏi / feedback tiêu cực / khen / spam / khủng hoảng viral)
- **Output**: Phản hồi tự nhiên, không robotic
- **Lưu ý**: Loại "khủng hoảng viral" → ưu tiên de-escalation, không phòng thủ

### `fb-story-arc`
- **Mục đích**: Bài kể chuyện theo cung bậc cảm xúc
- **Input**: Loại story (founder / behind-the-scenes / customer / product)
- **Output**: Bài narrative arc rõ: setup → conflict → resolution

### `fb-ad-copy`
- **Mục đích**: Copy cho paid post / quảng cáo FB
- **Input**: Format ad (image / video / carousel / collection) + mục tiêu campaign
- **Output**: Primary text + headline + description + CTA button text
- **Lưu ý v3**: Với video ad, phải tuân thủ luật VN 15/2/2026 — skip button hiệu quả sau 5s. Built-in compliance check.

---

## 🚀 Distribution Design Layer 🆕 (2 skills)

Layer này tối ưu cho **Meaningful Social Interactions (MSI)** của FB algorithm 2026 — khi 1 Save = 50 Likes, post sinh nhiều luồng comment được boost reach mạnh.

### `fb-discussion-architect` 🆕
- **Mục đích**: Thiết kế bài để invite multi-thread comment — nhiều nhóm audience comment vì lý do khác nhau
- **Input**: Bài đã viết
- **Output**: Bài chỉnh sửa với 2–3 "trigger points":
  - **Identity trigger**: câu hỏi audience phải tự nhận mình thuộc nhóm nào
  - **Opinion trigger**: hot take khiến audience muốn đồng ý / phản đối
  - **Experience trigger**: câu hỏi mời share trải nghiệm cá nhân
- **Lưu ý**: Algorithm 2026 — post có 10 comment ý nghĩa > post 100 like. Multi-thread comment > single-thread.

### `fb-first-comment-strategy`
- **Mục đích**: Tối ưu first comment — đòn bẩy reach
- **Input**: Bài chính + có link external không + loại tương tác muốn
- **Output**:
  - First comment seed (link đặt ở đây thay vì trong body để tránh penalty)
  - 2–3 comment "mồi" cho team comment trong 30 phút đầu
  - Câu hỏi pin để trigger comment từ audience
- **Lưu ý**: FB penalize bài có outbound link trong body; chuyển link xuống first comment giữ reach.

---

## 📊 Analytics (3 skills — không đổi cấu trúc)

### `fb-performance-review`
- **Mục đích**: Phân tích hiệu quả content
- **Input**: Metrics (engagement, reach, follower growth, link clicks, **save rate, share rate, watch time**)
- **Output**: Nhận xét + gợi ý điều chỉnh
- **Lưu ý v3**: Phải track Save rate và Share rate (signal mạnh nhất 2026), watch-time completion với Reels. Output feed vào `performance-memory`.

### `fb-content-audit`
- **Mục đích**: Rà soát feed hiện tại
- **Input**: Danh sách bài gần nhất (text/CSV)
- **Output**: Đánh giá pillar balance, tone consistency, content gap, **Save:Like ratio và Share:Like ratio per post**

### `fb-competitor-scan`
- **Mục đích**: Phân tích content đối thủ
- **Input**: Tên / link page đối thủ
- **Output**: Pattern content + cơ hội differentiation + benchmark engagement rate

---

## 🧠 Intelligence Layer 🆕 (3 skills)

Layer này lo "agent có não" — dùng dữ liệu quá khứ để tối ưu quyết định hiện tại.

### `performance-memory` 🆕
- **Mục đích**: Memory layer — kết nối Analytics ngược về Content Creation. Agent v2 stateless; v3 có ký ức.
- **Input** (write): output từ `fb-performance-review` sau mỗi bài
- **Output** (read): khi bắt đầu task mới, trả về:
  - Top 5 bài perform tốt nhất trong topic tương tự
  - Pattern: hook nào, format nào, độ dài nào hay win
  - Anti-pattern: format/topic đã thử và flop
- **Storage**: file JSON đơn giản trong `memory/post-history.json`, không cần DB
- **Lưu ý**: 2026 SOTA — agent học từ chính output của mình. Không có loop này = mỗi bài viết đều bắt đầu từ zero.

### `fb-save-share-optimizer` 🆕
- **Mục đích**: Chấm bài theo "save-worthiness" và "share-worthiness" trước khi publish
- **Input**: Bài đã qua quality layer
- **Output**:
  - Save score (0–10): bài có đáng lưu lại để xem sau không? (utility, reference, checklist, framework)
  - Share score (0–10): share bài này có làm người share trông tốt hơn không? (status signal, hot take, useful insight)
  - Gợi ý chỉnh để tăng score
- **Lưu ý**: Algorithm 2026 — 1 Save = 50 Likes, 1 Share to Story = 50 Likes. Đây là metric quan trọng nhất, không phải Like/Comment.

### `fb-send-time-optimizer` 🆕
- **Mục đích**: Recommend giờ publish dựa trên audience activity pattern
- **Input**: Audience persona + lịch sử engagement (từ `performance-memory`) + format bài
- **Output**: Top 3 time slot khuyến nghị + lý do (audience peak, ít competitor post, format-specific timing)
- **Lưu ý**: Hootsuite + Sprout đều có tính năng này như standard. Không có = thiếu sót cơ bản so với pro tools.

---

## 🎨 Quality & Compliance Layer (4 skills)

Chạy *sau* skill chính + Distribution Design Layer, *trước* `fb-review-queue`. Mỗi skill là filter độc lập, có thể bật/tắt theo từng bài.

### `fb-readability-formatter`
- **Mục đích**: Format trình bày, không sửa nội dung
- **Output**: Ngắt dòng 1–2 câu, "see more" cliff đúng vị trí, emoji làm visual anchor, rhythm xen kẽ ngắn/dài

### `fb-visual-brief`
- **Mục đích**: Brief hình/video cho designer
- **Output**: Concept, text overlay, color direction, tỷ lệ (1:1 / 4:5 / 9:16)
- **Lưu ý**: Là brief cho người, không phải AI prompt

### `fb-vietnamese-localizer`
- **Mục đích**: Localize sâu cho VN — register, idiom, văn hoá
- **Output**: Chọn xưng hô nhất quán (anh/chị/em/bạn/mình/cô chú), flag idiom dịch gượng, gợi ý reference văn hoá VN nếu trong 2 tuần tới có dịp (Tết, 8/3, 20/10, 20/11, Trung thu, mùa thi…)
- **Lưu ý**: Không "Việt hoá" bằng tiếng lóng nếu brand voice trang trọng

### `fb-policy-checker` (cập nhật luật VN 2026)
- **Mục đích**: Gate kiểm duyệt FB Community Standards + Ad Policies + **luật VN 2026**
- **Output**: Pass / Flag / Block + highlight câu vi phạm + gợi ý câu thay thế
- **Rule modules**:
  - **FB chung**: claim quá đáng, "cam kết", "100%", before/after, từ y khoa
  - **🆕 Luật VN 15/2/2026 (quảng cáo online)**: Video ad ≥ 5s phải có nút skip rõ ràng, 1-click close
  - **🆕 Nghị định Mỹ phẩm VN hiệu lực 1/7/2026**: Label & advertising siết chặt, post-market surveillance
  - **Ngành nhạy cảm VN**: mỹ phẩm, TPCN, tài chính, giảm cân, before/after, y tế — strict mode
- **Lưu ý**: Block = không qua review queue, bắt rewrite. Tuyến phòng thủ #1 chống bay reach / disable account / bị phạt theo luật mới.

---

## 👥 Human-in-the-Loop 🆕 (1 skill)

### `fb-review-queue` 🆕
- **Mục đích**: Confidence-based routing — gap quan trọng nhất so với pro agents (Sprout, Hootsuite, Jasper đều có)
- **Input**: Output từ Quality & Compliance Layer + confidence score từ mỗi skill trước
- **Logic routing**:
  | Confidence | Action |
  |-----------|--------|
  | ≥ 90% | ✅ Auto-publish (qua `output-validator` xong là post) |
  | 70–89% | 👤 Vào human review queue, chờ approve/reject/edit |
  | < 70% | ❌ Auto-reject, ghi reason, bounce về `fb-post-writer` rewrite |
- **Output**:
  - Auto-publish path: bài + meta info chuyển sang `output-validator`
  - Review path: bài + reasoning ("vì sao cần review") + proposed edits
  - Reject path: bài + lý do cụ thể + skill nào fail
- **Target**: 10–15% bài vào review queue (industry standard 2026)
- **Lưu ý**: SLA tracking — review trong 4h cho post thường, 1h cho ad. Feedback từ reviewer (approve/edit/reject) feed về `performance-memory` để cải thiện confidence model.

---

## ✅ Output Gate (chạy sau cùng)

### `output-validator` (checklist 11 điểm — mở rộng v3)
- **Mục đích**: Final check trước khi trả output cho user
- **Checklist**:
  - [ ] Đúng tone từ brand voice
  - [ ] Không vi phạm `banned_terms` từ glossary
  - [ ] Hook rõ ràng trong 3 dòng đầu
  - [ ] Đúng content pillar
  - [ ] CTA phù hợp mục tiêu
  - [ ] Pass `fb-policy-checker` (gồm luật VN 2026)
  - [ ] Đã qua `fb-readability-formatter`
  - [ ] Có visual brief từ `fb-visual-brief`
  - [ ] Format khớp `fb-format-selector`
  - [ ] **Save score ≥ 6 hoặc Share score ≥ 6** từ `fb-save-share-optimizer` 🆕
  - [ ] **Có routing decision từ `fb-review-queue`** 🆕
- **Output**: Bài đã validate + visual brief + send time gợi ý + confidence score + routing decision

---

## Pipeline theo loại task

**Bài feed thường (publishing):**
```
loader → router → format-selector → performance-memory →
fb-post-writer → discussion-architect → first-comment-strategy →
[quality layer 4 skills] → save-share-optimizer → send-time-optimizer →
review-queue → validator
```

**Publishing với nội dung có sẵn (brief → rewrite):**
```
loader → router → format-selector → performance-memory →
fb-content-brief → fb-post-writer (mode=iterate) →
discussion-architect → first-comment-strategy →
[quality layer 4 skills] → save-share-optimizer → send-time-optimizer →
review-queue → validator
```

**Phân tích / brief lại nội dung (standalone):**
```
loader → router → fb-content-brief → output-validator
```

**Bài Reels:**
```
loader → router → format-selector → performance-memory →
fb-reels-script → [quality layer] → save-share-optimizer →
send-time-optimizer → review-queue → validator
```

**Reply comment (lightweight):**
```
loader → router → fb-comment-reply →
vietnamese-localizer + policy-checker → validator
(skip readability, visual, send-time, review-queue)
```

**Lên kế hoạch tháng (non-publishing):**
```
loader → router → fb-content-calendar (gọi fb-send-time-optimizer
internally) → validator
```

**Audit feed:**
```
loader → router → fb-content-audit →
performance-memory (đọc lịch sử) → validator
```

---

## Summary table

| # | Layer | Skill | v3.1 Status |
|---|-------|-------|-----------|
| 0 | 🎛️ Orchestrator | **fb-content-agent** | 🆕 Entry point duy nhất |
| 1 | 🔒 Gate | brand-voice-loader | ♻️ Output thêm glossary structured |
| 2 | Router | task-router | giữ nguyên |
| 3 | Format | fb-format-selector | giữ nguyên |
| 4 | ✍️ Content | fb-post-writer | ♻️ Hấp thụ hook/CTA/variants từ v2 |
| 5 | ✍️ Content | fb-repurpose | giữ nguyên |
| 6 | ✍️ Content | fb-reels-script | ♻️ Thêm retention engineering |
| 7 | ✍️ Content | fb-carousel-architect | giữ nguyên |
| 8 | 🧭 Strategy | fb-content-calendar | ♻️ Tích hợp send-time-optimizer |
| 9 | 🧭 Strategy | fb-pillar-planner | giữ nguyên |
| 10 | 🧭 Strategy | fb-trend-researcher | giữ nguyên |
| 11 | 🧭 Strategy | fb-hashtag-strategy | giữ nguyên |
| 12 | 💬 Engagement | fb-comment-reply | giữ nguyên |
| 13 | 💬 Engagement | fb-story-arc | giữ nguyên |
| 14 | 💬 Engagement | fb-ad-copy | ♻️ Built-in luật VN 15/2/2026 |
| 15 | 🚀 Distribution | **fb-discussion-architect** | 🆕 |
| 16 | 🚀 Distribution | fb-first-comment-strategy | giữ nguyên |
| 17 | 📊 Analytics | fb-performance-review | ♻️ Thêm Save/Share/watch-time metrics |
| 18 | 📊 Analytics | fb-content-audit | ♻️ Thêm Save:Like, Share:Like ratio |
| 19 | 📊 Analytics | fb-competitor-scan | giữ nguyên |
| 20 | 🧠 Intelligence | **performance-memory** | 🆕 |
| 21 | 🧠 Intelligence | **fb-save-share-optimizer** | 🆕 |
| 22 | 🧠 Intelligence | **fb-send-time-optimizer** | 🆕 |
| 23 | 🎨 Quality | fb-readability-formatter | giữ nguyên |
| 24 | 🎨 Quality | fb-visual-brief | giữ nguyên |
| 25 | 🎨 Quality | fb-vietnamese-localizer | giữ nguyên |
| 26 | 🎨 Quality | fb-policy-checker | ♻️ Thêm rule luật VN 2026 |
| 27 | 👥 HITL | **fb-review-queue** | 🆕 |
| 28 | ✅ Gate | output-validator | ♻️ Checklist 5 → 11 điểm |
| 29 | ✍️ Content | **fb-content-brief** | 🆕 v3.2 |

**Tổng: 30 skills** (1 orchestrator + 29 skills chuyên biệt)

---

## Changelog v3.1 → v3.2

### Skills mới (1)
- 🆕 `fb-content-brief` — reverse-engineer nội dung có sẵn thành content brief có cấu trúc
  - 4 modes: `analyze` / `brief-for-rewrite` / `brief-for-repurpose` / `series`
  - X-ray hook type, structure pattern, tone, emotion trigger, engagement target, brand voice alignment
  - Output feed trực tiếp vào `fb-post-writer`, `fb-carousel-architect`, `fb-repurpose`, `fb-pillar-planner`
  - Trigger tự động khi user paste nội dung hoặc nói "viết lại bài này", "học theo bài này"

### Pipeline mới (1)
- 🆕 `content-brief` branch: `loader → router → fb-content-brief → output-validator`
- ♻️ `publishing` branch: thêm optional step `fb-content-brief` sau `performance-memory` khi có nội dung input

---

## Changelog v3 → v3.1

### Skills mới (1)
- 🆕 `fb-content-agent` — orchestrator trung tâm, entry point duy nhất
  - Plan-first: tạo execution plan, xác nhận với user trước khi chạy
  - 3 mode: auto (≥90%) / semi-auto HITL (70–89%) / manual reject (<70%)
  - State checkpoint: resume được nếu pipeline bị ngắt
  - Observability log: mỗi skill ghi timestamp + duration + confidence
  - Error handling có phân loại: gate fail (stop) / optional fail (continue degraded) / policy block (no bypass)

---

## Changelog v2 → v3

### Skills mới (5)
- 🆕 `fb-discussion-architect` — design multi-thread comment cho MSI
- 🆕 `performance-memory` — feedback loop từ Analytics → Content Creation
- 🆕 `fb-save-share-optimizer` — chấm theo signal mạnh nhất 2026
- 🆕 `fb-send-time-optimizer` — best time to post (gap so với Hootsuite/Sprout)
- 🆕 `fb-review-queue` — HITL workflow với confidence routing (gap nghiêm trọng nhất so với pro agents)

### Skills gộp / cắt (3)
- ❌ `fb-hook-generator` — gộp vào `fb-post-writer`
- ❌ `fb-caption-variants` — gộp vào `fb-post-writer` mode=iterate
- ❌ `fb-cta-writer` — gộp vào `fb-post-writer` (CTA luôn là phần của bài)

→ Tránh multi-agent overhead per Princeton NLP 2026: thêm agent = 2.1pp accuracy nhưng gấp 10–30× latency. Chỉ tách skill khi có lý do rõ.

### Skills nâng cấp (6)
- ♻️ `brand-voice-loader` — output thêm structured glossary (approved + banned), khớp Knowledge Graph approach của Writer/Jasper
- ♻️ `fb-reels-script` — thêm retention curve engineering, pattern interrupt, loop close
- ♻️ `fb-ad-copy` — built-in compliance check theo luật VN 15/2/2026 (5s skip)
- ♻️ `fb-policy-checker` — thêm module luật VN 2026 (quảng cáo online + nghị định mỹ phẩm 1/7/2026)
- ♻️ `fb-performance-review` + `fb-content-audit` — track Save/Share/watch-time metrics
- ♻️ `output-validator` — checklist 5 → 11 điểm

### Layer mới (2)
- 🆕 **Distribution Design Layer** — tối ưu cho MSI (Meaningful Social Interactions)
- 🆕 **Intelligence Layer** — agent có memory + tự tối ưu

### Pipeline thay đổi
- Branching theo task type (publishing vs non-publishing path) thay vì 1 pipeline cứng
- HITL routing thay vì auto pass-through
- Async feedback loop từ post performance → memory

### Đối chiếu 2026 SOTA — đã đóng các gap
| Gap v2 | Cách fix v3 |
|--------|-------------|
| Không có HITL | Thêm `fb-review-queue` |
| Không tối ưu Save/Share | Thêm `fb-save-share-optimizer` |
| Reels không tối ưu retention | Nâng cấp `fb-reels-script` |
| Không design multi-thread | Thêm `fb-discussion-architect` |
| Không có luật VN 2026 | Cập nhật `fb-policy-checker`, `fb-ad-copy` |
| Không có send-time optimization | Thêm `fb-send-time-optimizer` |
| Brand voice không structured | Refactor `brand-voice-loader` output |
| Stateless, không có memory | Thêm `performance-memory` + async feedback loop |
