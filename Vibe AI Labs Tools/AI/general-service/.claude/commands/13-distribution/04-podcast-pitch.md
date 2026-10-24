# Podcast Pitch Skill

Your job is to write cold pitches to podcast hosts — for the brand founder or expert to appear as a guest. A podcast pitch is a cold email with a specific structure: show you know their audience, offer a specific topic, prove you're worth the host's time, make it easy to say yes.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — pitch tone must match brand personality
- Core offer (Section 9) — the expertise behind the pitch
- USP (Section 8) — what makes this guest perspective unique
- Target audience (Section 6) — to match with podcast audiences

If brand.md doesn't exist: ask user for speaker bio, expertise, and target podcast before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided target podcast(s)**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết podcast pitch, mình cần biết:
1. **Podcast target:** Tên podcast bạn muốn pitch (hoặc loại podcast — AI / marketing / startup / SMB)?
2. **Speaker:** Ai sẽ là guest? (tên, vai trò, expertise)
3. **Topic angle:** Bạn muốn nói về chủ đề gì cụ thể — góc nhìn độc đáo nào?
4. **Proof:** Bạn đã từng được feature ở đâu chưa? Có credentials gì?
5. **CTA:** Bạn muốn họ làm gì — email reply / fill form / Zalo?"

Wait for answer before continuing.

## Step 3 — Write the podcast pitch

### Podcast pitch structure (5 elements)

**1. Subject line (the first filter)**
- Reference the show by name — shows you actually listen
- Hint at the topic value for their audience
- Under 8 words
- Examples:
  - "Guest pitch: AI marketing cho SMB Việt — [Show Name]"
  - "[Show Name] — góc nhìn khác về AI replacement"
  - "Mình nghe tập [X] — đây là angle tiếp theo"

**2. Opening (show you know their show)**
- Reference a specific episode, guest, or topic they covered
- One sentence on why their audience would care about this topic
- Never generic: "Tôi nghe podcast của bạn thường xuyên và rất thích"

**3. The pitch — your topic angle**
- One specific, provocative topic angle (not "AI marketing in Vietnam")
- 3 talking points they'll cover — specific, not vague
- Why this topic is timely right now
- What their audience will walk away knowing

**4. Why you (credibility)**
- One specific result or proof point
- Any prior media appearances (be honest — none is OK)
- One sentence on your unique vantage point

**5. Easy CTA**
- One ask: "Có phù hợp không nếu mình gửi thêm thông tin?"
- Or: "Mình sẵn sàng record bất kỳ lúc nào trong tháng 5 — bạn chọn ngày"
- Never: "Mong nhận được phản hồi sớm từ bạn"

### Topic angle development

The topic must be:
- **Specific:** "Tại sao 86% SMB dùng AI vẫn tốn thời gian hơn trước" not "AI marketing"
- **Timely:** Tie to something happening now — market trend, recent news, new tool launch
- **Counterintuitive:** Challenge a belief the audience currently holds
- **Actionable:** Listeners can do something with it after the episode

**3 proven angle formulas:**
- Contrarian: "Lý do AI tool của bạn không tiết kiệm thời gian (và cách fix)"
- Behind-the-scenes: "Mình setup 50+ AI marketing systems — đây là điều hầu hết bài hướng dẫn không nói"
- Data-driven: "93% dùng AI nhưng chỉ 13.8% thấy kết quả — data từ thị trường Việt Nam"

### Vietnamese podcast landscape

**Key Vietnamese podcasts (as of 2026) to target for AI/business:**
- Business/startup: Startup Vietnam Podcast, The Coffee House Talks, Wisdom Talks
- Marketing: Marketing Arena, Brand Camp
- Tech/AI: Technically Vietnam, The Vietnamese Podcast (English-language, international reach)
- SMB/entrepreneurship: Doanh Nhân Sài Gòn, Shark Tank Vietnam adjacent shows

**Pitch in Vietnamese or English:** Match the podcast's primary language. For bilingual podcasts, pitch in Vietnamese but offer to record in either.

**Response rate tips:**
- LinkedIn DM + email same day = higher response
- Follow their social first, engage once, then pitch — warm it up
- Reference their most recent episode — shows you're current

### Write 3 pitch versions

- **Version A:** Cold pitch to specific show (referencing their content)
- **Version B:** Template for outreach to similar shows (customizable)
- **Version C:** Short version for LinkedIn DM outreach (150 words max)

## Step 4 — Write output

Save to `/outputs/distribution/podcast-pitch-[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Podcast Pitch — [Speaker Name / Topic]
> Generated: [date] | Speaker: [name] | Topic: [angle] | Target: [podcast name/type]

---

## Version A — Specific Show Pitch

**Subject:** [Subject line]

---

[Full pitch — 5 elements]

---

## Version B — Template for Similar Shows

**Subject:** [Customizable subject]

---

[Template with [SHOW NAME], [RECENT EPISODE], [HOST NAME] placeholders]

---

## Version C — LinkedIn DM Version (150 words max)

[Short version for LinkedIn DM]

---

## Target Show List
| Show | Host | Audience | Contact | Fit score |
|---|---|---|---|---|
| [Show] | [Host] | [Description] | [How to reach] | High/Med/Low |

## Follow-up Plan
- Day 0: Send pitch email
- Day 1: LinkedIn DM (Version C)
- Day 7: Follow-up email if no reply (add one new data point)
- Day 14: Final follow-up or move on
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Podcast pitches cho '[Speaker/Topic]' đã hoàn chỉnh.**

**Versions:** Specific / Template / LinkedIn DM
**Topic angle:** '[angle in one sentence]'
**Primary target show:** [show name]

📁 Đã lưu vào: `/outputs/distribution/podcast-pitch-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Send pitches → prep talking points for when they say yes, hoặc chạy `/partnership-brief` để pitch distribution partnerships."

---
