# Proposal Writer Skill

Your job is to write customized sales proposals for specific prospects — after they've expressed interest. A proposal is not a quote. It's a document that reflects back the prospect's specific situation, shows you understood their problem, and makes the decision to proceed feel obvious.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — packages, pricing, what's included
- USP (Section 8) — what differentiates this from alternatives
- Brand voice (Section 5) — proposal tone

If `/outputs/strategy/offer-positioning-*.md` exists: use the refined package structure.
If `/outputs/assets/sales/case-study-*.md` exists: pull the most relevant case study for this prospect.

If brand.md doesn't exist: ask user for offer, pricing, and prospect situation before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided prospect details**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết proposal, mình cần biết:
1. **Prospect:** Tên công ty, industry, company size?
2. **Situation:** Họ đang gặp vấn đề gì cụ thể? (từ cuộc gọi/email trước)
3. **Goals:** Họ muốn đạt được gì trong 90 ngày?
4. **Package:** Bạn đang recommend gói nào?
5. **Timeline:** Họ muốn bắt đầu khi nào?"

Wait for answer before continuing.

## Step 3 — Write the proposal

### Proposal structure (7 sections)

**1. Cover page**
- Prospect company name + logo placeholder
- "Đề xuất hợp tác: [Project Name]"
- Prepared by: [Your name], [Date]
- Valid until: [Date + 14 days — creates urgency]

**2. Executive summary (1 page max)**
- Their situation in 2–3 sentences (show you listened)
- The outcome you're proposing to deliver
- Investment and timeline summary
- One sentence on why now

**3. Understanding their situation**
Reflect back what you heard in the discovery call:
- Current state: what they're doing now, what's not working
- The cost of the current situation (time, money, opportunity)
- What they told you they want instead
This section builds trust — it shows you were paying attention.

**4. Proposed solution**
- Which package/approach you're recommending and why (specific to their situation)
- What's included — detailed deliverables
- What's NOT included (prevents scope disputes later)
- The 3-step process: what happens in each phase

**5. Expected outcomes**
- Specific, measurable outcomes tied to their stated goals
- Timeline: what they'll have at 30 days, 60 days, 90 days
- How success is measured — define this clearly upfront
- Reference: "Based on [similar client], who achieved [result] in [timeframe]..."

**6. Investment**
- Package name + total price
- What's included at this price point
- Payment structure (full upfront vs installment)
- Price anchoring: compare to their current spend or alternative cost
- The guarantee — stated specifically

**7. Next steps**
- Decision by date (14 days from proposal date)
- What happens after they say yes (immediate next action)
- How to proceed: Zalo, email, or link to sign/pay
- "If you have questions before deciding:" — Zalo number

### Proposal writing rules

**Mirror their language:** Use words they used in the discovery call. If they said "mình cần hệ thống tự chạy được" — use that exact phrase. It signals you understood.

**Be specific about their situation:** "Bạn đang trả $500/tháng cho freelancer và output không nhất quán" hits harder than "nhiều doanh nghiệp đang gặp vấn đề với marketing."

**Recommend, don't menu-dump:** Tell them which package is right for them and why — don't list all options and make them choose. "Dựa trên những gì mình nghe, Growth Package phù hợp nhất với situation của bạn vì..."

**The guarantee section:** State it specifically. "Nếu sau setup bạn không tự chạy được 3 agents — mình làm lại miễn phí" is a guarantee. "Cam kết hài lòng" is not.

**Vietnamese proposal specifics:**
- Include VND pricing alongside USD
- Payment terms: full payment or 50/50 (50% before, 50% after setup) — Vietnamese businesses prefer milestone-based payments
- Include Zalo contact throughout — not just at the end
- "Valid until [date]" creates real urgency — use it

## Step 4 — Write output

Save to `/outputs/assets/sales/proposal-[prospect-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Proposal — [Prospect Company Name]
> Generated: [date] | Package: [name] | Investment: [amount] | Valid until: [date]

---

## Cover
**Đề xuất hợp tác:** [Project Name]
**Chuẩn bị cho:** [Prospect Name], [Company]
**Từ:** [Your Name], [Company Name]
**Ngày:** [Date] | **Hiệu lực đến:** [Date +14 days]

---

## Executive Summary
[2–3 sentences: situation + proposed outcome + investment]

---

## Tình huống hiện tại của [Company]
[Reflect back their situation — specific details from discovery call]

---

## Giải pháp đề xuất
**Package:** [Name]

**Bao gồm:**
- [Deliverable] — [why this matters for them specifically]

**Không bao gồm:**
- [Clear exclusion]

**Quy trình 3 bước:**
1. [Phase 1 — what happens, timeline]
2. [Phase 2]
3. [Phase 3 — what they have at the end]

---

## Kết quả kỳ vọng
- Sau 30 ngày: [specific milestone]
- Sau 60 ngày: [specific milestone]
- Sau 90 ngày: [specific outcome]

---

## Đầu tư
**[Package Name]:** [Amount VND / USD]
**Thanh toán:** [Structure]
**Cam kết:** [Specific guarantee]

So với: [cost of current approach × 12 months]

---

## Bước tiếp theo
Quyết định trước: [Date]

Để tiến hành: [specific action — Zalo/email/link]
Zalo: [number] — phản hồi trong 30 phút giờ hành chính
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Proposal cho '[Company]' đã hoàn chỉnh.**

**Package recommended:** [name] — [one-line reason]
**Investment:** [amount]
**Guarantee:** [statement]
**Valid until:** [date]

📁 Đã lưu vào: `/outputs/assets/sales/proposal-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Send proposal → follow up in 2 days via Zalo if no response. Chạy `/objection-handler` để prepare cho các câu hỏi từ prospect."

---
