# Sales Page Skill

Your job is to write a complete long-form sales page — from headline to order button — that converts warm traffic into buyers or consultation bookings. Not a landing page (that's CRO Agent). A sales page: longer, deeper, designed to handle every objection before the prospect raises it.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — every line must match brand tone
- Core offer (Section 9) — what's being sold, at what price, what's included
- USP (Section 8) — the central claim the page builds toward
- Target audience (Section 6) — who is reading this page and what they fear
- Key messages (Section 11) — must appear on the page
- Competitors (Section 10) — differentiation points to weave in

If `/outputs/strategy/offer-positioning-*.md` exists: read it — use the refined offer structure and guarantee.
If `/outputs/assets/cro/lp-builder-*.md` exists: check for existing page structure to extend.

If brand.md doesn't exist: ask user for offer details, price, audience, and guarantee before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified offer and page goal**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết sales page, mình cần biết:
1. **Offer cụ thể:** Bạn đang bán gì? (tên gói, gì được include, timeline)
2. **Giá:** Bao nhiêu? Có installment không?
3. **CTA:** Book call / Buy now / Apply now?
4. **Guarantee:** Bạn có cam kết gì không?
5. **Traffic source:** Page này nhận traffic từ đâu? (cold ads / warm retargeting / email / organic)"

Wait for answer before continuing.

## Step 3 — Write the sales page

### Sales page structure (12 sections)

**1. Pre-headline (1 line)**
Qualifier that tells the right reader "this is for you."
"Dành cho doanh nghiệp đang trả >$300/tháng cho agency và muốn sở hữu hệ thống marketing của riêng mình."

**2. Headline**
The single biggest promise of the page. Must include:
- Who it's for (specific)
- What they get (outcome, not feature)
- Optional: timeframe or qualifier
Formula: "[Outcome] for [specific person] — [timeframe/qualifier]"

**3. Sub-headline**
Expand on the headline. Add specificity or a second benefit.

**4. Hero section — The stakes**
Why does this matter NOW? What happens if they don't act?
- Cost of inaction: "Bạn đang trả $X/tháng. Trong 12 tháng: $X×12. Bạn còn sở hữu gì?"
- Urgency that's real: "Window này không kéo dài — agency sẽ bắt đầu offer AI tools riêng trong 12–18 tháng"

**5. Problem section**
Agitate the pain they're living right now. 3–5 specific symptoms:
- "ChatGPT output vẫn generic và phải sửa lại mỗi lần"
- "Mỗi lần mở AI tool là phải nhắc lại context từ đầu"
- "Không biết bao giờ thì output đủ tốt để dùng mà không cần chỉnh"

**6. Bridge — Why existing solutions fail**
Agency: expensive, you don't own it. ChatGPT alone: no memory, no system. Hiring in-house: slow, expensive. Set up the positioning for your offer.

**7. The solution — Introduce the offer**
Name the offer. One sentence on what it is. Then: what's included, how it works, what they get at the end. Frame as a system, not a service.

**8. How it works (3-step process)**
Step 1: [What happens first]
Step 2: [The core work]
Step 3: [What they walk away with]
Keep it simple — 3 steps maximum. More steps create friction.

**9. What's included (the deliverables)**
Bullet list of tangibles. For each: what it is + why it matters.
Anchor the value: "Brand.md file — bạn sở hữu hoàn toàn, dùng mãi mãi"

**10. Proof section**
- Case study: before/after with specific numbers
- Testimonials: direct quotes with name, role, company
- Social proof: number of clients, logos, or results aggregated

**11. Objection section — FAQ**
Answer 5–7 objections directly:
- "Giá có cao không?" → anchor to cost of alternative
- "Mình không biết gì về AI có dùng được không?" → setup is done-for-you
- "Mất bao lâu để thấy kết quả?" → specific timeline
- "Nếu không hài lòng thì sao?" → state the guarantee

**12. CTA section**
- Primary CTA: clear action + button text
- Repeat the offer name + key benefit in 1 sentence
- Urgency/scarcity (only if real): "Còn X slots tháng này"
- Secondary CTA: lower friction ("Chưa chắc? Book tư vấn miễn phí 15 phút trước")
- Risk-reversal reminder: restate guarantee

### Vietnamese sales page rules

- **Price anchoring:** Always show price relative to something — "So với $X/tháng agency trong 12 tháng = $X tổng cộng — bạn không sở hữu gì. So với setup một lần $X — bạn sở hữu mãi mãi."
- **VND conversion:** If pricing in USD, show VND equivalent at current rate
- **Zalo CTA:** Include Zalo number prominently — Vietnamese buyers want to message before buying
- **Installment option:** Even for one-time fees, offer installment framing if applicable
- **Guarantee specificity:** "Hài lòng 100%" means nothing. "Nếu sau 30 ngày bạn không tự chạy được 3 agents — mình setup lại miễn phí" is specific and credible

## Step 4 — Write output

Save to `/outputs/assets/sales/sales-page-[offer-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Sales Page — [Offer Name]
> Generated: [date] | Offer: [name] | Price: [amount] | CTA: [action]

---

## Pre-headline
[Qualifier line]

## Headline
[Main headline]

## Sub-headline
[Supporting line]

---

## The Stakes
[Why now, cost of inaction]

---

## The Problem
[3–5 pain symptoms]

---

## Why Existing Solutions Fail
[Agency / ChatGPT / in-house — why each falls short]

---

## The Solution
[Offer introduction]

---

## How It Works
**Step 1:** [...]
**Step 2:** [...]
**Step 3:** [...]

---

## What's Included
- [Deliverable] — [why it matters]
- [Deliverable] — [why it matters]

---

## Proof
[Case study + testimonials]

---

## FAQ
**Q: [Objection]**
A: [Response]

---

## CTA Section
[Primary CTA + guarantee restatement]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Sales page cho '[Offer]' đã hoàn chỉnh.**

**Structure:** [n] sections
**Price framing:** [how price is anchored]
**Guarantee:** [guarantee statement]
**Primary CTA:** [button text]

📁 Đã lưu vào: `/outputs/assets/sales/sales-page-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/proposal-writer` để customize cho specific prospects, hoặc `/page-audit` (CRO Agent) để review conversion rate."

---
