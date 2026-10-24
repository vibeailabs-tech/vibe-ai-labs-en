# Keyword Research Skill

Your job is to find keywords the brand should rank for — including gaps competitors own that this brand doesn't. Uses SerpAPI to pull real SERP data.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Industry, location, language (Sections 1–3)
- Core offer and target audience (Sections 6 + 9)
- Competitors (Section 10)

If brand.md doesn't exist: ask user to provide brand name, industry, location, and 3 competitor URLs manually.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided seed keywords or a topic**
Use those as starting seeds. Go to Step 3.

**Path B — No seeds provided**
Ask:
"Để research keyword, mình cần biết:
1. **Chủ đề chính:** Bạn muốn rank cho chủ đề gì? (VD: 'AI marketing', 'phần mềm kế toán', 'spa tại TPHCM')
2. **Mục tiêu:** Bạn muốn keyword cho trang nào? (homepage / blog / landing page cụ thể)
3. **Ưu tiên:** Volume cao, competition thấp, hay intent mua hàng?"

Wait for answer.

## Step 3 — Run keyword research

### SerpAPI calls to make (3 rounds):

**Round 1 — Seed keyword SERPs**
For each seed keyword, call SerpAPI Google Search:
- `q`: seed keyword (+ "Vietnam" or location if local)
- `gl`: vn, `hl`: vi (or en depending on brand language)
- `num`: 10

Extract from each SERP:
- Top 10 organic results (title, URL, snippet)
- People Also Ask questions
- Related searches at bottom of SERP

**Round 2 — Competitor keyword gaps**
For each competitor domain from brand.md, call SerpAPI:
- Search `site:[competitor-domain] [seed topic]` to see what they rank for
- Note recurring themes and angles they cover

**Round 3 — Long-tail variations**
Based on PAA and related searches from Round 1, pick the 5 most promising long-tail terms and run SerpAPI searches on those too.

### Analyze results:

**Keyword scoring criteria:**
1. **Search intent alignment** — does searcher intent match the brand's offer?
   - Informational: research phase (blog content)
   - Commercial: comparing options (comparison pages, case studies)
   - Transactional: ready to buy (landing pages, service pages)
2. **Competitor difficulty** — how strong are current top 10 results?
   - Check: are top results big brand domains (hard) or thin content (opportunity)?
3. **Topic cluster fit** — does this keyword belong in a logical cluster around a pillar topic?
4. **Vietnamese market specificity** — is there a Vietnamese-specific angle that global content misses?

**Classify each keyword:**
- Quick win: lower competition, clear intent, brand can rank in 60–90 days
- Strategic: higher volume, worth pursuing with strong content over 6+ months
- Skip: dominated by huge brands or irrelevant intent

## Step 4 — Build keyword map

Organize into 3 tiers:

**Tier 1 — Pillar keywords (1–3 keywords)**
High-volume, defines the brand's main topic. Hard to rank immediately but anchor the whole strategy.

**Tier 2 — Cluster keywords (5–10 keywords)**
Medium difficulty, support the pillar. Each one becomes a piece of content.

**Tier 3 — Quick wins (10–20 keywords)**
Low competition, clear intent. Start ranking here to build authority for Tier 1.

## Step 5 — Write output

Save to `/outputs/assets/seo/keyword-research-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Keyword Research — [Brand Name]
> Generated: [date] | Tools: SerpAPI | Location: [location]

## Executive Summary
- Pillar keyword: [main keyword]
- Total keywords mapped: [n]
- Quick wins identified: [n]
- Biggest competitor gap: [what they rank for that you don't]

---

## Tier 1 — Pillar Keywords

| Keyword | Est. Monthly Searches | Intent | Difficulty | Notes |
|---|---|---|---|---|
| | | | | |

---

## Tier 2 — Cluster Keywords

| Keyword | Intent | Content Type | Priority |
|---|---|---|---|
| | | | |

---

## Tier 3 — Quick Wins

| Keyword | Why It's a Quick Win | Recommended Page |
|---|---|---|
| | | |

---

## People Also Ask (High Value)
Questions from SERPs that represent content opportunities:
1. 
2. 
3. 

---

## Competitor Keyword Gaps
Keywords competitors rank for that [Brand] currently doesn't:

| Keyword | Competitor That Ranks | Opportunity |
|---|---|---|
| | | |

---

## Content Recommendations
Based on keyword clusters, these are the next 5 content pieces to create:
1. [Title] — targets [keyword] — [intent] — [page type]
2. 
3. 
4. 
5. 
```

## Step 6 — Confirm

After writing:

---
"✅ **Keyword research cho [Brand Name] hoàn chỉnh.**

**Highlights:**
- [n] pillar keywords, [n] cluster keywords, [n] quick wins
- Top quick win: '[keyword]' — [why]
- Biggest gap vs competitors: '[keyword]'

📁 Đã lưu: `/outputs/assets/seo/keyword-research-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/on-page-seo` để tối ưu trang hiện có cho các keywords này, hoặc `/content-brief` để brief bài viết nhắm vào quick wins."

---
