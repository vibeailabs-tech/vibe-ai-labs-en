# Agent 6 — SEO Agent
> Layer: 3 (Execution) | Skills: 6 | APIs: SerpAPI | Output: /outputs/assets/seo/

---

## What This Agent Does

The SEO Agent improves organic search visibility for Vietnamese businesses. It covers the full SEO stack — from finding the right keywords to fixing technical issues to acquiring backlinks — all with Vietnamese market context built in.

It uses **SerpAPI** for live keyword and SERP data. The other 5 skills (on-page, local, schema, technical, link-building) require no external APIs — pure analysis and recommendations.

---

## 6 Skills

### Skill 1 — `/keyword-research`
**What it does:** Pulls real Google SERP data via SerpAPI to find keywords worth ranking for, organized into a 3-tier map.

**3 rounds of SerpAPI calls:**
1. Seed keyword SERPs → top 10 results, PAA questions, related searches
2. Competitor domain scans → what competitors rank for
3. Long-tail variations → 5 most promising extended terms

**Output structure:**
- Tier 1: Pillar keywords (1–3, define the brand's main topic)
- Tier 2: Cluster keywords (5–10, each becomes a piece of content)
- Tier 3: Quick wins (10–20, low competition, fast ranking opportunity)
- Competitor gap table
- Content recommendations (5 next pieces to create)

**Saves to:** `/outputs/assets/seo/keyword-research.md`

---

### Skill 2 — `/on-page-seo`
**What it does:** Audits and rewrites on-page elements for a specific page + target keyword. No API — pure analysis.

**Audits 8 elements:**
- Title tag (length, keyword position, click appeal)
- Meta description (150–160 chars, keyword, CTA)
- H1 (unique, contains keyword, clear)
- H2/H3 structure (LSI terms, PAA questions as headings)
- Content body (keyword density 1–2%, first 100 words, readability)
- Internal links (outbound + inbound suggestions with anchor text)
- Images (alt text, file names)
- URL slug (short, keyword, no diacritics)

**Output:** Optimized versions of every element that scored below standard — 3 title tag variations, revised heading structure, first paragraph rewrite, internal link table.

**Saves to:** `/outputs/assets/seo/on-page-seo-[page-name].md`

---

### Skill 3 — `/local-seo`
**What it does:** Local search strategy for Vietnamese businesses — Google Business Profile, local keywords, Zalo/Facebook presence, citation building, reviews strategy.

**Vietnamese-specific coverage:**
- Google Maps is the primary local discovery channel
- Zalo OA setup (critical for local Vietnamese businesses)
- Facebook Business Page as secondary search surface
- Vietnamese directory list: yp.vn, doanhnghiep.vn + industry-specific
- Address formatting for Vietnamese locations (phường/xã, quận/huyện)
- Holiday hours (Tết, National Day, Labor Day)

**Output:** GBP audit checklist, local keyword map, location page templates, citation priority list, review request templates (Vietnamese), 30-day quick win plan.

**Saves to:** `/outputs/assets/seo/local-seo.md`

---

### Skill 4 — `/schema-markup`
**What it does:** Writes valid JSON-LD structured data for Vietnamese business pages — enabling rich results in Google SERPs.

**Schema types covered:**
- `Organization` / `LocalBusiness` — homepage/about
- `Service` / `Product` / `Offer` — service/product pages
- `Article` / `BlogPosting` — blog posts
- `FAQPage` — FAQ pages (highest CTR impact for Vietnamese sites)
- `BreadcrumbList` — navigation-heavy sites
- `AggregateRating` — review/testimonial pages

**Vietnamese-specific:** priceCurrency: VND, addressCountry: VN, phone format +84, inLanguage: vi

**Output:** Ready-to-paste JSON-LD blocks with implementation instructions and validation checklist.

**Saves to:** `/outputs/assets/seo/schema-markup-[page-name].md`

---

### Skill 5 — `/technical-seo-audit`
**What it does:** Audits site-wide technical health across 6 categories. No API — analysis based on URL inspection or user-provided data.

**6 categories audited:**
1. Crawlability (robots.txt, sitemap, orphan pages, canonical tags)
2. Indexability (duplicate content, URL structure, redirect chains, 404s)
3. Page Speed / Core Web Vitals (LCP, CLS, FID — Vietnamese mobile-first context)
4. Mobile-friendliness (responsive design, tap targets, font size)
5. HTTPS / Security (full site HTTPS, mixed content, SSL)
6. Structured Data (existing schema validation, gaps)

**Vietnamese-specific checks:**
- Vietnamese characters in URLs (should be ASCII-encoded)
- Vietnamese font loading (Noto Serif, Be Vietnam Pro are heavy — LCP risk)
- Facebook Pixel + Zalo SDK performance impact
- Shared hosting TTFB (common issue for Vietnamese SMBs)

**Severity levels:** 🔴 Critical (fix today) → 🟡 High (this week) → 🟢 Medium (this month) → ⚪ Low

**Saves to:** `/outputs/assets/seo/technical-seo-audit.md`

---

### Skill 6 — `/link-building-strategy`
**What it does:** 90-day link acquisition plan with Vietnamese market context and outreach templates.

**4-tier link structure:**
- Tier 1: Foundation links (GBP, Facebook Page, Zalo OA, directories — 2–3 hours, quick wins)
- Tier 2: Authority links (Vietnamese media guest posts, industry associations, partner co-marketing)
- Tier 3: Competitor gap links (where competitors have links you don't + broken link building)
- Tier 4: Earned media (linkable assets, original research, data studies)

**Vietnamese outreach approach:**
- Zalo/Facebook Messenger first, not email
- Build relationship before asking (relationship-based business culture)
- Frame as mutual benefit, not link request

**Includes 2 Vietnamese outreach templates:**
1. Guest post pitch (for Cafebiz, VnBusiness, Marketing AI, Brands Vietnam)
2. Partnership link request (for suppliers, related businesses)

**Saves to:** `/outputs/assets/seo/link-building-strategy.md`

---

## API Requirements

| API | Used In | Required For |
|---|---|---|
| SerpAPI | `/keyword-research` | SERP data, PAA, related searches, competitor gap analysis |

**Credentials needed:** SerpAPI key (set as environment variable `SERP_API_KEY`)

**Skills that need NO API:** on-page-seo, local-seo, schema-markup, technical-seo-audit, link-building-strategy

---

## Isolated Execution

All 6 skills can run without brand.md if the user provides data directly:

> "Run keyword research for 'AI marketing Vietnam' — brand is [Brand Name] ([industry], [location]), competitors are agency X and freelancer Y"

> "Audit on-page SEO for this page: [paste content] — target keyword: 'setup AI marketing agent team Vietnam'"

---

## Workflow Position

```
Research Agent (keyword research) 
    ↓
SEO Agent (keyword-research → on-page-seo → technical-seo-audit)
    ↓
Content Agent (uses keyword targets for blog briefs)
    ↓
Distribution Agent (organic SEO distribution)
```

The SEO Agent's `keyword-research.md` output feeds directly into Content Agent's `/content-brief` and `/blog-writer` skills — the Content Agent reads keyword priorities before writing.

---

## Output Files Summary

| File | Skill | Contents |
|---|---|---|
| `keyword-research.md` | `/keyword-research` | 3-tier keyword map, competitor gaps, content recommendations |
| `on-page-seo-[page].md` | `/on-page-seo` | Optimized title/meta/H1/headings/content, internal link table |
| `local-seo.md` | `/local-seo` | GBP checklist, local keywords, citation list, review templates |
| `schema-markup-[page].md` | `/schema-markup` | JSON-LD blocks, implementation instructions, validation checklist |
| `technical-seo-audit.md` | `/technical-seo-audit` | 6-category audit, severity-prioritized fix list |
| `link-building-strategy.md` | `/link-building-strategy` | 90-day plan, outreach templates, monitoring framework |
