---
name: Output file naming convention
description: All output files must include date prefix (YYYY-MM-DD) for tracking
type: feedback
---

Output files phải được đặt tên với ngày tháng ở đầu theo format: `YYYY-MM-DD-slug.md`

**Why:** User yêu cầu "tat ca cac file output thu them ngay thang o dau nua" — để dễ tracking, sorting, và reference sau này khi xem lại lịch sử content.

**How to apply:** Mọi file output tạo ra từ pipeline phải có date prefix. Ví dụ:
- `2026-05-05-qwen-3-5-analysis.md`
- `2026-05-06-product-launch.md`
- `2026-05-07-trend-report.md`

Không tạo file không có date prefix trong `/output/` folder.
