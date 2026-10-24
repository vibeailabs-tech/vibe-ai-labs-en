# Community Management Skill

Your job is to write reply templates for comments, DMs, and negative reviews — so the brand can respond at scale without losing voice. Every template must sound like a real human response, not a script. Brand voice is non-negotiable even when handling difficult conversations.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5) — every reply must match this exactly
- Target audience (Section 6) — understand their frustrations and language
- Core offer (Section 9) — know what questions are really about
- Key messages (Section 11) — what to reinforce in replies

If brand.md doesn't exist: ask user for brand voice description and 3 common questions they receive before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided specific comments or scenarios to handle**
Use their exact examples. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết reply templates, mình cần biết:
1. **Platform chính:** Facebook / TikTok / Zalo / LinkedIn?
2. **Loại tương tác phổ biến nhất:** Comments trên post / DM hỏi giá / Reviews / Khiếu nại?
3. **Có tình huống cụ thể nào bạn hay gặp khó không?** (VD: 'so sánh với đối thủ', 'hỏi giá liên tục nhưng không mua', 'review tiêu cực')
4. **Bạn muốn dùng Zalo để support không?** — nếu có, mình sẽ include Zalo-specific templates."

Wait for answer before continuing.

## Step 3 — Build reply template library

### Template categories to cover

**Category 1 — Engagement replies (comments on posts)**
- Compliment / positive reaction
- Question about the topic (educational)
- Tag a friend comment
- "Interesting, tell me more" type comment
- Skeptical or challenging comment

**Category 2 — Sales inquiry replies (DMs and comments)**
- "Giá bao nhiêu?" — first price question
- "Có phù hợp với mình không?" — fit question
- "Mình đang dùng [competitor], có nên đổi không?" — comparison question
- "Cho mình thêm thông tin" — info request
- "Mình cần nghĩ thêm" — soft objection

**Category 3 — Negative review / complaint handling**
- Public negative comment on post
- 1-star review (Facebook / Google)
- DM complaint about service/product
- Unreasonable or unfair criticism
- Competitor or troll comment

**Category 4 — Common Vietnamese social questions**
- "Có ship không?" / "Có hỗ trợ toàn quốc không?"
- "Có trả góp không?"
- "Cho mình xem thêm review/portfolio"
- "Mình có thể thử trước không?"
- "Liên hệ qua Zalo được không?"

### Reply writing rules

**Voice consistency:**
- Same "bạn/mình" register as brand voice
- Match energy: if comment is enthusiastic, reply with warmth. If serious, reply professionally.
- Never copy-paste exact same reply twice on the same post — change at least the opening line
- Never defensive, never dismissive

**Reply length by type:**
- Positive comment: 1–2 sentences — acknowledge + add value or invite DM
- Question: 1–3 sentences — answer directly + one follow-up or CTA
- Negative public: 2–4 sentences — acknowledge, don't argue, move to private. Public replies are for the audience watching, not just the commenter.
- DM inquiry: Conversational, not scripted. Use the template as structure, adapt the tone.

**What never to write:**
- "Cảm ơn bạn đã quan tâm đến sản phẩm/dịch vụ của chúng tôi" — this is the most hated corporate reply in Vietnamese social media
- "Vui lòng inbox để được tư vấn" alone — too lazy, add value before redirecting
- Defensive replies to negative reviews — this always makes it worse
- Exclamation mark overuse — "Bạn đúng lắm ạ!!!" sounds insincere

**Negative review framework (the 4-step public reply):**
1. Acknowledge — show you read and understood the specific complaint
2. Empathize — don't argue even if they're wrong (the audience is watching)
3. Own or clarify — take responsibility for what's fair, clarify what's inaccurate (briefly)
4. Redirect — invite them to contact directly to resolve

**Sales inquiry DM framework:**
1. Warm opening — use their name if visible
2. Answer the question directly — don't dodge price if asked
3. One qualifying question — understand their situation before pitching
4. Clear next step — Zalo call, free consultation, or specific action

### Vietnamese community management specifics
- **Zalo-first resolution:** For complaints and complex inquiries, always offer to continue on Zalo — Vietnamese users trust Zalo more for personal communication
- **Response time signal:** Vietnamese B2B buyers expect same-day replies. Delay = distrust.
- **"Inbox" CTA:** "Nhắn inbox mình nha" is extremely common and accepted in Vietnamese social — use it to move conversation private
- **Emoji in replies:** 1 emoji max in professional/B2B context. More is fine in casual consumer brands.
- **Competitor mentions:** Never speak negatively about competitors by name in public replies — always deflect to your own value

## Step 4 — Write output

Save to `/outputs/assets/social/community-management-templates-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Community Management Templates — [Brand Name]
> Generated: [date] | Platforms: [list] | Voice: [voice descriptor]

---

## Category 1 — Engagement Replies

### Positive comment / compliment
**Situation:** Someone leaves a positive comment on a post
**Template:**
[Reply text]
**Variation:**
[Alternative opening if needed]

---

### Educational question in comments
**Situation:** Someone asks a follow-up question about the topic
**Template:**
[Reply text]

---

[Continue for all engagement types]

---

## Category 2 — Sales Inquiry Replies

### "Giá bao nhiêu?" — first price question
**Situation:** Someone asks for price in comment or DM
**Public comment reply:**
[Reply text — acknowledge + redirect to DM/Zalo]
**DM reply:**
[Full DM response — answer + qualify + next step]

---

[Continue for all sales inquiry types]

---

## Category 3 — Negative Review / Complaint

### Public negative comment
**Situation:** Critical comment on a post, visible to audience
**Template (4-step):**
[Reply text]
**What NOT to say:**
[Common mistake to avoid]

---

### 1-star review (Facebook / Google)
**Template:**
[Reply text]

---

[Continue]

---

## Category 4 — Common Vietnamese Questions

### "Có hỗ trợ toàn quốc không?"
**Template:**
[Reply]

---

[Continue for all common questions]

---

## Quick Reply Cheat Sheet
For when you need a fast response:

| Situation | Opening line |
|---|---|
| Positive comment | [line] |
| Price question (comment) | [line] |
| Complaint | [line] |
| "Tell me more" | [line] |
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Community management templates cho [Brand Name] đã hoàn chỉnh.**

**Templates built:**
- [n] engagement reply templates
- [n] sales inquiry templates
- [n] negative review / complaint templates
- [n] common question templates

📁 Đã lưu vào: `/outputs/assets/social/community-management-templates-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/social-copy` để viết content mới, hoặc `/social-calendar` để lên lịch tháng tới."

---
