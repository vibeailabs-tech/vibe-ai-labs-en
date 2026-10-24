# Objection Handler Skill

Your job is to write responses to the most common sales objections — not to overcome them aggressively, but to understand them, acknowledge them honestly, and redirect the conversation toward the right outcome. The goal is not to win an argument. The goal is to find out if there's a real fit.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — objection responses must stay in brand tone — never defensive
- Core offer (Section 9) — understand what's actually being objected to
- USP (Section 8) — the strongest counter-positioning
- Competitors (Section 10) — comparison objections need specific context

If brand.md doesn't exist: ask user for offer, common objections they hear, and how they currently respond before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided specific objections to handle**
Use their exact objections. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết objection responses, mình cần biết:
1. **Channel:** Email reply / LinkedIn reply / Zalo / Phone call?
2. **Stage:** Cold outreach reply / Sales call / After proposal sent?
3. **Objections phổ biến nhất bạn hay gặp:** (liệt kê 3–5 câu khách hàng hay nói)
4. **Objection nào khó nhất:** Cái nào bạn không biết trả lời như thế nào?"

Wait for answer before continuing.

## Step 3 — Write objection responses

### Objection response framework (ACCA)

**A — Acknowledge**
Never argue with an objection. The prospect feels something — validate it first.
"Mình hiểu điều đó..." / "Đó là câu hỏi mình hay nghe..." / "Bạn đúng khi lo về điều đó..."

**C — Clarify**
Most objections are surface-level. The real objection is underneath. Ask one question to surface it.
"Khi bạn nói [objection], bạn có thể nói thêm ý bạn muốn là gì không?" — sometimes the real objection is different from what was stated.

**C — Counter (softly)**
Reframe with evidence — not argument. One proof point, one reframe, no lecturing.

**A — Ask**
End with a question that moves the conversation forward. Never end an objection response with a statement.

### Universal objections (write responses for all)

**Objection 1: "Giá cao quá"**
This is rarely about price. Usually about unclear ROI or insufficient trust.
Response strategy: Acknowledge → Anchor to cost of status quo → Show specific ROI → Ask what "reasonable" looks like for them.

**Objection 2: "Để tôi suy nghĩ thêm / Để tôi bàn với team"**
Translation: "I'm not convinced enough to decide yet."
Response strategy: Acknowledge → Ask what they need to feel confident → Remove an obstacle → Offer to help them present to team if needed.

**Objection 3: "Chúng tôi đang dùng [competitor/agency] rồi"**
This is information, not rejection. They have a solution — your job is to find the gap.
Response strategy: Acknowledge → Express genuine interest in how it's working → Ask one specific question about a gap your offer fills → Don't badmouth the competitor.

**Objection 4: "Chúng tôi chưa có budget"**
Often true. Sometimes means "I don't see the value yet."
Response strategy: Acknowledge → Ask when budget review happens → Ask if there's a smaller entry point → Offer to stay in touch with a specific next-touch date.

**Objection 5: "AI không phù hợp với ngành/công ty chúng tôi"**
Fear of change or genuine skepticism.
Response strategy: Acknowledge the concern → Ask what specifically worries them → Share a relevant case study → Don't over-promise.

**Objection 6: "Tôi đã thử AI rồi, không hiệu quả"**
Real experience. Don't dismiss it.
Response strategy: Ask what they tried and what specifically didn't work → Explain why your approach is different (system vs tool) → Offer proof before asking for commitment.

**Objection 7: "Chúng tôi tự làm được / Có nhân viên làm rồi"**
Objection to outsourcing, not to the outcome.
Response strategy: Validate their capability → Ask about the time cost and consistency → Position as augmentation, not replacement.

### Vietnamese objection handling specifics

**Cultural note:** Vietnamese B2B buyers rarely say "no" directly — they say "để xem xét thêm" or "hơi bận". These are soft nos or genuine "not now"s. The objection handler must distinguish between:
- Soft no: Respond with graceful close, set a future date
- Genuine not now: Stay warm, set a specific follow-up trigger
- Real objection: Engage with ACCA framework

**Never pressure:** High-pressure responses destroy trust in Vietnamese B2B culture. "Chỉ còn 2 slots" is fine if true. "Bạn phải quyết định ngay" is not.

**Zalo objections:** Shorter responses. If they object on Zalo, acknowledge briefly and offer to discuss in more detail on a call or over email. Don't write a paragraph on Zalo.

**Price objections in VND vs USD:** If your pricing is in USD and the prospect pushes back, offer VND equivalent + installment framing. "2,000 USD một lần" feels bigger than "48 triệu — hoặc 24 triệu x 2 đợt".

## Step 4 — Write output

Save to `/outputs/assets/outreach/objection-handler-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Objection Handler — [Brand Name]
> Generated: [date] | Channel: [email/LinkedIn/Zalo/call] | Stage: [outreach/proposal/close]

---

## Objection 1: "Giá cao quá"

**What they're really saying:** [underlying concern]

**Response (email/DM):**
[ACCA-structured response — 3–5 sentences]

**Response (Zalo — shorter):**
[2–3 sentences]

**Follow-up question to ask:**
"[Question that moves conversation forward]"

**If they still push back:**
[One more reframe or graceful exit]

---

## Objection 2: "Để tôi suy nghĩ thêm"
[Repeat structure]

---

[Continue for all 7 universal objections + any brand-specific ones]

---

## Quick Reference Cheat Sheet

| Objection | First sentence to say |
|---|---|
| "Giá cao" | [opening line] |
| "Suy nghĩ thêm" | [opening line] |
| "Đang dùng competitor" | [opening line] |
| "Không có budget" | [opening line] |
| "AI không phù hợp" | [opening line] |
| "Đã thử rồi, không hiệu quả" | [opening line] |
| "Tự làm được" | [opening line] |
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Objection handler cho [Brand Name] đã hoàn chỉnh.**

**Objections covered:** [n] — [list]
**Channels:** Email / Zalo / Call versions included
**Quick reference:** Cheat sheet included for fast lookup

📁 Đã lưu vào: `/outputs/assets/outreach/objection-handler-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/personalization-framework` để scale outreach, hoặc `/sales-page` (Agent 12) để build trang bán hàng hỗ trợ outreach."

---
