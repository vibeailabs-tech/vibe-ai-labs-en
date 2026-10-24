---
name: positioning
description: Builds competitive positioning, core offer definition, and competitor analysis for a Vietnamese business. Use this skill when the user wants to define how their brand stands out, what makes them different from competitors, or fill the Positioning, Core Offer, and Competitors sections of brand.md. Trigger whenever the user mentions positioning, differentiation, competitors, unique advantage, or how they're different from others.
---

# Positioning Skill

Your job is to define exactly where this brand sits in the market — who it's for, what it beats, and why a customer should choose it over every other option. Not vague claims like "chất lượng cao" or "dịch vụ tốt" — those mean nothing. You need a specific, defensible position.

In Vietnam, positioning is shaped by trust signals, social proof, price perception, and the specific anxieties of the local buyer. A good positioning statement answers: "Why this brand, not the one next door?"

## Step 1 — Check brand.md

Read the file `/outputs/profiles-output/brand.md`.

- If Section 5 (Brand Voice) is empty: warn — "Bạn chưa chạy /brand-voice. Mình vẫn có thể xây dựng định vị, nhưng kết quả sẽ tốt hơn nếu chạy /brand-voice trước."
- If Section 6 (Target Audience) is empty: warn — "Bạn chưa chạy /audience-profile. Định vị sẽ chính xác hơn nếu bạn đã có hồ sơ khách hàng."
- Note the Industry, Location, Brand Voice, and Target Audience already filled — use all of these to inform your analysis.
- You will write to Section 7 (Positioning), Section 9 (Core Offer), and Section 10 (Competitors). Never touch other sections.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User already described their competitors and differentiators**
Use what they gave you. Go to Step 3.

**Path B — No competitive info provided**
Ask all these questions at once:

---
"Để xây dựng định vị cạnh tranh, mình cần biết thêm:

1. **Đối thủ cạnh tranh:** Kể tên 2–3 đối thủ chính của bạn. Khách hàng thường so sánh bạn với ai?
2. **Điểm khác biệt:** Bạn làm được điều gì mà đối thủ không làm được — hoặc làm không tốt bằng bạn?
3. **Sản phẩm/dịch vụ chính:** Bạn đang bán gì? Mô tả ngắn gọn sản phẩm/dịch vụ chủ lực và mức giá.
4. **Khách hàng nói gì:** Khi khách hàng giới thiệu bạn cho người khác, họ thường nói gì về bạn?
5. **Bạn muốn được biết đến là gì:** Trong 3 năm tới, bạn muốn mọi người trong ngành nhớ đến thương hiệu của bạn như thế nào?"

*(To build your competitive positioning: 1. Name 2–3 main competitors. 2. What do you do that they can't or don't? 3. What's your main product/service and price point? 4. What do customers say when they refer you? 5. How do you want to be known in 3 years?)*

---

Wait for the user's answers before continuing.

## Step 3 — Analyze and build positioning

Based on the input and what's already in brand.md, build the full positioning output.

Think carefully — Vietnamese market positioning has specific dynamics:

**Competitive landscape analysis:**
- Who are the real alternatives a customer considers? (direct competitors, indirect substitutes, doing nothing)
- What is the dominant positioning in this category right now? (who owns "rẻ nhất", who owns "uy tín nhất", who owns "tiện lợi nhất")
- Is there a gap — an angle nobody else is claiming?

**Positioning statement — use this formula:**
> "For [specific audience], [brand name] is the only [category] that [key benefit] — unlike [competitors] who [their weakness]."

Make it tight. Every word must earn its place. Avoid generic phrases like "tốt nhất", "chuyên nghiệp", "chất lượng cao" — these are not positions, they are claims everyone makes.

**Vietnamese positioning angles to consider:**
- **Trust & reputation:** Years in business, certificates, number of customers served — Vietnamese buyers need reassurance
- **Specificity:** "Chuyên cho [specific audience]" beats "phục vụ mọi đối tượng" — specificity signals expertise
- **Convenience vs. quality:** Where does this brand sit — is the value proposition saving time, saving money, or delivering superior outcome?
- **Relationship-based:** Many Vietnamese SMBs win on relationship and community, not product specs
- **Transparency:** Showing process, ingredients, or behind-the-scenes builds trust faster than advertising claims

**Core offer — define it precisely:**
- What exactly is being sold (not a category — the specific thing)
- What does the customer get (outcome, not features)
- Price point and how it's framed (one-time, monthly, per unit)
- What makes the offer feel safe to buy (guarantee, trial, social proof)

**Competitor table — fill in honestly:**
- Their real strengths (don't underestimate competitors)
- Their real weaknesses (the specific gap this brand exploits)
- How this brand is different (one specific, verifiable claim per competitor)

**Competitive angle — one sentence:**
The single most important gap in the market that this brand fills. This becomes the foundation for all marketing messages.

## Step 4 — Write to brand.md

Update `/outputs/profiles-output/brand.md`:
- Write Section 7 (Positioning) — statement, core promise, market category, competitive angle
- Write Section 9 (Core Offer) — precise offer description
- Write Section 10 (Competitors) — filled competitor table
- Update the `Last updated` date
- Never touch any other section

## Step 5 — Confirm

After writing, reply:

---
"✅ **Định vị thương hiệu của [Brand Name] đã được lưu.**

**Tóm tắt:**
- Định vị: [one-sentence positioning statement]
- Cam kết cốt lõi: [core promise]
- Góc cạnh tranh: [the specific gap they own]
- Đối thủ chính: [Competitor 1] / [Competitor 2] / [Competitor 3]

**Câu định vị đầy đủ:**
"[Full positioning statement in Vietnamese]"

📁 Đã lưu vào: `/outputs/profiles-output/brand.md` — Mục 7 + Mục 9 + Mục 10

**Bước tiếp theo:** Chạy `/USP-definition` để xây dựng điểm bán hàng độc nhất và thông điệp chủ lực."

---
