---
name: USP-definition
description: Defines the Unique Selling Point, transformation story, proof points, and key messages for a Vietnamese business. Use this skill when the user wants to articulate what makes them truly unique, build their core marketing messages, or fill the USP and Key Messages sections of brand.md. Trigger whenever the user mentions USP, unique selling point, what makes them different, proof points, key messages, or their main marketing claim.
---

# USP Definition Skill

Your job is to find the one thing this brand does that no competitor does the same way — and turn it into a message sharp enough to make a customer stop and say "đúng rồi, cái này mình cần."

Most businesses think their USP is quality or service. It's not. Those are table stakes. A real USP is specific, provable, and hard to copy. Your job is to dig until you find it.

## Step 1 — Check brand.md

Read the file `/outputs/profiles-output/brand.md`.

- If Section 5 (Brand Voice) is empty: warn — "Bạn chưa chạy /brand-voice. Nên chạy trước để USP khớp với giọng thương hiệu."
- If Section 6 (Target Audience) is empty: warn — "Bạn chưa chạy /audience-profile. USP sẽ mạnh hơn nếu biết rõ khách hàng mục tiêu."
- If Section 7 (Positioning) is empty: warn — "Bạn chưa chạy /positioning. Nên chạy trước để USP bổ trợ đúng định vị."
- Note everything already filled — Brand Voice, Audience, Positioning all feed directly into the USP.
- You will write to Section 8 (USP) and Section 11 (Key Messages). Never touch other sections.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User already described their unique advantage and proof**
Use what they gave you. Go to Step 3.

**Path B — No USP info provided**
Ask all these questions at once:

---
"Để xây dựng điểm bán hàng độc nhất, mình cần biết thêm:

1. **Cơ chế độc đáo:** Bạn làm điều gì theo cách mà không ai khác làm? Có quy trình, công thức, phương pháp, hay cam kết nào chỉ riêng bạn có không?
2. **Trước và sau:** Khách hàng trông như thế nào TRƯỚC khi dùng sản phẩm/dịch vụ của bạn? Và họ thay đổi thế nào SAU đó?
3. **Bằng chứng:** Bạn có con số, giải thưởng, chứng chỉ, hay testimonial nào không? (Ví dụ: 500+ khách hàng, 5 năm kinh nghiệm, đạt chứng nhận X...)
4. **Điều khách hay khen:** Khách hàng khen bạn điều gì nhiều nhất — không phải bạn tự nói, mà họ tự nói?
5. **Cam kết:** Nếu bạn phải đưa ra một lời hứa với khách hàng — một điều bạn tự tin 100% có thể thực hiện — đó là gì?"

*(To define your USP: 1. What do you do in a way no one else does? 2. What does the customer look like before and after? 3. What proof do you have — numbers, awards, testimonials? 4. What do customers praise you for most? 5. What one promise can you make with 100% confidence?)*

---

Wait for the user's answers before continuing.

## Step 3 — Analyze and build the USP

Based on the input and everything in brand.md, build the complete USP output.

**Find the unique mechanism — this is the hardest part:**
A unique mechanism is not "good service" or "quality products." It is a specific, nameable process, method, ingredient, or commitment that:
- Produces a result the customer actually wants
- Is different from how competitors do it
- Can be explained in one sentence

Examples:
- A cafe that roasts its own beans weekly → "Rang tươi mỗi tuần — không bao giờ bán cà phê cũ hơn 7 ngày"
- A coach who uses a specific framework → "Phương pháp 3-bước XYZ — từ mục tiêu mơ hồ đến kế hoạch cụ thể trong 90 phút"
- A skincare brand → "Công thức không chất bảo quản — chỉ 7 nguyên liệu, không thêm gì khác"

If the user can't articulate one, look for it in what customers praise and what the business does differently in practice. Name it. Give it a label.

**Transformation — make it visceral:**
- Before: describe the specific frustration, anxiety, or struggle the customer has before buying. Use emotional language, not abstract categories.
- After: describe the specific outcome they experience. Not "họ hài lòng" — what does their life actually look like now?

**Proof points — specificity builds trust in Vietnam:**
- Numbers are powerful: "đã phục vụ 1,200+ khách hàng"
- Time signals reliability: "5 năm kinh nghiệm trong ngành"
- Social proof: specific testimonials, not generic praise
- Credentials: certificates, awards, media mentions
- If they have no formal proof yet: help them identify proof they do have but haven't framed (repeat customers, word-of-mouth rate, etc.)

**5 headline directions — each attacks from a different angle:**
1. **Outcome headline** — lead with the result the customer gets
2. **Mechanism headline** — lead with the unique way you do it
3. **Before/after headline** — contrast the struggle with the solution
4. **Social proof headline** — lead with the number or testimonial
5. **Challenge headline** — call out what everyone else does wrong, then position this brand as the fix

Write each headline in Vietnamese. Keep them punchy — under 12 words. These will be used in ads, posts, and landing pages.

**Key messages — 3 things this brand always says:**
These are the 3 core ideas that show up in every piece of content, every sales conversation, every post. They should:
- Reinforce the positioning from Section 7
- Connect directly to what the target audience cares about
- Be specific enough to actually guide content decisions

Not "chúng tôi luôn đặt khách hàng lên hàng đầu" — that's noise. Think: what are the 3 beliefs this brand keeps coming back to?

## Step 4 — Write to brand.md

Update `/outputs/profiles-output/brand.md`:
- Write Section 8 (USP) — unique mechanism, transformation, proof points, 5 headline directions
- Write Section 11 (Key Messages) — 3 core messages
- Update the `Last updated` date
- Never touch any other section

## Step 5 — Confirm

After writing, reply:

---
"✅ **USP của [Brand Name] đã được xác định và lưu lại.**

**Tóm tắt:**
- Cơ chế độc đáo: [one sentence — the unique mechanism]
- Chuyển hóa: Từ [before state] → Đến [after state]
- Bằng chứng mạnh nhất: [top proof point]

**5 hướng headline:**
1. [Headline 1 — outcome]
2. [Headline 2 — mechanism]
3. [Headline 3 — before/after]
4. [Headline 4 — social proof]
5. [Headline 5 — challenge]

**3 thông điệp chủ lực:**
1. [Message 1]
2. [Message 2]
3. [Message 3]

📁 Đã lưu vào: `/outputs/profiles-output/brand.md` — Mục 8 + Mục 11

**Bước tiếp theo:** Chạy `/brand-setup` để xem toàn bộ brand profile hoàn chỉnh của bạn."

---
