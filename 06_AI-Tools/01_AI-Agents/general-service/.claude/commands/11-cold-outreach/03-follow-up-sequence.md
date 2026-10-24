# Follow-Up Sequence Skill

Your job is to write multi-touch follow-up sequences — the messages sent after the first cold outreach when there's no reply. Most deals don't close on the first touch. Most salespeople give up after one or two attempts. The follow-up sequence is where the gap is.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — every follow-up must stay in brand voice
- Core offer (Section 9) — the sequence builds toward this
- Target audience (Section 6) — their behavior patterns and objections

If `/outputs/assets/outreach/cold-email-*.md` exists: read it — the follow-up continues from the first touch.
If `/outputs/assets/outreach/linkedin-dm-*.md` exists: build a multi-channel sequence.
If brand.md doesn't exist: ask user for offer, first touch context, and prospect type before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided first touch context**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết follow-up sequence, mình cần biết:
1. **First touch đã gửi gì:** Email / LinkedIn DM / Zalo?
2. **Bao nhiêu follow-ups:** 3 / 5 / 7 touches?
3. **Channel:** Email only / Multi-channel (email + LinkedIn + Zalo)?
4. **Spacing:** Aggressive (2–3 ngày) / Standard (5–7 ngày) / Gentle (7–14 ngày)?
5. **Break-up email:** Có muốn include email cuối 'mình sẽ không liên hệ nữa' không?"

Wait for answer before continuing.

## Step 3 — Write the follow-up sequence

### Follow-up sequence principles

**Each follow-up must add new value — never just bump**
"Just following up on my previous email" is the most useless follow-up in existence. It adds nothing. Every follow-up should introduce a new angle, a new piece of evidence, or a new reason to respond.

**Change the angle each time**
- Touch 1 (cold email): Problem angle
- Touch 2: Different proof or case study
- Touch 3: New insight or relevant content
- Touch 4: Reframe the ask (lower friction)
- Touch 5: Social proof or urgency
- Touch 6: Break-up — honest, no-pressure close

**Subject line variation**
Never repeat the same subject line. Each follow-up should look like a fresh thread OR reply to the existing thread. Both work — test which performs better.

**Length decreases over time**
- Touch 1: 5–8 sentences
- Touch 2–3: 3–5 sentences
- Touch 4–5: 2–3 sentences
- Touch 6 (break-up): 3–4 sentences

### Standard 6-touch sequence

**Touch 1 — Cold email (Day 0)**
Already written by `/cold-email` skill. Reference it here.

**Touch 2 — New angle (Day 3–5)**
Introduce a different proof point or reframe the problem from a new angle.
Subject: Reply to original thread OR new subject
Length: 4–5 sentences

**Touch 3 — Value add (Day 8–10)**
Share something genuinely useful — a relevant article, a data point, a short insight. No ask except a soft "curious if this is relevant to you."
Length: 3–4 sentences

**Touch 4 — Case study or social proof (Day 15–17)**
Share a specific result from a similar company. Make it concrete.
Length: 4–5 sentences, one clear ask

**Touch 5 — Reframe the ask (Day 22–25)**
Lower the friction — instead of asking for a call, ask for a yes/no answer, or offer to send a one-pager first.
Length: 2–3 sentences

**Touch 6 — Break-up email (Day 30–35)**
Honest, no-pressure. "Mình hiểu bạn bận và không muốn làm phiền thêm. Nếu thời điểm chưa phù hợp, mình sẽ không liên hệ nữa — chỉ cần reply 'chưa phù hợp' là đủ."
This email often gets the highest reply rate of the sequence — people feel safe replying because there's no pressure.
Length: 3–4 sentences

### Multi-channel sequencing

When combining email + LinkedIn + Zalo:

```
Day 0:   Email (cold email — Version A)
Day 1:   LinkedIn connection request (if not connected)
Day 3:   LinkedIn DM (after connection accepted)
Day 5:   Email follow-up (Touch 2 — new angle)
Day 8:   LinkedIn follow-up DM (value add)
Day 12:  Email (Touch 3 — case study)
Day 18:  Zalo message (if number available — short, warm)
Day 25:  Email (Touch 4 — reframe ask)
Day 32:  Email (Touch 5 — break-up)
```

Multi-channel increases reply rate significantly — different people check different channels first.

### Vietnamese follow-up specifics

**Zalo in the sequence:** If you have their Zalo number, a short Zalo message mid-sequence is highly effective. Vietnamese B2B contacts check Zalo more frequently than email. Keep it to 2–3 sentences — Zalo is messaging, not email.

**Vietnamese business culture:** Vietnamese B2B prospects may not reply not because they're uninterested but because they're busy or waiting for the right moment. A gentle, respectful follow-up sequence signals persistence without aggression.

**Timing around Vietnamese holidays:** Avoid sending follow-ups in the 3 days before and after Tết, 30/4–1/5, and 2/9. Prospects are in holiday mode and emails get buried.

**The break-up email in Vietnamese:** Must be warm, not cold. "Mình hiểu bạn có nhiều việc hơn là reply email của mình" — acknowledge their busyness with warmth, not passive aggression.

## Step 4 — Write output

Save to `/outputs/assets/outreach/follow-up-sequence-[prospect-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Follow-Up Sequence — [Prospect/Campaign]
> Generated: [date] | Touches: [n] | Channels: [email/LinkedIn/Zalo] | Spacing: [aggressive/standard/gentle]

---

## Sequence Overview

| Touch | Day | Channel | Angle | Length |
|---|---|---|---|---|
| 1 | 0 | Email | Problem-led | 5–8 sentences |
| 2 | [n] | [channel] | [angle] | [length] |
[...]

---

## Touch 1 — Cold Email (Day 0)
*[Reference to cold-email output or write here if standalone]*

---

## Touch 2 — [Angle] (Day [n])
**Channel:** [Email/LinkedIn/Zalo]
**Subject:** [subject line]

[Body]

---

## Touch 3 — Value Add (Day [n])
**Channel:** [channel]
**Subject:** [subject]

[Body]

---

[Continue through all touches]

---

## Touch [N] — Break-up (Day [n])
**Channel:** Email
**Subject:** [subject]

[Body]

---

## Sequence Notes
- Total timeline: [n] days
- Expected reply rate: [%] range for this prospect type
- If reply at any touch: [what to do — pivot to objection handler or pitch]
- CRM tags to set: [interested / not now / wrong person / unsubscribe]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Follow-up sequence cho '[Prospect/Campaign]' đã hoàn chỉnh.**

**Sequence:** [n] touches over [n] days
**Channels:** [list]
**Break-up email:** Touch [n] — Day [n]

📁 Đã lưu vào: `/outputs/assets/outreach/follow-up-sequence-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/objection-handler` để prepare responses khi prospect replies với objections."

---
