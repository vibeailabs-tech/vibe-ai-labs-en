---
name: lead-magnet
description: Creates 3 lead magnet concepts tailored to the brand's audience and offer. Use this skill when the user wants to grow their email list, capture leads, or create a free offer to attract potential customers. Trigger whenever the user mentions lead magnet, free offer, freebie, email capture, or list building.
---

# Lead Magnet Skill

Your job is to design 3 lead magnet concepts that attract the exact right buyers — not tire-kickers — and move them toward the core offer. In Vietnam, the best lead magnets solve a specific, immediate problem and can be consumed quickly.

## Step 1 — Read inputs

Read:
- `/outputs/profiles-output/brand.md` — ICP pain points (Section 6), core offer (Section 9), USP (Section 8), content pillars (Section 12)
- `/outputs/research/keyword-research-*.md` — "People Also Ask" questions (if exists)
- `/outputs/research/competitor-analysis-*.md` — what competitors are giving away (if exists)

If brand.md doesn't exist: stop and ask user to run `/brand-setup` first.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified a type or topic**
Use their direction. Go to Step 3.

**Path B — No direction provided**
Ask:
"Bạn muốn lead magnet phục vụ mục đích gì?
1. Thu thập email/số điện thoại từ người lạ
2. Warm up khách hàng đang cân nhắc
3. Kích hoạt lại khách hàng cũ
4. Tất cả — đề xuất 3 loại khác nhau"

Wait for answer before continuing.

## Step 3 — Design 3 lead magnet concepts

### Lead magnet principles for Vietnam market

**What works:**
- Solves ONE specific, named pain point (not "improve your marketing")
- Immediately actionable — consumer can use it today
- Quick to consume — checklist, template, calculator, short guide (not 50-page ebook)
- Creates "aha" moment that makes the paid offer feel obvious
- Vietnamese language, with specific numbers and examples
- Delivery via Zalo or email (not gated PDF nobody downloads)

**What doesn't work:**
- Generic "ultimate guide to X" — too broad, no urgency
- Anything requiring too much setup before seeing value
- Content that competes with what they can Google in 30 seconds
- Ebooks longer than 10 pages

### Lead magnet formats ranked by conversion rate (Vietnam context):
1. **Calculator / quiz** — interactive, personalized result ("Chi phí thật của bạn là...")
2. **Checklist** — quick scan, immediate value ("10 điều cần check trước khi...")
3. **Template** — copy-paste ready ("Template [X] cho doanh nghiệp Việt Nam")
4. **Mini video / screen-record** — show don't tell (demo, walkthrough, behind-the-scenes)
5. **Cheat sheet** — condensed reference ("Tất cả bạn cần biết về X trong 1 trang")
6. **Free consultation / audit** — highest intent, lowest volume (for high-ticket offers)
7. **Case study / result breakdown** — proof + education combined

### For each of the 3 concepts, define:

**Concept structure:**
- **Name** — specific, benefit-driven title (not "Free Guide")
- **Format** — checklist / calculator / template / video / consultation
- **Specific problem it solves** — one sentence, exact language the ICP uses
- **What's inside** — 3–5 bullet points of what they get
- **The "aha" moment** — what insight makes them think "I need the paid offer"
- **Delivery method** — Zalo / email / direct download / Facebook Messenger
- **CTA to paid offer** — how it naturally leads to the next step
- **Estimated conversion** — how qualified are the leads this attracts?

### Lead magnet ladder:
Design the 3 concepts at different funnel stages:
- **Concept 1 — Top of funnel** (broad audience, low commitment, high volume)
- **Concept 2 — Middle of funnel** (problem-aware, moderate commitment, qualified)
- **Concept 3 — Bottom of funnel** (solution-aware, high commitment, highest intent)

## Step 4 — Write output

Save to `/outputs/strategy/lead-magnets-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Lead Magnet Concepts — [Brand Name]
> Generated: [date]

## Concept 1 — [Name] (Top of Funnel)
**Format:** 
**Problem solved:** 
**What's inside:**
- 
- 
- 
**The "aha" moment:** 
**Delivery:** 
**CTA to paid offer:** 
**Estimated lead quality:** Low-medium (volume play)

---

## Concept 2 — [Name] (Middle of Funnel)
**Format:** 
**Problem solved:** 
**What's inside:**
- 
- 
- 
**The "aha" moment:** 
**Delivery:** 
**CTA to paid offer:** 
**Estimated lead quality:** Medium-high (intent qualified)

---

## Concept 3 — [Name] (Bottom of Funnel)
**Format:** 
**Problem solved:** 
**What's inside:**
- 
- 
- 
**The "aha" moment:** 
**Delivery:** 
**CTA to paid offer:** 
**Estimated lead quality:** High (ready to buy)

---

## Recommended First Build
[Which of the 3 to build first and why — based on current stage, audience size, and fastest path to revenue]

## Promotion Plan
[How to get the lead magnet in front of the right people — organic posts, paid ads, Zalo broadcast, etc.]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **3 lead magnet concepts cho [Brand Name] đã hoàn chỉnh.**

**Đề xuất build trước:**
- [Concept name] — [format] — [why this one first]

**Tóm tắt 3 concepts:**
1. [Name] — [one line description]
2. [Name] — [one line description]
3. [Name] — [one line description]

📁 Đã lưu vào: `/outputs/strategy/lead-magnets-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/campaign-brief` để đóng gói toàn bộ strategy thành brief cho execution agents."

---
