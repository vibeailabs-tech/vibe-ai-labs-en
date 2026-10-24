---
name: keyword-research
description: Finds keywords competitors rank for and discovers untapped opportunities using SerpAPI. Use this skill when the user wants to find what keywords to target, what their competitors rank for, or what Vietnamese customers are searching for. Trigger whenever the user mentions keyword research, SEO keywords, search terms, or what people are searching for.
---

# Keyword Research Skill

Your job is to find real search data — not guesses — about what potential customers are actually typing into Google. Then map those keywords to content opportunities this brand can realistically win.

## Step 1 — Read brand.md

Read `/outputs/profiles-output/brand.md`. Extract:
- Industry and business type
- Location (city/region)
- Target audience
- Competitors from Section 10 (if available)
- Core offer from Section 9

If brand.md doesn't exist: ask the user for their industry and main product/service before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified keywords or topics**
Use their focus. Go to Step 3.

**Path B — No focus provided**
Ask:
"Bạn muốn mình tìm từ khóa theo hướng nào?
1. Từ khóa khách hàng tìm để mua (buyer intent)
2. Từ khóa đối thủ đang dùng (competitor keywords)
3. Từ khóa nội dung và blog (informational)
4. Tất cả (full keyword map)"

Wait for answer before continuing.

## Step 3 — Run keyword research via SerpAPI

Use the `SERPAPI_KEY` environment variable to make requests to SerpAPI.

### Query 1 — Seed keywords (Google Suggest)
```
GET https://serpapi.com/search.json?engine=google_autocomplete&q=[MAIN_KEYWORD]&gl=vn&hl=vi&api_key=$SERPAPI_KEY
```

Replace `[MAIN_KEYWORD]` with the brand's core service in Vietnamese.

### Query 2 — Competitor keyword analysis
```
GET https://serpapi.com/search.json?engine=google&q=[COMPETITOR_NAME]+[INDUSTRY]&gl=vn&hl=vi&num=10&api_key=$SERPAPI_KEY
```

Run for each competitor found in brand.md Section 10.

### Query 3 — "People also ask" mining
```
GET https://serpapi.com/search.json?engine=google&q=[MAIN_KEYWORD]+Vietnam&gl=vn&hl=vi&api_key=$SERPAPI_KEY
```

Extract the `related_questions` and `related_searches` fields from the response — these are gold for content ideas.

### Query 4 — Local intent keywords
```
GET https://serpapi.com/search.json?engine=google&q=[SERVICE]+[CITY]&gl=vn&hl=vi&api_key=$SERPAPI_KEY
```

Use the brand's city from brand.md (e.g., "dịch vụ marketing TPHCM", "agency marketing Hà Nội").

## Step 4 — Categorize and prioritize keywords

From API responses, build keyword clusters:

**Tier 1 — High intent (buy now):**
- Contains: "giá", "mua", "thuê", "dịch vụ", "chi phí", city name
- Example: "thuê agency marketing TPHCM", "giá thiết kế logo"
- Priority: highest — these convert directly

**Tier 2 — Comparison (almost buying):**
- Contains: "tốt nhất", "uy tín", "nên chọn", "so sánh", "review"
- Example: "agency marketing uy tín Hà Nội", "công ty SEO tốt nhất"
- Priority: high — capture decision-stage buyers

**Tier 3 — Problem-aware (education needed):**
- Contains: "cách", "làm sao", "tại sao", "là gì", "hướng dẫn"
- Example: "cách tăng doanh thu online", "marketing hiệu quả là gì"
- Priority: medium — build authority, feed top-of-funnel

**Tier 4 — Awareness (early stage):**
- Broad industry terms, no intent signal
- Priority: low for now — chase these after authority is established

For each keyword, note:
- Estimated difficulty (based on number/quality of results)
- Content type that ranks (blog, service page, YouTube, etc.)
- Whether a competitor ranks for it

## Step 5 — Identify quick wins

Quick wins = keywords where:
- Competitors have thin/weak content
- No dominant result (scattered rankings)
- Long-tail (3+ words) with clear intent
- The brand can answer better with a dedicated page

Flag these as **Priority targets** in the output.

## Step 6 — Write output

Save to `/outputs/research/keyword-research-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Keyword Research — [Brand Name]
> Generated: [date] | Industry: [industry] | Market: Vietnam

## Keyword Map

### Tier 1 — High Intent (Target First)
| Keyword | Est. Difficulty | Content Type | Competitor Ranking |
|---|---|---|---|
| [keyword] | Low/Med/High | Landing page / Blog | [Competitor] |

### Tier 2 — Comparison Keywords
| Keyword | Est. Difficulty | Content Type | Notes |
|---|---|---|---|

### Tier 3 — Educational / Blog Keywords  
| Keyword | Est. Difficulty | Content Type | Notes |
|---|---|---|---|

---

## "People Also Ask" — Content Gold
Questions from Google's PAA boxes:
- [Question 1] → [Content format to answer it]
- [Question 2] → [Content format to answer it]
- [Question 3] → [Content format to answer it]

---

## Quick Win Opportunities
Keywords with weak competition that this brand can target immediately:
1. [keyword] — Why it's a quick win: [reason]
2. [keyword] — Why it's a quick win: [reason]
3. [keyword] — Why it's a quick win: [reason]

---

## Competitor Keyword Gaps
Keywords competitors rank for that this brand doesn't yet cover:
- [Competitor 1] ranks for: [keyword list]
- [Competitor 2] ranks for: [keyword list]
- Gap: [keywords neither is targeting well]

---

## Recommended Content Priorities
Based on this data, the first 5 pieces of content to create:
1. [Content piece] — targets [keyword] — format: [blog/landing page/video]
2. ...
```

## Step 7 — Confirm

After writing, reply:

---
"✅ **Keyword research cho [Brand Name] đã hoàn chỉnh.**

**Highlights:**
- Từ khóa tier 1 tìm được: [count] keywords
- Quick wins hàng đầu: [top 2–3 quick win keywords]
- Questions từ Google PAA: [count] câu hỏi nội dung

📁 Đã lưu vào: `/outputs/research/keyword-research-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/trend-monitoring` để theo dõi xu hướng thị trường mới nhất."

---
