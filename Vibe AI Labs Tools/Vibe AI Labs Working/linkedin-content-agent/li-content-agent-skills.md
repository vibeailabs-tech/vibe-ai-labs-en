# LinkedIn Content Agent — Skill Structure (v1.0)

> **v1.0 là gì?** Spec source of truth cho toàn bộ hệ thống LinkedIn Content Agent gồm 34 skills: 1 orchestrator + 33 skills chuyên biệt. Tổ chức theo 10 layers phản ánh đúng thứ tự thực thi trong pipeline.

---

## Changelog

### v1.0 (2026-05)
- Initial spec — 34 skills, 10 layers
- Orchestrator điều phối toàn bộ pipeline, đọc skill files từ `skills/`
- Brand voice từ `brand-voice/`, memory từ `memory/`
- 15 pipeline flows: publishing (text, carousel, newsletter, article, video, poll) + strategy + analytics + engagement + utility
- HITL routing 3 tiers: ≥90% auto / 70-89% review-suggested / <70% reject+rewrite
- Hard gates: brand-voice-loader (bắt buộc đầu pipeline), output-validator (bắt buộc cuối pipeline), policy-checker (block thật sự)
- LinkedIn-native: dwell time là signal số 1, comment depth là signal số 2, carousel là format có dwell cao nhất
- LinkedIn khác Facebook: không có Meaningful Social Interactions, không có Save=50 Likes; thay vào đó: dwell time + comment depth + carousel saves

---

## Architecture Overview

```
[User Input]
     │
     ▼
╔══════════════════════════════════════════════════════════════════╗
║            li-content-agent  (ORCHESTRATOR — Skill 00)           ║
║                                                                  ║
║  ┌───────────────────────────────────────────────────────────┐  ║
║  │ 1. Load brand voice (hard gate — stop nếu missing)        │  ║
║  │ 2. Read performance memory                                │  ║
║  │ 3. Classify intent (task-router)                          │  ║
║  │ 4. Announce execution plan                                │  ║
║  │ 5. Execute pipeline skill-by-skill                        │  ║
║  │ 6. Collect output → pass to next skill                    │  ║
║  │ 7. Route qua HITL (review-queue)                          │  ║
║  │ 8. Final gate (output-validator)                          │  ║
║  │ 9. Write to memory                                        │  ║
║  └───────────────────────────────────────────────────────────┘  ║
║                                                                  ║
║  ┌──────────────────────┐                                        ║
║  │ brand-voice-loader   │ GATE — chạy đầu tiên, mọi pipeline    ║
║  └──────────────────────┘                                        ║
║           │                                                      ║
║           ▼                                                      ║
║  ┌──────────────────────────────────────┐                        ║
║  │ task-router → voice-router           │                        ║
║  │ format-selector (nếu cần)            │                        ║
║  └──────────────────────────────────────┘                        ║
║           │                                                      ║
║     ┌─────┴──────────────────────────────────────┐              ║
║     ▼ (Publishing branch)    ▼ (Non-publishing)  ║              ║
║  Content Creation Skills     Analytics / Strategy ║              ║
║  (post/carousel/newsletter/  / Engagement skills  ║              ║
║   article/video/poll/        / Standalone tools   ║              ║
║   repurpose/story-arc)                            ║              ║
║     │                                             ║              ║
║     ▼                                             ║              ║
║  DISTRIBUTION LAYER                               ║              ║
║  (discussion-architect +                          ║              ║
║   first-comment-strategy)                         ║              ║
║     │                                             ║              ║
║     ▼                                             ║              ║
║  QUALITY LAYER                                    ║              ║
║  (hook-engineer → readability-formatter →         ║              ║
║   visual-brief → policy-checker)                  ║              ║
║     │                                             ║              ║
║     ▼                                             ║              ║
║  INTELLIGENCE LAYER                               ║              ║
║  (dwell-time-optimizer + send-time-optimizer)     ║              ║
║     │                                             ║              ║
║     ▼                                             ║              ║
║  HITL: li-review-queue                            ║              ║
║  ≥90% auto / 70-89% review / <70% reject          ║              ║
║     │                                             ║              ║
║     ▼ ◄────────────────────────────────────────── ┘              ║
║  output-validator  GATE (11-point checklist)                     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
     │
     ▼
[Final Output: post + first comment + visual brief + send time +
 confidence score + quality report + pipeline log]

         ┌─────────────────────────────────────────┐
         │ ASYNC: sau khi publish, user cập nhật    │
         │ metrics → performance-memory (update)   │
         └─────────────────────────────────────────┘
```

---

## Path Notes

| Data type | Đọc từ | Ghi vào |
|-----------|--------|---------|
| Skill instructions | `skills/[skill-name].md` | (read-only) |
| Brand voice | `brand-voice/` (6 files) | User tự điền |
| Performance memory | `memory/post-history.json` | Orchestrator sau mỗi pipeline |
| Task state | `memory/task-state.json` | Orchestrator |
| Archive | `memory/post-history-archive.json` | Auto khi >200 records |

---

## 🎛️ Layer 00 — Orchestrator (Entry Point Duy Nhất)

### Skill 00: `li-content-agent`
- **File**: `skills/00-li-content-agent.md`
- **Mục đích**: Entry point duy nhất của hệ thống. User chỉ nói chuyện với skill này — nó dispatch, pipe, pause, retry, và aggregate toàn bộ 33 skills còn lại.
- **Input**: Raw user message (bất kỳ ngôn ngữ, bất kỳ format) qua `$ARGUMENTS`
- **Output**: Final content package: post text + first comment + visual brief + send time + confidence score + quality report + pipeline execution log

#### 7 bước thực thi

| Bước | Hành động |
|------|-----------|
| 1 | Load brand voice (hard gate — stop nếu thiếu file) |
| 2 | Read performance memory (đọc `post-history.json`) |
| 3 | Classify intent → show task type + topic + confidence % |
| 4 | Route to pipeline → announce execution plan trước khi chạy |
| 5 | Execute pipeline: mỗi skill đọc từ `skills/[skill-name].md`, in output rõ ràng |
| 6 | Final output qua output-validator |
| 7 | Write to memory (`post-history.json` + `task-state.json`) |

#### 15 Pipelines được dispatch

| Task Type | Signals (VN / EN) | Pipeline |
|-----------|-------------------|----------|
| PUBLISH_TEXT | "viết bài", "post về", "chia sẻ" | voice-router → post-writer → discussion-architect → first-comment → hook-engineer → readability → visual-brief → policy → dwell → send-time → review-queue → validator |
| PUBLISH_CAROUSEL | "carousel", "slide", "PDF" | voice-router → format-selector → carousel-architect → discussion-architect → [quality 4] → dwell → send-time → review-queue → validator |
| PUBLISH_NEWSLETTER | "newsletter", "bản tin" | voice-router → newsletter-architect → [quality 4] → send-time → review-queue → validator |
| PUBLISH_ARTICLE | "article", "bài dài", "long-form" | voice-router → article-writer → [quality 4] → send-time → review-queue → validator |
| PUBLISH_VIDEO | "script video", "video LinkedIn" | voice-router → video-script → visual-brief → policy → send-time → review-queue → validator |
| PUBLISH_POLL | "poll", "khảo sát" | voice-router → poll-strategist → policy → send-time → review-queue → validator |
| REPURPOSE | "repurpose", "chuyển từ blog/podcast" | content-brief (mode=brief-for-repurpose) → repurpose → [quality 4] → dwell → send-time → review-queue → validator |
| ANALYZE | "phân tích bài này", "x-ray" | content-brief (mode=analyze) → validator |
| REPLY | "reply comment", "trả lời" | comment-reply → policy → validator |
| PLAN_CALENDAR | "lên lịch", "kế hoạch tháng" | content-calendar → validator |
| AUDIT | "kiểm tra feed", "audit" | content-audit → performance-memory (write) → validator |
| STRATEGY | "xây pillar", "chiến lược" | pillar-planner → validator |
| COMPETITOR | "phân tích đối thủ" | competitor-scan → validator |
| TREND | "trending", "xu hướng" | trend-researcher → validator |
| HASHTAG | "hashtag cho bài" | hashtag-strategy → validator |

