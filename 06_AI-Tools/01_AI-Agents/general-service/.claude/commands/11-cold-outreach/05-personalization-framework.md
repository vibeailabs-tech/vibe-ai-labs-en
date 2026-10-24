# Personalization Framework Skill

Your job is to build a repeatable system for personalizing cold outreach at scale — so every prospect gets a message that feels written specifically for them, without writing every message from scratch. Personalization is the single biggest lever in cold outreach response rates.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — the personalization must connect back to this
- Target audience (Section 6) — ICP segments that need different personalization approaches
- Brand voice (Section 5) — personalized messages must still sound like the brand

If `/outputs/assets/outreach/cold-email-*.md` exists: apply the framework to existing email templates.
If `/outputs/research/competitor-analysis-*.md` exists: check for company-specific signals to use.
If brand.md doesn't exist: ask user for offer, ICP, and outreach channel before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided a prospect list or specific prospects**
Build personalization for each prospect. Go to Step 3.

**Path B — User wants a reusable system**
Ask:
"Để build personalization framework, mình cần biết:
1. **ICP segments:** Bạn target mấy loại prospect khác nhau? (VD: Marketing Manager tại SaaS / Founder tại F&B / CMO tại retail)
2. **Volume:** Bạn outreach bao nhiêu prospects/tuần?
3. **Research time per prospect:** Bạn sẵn sàng dành bao lâu để research mỗi người? (2 phút / 5 phút / 10 phút)
4. **Data sources:** Bạn dùng LinkedIn, website, Facebook, hay nguồn nào khác?"

Wait for answer before continuing.

## Step 3 — Build the personalization framework

### Why personalization works (and why most people do it wrong)

**Bad personalization:** "Chào [Tên], mình thấy bạn là [Job Title] tại [Company]." This is mail merge, not personalization. Everyone knows you found this on LinkedIn.

**Good personalization:** References something specific they did, said, or created — something that shows you actually paid attention. "Mình đọc bài bạn đăng hôm thứ Ba về [specific topic] — đặc biệt phần về [specific point]. Điều đó khiến mình nghĩ đến..."

**The 1-3-1 rule:** 1 minute of research, 3 personalization signals found, 1 used per message. Don't use all 3 — it feels like surveillance.

### Personalization signal categories

**Tier 1 — High signal (use these first)**
These show genuine attention and generate the highest reply rates:
- Recent LinkedIn post or article they wrote
- Comment they left on someone else's post
- Company news: funding, new hire, product launch, expansion
- Job change: new role in last 90 days
- Content they shared with a specific opinion attached
- Award or recognition they or their company received

**Tier 2 — Medium signal**
Relevant but less specific:
- Industry they're in + current market trend affecting them
- Company size + typical challenges at that scale
- Tech stack they use (visible from job listings or website)
- Competitor they work with or mention publicly

**Tier 3 — Low signal (last resort)**
Generic but better than nothing:
- Their job title + common pain for that role
- Location + local market context
- Company founding year (speaks to their stage)

### Research process (5 minutes per prospect)

**Step 1 (1 min): LinkedIn profile scan**
- Recent posts (last 30 days) — look for opinions, not just shares
- "About" section — often reveals priorities and personality
- Recent job change flag

