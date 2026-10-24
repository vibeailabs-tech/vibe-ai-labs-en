# CLAUDE.md

File này hướng dẫn Claude Code khi làm việc trong repository này.

## Hệ thống là gì

**LinkedIn Content Agent** — hệ thống custom command trên Claude Code, viết, tối ưu và kiểm duyệt nội dung LinkedIn. User chạy `/li-content-agent` và orchestrator tự động điều phối 33 skill chuyên biệt.

Spec đầy đủ: [li-content-agent-skills.md](li-content-agent-skills.md) (v1.0, 34 skills).  
Viết bằng tiếng Việt / English mix — giữ nguyên phong cách này khi chỉnh sửa skill files.

## Cách dùng (dành cho end user)

1. Điền 6 file brand voice trong `brand-voice/` — hoặc chạy `/li-content-agent` để được hướng dẫn onboarding tự động
2. Chạy trong Claude Code: `/li-content-agent [yêu cầu của bạn]`
3. Xác nhận execution plan khi được hỏi
4. Nhận content package hoàn chỉnh

## Cấu trúc thư mục

```
.claude/commands/00-li-content-agent.md   ← Entry point duy nhất (orchestrator)
skills/                                    ← 33 skill prompt files (orchestrator đọc từ đây)
brand-voice/                               ← User tự điền (6 files bắt buộc)
  01-tone.md, 02-audience.md, 03-pillars.md
  04-examples.md, 05-glossary.json, 06-authority.md
memory/
  post-history.json                        ← Lịch sử bài (performance-memory skill ghi)
  task-state.json                          ← Checkpoint pipeline (resume khi bị ngắt)
```

## Kiến trúc pipeline

Mọi yêu cầu publish đều đi qua pipeline sau:

```
brand-voice-loader (HARD GATE)
  → task-router → li-voice-router → performance-memory (đọc)
  → [li-content-brief — tùy chọn, khi user cung cấp nội dung có sẵn]
  → [content skill] → li-discussion-architect → li-first-comment-strategy
  → li-hook-engineer → li-readability-formatter → li-visual-brief → li-policy-checker
  → li-dwell-time-optimizer → li-send-time-optimizer
  → li-review-queue (HITL) → output-validator (HARD GATE)
```

Pipeline nhẹ hơn dành cho strategy, analytics, reply comment và content-brief (xem spec).

## Hai hard gates — không bao giờ bypass

1. **`brand-voice-loader`**: Phải load đủ 6 file brand voice trước khi bất kỳ skill nào chạy. Thiếu context = dừng hoàn toàn.
2. **`output-validator`**: Checklist 11 điểm. Fail = bounce về skill lỗi, retry tối đa 2 lần.
3. **`li-policy-checker` kết quả Block**: Pipeline dừng, bắt buộc rewrite. Không bypass dù user yêu cầu.

## HITL confidence routing

| Confidence | Hành động |
|---|---|
| ≥ 90% | Auto — thẳng vào output-validator |
| 70–89% | Dừng để human review (show bài, hỏi approve/edit/reject) |
| < 70% | Auto-reject — bounce về content skill để viết lại |

## Brand voice folder contract

Loader đọc đúng các tên file này — không đổi tên:
- `01-tone.md`, `02-audience.md`, `03-pillars.md`, `04-examples.md`, `06-authority.md` — Markdown
- `05-glossary.json` — `{ "approved": [...], "banned": [...], "reasoning": {...} }`

## Thêm hoặc chỉnh sửa skill

Mỗi file trong `skills/` định nghĩa một skill: mục đích, input, logic xử lý, output schema. Orchestrator đọc skill file tại runtime và làm theo.

Khi chỉnh sửa skill:
- Giữ input/output schema tương thích với skill upstream/downstream
- `banned_terms` và `approved_glossary` đến từ brand-voice-loader — các skill không tự đọc brand-voice folder
- `li-policy-checker` phải chạy trước `li-review-queue`
- Skills đọc từ `skills/` — không đọc từ `.claude/commands/`

## Không có build system

Không có build step, test runner, hay package manifest. Skills là markdown prompt files, Claude thực thi tại runtime.
