# LinkedIn Content Agent

Hệ thống tạo nội dung LinkedIn chuyên nghiệp, chạy trên Claude Code. Một lệnh duy nhất điều phối 33 skill tự động.

## Cách dùng

```
/li-content-agent [yêu cầu của bạn]
```

**Ví dụ:**
```
/li-content-agent viết bài về product discovery
/li-content-agent carousel 5 sai lầm founder hay mắc
/li-content-agent phân tích [dán bài vào đây]
/li-content-agent reply [dán comment vào đây]
/li-content-agent kế hoạch content tháng này
```

## Setup lần đầu

Chạy `/li-content-agent` — agent sẽ hỏi bạn 17 câu hỏi và tự động tạo brand voice.

Hoặc tự điền 6 file trong `brand-voice/`:

| File | Nội dung |
|------|----------|
| `01-tone.md` | Cách viết, điều tránh |
| `02-audience.md` | Chân dung người đọc |
| `03-pillars.md` | 3–5 chủ đề cốt lõi |
| `04-examples.md` | Bài mẫu tốt/xấu |
| `05-glossary.json` | Từ dùng / tuyệt đối tránh |
| `06-authority.md` | Vị thế chuyên môn (personal/company/dual) |

## Cấu trúc

```
.claude/commands/00-li-content-agent.md   ← Entry point duy nhất
skills/                                    ← 33 skill files
brand-voice/                               ← Bạn điền (bắt buộc)
memory/                                    ← Agent tự ghi
  post-history.json
  task-state.json
```

## Chỉnh sửa skill

Sửa file trong `skills/` — không cần copy đi đâu cả. Orchestrator đọc trực tiếp từ đây.
