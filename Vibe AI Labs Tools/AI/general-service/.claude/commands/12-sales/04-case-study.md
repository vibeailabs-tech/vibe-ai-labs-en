# Case Study Skill

Your job is to write customer case studies — before/after stories with specific numbers that turn skeptical prospects into buyers. A case study is not a testimonial and not a portfolio piece. It's a structured proof document that mirrors the reader's situation, shows what changed, and makes the result feel achievable for them too.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — what the case study should demonstrate
- Target audience (Section 6) — the reader this case study needs to resonate with
- Key messages (Section 11) — the narrative the case study should reinforce
- USP (Section 8) — what made the result possible

If brand.md doesn't exist: ask user for client details and results before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided client details and results**
Use their input. Go to Step 3.

**Path B — No client info provided**
Ask:
"Để viết case study, mình cần biết:
1. **Client:** Tên (hoặc anonymous), industry, company size, location?
2. **Before:** Họ đang gặp vấn đề gì trước khi làm việc với bạn? Cụ thể nhất có thể.
3. **After:** Kết quả cụ thể sau khi xong — số liệu, thời gian, tiền bạc, cảm nhận?
4. **Timeline:** Mất bao lâu để đạt kết quả?
5. **Quote:** Họ nói gì về trải nghiệm? (dù 1–2 câu cũng được)"

Wait for answer before continuing.

## Step 3 — Write the case study

### Case study structure (6 sections)

**1. Title**
Formula: "[Specific result] — [Client type] in [Timeframe]"
Example: "Từ $500/tháng Freelancer Xuống $80/tháng API — SMB Founder tại TPHCM trong 30 ngày"

**2. The snapshot (3 numbers)**
Before reading, the prospect should see 3 numbers that make them curious:
- Time saved: "3 giờ/ngày → 45 phút/tuần"
- Cost saved: "$500/tháng → $80/tháng"
- Timeline: "9 ngày setup"

**3. Background — Who they are**
One paragraph: who the client is (industry, size, role), what they were doing for marketing before, and the single sentence that captures their frustration. Use their exact words if possible.

**4. The problem — Before state**
Specific pain points. Not "they had marketing challenges." What exactly was happening:
- "Tốn 2–3 giờ mỗi ngày viết content nhưng output vẫn generic"
- "Trả freelancer $500/tháng nhưng phải sửa lại hầu hết bài"
- "Không có file nào thuộc sở hữu của công ty sau 8 tháng"

**5. What happened — The process**
Walk through what was done: what was built, in what sequence, what the client experienced. Keep it concrete — name the steps, the tools, the timeline. This is where the methodology shines.

**6. The result — After state**
Specific numbers + specific timeline + direct quote from the client.
- Quantitative: time, money, output volume
- Qualitative: how they feel, what changed in how they work
- Quote: their words in quotation marks — the most credible element on the page

### Case study formats

**Short case study (300–400 words)**
Used for: sales page proof section, email sequence, social media
Structure: Snapshot → Problem (1 para) → What changed (1 para) → Result + quote

**Full case study (600–900 words)**
Used for: dedicated case study page, sales call leave-behind, proposal appendix
Structure: All 6 sections fully developed

**Quote card (50 words)**
Used for: social media, email headers, ad creative
Extract: The single most powerful quote + client name/role + 1 number

### Writing a credible case study

**Specificity is credibility:**
- "Tiết kiệm thời gian đáng kể" = not credible
- "Từ 3 giờ/ngày xuống 45 phút/tuần — đo bằng time tracking trong 30 ngày" = credible

**Acknowledge what was hard:**
A case study that claims everything was perfect is not believable. Include one challenge or learning: "Phần khó nhất là buổi đầu tiên build brand.md — mất 90 phút nhưng đây là foundation cho mọi thứ sau đó."

**The client quote must be genuine:**
Never paraphrase and frame it as a quote. If you don't have a real quote, write "Client shared: [paraphrase]" — not fake quotation marks.

**Mirror the target reader's situation:**
The client in the case study should look like the target reader — same industry, similar size, similar pain. If your reader is a TPHCM SMB founder, the case study should feature a TPHCM SMB founder.

### Vietnamese case study specifics

**Privacy:** Many Vietnamese business owners prefer not to have their company named. Use first name only + role + city: "Minh Tuấn, co-founder SaaS B2B tại TPHCM." Ask permission before publishing full company name.

**VND vs USD:** Present costs in both if relevant — some readers relate better to VND amounts.

**Community recognition:** If the client is known in a specific Vietnamese business community (Startup Vietnam, YPO Vietnam, etc.) — mention it. Peer recognition increases case study credibility.

## Step 4 — Write output

Save to `/outputs/assets/sales/case-study-[client-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Case Study — [Title]
> Generated: [date] | Client: [type] | Industry: [industry] | Timeline: [timeframe]

---

## Snapshot
- [Metric 1 before → after]
- [Metric 2 before → after]
- [Timeline]

---

## Background
[Who they are — 1 paragraph]

---

## The Problem
[Specific before state — 3–5 pain points]

---

## What Happened
[Process walkthrough — concrete steps and timeline]

---

## The Result
[Specific numbers + direct client quote]

---

## Short Version (for sales page / email)
[300-word condensed version]

---

## Quote Card
"[Direct quote]"
— [Name], [Role], [Company/City]
[Key number]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Case study '[Title]' đã hoàn chỉnh.**

**Format:** Full + Short version + Quote card
**Key result:** [primary metric]
**Best quote:** '[first 10 words of quote]...'

📁 Đã lưu vào: `/outputs/assets/sales/case-study-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Add case study to sales page proof section, hoặc chạy `/testimonial-framework` để collect more proof systematically."

---