#### Quick Commands
```
/li-content-agent viết bài về [chủ đề]         → PUBLISH_TEXT pipeline
/li-content-agent carousel [chủ đề]             → PUBLISH_CAROUSEL pipeline
/li-content-agent phân tích [dán content]        → ANALYZE pipeline
/li-content-agent reply [dán comment]            → REPLY pipeline
/li-content-agent kế hoạch tháng                → PLAN_CALENDAR pipeline
```

---

## 🔒 Layer 01 — Gate (Bắt Buộc Đầu Pipeline)

### Skill 01: `brand-voice-loader`
- **File**: `skills/01-brand-voice-loader.md`
- **Mục đích**: Đọc và validate toàn bộ brand voice folder. Inject brand voice context vào tất cả skills phía sau. **Hard gate** — nếu folder thiếu hoặc thiếu file, dừng toàn bộ pipeline.
- **Input**: `brand-voice/` folder (6 files bắt buộc)
- **Output**: Structured Brand Voice Context block:
  ```
  AUTHORITY TYPE: [personal/company/dual]
  NAME, VOICE PRONOUN, TITLE
  TONE SUMMARY (key points + never-do rules)
  AUDIENCE (1 sentence + pain points)
  CONTENT PILLARS (list + descriptions)
  VOCABULARY (preferred terms + banned terms)
  CREDIBILITY ANCHORS
  AUTHORITY LIMITS (can_claim / cannot_claim)
  ```
- **Vị trí**: Bắt buộc chạy đầu tiên trong mọi pipeline

#### Brand Voice Folder Contract (`brand-voice/`)

| File | Nội dung bắt buộc |
|------|------------------|
| `01-tone.md` | Writing style, "never do" rules, sentence structure preference |
| `02-audience.md` | Primary audience 1-sentence desc, top pain points, what they want |
| `03-pillars.md` | 3-5 pillar names + brief descriptions |
| `04-examples.md` | Good post examples (hook type, structure) + bad post patterns |
| `05-glossary.json` | `{ "use": [...], "avoid": [...] }` — preferred & banned terms |
| `06-authority.md` | `type` (personal/company/dual), `name`, `voice`, `can_claim`, `cannot_claim`, `credibility_anchors`, optional `cross_post` flag |

**Lưu ý**:
- Nếu `06-authority.md` missing → GATE FAILED, dừng ngay
- Nếu `04-examples.md` hoặc `05-glossary.json` missing → warning nhưng tiếp tục
- Type `dual` → voice-router phải hỏi user chọn voice, KHÔNG tự chọn

---

## 🧭 Layer 02 — Router & Format

### Skill 02: `task-router`
- **File**: `skills/02-task-router.md`
- **Mục đích**: Phân loại intent từ user input → chọn task type và pipeline
- **Input**: Raw user message + content pasted (nếu có)
- **Output**: Task Classification block (task type, topic, pillar match, format, urgency, confidence %)
- **Confidence logic**: Clear keyword match → 90-100% | Implied intent → 60-75% | Ambiguous → 50-65%
- **Nếu confidence < 70%**: Hỏi user với 5 options cụ thể, KHÔNG đoán

### Skill 03: `li-voice-router`
- **File**: `skills/03-li-voice-router.md`
- **Mục đích**: Xác định voice (personal / company) dựa trên authority type từ brand voice
- **Input**: Brand Voice Context (authority type) + task type
- **Output**: Voice Selection block (type, pronoun, hook style, CTA style, authority name/title, cross-post flag)
- **Logic**:
  - `personal` → voice = "tôi", hook = personal story/observation, CTA = invite discussion
  - `company` → voice = "chúng tôi", hook = data-led/industry, CTA = action-oriented
  - `dual` → PAUSE, hỏi user chọn 1/2, KHÔNG default
- **Lưu**: `selected_voice` vào `memory/task-state.json`

### Skill 04: `li-format-selector`
- **File**: `skills/04-li-format-selector.md`
- **Mục đích**: Chọn optimal format dựa trên topic, mục tiêu, và performance history
- **Input**: Task type + topic + brand voice context + `post-history.json`
- **Output**: Format Selection block (selected format, reasoning, historical performance, alternative format)
- **Format options**: text_post / carousel_pdf / article / newsletter / poll / video_script / live
- **Selection rules**:
  - Carousel khi content có 5+ distinct points, how-to, framework, checklist → highest save rate + dwell time
  - Text post khi content là single insight, opinion, story, 150-300 words
  - Newsletter khi recurring series, 800+ words, goal là audience retention
  - Poll khi topic genuinely divisive, có follow-up post planned
  - Article khi 1500+ words needed, SEO opportunity
  - Video khi better shown than written, native upload > YouTube link

---

## ✍️ Layer 03 — Content Creation (9 skills)

### Skill 05: `li-content-brief`
- **File**: `skills/05-li-content-brief.md`
- **Mục đích**: X-ray nội dung có sẵn để extract patterns, tạo rewrite brief, hoặc xây repurpose strategy. Không viết lại nội dung — chỉ phân tích và brief.
- **Input**: Nội dung paste vào + mode + brand voice context
- **Trigger tự động**: Khi user paste content + nói "phân tích", "viết lại bài này", "học từ bài này"
- **Vị trí pipeline**: Optional step sau format-selector (publishing branch) HOẶC standalone (ANALYZE branch) HOẶC trước repurpose (REPURPOSE branch)
- **4 Modes**:

| Mode | Làm gì | Output |
|------|--------|--------|
| `analyze` | X-ray đầy đủ: hook type, structure, tone, pillar, dwell potential | Content X-Ray block (scores 1-10) |
| `brief-for-rewrite` | Analyze + tạo rewrite brief | X-Ray + Rewrite Brief (keep/improve/new hook/new angle/CTA upgrade) |
| `brief-for-repurpose` | Analyze source + tạo LinkedIn repurpose plan | X-Ray + Repurpose Brief (extract/drop/reframe) |
| `series` | Analyze 3+ posts → tìm patterns chung | Series Analysis (patterns + gaps + next recommendations) |

### Skill 06: `li-post-writer`
- **File**: `skills/06-li-post-writer.md`
- **Mục đích**: Viết LinkedIn text post hoàn chỉnh, publication-ready
- **Input**: Topic + brand voice context + performance memory insights
- **Output**: Full post text + post metadata (format, hook type, pillar, voice, word count, est. dwell)
- **3 Modes**:

