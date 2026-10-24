# Branded Deck Skill

Your job is to write the complete content for a branded presentation deck — slide by slide, with headline, body copy, speaker notes, and visual direction for each slide. The output is a production-ready content document a designer can build from directly in Canva, Figma, or PowerPoint.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — slide copy must match brand tone
- Core offer (Section 9) — the deck should build toward this
- USP (Section 8) — the central argument the deck makes
- Key messages (Section 11) — weave throughout
- Competitors (Section 10) — positioning context for differentiation slides

If `/outputs/strategy/campaign-brief-*.md` exists: read it — deck may be part of a campaign or pitch.
If `/outputs/assets/sales/` exists: check for existing sales materials to align with.

If brand.md doesn't exist: ask user for brand name, offer, audience, and deck purpose before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified deck type and audience**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết branded deck, mình cần biết:
1. **Loại deck:** Sales pitch / Investor deck / Client onboarding / Webinar / Product explainer?
2. **Audience:** Khách hàng tiềm năng / Investor / Partner / Internal team?
3. **Độ dài:** Ngắn (8–12 slides) / Trung bình (15–20 slides) / Dài (25+ slides)?
4. **Mục tiêu cuối:** Book meeting / Close deal / Educate / Onboard?
5. **Có số liệu thật không:** Results, case studies, pricing để đưa vào không?"

Wait for answer before continuing.

## Step 3 — Write the deck

### Deck types and their structure

**Sales pitch deck (10–15 slides)**
Goal: Get a meeting or close a deal.
Structure:
1. Cover — company name + one-line value proposition
2. The Problem — pain the audience lives with right now
3. Why this problem is worse than they think — agitate
4. The Solution — your offer in one clear statement
5. How it works — 3-step process (not feature list)
6. Proof — case study or results (specific numbers)
7. What they get — deliverables, timeline, what's included
8. Pricing — or "starting from" if tiered
9. Why us — differentiators vs alternatives
10. Next step — one clear action

**Client onboarding deck (8–12 slides)**
Goal: Set expectations, build confidence, start the relationship right.
Structure:
1. Welcome + relationship overview
2. What we're building together — project summary
3. Timeline and milestones
4. What we need from you — inputs, approvals, communication
5. How we work — process, tools, meeting cadence
6. What success looks like — KPIs and definitions
7. Your team contact — who does what
8. First 30 days — specific next actions

**Webinar / educational deck (20–30 slides)**
Goal: Deliver value, build authority, generate leads at the end.
Structure:
1. Cover + hook (why this matters now)
2. About the presenter (brief — 1 slide)
3. Agenda (what they'll learn)
4–N: Content sections (one point per slide)
N+1: Summary — key takeaways
N+2: The offer or next step
N+3: Q&A / Thank you

### Slide writing rules

**One idea per slide:** If you need two sentences to explain a slide, it's two slides.

**Headline is the point:** Every slide headline should be a complete thought, not a topic label.
- Bad: "Our Process"
- Good: "Setup takes 9 days — then you run it yourself"

**Body copy on slides:** Maximum 3 bullet points. Maximum 8 words per bullet. If you need more, it goes in speaker notes.

**Data slides:** One number per data slide. Big, bold, centered. Explanation below in smaller text.

**Speaker notes:** Write full sentences in speaker notes — this is what gets said, not read off the slide. The slide shows the point; the notes tell the story behind it.

**Vietnamese deck conventions:**
- Vietnamese B2B audiences expect pricing transparency — include pricing or "starting from" range
- Case studies with Vietnamese companies/names build more trust than international examples
- Keep slide count lean — Vietnamese business meetings are shorter than Western equivalents
- Include Zalo QR code on final slide for immediate contact

### Slide content template

For each slide, provide:
- **Slide number and name**
- **Headline** (the point, max 10 words)
- **Body copy** (max 3 bullets, 8 words each — or 1–2 short sentences)
- **Visual direction** (what image, chart, or graphic should appear)
- **Speaker notes** (full sentences — what to say while this slide is shown)

## Step 4 — Write output

Save to `/outputs/assets/creative/branded-deck-[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Branded Deck — [Deck Name]
> Generated: [date] | Type: [deck type] | Slides: [n] | Audience: [audience]

**Deck goal:** [One sentence]
**Key argument:** [What this deck proves]

---

## Slide 1 — Cover

**Headline:** [Company name + tagline]
**Body:** [Optional: one-line value proposition]
**Visual:** [Logo centered, brand color background, optional: founder photo]
**Speaker notes:** [Opening line — what to say as deck opens]

---

## Slide 2 — [Name]

**Headline:** [Point in max 10 words]
**Body:**
- [Bullet 1 — max 8 words]
- [Bullet 2 — max 8 words]
- [Bullet 3 — max 8 words]

**Visual:** [Description of graphic/image/chart]
**Speaker notes:** [Full sentences — the story behind this slide]

---

[Continue for all slides]

---

## Final Slide — Next Step

**Headline:** [CTA in max 8 words]
**Body:** [Contact info / booking link / Zalo QR]
**Visual:** [Founder photo or brand graphic]
**Speaker notes:** [Closing — what to say, how to handle the handoff]

---

## Design Notes
- Color palette: [primary / secondary / accent]
- Font: [font family recommendation]
- Logo placement: [top-left / centered on cover]
- Slide size: 1920×1080 (16:9)
- File needed: [Canva / PPT / PDF]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Branded deck '[Name]' đã hoàn chỉnh.**

**Stats:**
- Slides: [n]
- Type: [deck type]
- Key argument: [one sentence]
- CTA: [final slide action]

📁 Đã lưu vào: `/outputs/assets/creative/branded-deck-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/creative-brief` để brief the visual design, hoặc chuyển content doc này cho designer để build trong Canva/Figma."

---
