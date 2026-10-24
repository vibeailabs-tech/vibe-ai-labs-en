# Objection Handler Skill

Your job is to write responses to sales objections — for email, Zalo, and sales calls. An objection is not a rejection. It's a request for more information or reassurance. The right response doesn't argue — it acknowledges, clarifies, counters with evidence, and re-opens the conversation.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — what you're defending
- USP (Section 8) — the differentiation that counters most objections
- Target audience (Section 6) — their fears and hesitations
- Key messages (Section 11) — proof points to use in responses

If `/outputs/assets/sales/case-study-*.md` exists: pull specific results to use as counter-evidence.
If brand.md doesn't exist: ask user for offer, price, and common objections heard before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified objections to handle**
Write responses for those specific objections. Go to Step 3.

**Path B — No direction provided**
Write responses for the 7 universal objections. Go to Step 3.

## Step 3 — Write objection responses

### The ACCA framework for every objection

**A — Acknowledge:** Validate the concern. Never argue or dismiss immediately.
**C — Clarify:** Ask one question to understand the real objection behind the surface one. Most surface objections ("giá cao") hide a deeper one ("I don't see the ROI yet").
**C — Counter:** Provide specific evidence, reframe, or address the real concern.
**A — Ask:** Re-open with a low-friction question that moves the conversation forward.

### The 7 universal objections

**Objection 1: "Giá cao quá"**
Real concern: "I don't see the ROI clearly enough to justify this."
Counter: Anchor to cost of alternative. "Bạn đang trả $X/tháng cho agency × 12 tháng = $X — và bạn không sở hữu gì. Setup một lần $X — bạn sở hữu mãi mãi."

**Objection 2: "Để suy nghĩ thêm / Để xem xét"**
Real concern: Insufficient conviction — something wasn't clear or compelling enough.
Counter: Surface the real hesitation. "Hoàn toàn hợp lý. Thường khi mọi người nói vậy, có một điều cụ thể chưa rõ — là phần nào bạn muốn mình giải thích thêm?"

**Objection 3: "Đang dùng [Competitor] rồi"**
Real concern: Switching cost, or genuinely satisfied (rare).
Counter: Acknowledge their choice, ask about gaps. "Tốt — [Competitor] có điểm mạnh riêng. Bạn đang dùng cho phần nào? Mình hay gặp nhất là [specific gap] — đó có phải vấn đề với bạn không?"

**Objection 4: "Không có budget lúc này"**
Real concern: Sometimes true. Often means "I don't see enough value yet."
Counter: Distinguish between the two. "Mình hiểu. Nếu budget thật sự là vấn đề — mình có thể suggest cách tiếp cận nhỏ hơn để bắt đầu. Nhưng nếu câu hỏi thật sự là ROI — bạn muốn mình walk through số không?"

**Objection 5: "AI không phù hợp với ngành/công ty mình"**
Real concern: Fear of change, or genuine industry-specific concern.
Counter: Ask for specifics. "Điều gì về ngành của bạn khiến bạn nghĩ vậy? Mình đã setup cho [relevant industry example] — và vấn đề chính thường không phải là ngành mà là [common real issue]."

**Objection 6: "Đã thử AI rồi, không hiệu quả"**
Real concern: Real past experience — this deserves genuine respect, not dismissal.
Counter: Dig into what they tried. "Mình muốn hiểu thêm — bạn đã thử gì cụ thể? Thường khi AI không work, nguyên nhân là [no brand memory / no system / wrong tool for the job] — và đó chính xác là thứ mình build khác."

**Objection 7: "Tự làm được / Không cần thuê ngoài"**
Real concern: They want control and ownership (actually aligned with your offer).
Counter: Agree with the goal, redirect to the method. "Hoàn toàn đúng — đó là lý do mình không bán dịch vụ retainer. Mình setup để bạn tự chạy và sở hữu toàn bộ. Câu hỏi là bao lâu bạn tự build được vs setup sẵn trong 9 ngày."

### Response formats by channel

**Email response (3–5 sentences):**
- Acknowledge in 1 sentence
- Clarifying question OR counter in 2 sentences
- Re-ask in 1 sentence
- Never over-explain — one strong counter beats three weak ones

**Zalo response (2–3 sentences):**
- Even shorter — Zalo is conversational
- Acknowledge + one question or one counter
- Emoji OK if brand voice allows (1 max)

**Call script (spoken format):**
- Pause after they finish — don't rush to respond
- "Mình hiểu..." + 1 sentence acknowledge
- "Bạn có thể nói thêm về..." (clarify) OR go straight to counter if clear
- Counter with one proof point — don't over-defend
- "Điều đó có giải quyết được lo ngại của bạn không?"

### Vietnamese sales culture specifics

**"Để xem xét" is rarely a hard no:** Vietnamese buyers avoid direct rejection. "Để suy nghĩ thêm" can mean genuine consideration, soft no, or "I need to talk to my partner/co-founder." Always clarify which.

**Price negotiation is expected:** Vietnamese buyers often negotiate on price even if they intend to buy. Don't drop price immediately — offer value-add (extra session, extended support) before discounting.

**Decision makers:** In Vietnamese SMBs, the founder often decides alone but may consult a spouse or business partner. "Để hỏi thêm" sometimes means this. Offer to join a second call with both.

**Never argue:** Vietnamese business culture avoids confrontation. Arguing with an objection — even when you're right — creates resistance. Agree partially, then redirect.

## Step 4 — Write output

Save to `/outputs/assets/sales/objection-handler-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Objection Handler — [Brand Name]
> Generated: [date]

---

## Objection 1: "Giá cao quá"

**Real concern:** [what's actually behind this]

**Email response:**
[3–5 sentences, ACCA]

**Zalo response:**
[2–3 sentences]

**Call script:**
[Spoken format with pause notes]

---

[Repeat for all 7 objections]

---

## Quick Reference Cheat Sheet

| Objection | Real concern | One-line counter |
|---|---|---|
| Giá cao | ROI unclear | [anchor to alternative cost] |
| Suy nghĩ thêm | Something unclear | "Phần nào bạn muốn mình giải thích thêm?" |
| Đang dùng competitor | Switching cost | "Bạn đang dùng cho phần nào?" |
| Không có budget | May be value issue | "ROI hay thật sự là budget?" |
| AI không phù hợp | Fear of change | "Điều gì cụ thể khiến bạn nghĩ vậy?" |
| Đã thử AI rồi | Real bad experience | "Bạn đã thử gì cụ thể?" |
| Tự làm được | Want control | "Đó là lý do mình không bán retainer" |
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Objection handler cho '[Brand]' đã hoàn chỉnh.**

**Objections covered:** 7 universal + [any additional requested]
**Formats:** Email / Zalo / Call script
**Quick reference:** Cheat sheet included

📁 Đã lưu vào: `/outputs/assets/sales/objection-handler-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/case-study` để build proof that counters objections, hoặc `/proposal-writer` để write customized proposals."

---
