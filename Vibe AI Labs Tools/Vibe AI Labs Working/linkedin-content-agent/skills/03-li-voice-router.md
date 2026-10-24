# Li Voice Router — Chọn Voice

Xác định brand voice nào sẽ được sử dụng để viết, dựa trên loại authority.

## Đầu vào

Đọc loại authority từ Brand Voice Context (được tải bởi brand-voice-loader).
Cũng đọc loại task từ đầu ra của task-router.

## Logic Quyết định Voice

### Type: personal
- **Voice**: "tôi" (ngôi thứ nhất cá nhân)
- **Hook style**: câu chuyện cá nhân, quan sát cá nhân, sai lầm/bài học cá nhân
- **CTA style**: mời bình luận, chia sẻ trải nghiệm của bạn, bạn nghĩ gì về X
- **Credibility**: "Tôi đã...", "Từ kinh nghiệm của tôi...", "Khi tôi..."
- **Output**: `✅ Voice: PERSONAL | Pronoun: tôi | Hook style: personal narrative | CTA: invite discussion`

### Type: company
- **Voice**: "chúng tôi" (ngôi thứ nhất số nhiều/công ty)
- **Hook style**: dẫn dắt bằng dữ liệu, quan sát ngành, insight từ khách hàng, case study
- **CTA style**: tìm hiểu thêm, đặt lịch demo, tải tài nguyên, theo dõi để cập nhật
- **Credibility**: "Sau X năm làm việc với...", "Dữ liệu từ...", "Khách hàng của chúng tôi..."
- **Output**: `✅ Voice: COMPANY | Pronoun: chúng tôi | Hook style: data-led | CTA: action-oriented`

### Type: dual
Hỏi người dùng trước khi tiếp tục:

```
🔀 Dual brand detected.

Bài này bạn muốn đăng dưới danh nghĩa nào?

1. [Personal name] — cá nhân (tôi) — phù hợp cho: story, opinion, lesson learned
2. [Company name] — công ty (chúng tôi) — phù hợp cho: case study, product insight, industry data

Chọn 1 hoặc 2:
```

Chờ phản hồi của người dùng trước khi tiếp tục. KHÔNG tự chọn mặc định.

Sau khi người dùng chọn:
- Áp dụng các quy tắc voice tương ứng ở trên
- Kiểm tra xem cross-posting có được bật không (từ trường `cross_post` trong 06-authority.md) — nếu có, gợi ý tạo thêm một bản biến thể sau khi hoàn thành bài chính

## Ánh xạ Voice — Loại nội dung

| Loại nội dung | Voice phù hợp nhất |
|-------------|-----------|
| Câu chuyện founder, thất bại/chiến thắng cá nhân | personal |
| Framework từ kinh nghiệm thực tế | personal |
| Dữ liệu ngành, phân tích xu hướng | company |
| Tính năng sản phẩm, case study mang thương hiệu công ty | company |
| Thought leadership opinion | personal (thường gặp) |
| Thông báo tuyển dụng, tin tức về team | company |
| Newsletter | voice nào là mặc định thì dùng voice đó |

## Đầu ra

```
━━━━━━━━━━━━━━━━━━
🎙️ VOICE SELECTED
━━━━━━━━━━━━━━━━━━
Type: [personal/company]
Pronoun: [tôi/chúng tôi]
Hook style: [personal narrative / data-led / industry observation]
CTA style: [invite discussion / action-oriented / learn more]
Authority: [name and title from 06-authority.md]
Cross-post: [yes/no — if dual type]
━━━━━━━━━━━━━━━━━━
```

Ghi `selected_voice` vào `memory/task-state.json`.

Truyền lựa chọn voice sang li-post-writer (hoặc skill tạo nội dung liên quan).
