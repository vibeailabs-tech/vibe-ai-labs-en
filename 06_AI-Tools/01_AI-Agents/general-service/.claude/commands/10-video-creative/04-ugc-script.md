# UGC Script Skill

Your job is to write User Generated Content (UGC) scripts — scripts designed to be performed by customers, creators, or brand advocates, not the founder or brand itself. UGC looks and sounds like organic content, not advertising. It's the most trusted ad format in 2026 because it feels real.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — what the UGC creator is endorsing
- Target audience (Section 6) — the UGC creator should look and sound like this audience
- USP (Section 8) — the specific claim the creator makes
- Key messages (Section 11) — the message to get across naturally

If `/outputs/assets/ads/ad-copy-*.md` exists: check what angles are being tested — UGC should complement, not duplicate.
If `/outputs/assets/email/email-sequence-*.md` exists: check if social proof from email sequences can become UGC talking points.

If brand.md doesn't exist: ask user for offer, target customer profile, and key benefit before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified creator type or UGC angle**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết UGC script, mình cần biết:
1. **Creator type:** Khách hàng thật / Micro-creator / Nhân viên / Brand ambassador?
2. **Platform:** TikTok / Instagram Reels / Facebook?
3. **Angle:** Testimonial (kết quả) / Day-in-life / Before/after / Tutorial / Reaction?
4. **Độ dài:** 15–30 giây / 30–60 giây?
5. **Paid hay organic:** Paid UGC ad hay organic post?"

Wait for answer before continuing.

## Step 3 — Write the UGC scripts

### What makes UGC work

**It must not look like an ad.** The moment a viewer identifies content as advertising, their guard goes up. UGC works because it looks like a friend talking to a friend — personal, unpolished, specific.

**The creator is the proof.** UGC is not about the product — it's about the person who used it. The script must be written from the creator's perspective, in their voice, about their experience.

**Specificity is everything.** "Mình tiết kiệm được nhiều thời gian" is forgettable. "Mình từng tốn 3 tiếng mỗi ngày viết content — giờ mất 45 phút một tuần" is credible and memorable.

### UGC formats for Vietnamese market

**Testimonial / Result UGC (most common for B2B)**
Creator shares a specific result they got. Structure:
- Hook: State the result upfront — "Mình vừa giảm chi phí marketing từ $500 xuống $80 mỗi tháng."
- Context: Who they are and what problem they had before
- The experience: What using the product/service was like (not a feature list — how it felt)
- The result: Specific, measurable, honest
- Recommendation: Natural, not forced — "Nếu bạn đang trong tình huống giống mình..."

**Day-in-life UGC**
Creator shows how the product fits into their actual workflow. Structure:
- Hook: "Đây là cách mình làm marketing cho công ty mỗi sáng thứ Hai..."
- Show the routine — with the product as a natural part of it
- One specific thing they do that others don't
- Soft CTA: "Cái này mình học được từ [brand]..."

**Before/After UGC**
Contrast is the most powerful storytelling device. Structure:
- Before: Paint the old situation in 2–3 sentences (painful, relatable)
- The turn: "Sau đó mình thử..."
- After: The new situation (specific numbers, specific feelings)
- CTA: "Link bio nếu bạn muốn biết mình dùng gì"

**Reaction / Unboxing UGC**
Creator reacts in real time. Structure:
- First impression hook
- Walk through what they're seeing/experiencing
- Genuine reaction — surprise, delight, confusion that resolves
- End state: Would they recommend it?

### Script format for UGC

UGC scripts are written in first-person, conversational tone — as if the creator is writing their own script. Mark the creator's natural pauses and emphasis.

```
[CREATOR TYPE: e.g., Vietnamese SMB owner, female, 30s, TP.HCM]
[LENGTH: X seconds]
[PLATFORM: TikTok]
[ANGLE: Testimonial]

---

[0:00–0:03] HOOK
VISUAL: Creator on camera, casual setting (home office or café)
SPOKEN: "[Hook line — result or bold claim]"

[0:03–0:35] STORY
VISUAL: [B-roll of their workspace / screen / product if relevant]
SPOKEN: "[Story — context, before, experience, after]"
NOTE: [Should feel unscripted — creator can add their own filler words]

[0:35–0:45] SOFT CTA
VISUAL: Creator back on camera
SPOKEN: "[Natural recommendation — not salesy]"
```

### Vietnamese UGC specifics

**Authenticity signals for Vietnamese audience:**
- Background: Real home, café, or office — not studio
- Lighting: Natural light preferred — ring light is OK but not professional lighting setup
- Audio: Natural ambient sound OK — Vietnamese audiences are used to it
- Outfit: Everyday clothes — no corporate attire for casual UGC
- Dialect: Saigon accent for TPHCM audience, Hanoi for northern targeting

**What kills UGC credibility:**
- Reading off a teleprompter (eyes dart side-to-side)
- Perfect hair and makeup for a "casual" video
- Too many cuts in 30 seconds — feels edited, not authentic
- Corporate phrases: "sản phẩm chất lượng cao", "dịch vụ chuyên nghiệp"
- Mentioning the brand name too many times (feels paid)

**Disclosure:** Paid UGC must be disclosed (#quảngcáo or #ad). Script should still feel natural — disclosure at end of caption, not awkwardly inserted into the video itself.

### Writing 3 script variations

Always write 3 variations per UGC format:
- **Version A:** Emotional angle — focuses on how it felt, the relief, the transformation
- **Version B:** Logical angle — focuses on numbers, time saved, money saved
- **Version C:** Social angle — focuses on what others said or noticed

Test all 3 — different creators will naturally gravitate toward different angles.

## Step 4 — Write output

Save to `/outputs/assets/creative/ugc-script-[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# UGC Script — [Campaign/Product]
> Generated: [date] | Format: [testimonial/day-in-life/before-after] | Platform: [platform] | Length: [X sec]

---

## Creator Profile
[Who should perform this script — age, gender, role, location, vibe]

---

## Version A — Emotional angle

[CREATOR TYPE: ...]
[LENGTH: X seconds]

[0:00–0:03] HOOK
VISUAL: [setting]
SPOKEN: "[words]"

[0:03–X:XX] STORY
VISUAL: [b-roll or on-camera]
SPOKEN: "[words]"
NOTE: [authenticity note]

[X:XX–end] CTA
VISUAL: [back on camera]
SPOKEN: "[words]"

**Caption:** [TikTok/Instagram caption for this video]
**Hashtags:** [5–8 hashtags]

---

## Version B — Logical angle
[Repeat structure]

---

## Version C — Social angle
[Repeat structure]

---

## Casting Notes
- Creator must: [specific requirements]
- Avoid casting: [who won't work]
- Compensation: [gift / payment / affiliate — brand to decide]
- Usage rights: [organic only / paid ads / both]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **UGC scripts cho '[Campaign]' đã hoàn chỉnh.**

**Scripts written:** 3 versions — Emotional / Logical / Social angle
**Format:** [format]
**Platform:** [platform]
**Creator profile:** [one-line description]

📁 Đã lưu vào: `/outputs/assets/creative/ugc-script-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Tìm creator phù hợp với creator profile, hoặc chạy `/ad-campaign-structure` để plan UGC ads campaign."

---