| Mode | Làm gì |
|------|--------|
| `fresh` (default) | 1 complete post với hook + body + CTA |
| `iterate` | 3 variants — Variant A (contrarian hook) / B (number hook) / C (story hook) |
| `thread` | 3-post thread: Post 1 standalone insight / Post 2 deep dive / Post 3 application + CTA |

- **Post structure rules**:
  - Line 1-2: Hook (specific, scroll-stopping, <150 chars, không "Tôi muốn chia sẻ" / "Hôm nay")
  - Line 3: "See more" cliff (setup without payoff, surprising statement, hoặc name reader's problem)
  - Body: max 2 lines/paragraph, blank line between paragraphs, 1+ specific detail, bullets dùng ▸ hoặc —
  - CTA cuối: exactly 1 CTA, KHÔNG generic ("thoughts?"), phải targeted và specific
  - Length sweet spot: 150-300 words; max 400; min 80

### Skill 07: `li-newsletter-architect`
- **File**: `skills/07-li-newsletter-architect.md`
- **Mục đích**: Viết LinkedIn Newsletter edition hoàn chỉnh. Newsletters push notification đến 100% subscribers — highest guaranteed reach của LinkedIn.
- **Input**: Topic + brand voice + goal (audience retention / thought leadership / series)
- **Output**: Full newsletter draft (subject lines x3, preview text, greeting, main story, takeaways, resources, CTA, sign-off) + shareable quote + word count + estimated open rate range
- **Newsletter structure**:
  1. Subject line (50 chars max) — viết 3 options (A/B/C)
  2. Preview text (100 chars — không repeat subject, add new info)
  3. Greeting (personal, peer-to-peer — không "Dear subscribers")
  4. Main story / core insight (500-800 words, 1 central idea, narrative / framework / case study / opinion structure)
  5. Key takeaways (3-5 bullets, each <25 words, standalone)
  6. Resources (2-3 external links max, only if genuinely useful)
  7. CTA (1 clear action — reply / share / try / follow for next issue)
  8. Sign-off (personal, brief)
- **Benchmark open rate**: 30-60% = good; <20% = subject line failing; >60% = excellent

### Skill 08: `li-article-writer`
- **File**: `skills/08-li-article-writer.md`
- **Mục đích**: Viết LinkedIn long-form article (1500-3000 words). Articles được Google index — phục vụ cả LinkedIn authority lẫn SEO.
- **Input**: Topic + target keyword + brand voice + depth (full article / outline)
- **Output**: Full article với SEO title + primary keyword + meta description + article content (title, intro, H2 sections, counterargument section, conclusion, author bio) + stats + SEO notes + 3 hashtags
- **Khi nào dùng article vs text post**: Article khi topic cần 1500+ words, SEO keyword opportunity, cần permanent reference resource, case study cần full context. Text post khi single insight, goal là feed reach, time-sensitive.
- **Specificity rule**: Mỗi paragraph phải có ≥1 trong: specific number/%, specific example/company, specific timeframe, direct quote
- **SEO requirements**: Primary keyword trong title + first 100 words + 2-3 H2 headers

### Skill 09: `li-carousel-architect`
- **File**: `skills/09-li-carousel-architect.md`
- **Mục đích**: Thiết kế LinkedIn Carousel PDF (10-15 slides). Highest-performing format trên LinkedIn 2026 — save rate 3-5x text posts, maximum dwell time.
- **Input**: Topic + số slides target + brand voice
- **Output**: Full slide-by-slide content (headline + body text cho mỗi slide) + overall design brief (dimensions, color palette, typography, mood, slide-by-slide visual notes)
- **Slide structure**:

| Slides | Type | Content |
|--------|------|---------|
| 1 | Cover | Scroll-stopping headline + name/handle |
| 2-3 | Problem setup | Why this matters, reader's pain |
| 4-9 | Core content | 1 insight per slide, max 50 words, visual hierarchy |
| 10-11 | Synthesis | Key takeaways, summary framework |
| 12-13 | Proof (optional) | Personal example, specific result |
| 14 | CTA | "Save this" / "Follow for more" / "DM me [keyword]" |
| 15 | About (optional) | Name, title, credentials, next preview |

- **Formats**: 1:1 square (1080×1080) hoặc 4:5 portrait (1080×1350)

### Skill 10: `li-video-script`
- **File**: `skills/10-li-video-script.md`
- **Mục đích**: Viết script cho LinkedIn video. LinkedIn video ≠ TikTok — professional medium, depth wins over entertainment.
- **Input**: Topic + target length (60-180 seconds) + brand voice
- **Output**: Full timestamped script (hook / promise / main points / pivot / CTA) + on-screen text overlay specs + 3 hook variants + production notes
- **LinkedIn video context 2026**:
  - Algorithm favors native video với high watch time (completion rate)
  - 85% xem không có sound → captions bắt buộc
  - Sweet spot length: 60-180 seconds
  - Native upload outperforms YouTube links 3-5x
- **Script structure**: Hook 0-3s (mid-sentence, bold statement) → Promise 3-8s (exact outcome) → Main content 8-90s (3-5 labeled points) → Pivot ~90s (non-obvious insight) → CTA last 10-15s (1 specific action)

### Skill 11: `li-poll-strategist`
- **File**: `skills/11-li-poll-strategist.md`
- **Mục đích**: Thiết kế strategic LinkedIn poll. Network effect: mỗi người vote → LinkedIn show activity đến THEIR connections → multiply reach.
- **Input**: Topic + pillar context + brand voice
- **Output**: Poll design (question max 140 chars, 2 or 4 options max 30 chars each, duration 1 week) + launch post (80-150 words) + follow-up post plan (angle, hook, insight to share after results)
- **Khi nào dùng poll**: Topic genuinely divisive, có follow-up planned, muốn validate content idea. KHÔNG dùng khi "right answer" obvious, muốn engagement không có insight, không plan follow-up.
- **Design rule**: 2 hoặc 4 options (không 3 — psychological asymmetry), mỗi option phải là defensible position

### Skill 12: `li-repurpose`
- **File**: `skills/12-li-repurpose.md`
- **Mục đích**: Chuyển hóa nội dung từ source bất kỳ thành native LinkedIn post. Key word là NATIVE — không phải summary, không phải copy-paste, mà là transformation.
- **Input**: Source content (blog / podcast / report / email / thread / slides / YouTube) + brand voice
- **Output**: Repurpose result block (source type, core insight extracted, selected format, transformation approach) + LinkedIn post + first comment with source link + metadata
- **Repurpose process**:
  1. Extract core insight (ONE thing reader would remember)
  2. Find LinkedIn angle (reframe cho professional aged 28-45)
  3. Select best LinkedIn format (1-2 insights → text post; 5+ steps → carousel; deep dive → article)
  4. Write new LinkedIn-native hook (KHÔNG dùng original title)
  5. Reframe body (cut ruthlessly, add LinkedIn context, add personal angle if personal brand)
  6. Write new CTA (original's CTA không work trên LinkedIn)
- **Rule**: Source link luôn vào first comment, KHÔNG trong body post

### Skill 32: `li-story-arc`
- **File**: `skills/32-li-story-arc.md`
- **Mục đích**: Viết narrative LinkedIn post — founder story, case study, hoặc lesson learned. Story-driven posts có highest dwell time khi execute đúng.
- **Input**: Story type + raw story details + brand voice
- **Output**: Full narrative post + hook variants (A, B) + pillar + word count
- **3 Arc types**:

| Arc | Best for | Structure |
|-----|----------|-----------|
| `founder` | Turning points, perspective shifts, founding moments | The Moment → False Belief → Turning Point → What I Know Now → Invitation |
| `case-study` | Expertise demo, results, framework in action | Challenge → Wrong Approach → Insight → Solution → Lesson → CTA |
| `lesson` | Mistakes, failures, things I'd do differently | The Mistake → What I Was Thinking → Consequence → What I Changed → Principle → CTA |

- **Universal story rules**: Specific over general, vulnerable but purposeful, ending pays off setup, NEVER explain the moral explicitly (let reader arrive at it), one story per post

---

## 🚀 Layer 04 — Distribution Design

### Skill 13: `li-discussion-architect`
- **File**: `skills/13-li-discussion-architect.md`
- **Mục đích**: Transform post để invite genuine professional debate — KHÔNG phải engagement bait. Real discussion là powerful signal cho LinkedIn algorithm — comments từ practitioners và thought leaders dramatically increase reach.
- **Input**: Completed post text
- **Output**: Discussion Architect Review (original CTA type, discussion potential, technique applied, changes made, revised post + revised CTA)
- **5 Engineering techniques**:

| Technique | Cách dùng |
|-----------|-----------|
| Expertise Trigger | Claim đủ specific để practitioners muốn confirm/refute/add counterexample |
| Challenge Consensus | Identify "what most people believe" → challenge 1 specific aspect với signal "this is my perspective" |
| Name a Real Tension | Frame post quanh genuine dilemma không có easy answer (must be real, not manufactured) |
| Role-Specific Invitation | Reference specific roles/contexts trong CTA để attract right commenters |
| Unresolved Story Ending | End với situation genuinely unresolved, ask for input thật sự |

- **Engagement bait (avoid)**: "What do you think? 👇", "Like if you agree!", generic reactions
- **Professional debate (target)**: Specific defensible claim, genuine tension, commenters positioned as experts

### Skill 14: `li-first-comment-strategy`
- **File**: `skills/14-li-first-comment-strategy.md`
- **Mục đích**: Optimize first comment — post ngay sau khi publish. LinkedIn suppresses posts có links trong body (~30% reach reduction) → links đặt đây. First comment cũng seed discussion và extend content.
- **Input**: Main post + has external links? + desired interaction type
- **Output**: First comment text (content extension + 2-3 seed questions + links section + hashtags) + timing instruction
- **First comment structure**:
  1. Content extension (1 additional insight didn't fit in post, 2-3 lines, optional)
  2. Seed questions (2-3 questions requiring domain knowledge, different angles)
  3. Links / resources (format: "📎 [description]: [URL]")
  4. Hashtags (3-5, mix of broad/mid/niche — if not in post body)
- **CRITICAL timing**: Post within 60 seconds of publishing main post (algorithm reads this as content active signal)

---

## 🎨 Layer 05 — Quality & Compliance

### Skill 15: `li-hook-engineer`
- **File**: `skills/15-li-hook-engineer.md`
- **Mục đích**: Strengthen the post hook. Hook là single most important element của LinkedIn post — determines if user clicks "see more" or scrolls past.
- **Input**: Draft post với hook hiện tại
- **Output**: Hook Engineer Report (original hook, hook score 1-10, issues found, 3 rewritten options A/B/C, recommended option + reasoning)
- **6 Checks**:

| Check | Pass condition |
|-------|---------------|
| Specificity | Has specific number, name, timeframe, or specific claim |
| Scroll-stop | Would stop someone scrolling a busy LinkedIn feed |
| Curiosity gap | Creates a "wait, what does that mean? need to read more" feeling |
| Length | Under 150 characters |
| Cliché check | No banned phrases (list: "I'm excited to share", "Game-changer", "Unpopular opinion:", "Hot take:", "Hôm nay tôi muốn chia sẻ", etc.) |
| Brand voice match | Hook matches authority type (personal → story/claim; company → data-led) |

- **3 Hook templates**: A (Contrarian) / B (Specific number: "After [N] [units]...") / C (Unfinished story: "[scene]. [unexpected result]. [setup]")

### Skill 16: `li-readability-formatter`
- **File**: `skills/16-li-readability-formatter.md`
- **Mục đích**: Format post cho maximum readability trên mobile. 80%+ LinkedIn reads trên mobile. Không sửa content — chỉ format.
- **Input**: Post text sau khi đã qua hook-engineer
- **Output**: Readability Formatter Result (changes made, see-more cliff check, formatted post, hashtags moved to first comment)
- **8 Formatting rules**:

| Rule | Yêu cầu |
|------|---------|
| Paragraph length | Max 2 lines per paragraph — split nếu 3+ |
| Blank lines | Every paragraph followed by blank line |
| See-more cliff | Line 3 phải compelling — incomplete thought, surprising statement, specific number |
| No markdown | Remove **bold**, *italic*, # headers, --- dividers |
| Bullets | Dùng ▸ hoặc — (not • or -), each on own line |
| Emoji | 0-2 max (check brand voice); never as bullet replacements |
| CTA isolation | CTA trên own line, blank line before, 1 sentence |
| Post ending | Last thing = CTA — clean. KHÔNG end with hashtags |

### Skill 17: `li-visual-brief`
- **File**: `skills/17-li-visual-brief.md`
- **Mục đích**: Tạo visual brief cho designer hoặc AI image tools. Brief cho người, không phải AI prompt (mặc dù có include AI prompt bonus).
- **Input**: Post content + format type + brand colors (nếu có trong brand voice)
- **Output**: Visual Brief (use case, dimensions, visual concept, text overlay, colors, typography, mood/style, avoid list) + AI Image Prompt (Midjourney/DALL-E format)
- **LinkedIn image specs**:

| Use case | Ratio | Dimensions |
|----------|-------|-----------|
| Single image (square) | 1:1 | 1080×1080 |
| Single image (landscape) | 1.91:1 | 1200×628 |
| Single image (portrait, recommended) | 4:5 | 1080×1350 |
| Carousel slides | 1:1 or 4:5 | 1080×1080 or 1080×1350 |
| Article thumbnail | 1.91:1 | 1200×628 |

- **Recommended default**: 4:5 portrait (1080×1350) — takes most vertical space on mobile feed

### Skill 18: `li-policy-checker`
- **File**: `skills/18-li-policy-checker.md`
- **Mục đích**: Compliance gate — kiểm tra LinkedIn Community Policy + Vietnamese advertising law. **Hard gate** — FAIL = post không thể publish as-is, phải rewrite.
- **Input**: Post text + brand voice (authority claims check)
- **Output**: Policy Checker Result (verdict: PASS/NEEDS_REVISION/FAIL, risk level, issues list với location + rule + fix suggestion, advisory notes)
- **Check 1 — LinkedIn Community Policy**:
  - 1a. False/misleading claims (stats without source, unverifiable outcomes, before/after without context)
  - 1b. Spam signals (repetitive phrases, artificial engagement requests "comment anything to get template", mass tagging >3 people)
  - 1c. Deceptive practices (advertising as organic without disclosure, vague job/partnership offers)
  - 1d. Professional conduct (naming individuals negatively, harassment, confidential client data — kể cả anonymized nhưng identifying)
- **Check 2 — Vietnamese Advertising Law (Luật Quảng cáo 2012, amendments 2024)**:
  - 2a. Superlatives without certification: "số 1", "hàng đầu", "tốt nhất", "duy nhất tại Việt Nam", "best", "#1"
  - 2b. Sector-specific: healthcare (cần disclaimer "tham khảo ý kiến bác sĩ"), financial services ("đây không phải tư vấn đầu tư"), education (qualify learning outcome claims)
  - 2c. AI-generated content disclosure (best practice, not mandatory — flag as advisory)
  - 2d. Testimonials/case studies (fabricated = illegal; nếu không có permission → anonymize + "một khách hàng trong ngành X"; invented numbers = not acceptable)

**Verdict system**:
| Verdict | Ý nghĩa | Hành động |
|---------|---------|-----------|
| PASS | No issues | Proceed to next step |
| NEEDS_REVISION | Issues fixable | Show issues + fixes, user decides |
| FAIL | Serious violation | Block — require rewrite before continuing |

**Auto-FAIL conditions**: Fabricated statistics, unverified superlatives for promoted products/services, named individual harassment, confidential client data exposure risk

---

## 🧠 Layer 06 — Intelligence

### Skill 19: `performance-memory`
- **File**: `skills/19-performance-memory.md`
- **Mục đích**: Memory layer — connect analytics ngược về content creation. Không có skill này, mỗi bài viết đều bắt đầu từ zero.
- **Storage**: `memory/post-history.json` (JSON array, max 200 records, archive older to `post-history-archive.json`)
- **3 Modes**:

| Mode | Trigger | Làm gì |
|------|---------|--------|
| READ | Đầu mỗi pipeline | Load history → extract insights (best hook type, best format, recent topics to avoid, timing patterns) |
| WRITE | Sau khi content finalized | Append new record to post-history.json |
| UPDATE | User cung cấp real metrics | Tìm record theo date → update impressions/dwell_score/comment_depth |

- **Record schema**:
  ```json
  {
    "date": "YYYY-MM-DD",
    "topic": "2-4 word topic",
    "format": "text|carousel|newsletter|article|poll|video",
    "hook_type": "contrarian|number|story|question|other",
    "authority_type": "personal|company",
    "pillar": "pillar name",
    "impressions": 0,
    "comment_depth": 0,
    "dwell_score": 0
  }
  ```
- **READ output**: Best hook type (avg dwell score), best format, pillar performance, topics to avoid (last 14 days), posting consistency patterns

### Skill 20: `li-dwell-time-optimizer`
- **File**: `skills/20-li-dwell-time-optimizer.md`
- **Mục đích**: Score và improve content retention. Dwell time là LinkedIn's strongest ranking signal 2026. Post giữ attention 30+ seconds > post có 100 likes nhưng bị lướt qua.
- **Input**: Post text sau quality layer
- **Output**: Dwell Time Score (7 dimensions with weights + total 0-100 + top 2 improvements)
- **LinkedIn algorithm signal ranking 2026**:
  1. Dwell time — highest weight
  2. Comment depth (back-and-forth)
  3. Shares
  4. Reactions/likes — lowest weight
- **7-dimension scoring** (weighted total = dwell score 0-100):

| Dimension | Weight | Score 1-10 | What it measures |
|-----------|--------|------------|-----------------|
| Hook Strength | 20% | 7-10 = scroll-stopping | Does line 1 stop scrolling? |
| See-More Pull | 20% | 7-10 = compelled click | Does line 3 compel "see more"? |
| Information Density | 15% | 7-10 = every line delivers | No filler, no padding |
| Reading Pace | 15% | 7-10 = natural rhythm | Sentence length varies |
| Visual Breaks | 10% | 7-10 = effortless scan | White space and structure |
| Narrative Pull | 10% | 7-10 = led through journey | Each paragraph sets up next |
| Ending Reward | 10% | 7-10 = CTA earns its place | Conclusion pays off hook |

**Interpretation**: 80-100 = High (algorithm likely boosts) / 60-79 = Average / 40-59 = Weak / <40 = Rewrite recommended

### Skill 21: `li-send-time-optimizer`
- **File**: `skills/21-li-send-time-optimizer.md`
- **Mục đích**: Recommend optimal day + time to publish cho Vietnamese professional audience (GMT+7).
- **Input**: Content type + audience persona + post-history.json (for historical patterns)
- **Output**: Send Time block (primary slot + reasoning, backup slot, avoid list, historical note if 10+ posts tracked)
- **Baseline (Vietnamese B2B professionals, GMT+7)**:

| Day | Best windows | Notes |
|-----|-------------|-------|
| Monday | 8:00-9:30am | Week-start mindset |
| Tuesday | 7:30-8:30am, 12:00-1:00pm | Consistently strongest |
| Wednesday | 7:30-8:30am, 12:00-1:00pm | Second strongest |
| Thursday | 8:00-9:00am, 5:00-6:30pm | Good for thought leadership |
| Friday | 8:00-9:00am only | Afternoon drops |
| Saturday | 9:00-11:00am | Lower reach |
| Sunday | Avoid | Very low professional engagement |

- **Content-type adjustments**: Newsletter → Tue/Wed morning only; Poll → Mon 8am (full 7-day run); Story/founder → Thu/Fri morning; Carousel → Tue/Wed morning; Trending/news → ASAP (speed > optimal timing)
- **Historical weighting**: <10 posts → rely on baseline; ≥10 posts → 50% baseline + 50% historical data

---

## 👥 Layer 07 — Human-in-the-Loop

### Skill 22: `li-review-queue`
- **File**: `skills/22-li-review-queue.md`
- **Mục đích**: Confidence-based routing — calculate overall confidence score và route accordingly. High confidence = auto-approve, low confidence = review hoặc rewrite.
- **Input**: Output từ Quality + Intelligence layers + scores từ các skills đã chạy
- **Output**: Review Queue Routing block (confidence breakdown per factor, overall %, routing decision + routing-specific block)
- **5-factor confidence calculation**:

| Factor | Weight | Score logic |
|--------|--------|-------------|
| Brand Voice Match | 25% | Tone correct? Banned words? Right pronoun? |
| Hook Strength | 20% | From li-hook-engineer: 80-100→100; 50-79→60; 0-49→0 |
| Policy Compliance | 25% | PASS→100; NEEDS_REVISION→50; FAIL→0 |
| Dwell Score | 15% | ≥80→100; 60-79→75; 40-59→50; <40→25 |
| Pillar Alignment | 15% | Clear match→100; loose→60; no match→20 |

**Formula**: `Confidence = (F1×0.25) + (F2×0.20) + (F3×0.25) + (F4×0.15) + (F5×0.15)`

**HITL Routing thresholds**:

| Score | Routing | Action |
|-------|---------|--------|
| ≥90% | AUTO-APPROVE | Output immediately — no human review needed |
| 70-89% | REVIEW SUGGESTED | Show content + review checklist của lowest-scoring factors + option "approve as-is" hoặc "request improvement" |
| <70% | REJECT AND REWRITE | Block output, show breakdown, auto-trigger skill that addresses lowest factor |

- **Auto-triggered fix skills**: Low hook → re-run hook-engineer; Low policy → re-run policy-checker; Low dwell → re-run dwell-optimizer; Low pillar → ask user to specify pillar; Low brand voice → show mismatch, ask for guidance

---

## 📊 Layer 08 — Analytics

### Skill 23: `li-performance-review`
- **File**: `skills/23-li-performance-review.md`
- **Mục đích**: Phân tích LinkedIn performance data để hiểu what's working và what to change.
- **Input**: Metrics từ user (paste) hoặc từ `post-history.json`; optional period (30d / 90d)
- **Output**: Performance Review (overview, top 3 performers với why-it-worked hypothesis, underperformers, format comparison table, trend analysis, 3 actionable recommendations)
- **Post-level metrics**: Impressions, engagement rate (benchmark: 2-5% = good; >5% = excellent), comment depth, dwell time, saves, reposts
- **Profile-level metrics**: Follower growth, profile views, newsletter open rate (benchmark: 30-60% = good; <20% = subject line problem)
- **Analysis framework**: Top performers (pattern finding) → Underperformers (hypothesis) → Trend (improving/declining/flat) → Anomaly detection (over/under vs average) → Format comparison table → 3 specific recommendations (1 format, 1 hook/content, 1 timing/frequency)

### Skill 24: `li-content-audit`
- **File**: `skills/24-li-content-audit.md`
- **Mục đích**: Audit existing LinkedIn feed content để identify imbalances, inconsistencies, gaps. Chạy monthly hoặc trước khi lên kế hoạch content period mới.
- **Input**: 10-20 recent posts (text paste hoặc LinkedIn profile URL)
- **Output**: Content Audit (7-dimension scorecard, top 3 issues, content gaps, recommendations for next 2 weeks)
- **7 Audit dimensions**:

| Dimension | Flag conditions |
|-----------|----------------|
| Pillar Balance | Any pillar >50% (overposted), <10% (neglected), 0% last 30 days (abandoned) |
| Tone Consistency | Banned vocabulary, pronoun switching, wrong register, engagement bait language |
| Authority Signals | Posts with zero credibility anchors, no experience references |
| Format Diversity | >60% same format (format fatigue), no carousel last 30 days, no newsletter last 4 weeks |
| Hook Pattern | Same hook type 3+ times in 7 posts, all questions (question fatigue), no contrarian hooks |
| CTA Quality | >30% same phrasing, generic CTAs dominate, no save/share-inviting CTAs |
| Content Freshness | Target 70% evergreen / 30% timely |

### Skill 25: `li-competitor-scan`
- **File**: `skills/25-li-competitor-scan.md`
- **Mục đích**: Phân tích competitor / thought leader LinkedIn content để identify what's working và find differentiation opportunities.
- **Input**: Competitor name / URL / paste their recent posts (1-5 accounts)
- **Output**: Competitor Scan (per-account analysis, differentiation map, positioning recommendation, top 2 content ideas)
- **7 analysis dimensions**: Posting frequency & consistency, top performing content (by visible engagement), format preferences, content pillars, hook styles, engagement quality, gaps and weaknesses
- **Differentiation Map output**: "What they ALL do" (avoid, high competition) + "What only 1-2 do" (emerging opportunity) + "What nobody does well" (your lane to own) + "Your unique angle" (tied to your authority)

---

## 🗓️ Layer 09 — Strategy

### Skill 26: `li-content-calendar`
- **File**: `skills/26-li-content-calendar.md`
- **Mục đích**: Build structured content calendar cho 1 week hoặc 1 month. Integrates pillar rotation, format diversity, send-time optimization, topic history.
- **Input**: Scope (week / month) + optional theme or goal + brand voice + post-history
- **Output**: Content calendar table (date, day, time GMT+7, format, pillar, topic idea, hook angle, notes) + backup topics (3 extras) + time-sensitive opportunities
- **Constraints**: No same topic within 14 days, no same hook type 3 posts in a row, no same format 4 posts in a row, ≥2 different pillars per week
- **Default weekly template (3 posts/week)**:
  - Monday morning: Thought leadership / contrarian
  - Wednesday morning: Practical framework / carousel
  - Friday morning: Story / case study / lesson
- **Monthly template**: Week 1 (Establish & Educate) → Week 2 (Engage & Debate) → Week 3 (Proof & Social Validation) → Week 4 (Convert & CTA-focused)

### Skill 27: `li-pillar-planner`
- **File**: `skills/27-li-pillar-planner.md`
- **Mục đích**: Build hoặc review content pillars — 3-5 core topics brand consistently owns on LinkedIn.
- **Input**: Scope (build / review / test) + brand context
- **Output**: Pillar definitions (BUILD mode: ready-to-save to `03-pillars.md`) hoặc Pillar Health scorecard (REVIEW mode) hoặc Idea list per pillar + verdict (TEST mode)
- **3 Modes**:

| Mode | Làm gì |
|------|--------|
| `build` | Discovery interview (5 questions) → Draft 5 candidates → Filter to 3-5 → Define each với name, core question, unique angle, business goal, 5 example posts |
| `review` | Check differentiation, business alignment, content distribution, audience relevance, freshness |
| `test` | Generate 5 new post ideas per pillar → if can't generate 5 → pillar too narrow |

- **5 Tests khi filter pillars**: 20-post test, differentiation test, sustainability test, audience relevance test, authority test (reference `06-authority.md`)

### Skill 28: `li-trend-researcher`
- **File**: `skills/28-li-trend-researcher.md`
- **Mục đích**: Research real-time trending topics trong user's industry + filter qua brand voice lens.
- **Input**: Brand voice context (auto) hoặc override industry / topic
- **Output**: Trend Researcher report (N topics với why trending, pillar fit, unique angle available, relevance window, priority) + Top 2 to prioritize this week (hook direction, format, your angle, "post by" date)
- **Process**: Identify industry from brand voice → web search (5 queries: LinkedIn trending, top discussions, pillar debate, controversy, audience viral) → Filter (relevance/differentiation/authority/sustainability) → Generate post concepts
- **Filter logic**: Priority 1 = high pillar alignment + unique angle available; Priority 3 = off-pillar or can only restate others

### Skill 29: `li-hashtag-strategy`
- **File**: `skills/29-li-hashtag-strategy.md`
- **Mục đích**: Recommend optimal 3-5 hashtags. LinkedIn hashtag strategy khác Instagram/TikTok — more hashtags ≠ more reach.
- **Input**: Post content + topics + audience from brand voice
- **Output**: Hashtag Strategy block (recommended set: 1 broad + 1-2 mid + 1 niche, placement, reasoning, alternatives)
- **LinkedIn hashtag reality 2026**: Sweet spot = 3-5 (>5 hurts reach); function = topic channels, not discovery tools; first comment placement preferred
- **Tier system**: Tier 1 = Broad 1M+ followers (1 per post), Tier 2 = Mid 100K-1M (1-2 per post), Tier 3 = Niche 10K-100K (1-2 per post)
- **Vietnamese tech/startup hashtags**: Broad (#Vietnam, #Business); Mid (#VietnamBusiness, #StartupVietnam, #TechVietnam, #B2B); Niche (#VietnamStartups, #KhoiNghiep, #ProductVietnam, #SaaSVietnam, #FounderVietnam)

---

## 💬 Layer 10 — Engagement

### Skill 30: `li-comment-reply`
- **File**: `skills/30-li-comment-reply.md`
- **Mục đích**: Craft thoughtful reply đến comment trên post của mình. Turn comment thành mini-discussion — extend comment depth, LinkedIn's top algorithmic signal.
- **Input**: Original post text + comment to reply to
- **Output**: Comment Reply block (comment type, reply strategy, full reply text, strategic note, word count)
- **4 Reply principles**:
  1. Reference something specific from their comment
  2. Add genuine value (new dimension, nuance, example, limitation)
  3. Ask ONE specific follow-up question (kéo dài thread)
  4. Match their energy and tone (analytical/enthusiastic/critical → adapt accordingly)
- **Keep under 150 words**: Best replies = 2-4 sentences + 1 question
- **4 Reply frameworks**: Agreement+extension / Respectful disagreement / Answering direct question / Responding to criticism (professional, not defensive)
- **Avoid**: "Thanks for sharing!" alone, self-promotion, same reply format repeatedly

### Skill 31: `li-comment-strategist`
- **File**: `skills/31-li-comment-strategist.md`
- **Mục đích**: Write strategic comment trên post của người KHÁC. Your comment appears in feeds của YOUR followers — free distribution.
- **Input**: Original post (URL hoặc paste) + commenting goal
- **Output**: Strategic Comment block (post assessed, comment goal, strategy, full comment text, selection advice, timing instruction)
- **When to comment**: High-engagement post in your space, post from thought leader your audience follows, post touching your content pillars, genuine expertise/counter-point available, potential client/collaborator post
- **When to skip**: Completely off-pillar, nothing to add beyond agreement, controversial in collateral-damage way, 200+ comments already (low visibility)
- **Strategic Comment Formula**: Sentence 1 (anchor to specific thing in post) → Sentences 2-3 (your unique perspective from experience/data) → Sentence 4 (bridge to your expertise, natural not forced) → Sentence 5 (question inviting response)
- **4 Goals**: Build relationship with poster / Reach their audience / Demonstrate expertise / Attract new followers (each has different strategy)
- **Timing**: Comment within 2h of post going live for maximum visibility

---

## ✅ Layer 11 — Output Gate (Bắt Buộc Cuối Pipeline)

### Skill 33: `output-validator`
- **File**: `skills/33-output-validator.md`
- **Mục đích**: Final quality gate — 11-point check trước khi deliver output cho user. Last gate trong mọi pipeline. Block nếu critical checks fail.
- **Input**: Complete output package từ toàn bộ pipeline
- **Output**: "OUTPUT VALIDATED — READY TO PUBLISH" block HOẶC "OUTPUT BLOCKED" block
- **11-Point Checklist**:

| # | Category | Check | Fail action |
|---|----------|-------|-------------|
| 1 | CRITICAL | Policy: li-policy-checker đã run, result = PASS? | Block — run/fix first |
| 2 | CRITICAL | Brand voice tone: correct pronoun, no banned vocab, correct structure, no clichéd openers | Block |
| 3 | CRITICAL | Authority match: voice matches authority type selected, no forbidden claims from `cannot_claim` | Block |
| 4 | CRITICAL | Pillar alignment: post clearly serves ≥1 defined pillar | Flag (proceed with warning) |
| 5 | IMPORTANT | Hook quality: specific, scroll-stopping, <150 chars | Flag STRONG/ADEQUATE/WEAK |
| 6 | IMPORTANT | Formatting: paragraphs ≤2 lines, blank lines, no markdown, no excessive emoji | Flag CLEAN/NEEDS_CLEANUP |
| 7 | IMPORTANT | CTA quality: exactly 1 CTA, specific | Flag STRONG/GENERIC/MISSING |
| 8 | IMPORTANT | Dwell score ≥60 | Flag ≥80 EXCELLENT/60-79 ADEQUATE/<60 LOW |
| 9 | ADVISORY | Send time provided | Note PROVIDED/NOT PROVIDED |
| 10 | ADVISORY | Visual brief included (nếu cần) | Note NEEDED/PROVIDED/NOT NEEDED |
| 11 | ADVISORY | First comment prepared | Note PROVIDED/NOT PROVIDED |

- **Final output format**: Post text (copy-paste ready) + First comment + Visual brief + Send time + Quality Report (confidence %, checks N/11, per-check status) + Pipeline log

---

## Pipeline Flows

### Full Publishing Pipeline — Text Post
```
brand-voice-loader [GATE]
  → task-router → li-voice-router
  → performance-memory (READ)
  → li-post-writer
  → li-discussion-architect
  → li-first-comment-strategy
  → li-hook-engineer
  → li-readability-formatter
  → li-visual-brief
  → li-policy-checker [GATE]
  → li-dwell-time-optimizer
  → li-send-time-optimizer
  → li-review-queue (HITL)
  → output-validator [GATE]
  → performance-memory (WRITE)
```

### Carousel Pipeline
```
brand-voice-loader → task-router → li-voice-router
  → li-format-selector
  → li-carousel-architect
  → li-discussion-architect → li-first-comment-strategy
  → li-hook-engineer → li-readability-formatter
  → li-visual-brief → li-policy-checker
  → li-dwell-time-optimizer → li-send-time-optimizer
  → li-review-queue → output-validator
  → performance-memory (WRITE)
```

### Newsletter Pipeline
```
brand-voice-loader → task-router → li-voice-router
  → li-newsletter-architect
  → li-readability-formatter → li-visual-brief
  → li-policy-checker
  → li-send-time-optimizer
  → li-review-queue → output-validator
```

### Article Pipeline
```
brand-voice-loader → task-router → li-voice-router
  → li-article-writer
  → li-readability-formatter → li-visual-brief
  → li-policy-checker
  → li-send-time-optimizer
  → li-review-queue → output-validator
```

### Video Script Pipeline
```
brand-voice-loader → task-router → li-voice-router
  → li-video-script
  → li-visual-brief → li-policy-checker
  → li-send-time-optimizer
  → li-review-queue → output-validator
```

### Poll Pipeline
```
brand-voice-loader → task-router → li-voice-router
  → li-poll-strategist
  → li-policy-checker
  → li-send-time-optimizer
  → li-review-queue → output-validator
```

### Repurpose Pipeline
```
brand-voice-loader → task-router
  → li-content-brief (mode=brief-for-repurpose)
  → li-repurpose
  → li-discussion-architect → li-first-comment-strategy
  → li-hook-engineer → li-readability-formatter
  → li-visual-brief → li-policy-checker
  → li-dwell-time-optimizer → li-send-time-optimizer
  → li-review-queue → output-validator
```

### Story Arc Pipeline (variant of Text Post)
```
brand-voice-loader → task-router → li-voice-router
  → li-story-arc
  → li-discussion-architect → li-first-comment-strategy
  → li-hook-engineer → li-readability-formatter
  → li-visual-brief → li-policy-checker
  → li-dwell-time-optimizer → li-send-time-optimizer
  → li-review-queue → output-validator
```

### Analyze / Content Brief Pipeline (standalone)
```
brand-voice-loader → task-router
  → li-content-brief (mode=analyze | series)
  → output-validator
```

### Reply Pipeline (lightweight — skip distribution, quality light)
```
brand-voice-loader → task-router
  → li-comment-reply
  → li-policy-checker
  → output-validator
  (skip: discussion-architect, visual-brief, dwell, send-time, review-queue)
```

### Calendar Pipeline (non-publishing)
```
brand-voice-loader → task-router
  → li-content-calendar
  → output-validator
```

### Audit Pipeline
```
brand-voice-loader → task-router
  → li-content-audit
  → performance-memory (WRITE insights)
  → output-validator
```

### Strategy Pipeline (Pillar Planner)
```
brand-voice-loader → task-router
  → li-pillar-planner
  → output-validator
```

### Competitor Scan Pipeline
```
brand-voice-loader → task-router
  → li-competitor-scan
  → output-validator
```

### Trend Research Pipeline
```
brand-voice-loader → task-router
  → li-trend-researcher
  → output-validator
```

### Hashtag Pipeline (utility)
```
brand-voice-loader → task-router
  → li-hashtag-strategy
  → output-validator
```

---

## Hard Gates & HITL Routing Rules

### Hard Gates (pipeline stops hoàn toàn)

| Gate | Condition | Consequence |
|------|-----------|-------------|
| `brand-voice-loader` | `brand-voice/` folder missing hoặc thiếu `06-authority.md` | STOP — báo path lỗi, hướng dẫn setup, KHÔNG tiếp tục |
| `li-policy-checker` FAIL | Fabricated stats, unverified superlatives, harassment, confidential data | BLOCK output — bắt buộc rewrite, không có bypass |
| `output-validator` — Critical check fail | Policy không pass, tone sai, authority claims vi phạm | BLOCK output — trigger fix skill tương ứng, max 2 retries |

### HITL Routing (li-review-queue)

| Confidence | Action | Orchestrator làm gì |
|------------|--------|---------------------|
| ≥90% | AUTO-APPROVE | Output ngay — không cần human review |
| 70-89% | REVIEW SUGGESTED | Show content + checklist + lowest factors + "approve as-is / request improvement" |
| <70% | REJECT AND REWRITE | Block, breakdown, auto-trigger fix skill cho lowest factor |

**Target**: ~10-15% bài vào review tier (70-89%). Nếu thường xuyên <70%, cần cải thiện skill upstream.

### Policy Block Logic
```
if policy-checker verdict == FAIL:
    block pipeline
    do NOT bypass under any condition
    require rewrite
    re-run policy-checker on revised content before proceeding
```

### Dual Authority — Force Choice Logic
```
if authority_type == "dual":
    PAUSE pipeline
    ask user: "Post này dưới danh nghĩa [Personal Name] hay [Company Name]?"
    wait for answer
    DO NOT default to either option
    proceed only after explicit selection
```

---

## Summary Table — 34 Skills

| # | Skill name | Layer | Pipeline role | Mandatory? |
|---|-----------|-------|---------------|-----------|
| 00 | li-content-agent | Orchestrator | Entry point + dispatcher | Yes |
| 01 | brand-voice-loader | Gate | First step, every pipeline | HARD GATE |
| 02 | task-router | Router | Classify intent → pipeline | Yes |
| 03 | li-voice-router | Router | Select tôi/chúng tôi + hook style | Publishing branch |
| 04 | li-format-selector | Router | Select optimal format | When format unclear |
| 05 | li-content-brief | Content | X-ray, rewrite brief, repurpose brief | ANALYZE/REPURPOSE branch |
| 06 | li-post-writer | Content | Write text post (fresh/iterate/thread) | PUBLISH_TEXT |
| 07 | li-newsletter-architect | Content | Write newsletter edition | PUBLISH_NEWSLETTER |
| 08 | li-article-writer | Content | Write long-form article | PUBLISH_ARTICLE |
| 09 | li-carousel-architect | Content | Design carousel PDF (10-15 slides) | PUBLISH_CAROUSEL |
| 10 | li-video-script | Content | Write video script with overlays | PUBLISH_VIDEO |
| 11 | li-poll-strategist | Content | Design poll + launch post + follow-up plan | PUBLISH_POLL |
| 12 | li-repurpose | Content | Convert any source → native LinkedIn | REPURPOSE |
| 32 | li-story-arc | Content | Narrative post (founder/case-study/lesson) | Story branch |
| 13 | li-discussion-architect | Distribution | Engineer professional debate | Publishing branch |
| 14 | li-first-comment-strategy | Distribution | Seed thread + links in comment | Publishing branch |
| 15 | li-hook-engineer | Quality | Strengthen hook (6 checks, 3 rewrites) | Publishing branch |
| 16 | li-readability-formatter | Quality | Format for mobile readability | Publishing branch |
| 17 | li-visual-brief | Quality | Visual direction for designer/AI tools | Publishing branch |
| 18 | li-policy-checker | Quality | Compliance gate LI + VN law | HARD GATE |
| 19 | performance-memory | Intelligence | Read/write/update post history | READ: publishing start; WRITE: after output |
| 20 | li-dwell-time-optimizer | Intelligence | Score retention (7 dimensions, 0-100) | Publishing branch |
| 21 | li-send-time-optimizer | Intelligence | Optimal publish time GMT+7 | Publishing branch |
| 22 | li-review-queue | HITL | Confidence routing: auto/review/reject | Every publishing pipeline |
| 23 | li-performance-review | Analytics | Analyze metrics, find patterns | AUDIT/standalone |
| 24 | li-content-audit | Analytics | Feed audit (7 dimensions) | AUDIT |
| 25 | li-competitor-scan | Analytics | Competitor/thought leader analysis | COMPETITOR |
| 26 | li-content-calendar | Strategy | Build 1-week or 1-month plan | PLAN_CALENDAR |
| 27 | li-pillar-planner | Strategy | Build/review/test content pillars | STRATEGY |
| 28 | li-trend-researcher | Strategy | Real-time trend research + angle | TREND |
| 29 | li-hashtag-strategy | Strategy | 3-5 hashtags (tier system) | HASHTAG / first-comment |
| 30 | li-comment-reply | Engagement | Reply to comments on your posts | REPLY |
| 31 | li-comment-strategist | Engagement | Strategic comment on others' posts | Standalone |
| 33 | output-validator | Gate | 11-point final check | HARD GATE (last step) |

**Tổng: 34 skills** (1 orchestrator + 33 skills chuyên biệt)

---

## LinkedIn vs Facebook — Key Differences Affecting Design

| Signal | LinkedIn (2026) | Facebook (2026) |
|--------|----------------|----------------|
| #1 algorithm signal | Dwell time | Meaningful Social Interactions |
| Best format | Carousel PDF (save rate + dwell) | Carousel (save rate) |
| Comment quality | Comment depth (back-and-forth) > reaction count | Multi-thread MSI |
| Share importance | High (but less than FB) | 1 Share = 50 Likes (FB) |
| Video strategy | Watch-time completion, native > YouTube links | 15s completion > 60s scrolled |
| Audience mindset | Professional, time-poor, wants insight | Social browsing |
| Link penalty | Links in body reduce reach ~30% → first comment | Same (links hurt reach) |
| Hashtag limit | 3-5 optimal (>5 hurts) | Less strict |
| Audience timing | Morning commute / lunch / end-of-work-day | Evening / weekend |
| Content tone | Professional depth wins | Entertainment + authenticity |

Vì LinkedIn thiếu MSI mechanism của Facebook, hệ thống này tập trung vào:
1. Dwell time optimization (skill 20) thay vì save/share optimizer (không có equivalent)
2. Comment depth qua discussion-architect + reply strategy (skills 13, 30, 31)
3. Carousel dwell qua carousel-architect (skill 09) thay vì carousel cho save rate
4. Professional debate engineering thay vì MSI trigger design
