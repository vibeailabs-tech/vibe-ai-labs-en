---
name: Auto-save output to MD
description: Sau khi hoàn thành bài viết hoặc quality check, tự động lưu file MD — không hỏi user
type: feedback
---

Sau khi pipeline hoàn thành (viết bài, quality check, rewrite), tự động lưu file vào thư mục `output/` dưới dạng `.md` mà không hỏi user có muốn lưu không.

**Why:** User thấy việc hỏi "muốn xuất file md không?" là dư thừa và làm gián đoạn flow.

**How to apply:** Bất cứ khi nào output là bài Facebook hoàn chỉnh (đã qua check hoặc đã rewrite), tự lưu luôn vào `output/<tên-bài>.md` với metadata (pillar, trạng thái, lưu ý) ở đầu file.