**Step 2 (1 min): Company LinkedIn page**
- Recent company updates
- Hiring patterns (tells you where they're investing)
- Recent announcements

**Step 3 (1 min): Their website**
- Homepage messaging (what problem they say they solve)
- Blog or news section (recent updates)
- Team page (size, growth signals)

**Step 4 (1 min): Google search: "[Name] [Company]"**
- Interviews, podcast appearances, articles written
- Awards or press mentions

**Step 5 (1 min): Write the personalization line**
One sentence. Specific. Genuine. Connects to your offer without forcing it.

### Personalization line formulas

**Formula 1 — Observation + Connection:**
"Mình đọc [specific thing they did/said] — [genuine observation]. Điều đó khiến mình nghĩ đến [connection to your offer]."

**Formula 2 — Shared context:**
"Mình thấy [Company] vừa [news/event] — [relevant observation]. Mình đang work với một vài công ty ở giai đoạn tương tự về [your offer area]."

**Formula 3 — Direct compliment + curiosity:**
"[Specific thing they made/said] là [genuine compliment — one word]. Tò mò về [specific aspect] — [connection to why you're reaching out]."

### Segment-specific personalization templates

Build a template bank per ICP segment. Each template has:
- **Research prompt:** What to look for (30 seconds of scanning)
- **Personalization slot:** The [PERSONALIZE HERE] placeholder in the template
- **Connection bridge:** How the personalization connects to the offer

**Example for Vietnamese SMB founder:**
- Research: Look for recent Facebook or LinkedIn post about marketing challenges
- Slot: "Mình vừa đọc bài bạn về [topic from post]"
- Bridge: "— điều đó relevant vì hầu hết founder mình nói chuyện đang gặp cùng vấn đề với [specific pain]"

**Example for Marketing Manager at mid-size company:**
- Research: Look for recent campaign they ran or tool they mentioned
- Slot: "Mình thấy [Company] vừa chạy [campaign type]"
- Bridge: "— curious bạn đang dùng gì để handle [content/automation/reporting] side của nó"

### Scaling personalization with templates

The framework outputs:
1. **Research checklist** per prospect type (what to look for, where, how long)
2. **Template bank** per ICP segment (3 templates per segment, each with personalization slot)
3. **Personalization line examples** (10 real examples they can pattern-match from)
4. **Quick-apply format** for high-volume outreach (for when you need to send 20+ per day)

## Step 4 — Write output

Save to `/outputs/assets/outreach/personalization-framework-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Personalization Framework — [Brand Name]
> Generated: [date] | ICP segments: [n] | Volume: [prospects/week]

---

## Research Process (5 min per prospect)

| Step | Source | What to look for | Time |
|---|---|---|---|
| 1 | LinkedIn profile | Recent posts, opinions, job change | 1 min |
| 2 | Company LinkedIn | News, hiring, announcements | 1 min |
| 3 | Website | Homepage messaging, blog, team size | 1 min |
| 4 | Google | Interviews, press, awards | 1 min |
| 5 | Write the line | One specific, genuine sentence | 1 min |

---

## Signal Tiers

### Tier 1 — Use these (highest reply rate)
[List of high-signal personalization types for this brand's ICP]

### Tier 2 — Use if Tier 1 not available
[List]

### Tier 3 — Last resort
[List]

---

## Segment Templates

### Segment 1: [ICP Segment Name]

**Research prompt:** [What to look for in 30 seconds]

**Template A:**
Subject: [subject with personalization slot]
Opening: "[PERSONALIZE: specific observation] — [bridge to offer]"
[Rest of template]

**Template B:**
[Alternative angle]

**Template C:**
[Third option]

---

### Segment 2: [ICP Segment Name]
[Repeat]

---

## Personalization Line Examples (10 real examples)

1. "[Example — specific, genuine, connects to offer]"
2. "[Example]"
[...]

---

## High-Volume Quick-Apply Format

When sending 20+ emails/day, use this 2-minute research process:
1. [Fastest research step]
2. [What to prioritize]
3. [Minimum viable personalization]

---

## Quality Check

Before sending any personalized outreach, verify:
- [ ] The personalization is specific (not generic)
- [ ] It references something they actually did/said (not just their job title)
- [ ] The connection to the offer feels natural, not forced
- [ ] It doesn't feel like surveillance (one signal used, not all three)
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Personalization framework cho [Brand Name] đã hoàn chỉnh.**

**Segments covered:** [n] ICP segments
**Templates per segment:** 3
**Research process:** 5 min/prospect standard, 2 min high-volume

📁 Đã lưu vào: `/outputs/assets/outreach/personalization-framework-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Apply framework to `/cold-email` or `/linkedin-dm` templates, hoặc build Agent 12 Sales Enablement để prepare for when prospects respond."

---
