# Transactional Email Skill

Your job is to write transactional emails — confirmations, receipts, onboarding triggers, notifications — that are clear, on-brand, and use every interaction as a trust-building moment. Transactional emails have the highest open rates of any email type. Most brands waste them.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand name and voice (Sections 1 + 5) — transactional emails must still sound like the brand
- Core offer (Section 9) — for upsell/cross-sell moments where appropriate
- Language (Section 4)

If brand.md doesn't exist: ask user for brand name, tone, and which transaction to write for before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified which transactional email to write**
Use what they gave. Go to Step 3.

**Path B — No specifics**
Ask:
"Loại transactional email nào bạn cần?
1. **Order confirmation** — xác nhận đơn hàng / thanh toán
2. **Welcome / onboarding** — sau khi đăng ký tài khoản hoặc mua lần đầu
3. **Delivery / fulfillment** — xác nhận giao hàng hoặc access
4. **Password reset / account** — security email
5. **Appointment confirmation** — xác nhận lịch hẹn / booking
6. **Invoice / receipt** — hóa đơn điện tử
7. **Notification** — trigger-based alert (payment due, expiry reminder, usage milestone)"

Wait for answer.

## Step 3 — Write the transactional email

### Transactional email principles

**The primary job: confirm and reassure**
Every transactional email must answer: "Did my action work?" within the first 2 lines. Don't make them search for the confirmation.

**The secondary job: build trust and move forward**
After confirming, use the email to:
- Reinforce the brand promise
- Set expectations for what happens next
- Provide one helpful resource or next step
- (Optional) plant the seed for the next action — without being pushy

**What NOT to do:**
- Don't bury the confirmation under a brand intro
- Don't put 3 CTAs — one secondary suggestion max
- Don't make it feel like a promotional email — people expect pure utility
- Don't skip branding entirely — a plain text receipt is a missed brand moment

### Transactional email structure

```
[Brand logo/name — minimal header]

[Confirmation statement — 1 sentence, bold or prominent]
"Đơn hàng của bạn đã được xác nhận." / "Lịch hẹn đã được đặt." / etc.

[Key details — the facts they need]
- What: [product/service/appointment]
- When: [date/time if applicable]
- Amount: [if financial transaction]
- Reference: [order number, booking ID]

[What happens next — 1–3 bullet points]
"Bạn sẽ nhận được [X] trong [timeframe]."

[One helpful resource or next step — optional but recommended]
Link to: FAQ / getting started guide / calendar add / contact support

[Support info — always include]
"Có câu hỏi? Nhắn Zalo [number] hoặc email [address]. Mình phản hồi trong [timeframe]."

[Sign-off — personal, not corporate]
```

### Vietnamese market specifics

**Payment confirmations:**
- Always include exact amount in VND (even if invoice is in USD — add VND equivalent)
- Include bank transfer reference if paid by bank transfer (phổ biến ở Việt Nam)
- Zalo support link > email for Vietnamese users — faster, more trusted channel

**Appointment/booking confirmations:**
- Include Zalo calendar link or Google Calendar link to add
- Include exact address with Google Maps link (Vietnamese users rely heavily on Maps)
- Include "Nếu cần đổi lịch: nhắn Zalo [number]" — flexible rescheduling builds trust

**Onboarding welcome:**
- First email after purchase is highest-read email in the relationship — use it fully
- Set clear expectations: "Trong 24 giờ tới bạn sẽ nhận được [X]"
- Introduce the human behind the brand: "Mình là [Tên] — người sẽ setup hệ thống cho bạn"

**Receipt/invoice:**
- Vietnamese businesses often need VAT invoice (hóa đơn VAT) — include note on how to request
- PDF attachment preferred over inline-only for record keeping

### Tone calibration for transactional emails

Transactional emails should be:
- **Clearer** than marketing emails (utility first)
- **Warmer** than generic system emails (it's still your brand)
- **Shorter** than newsletters (get to the point fast)

The "bạn/mình" register still applies. A confirmation email that says "Kính gửi Quý khách" when all your other emails say "bạn" breaks the brand experience.

## Step 4 — Write output

Save to `/outputs/assets/email/transactional-[type]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Transactional Email — [Type]
> Generated: [date] | Type: [transaction type] | Trigger: [what sends this email]

## Trigger
[Exact event that sends this email — e.g., "Stripe payment confirmed", "Calendly booking created"]

## Email

**Subject:** [subject line — clear, not clever]
**From name:** [Brand name or "Tên từ Brand"]

---

[Full email content]

---

## Notes
- Dynamic fields: [list all {{variables}} used — name, order number, date, amount, etc.]
- Fallback for missing data: [what to show if variable is blank]
- Send timing: [immediately / delay X minutes / trigger condition]
- Reply-to: [support email or no-reply + Zalo]
- VAT invoice note: [include or not]

## Upsell / Cross-sell Opportunity
[If applicable: one low-friction next step to include — or "None — keep pure utility"]
```

## Step 5 — Confirm

After writing:

---
"✅ **Transactional email '[Type]' hoàn chỉnh.**

**Trigger:** [event]
**Primary job:** [confirmation statement]
**Secondary:** [one next step or resource]
**Dynamic fields:** [list]

📁 Đã lưu: `/outputs/assets/email/transactional-[type]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/email-sequence` để viết onboarding sequence sau transactional email này, hoặc `/re-engagement` để build win-back cho customers đã lapsed."

---
