# Testimonial Framework Skill

Your job is to build a system for collecting, formatting, and deploying testimonials — so the brand always has fresh, specific social proof at every stage of the sales funnel. Most brands collect testimonials accidentally. This framework makes it a repeatable process.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — what the testimonials should prove
- Target audience (Section 6) — what proof they need to see to trust the brand
- Key messages (Section 11) — what claims need supporting evidence
- USP (Section 8) — the differentiation that testimonials should reinforce

If `/outputs/assets/sales/case-study-*.md` exists: use existing case studies as testimonial source material.
If brand.md doesn't exist: ask user for offer, client types, and key objections before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User has existing testimonials to format and deploy**
Format and place them. Go to Step 3.

**Path B — User needs a collection system**
Ask:
"Để build testimonial framework, mình cần biết:
1. **Hiện có testimonials chưa:** Bạn đang có bao nhiêu testimonials (dù thô)?
2. **Collection method:** Bạn muốn collect qua Zalo, email, Google Form, hay video?
3. **Objections cần counter:** Khách hàng thường lo ngại điều gì trước khi mua?
4. **Formats cần:** Text / Video / Star rating / Số liệu cụ thể?
5. **Deploy locations:** Sales page / Email / Social / Ads / Proposal?"

Wait for answer before continuing.

## Step 3 — Build the testimonial framework

### Part 1 — The collection system

**When to ask (timing is everything):**
- Best moment: Right after a win or milestone — "Mình vừa tự chạy xong agent đầu tiên!"
- Second best: End of setup/onboarding — 30 days in
- Never: Immediately after sale (no results yet) or when there's an open issue

**How to ask (the request message):**
Keep it short and specific. Don't say "viết review cho mình nhé." Say:
"[Tên], mình thấy bạn vừa [specific win]. Bạn có thể chia sẻ ngắn gọn: trước đây bạn đang gặp vấn đề gì, và giờ thay đổi như thế nào? Chỉ 2–3 câu thôi — mình muốn dùng để giúp người khác trong tình huống giống bạn."

**The 5-question testimonial framework:**
Ask these questions to extract a structured testimonial:
1. "Trước khi làm việc với [Brand], bạn đang gặp vấn đề gì cụ thể?"
2. "Điều gì khiến bạn quyết định thử — bạn lo ngại gì nhất lúc đầu?"
3. "Sau khi xong, điều gì thay đổi cụ thể nhất? (số liệu nếu có)"
4. "Bạn sẽ recommend cho ai — và nói gì về họ?"
5. "Có điều gì bạn không ngờ tới không?"

Question 2 (their hesitation before buying) is gold — it counters objections for future prospects.
Question 5 (unexpected benefit) often produces the most authentic, quotable lines.

**Collection channels:**
- Zalo: Best for Vietnamese market — voice note or text message. Transcribe voice notes.
- Google Form: For higher volume, link in post-setup email
- Video: Highest value but lowest collection rate — offer incentive or make it easy (phone recording is fine)

### Part 2 — Formatting testimonials

**The 3 elements of a strong testimonial:**
1. **Specific result** — number, timeframe, or concrete change
2. **Emotional truth** — how it felt, not just what happened
3. **Credibility signal** — name, role, company (even first name + industry works)

**Weak testimonial:**
"Mình rất hài lòng với dịch vụ. Chuyên nghiệp và hiệu quả. Recommend!"
→ No specifics, no result, no credibility signal. Generic. Could be anyone.

**Strong testimonial:**
"Trước đây mình tốn 3 tiếng/ngày cho content mà vẫn phải sửa lại. Giờ 45 phút/tuần — và output nhất quán hơn nhiều. Lần đầu tiên mình cảm giác mình đang xây thứ gì đó cho mình, không phải thuê của người khác."
— Minh Tuấn, Co-founder SaaS B2B, TPHCM
→ Specific time, specific change, emotional truth, full credibility signal.

**Editing testimonials (ethical guidelines):**
- Fix typos and grammar — OK
- Tighten for length — OK, with approval
- Change meaning or add claims they didn't make — never
- Always send edited version back for approval before publishing

### Part 3 — Deployment map

Map each testimonial to the funnel stage where it does the most work:

**Top of funnel (awareness):** Use result-focused testimonials in social posts and ads. Lead with the number.

**Middle of funnel (consideration):** Use process testimonials on the sales page. "I was worried about X, but Y" counters objections mid-read.

**Bottom of funnel (decision):** Use specific outcome + quote in proposals and email sequences. The most credible proof, closest to the buying decision.

**Objection-specific placement:** Map each testimonial to the objection it counters:
- "Giá cao" objection → testimonial about ROI/cost comparison
- "AI không hiệu quả" objection → testimonial about unexpected positive results
- "Mất nhiều thời gian" objection → testimonial about speed of setup

### Part 4 — Vietnamese testimonial specifics

**Privacy first:** Always ask permission before publishing. Many Vietnamese business owners are comfortable with first name + industry + city but not full company name.

**Zalo screenshots:** In Vietnamese market, Zalo conversation screenshots work as social proof — they feel authentic and unfiltered. Save and use with permission.

**Video testimonials:** Short (30–60 second) phone-recorded videos outperform polished studio testimonials for Vietnamese audiences. The slightly rough quality reads as genuine.

**Star ratings:** Vietnamese buyers look at Google Business Profile and Facebook reviews. Incentivize reviews on these platforms alongside collecting private testimonials.

## Step 4 — Write output

Save to `/outputs/assets/sales/testimonial-framework-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Testimonial Framework — [Brand Name]
> Generated: [date]

---

## Collection System

### When to ask
[Optimal timing guidance]

### Request message templates
**Zalo version:**
[Message text]

**Email version:**
[Message text]

### 5-question testimonial interview
1. [Question]
2. [Question]
3. [Question]
4. [Question]
5. [Question]

---

## Formatting Standards

### Strong testimonial template
"[Specific before] → [Specific after]. [Emotional truth]."
— [First name], [Role], [Industry/City]

### Weak → Strong rewrites
| Weak version | What's missing | Strong version |
|---|---|---|
| [example] | [what to add] | [rewritten] |

---

## Deployment Map

| Funnel stage | Testimonial type | Platform |
|---|---|---|
| Awareness | Result-focused | Facebook, TikTok, ads |
| Consideration | Process/objection-handling | Sales page, email |
| Decision | Specific outcome + quote | Proposal, closing email |

---

## Objection-to-Testimonial Map

| Objection | Testimonial that counters it | Where to place |
|---|---|---|
| [Objection 1] | [Testimonial type needed] | [Location] |

---

## Current Testimonial Inventory
[If user provided existing testimonials — formatted versions here]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Testimonial framework cho '[Brand]' đã hoàn chỉnh.**

**System includes:**
- Collection timing + request messages
- 5-question interview framework
- Formatting standards (weak → strong examples)
- Deployment map by funnel stage
- Objection-to-testimonial mapping

📁 Đã lưu vào: `/outputs/assets/sales/testimonial-framework-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Start collecting with the request message templates, hoặc chạy `/case-study` để turn existing client results into full case studies."

---
