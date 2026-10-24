---
name: competitor-analysis
description: Scrapes and analyzes competitor websites using Firecrawl MCP and Playwright MCP. Use this skill when the user wants to understand what competitors are doing, their messaging, content strategy, offers, and weaknesses. Trigger whenever the user mentions competitor analysis, what competitors are doing, or wants to find gaps in the market.
---

# Competitor Analysis Skill

Your job is to scrape real competitor data — not guesses — and turn it into actionable intelligence about their messaging, offers, content strategy, and weaknesses.

## Step 1 — Read brand.md

Read `/outputs/profiles-output/brand.md`. Extract:
- Industry and business type
- Competitors listed in Section 10
- Positioning and USP

If no competitors are listed in brand.md: ask the user to provide 2–3 competitor URLs or names before continuing.

## Step 2 — Collect competitor URLs

**Path A — Competitors with URLs already in brand.md**
Use those URLs. Go to Step 3.

**Path B — Competitor names but no URLs**
Ask: "Bạn có thể cung cấp URL website của từng đối thủ không? Nếu không có website, mình sẽ dùng tên để tìm kiếm."

**Path C — No competitors identified**
Ask: "Kể tên 2–3 đối thủ chính của bạn (tên thương hiệu hoặc URL website)."

## Step 3 — Scrape competitor websites with Firecrawl

For each competitor, use Firecrawl MCP to scrape their website:

```
Use the firecrawl-mcp tool to scrape [COMPETITOR_URL]
Extract: homepage content, about page, services/products page, pricing page (if exists)
Focus on: headlines, value propositions, CTAs, key messages, offers
```

For each competitor, extract:
- **Hero headline** — what's the first thing they say?
- **Value proposition** — what do they promise?
- **Target audience** — who are they talking to?
- **Key offers** — what are they selling and at what price?
- **CTAs** — what action do they want visitors to take?
- **Content themes** — what topics do they talk about?
- **Tone** — formal/casual, Vietnamese/English?

## Step 4 — Screenshot with Playwright

Use Playwright MCP to take screenshots of each competitor's homepage:

```
Use playwright to navigate to [COMPETITOR_URL] and take a screenshot
```

This captures visual positioning — design quality, color palette, imagery style, above-the-fold layout.

Note for each competitor:
- Design quality (premium / mid-range / basic)
- Visual identity (modern / traditional / minimal / busy)
- Trust signals visible (reviews, numbers, certifications, logos)

## Step 5 — Analyze gaps

After scraping all competitors, synthesize:

**What everyone claims** — the overcrowded positioning angles (avoid or counter these)

**What nobody is saying** — gaps in messaging that this brand can own

**Weaknesses to exploit:**
- Competitor X is strong on [X] but weak on [Y]
- Nobody is talking about [specific pain point]
- All competitors target [segment] but ignore [underserved segment]

**Content gaps:**
- Topics competitors aren't covering
- Questions their audiences are asking that no one is answering

## Step 6 — Write output

Save to `/outputs/research/competitor-analysis-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Competitor Analysis — [Brand Name]
> Generated: [date]

## Competitor Profiles

### [Competitor 1 Name]
- URL: 
- Hero message: 
- Value proposition: 
- Target audience: 
- Key offer + price: 
- CTA: 
- Tone: 
- Design quality: 
- Trust signals: 
- Strengths: 
- Weaknesses: 

### [Competitor 2 Name]
[same structure]

### [Competitor 3 Name]
[same structure]

---

## Gap Analysis

### Overcrowded angles (avoid)
- 

### Unclaimed positioning opportunities
- 

### Content gaps (topics competitors ignore)
- 

### Underserved audience segments
- 

---

## Strategic Recommendations
[3–5 specific actions this brand should take based on competitor weaknesses]
```

## Step 7 — Confirm

After writing, reply:

---
"✅ **Phân tích đối thủ cho [Brand Name] đã hoàn chỉnh.**

**Highlights:**
- Đã phân tích: [Competitor 1] / [Competitor 2] / [Competitor 3]
- Góc định vị bị bỏ ngỏ: [biggest gap]
- Điểm yếu lớn nhất của đối thủ: [key weakness to exploit]

📁 Đã lưu vào: `/outputs/research/competitor-analysis-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/keyword-research` để tìm từ khóa đối thủ đang dùng."

---
