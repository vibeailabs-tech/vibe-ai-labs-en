# On-Page SEO Skill

Your job is to optimize a specific page for a target keyword — titles, meta, headings, internal links, content structure. No APIs needed; pure analysis and rewrite.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand name, language, location (Sections 1–3)
- Core offer and audience (Sections 6 + 9)

Check if `/outputs/assets/seo/keyword-research-*.md` exists. If it does, reference the keyword map for recommended pages and keywords.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided page content + target keyword**
Use what they gave. Go to Step 3.

**Path B — Missing page content or keyword**
Ask:
"Để tối ưu on-page SEO, mình cần:
1. **Nội dung trang:** Paste full content của trang cần tối ưu (hoặc URL nếu mình có thể scrape)
2. **Keyword mục tiêu:** Keyword chính bạn muốn trang này rank cho
3. **Loại trang:** Blog post / Landing page / Homepage / Service page / Product page"

Wait for answer.

## Step 3 — Audit current on-page signals

Check each element:

**Title tag**
- Length: 50–60 characters optimal (not truncated in SERP)
- Primary keyword: ideally in first 3 words
- Brand name: at end, separated by " — " or "|"
- Click appeal: does it make someone want to click?

**Meta description**
- Length: 150–160 characters
- Primary keyword present
- Contains a clear benefit or hook
- Ends with implicit or explicit CTA

**H1**
- Only one H1 per page
- Contains primary keyword
- Different from title tag (but on the same topic)
- Clear, specific, answers "what is this page about?"

**H2s and H3s**
- Are secondary keywords and LSI terms included naturally?
- Does heading structure create a clear content outline?
- Are PAA-style questions addressed as H2s or H3s?

**Content body**
- Keyword density: 1–2% (not stuffed, not absent)
- First 100 words: does primary keyword appear?
- LSI terms: related vocabulary used naturally throughout?
- Content length vs. top-ranking competitors (too short = thin content signal)
- Readability: short paragraphs, bullet points where appropriate for Vietnamese readers

**Internal links**
- Does the page link OUT to relevant deeper content?
- Do other pages link IN to this page with relevant anchor text?
- Is the internal link structure logical for crawlability?

**Images**
- Alt text contains keyword or relevant description?
- File names descriptive (not IMG_001.jpg)?
- Images compressed for page speed?

**URL slug**
- Short, contains keyword, no stop words, no underscores
- Vietnamese-friendly (avoid diacritics in URLs)

## Step 4 — Rewrite and optimize

Produce optimized versions of every element that scored below standard:

**Rewrites to include:**
1. Optimized title tag (3 variations, pick best)
2. Optimized meta description
3. Optimized H1
4. Revised H2 structure (just the headings, not rewriting full content)
5. First paragraph rewrite (keyword in first 100 words)
6. Internal link suggestions (2–3 specific pages to link to/from with anchor text)
7. Image alt text suggestions

**What NOT to do:**
- Don't change the core message or brand voice
- Don't stuff keywords — if it reads awkward, it's wrong
- Don't recommend things that require technical access (canonical tags, structured data — those go to technical-seo-audit)

## Step 5 — Write output

Save to `/outputs/assets/seo/on-page-seo-[page-name]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# On-Page SEO Audit — [Page Name]
> Generated: [date] | Target keyword: [keyword] | Page type: [type]

## Audit Score

| Element | Current State | Score | Action Required |
|---|---|---|---|
| Title tag | | /10 | |
| Meta description | | /10 | |
| H1 | | /10 | |
| Heading structure | | /10 | |
| Keyword in first 100 words | | /10 | |
| Internal links | | /10 | |
| **Overall** | | **/10** | |

---

## Optimized Elements

### Title Tag
**Current:** [current title]
**Option 1:** [optimized — recommended]
**Option 2:** [alternative]
**Option 3:** [alternative]

### Meta Description
**Current:** [current]
**Optimized:** [new — 150–160 chars]

### H1
**Current:** [current]
**Optimized:** [new]

### Heading Structure
**Current structure:**
- H1: ...
- H2: ...

**Recommended structure:**
- H1: ...
- H2: [includes target keyword or LSI]
  - H3: [PAA question if applicable]
- H2: ...

### First Paragraph
**Current:**
[first 100 words]

**Optimized:**
[rewritten with keyword in first sentence]

---

## Internal Link Opportunities

| Link FROM | Link TO | Anchor Text |
|---|---|---|
| | | |

---

## Image Alt Text
| Image | Recommended Alt Text |
|---|---|
| | |

---

## Quick Wins (implement today)
1. 
2. 
3. 

## Medium Term (implement this week)
1. 
2. 
```

## Step 6 — Confirm

After writing:

---
"✅ **On-page SEO audit cho [page name] hoàn chỉnh.**

**Overall score:** [n]/10
**Biggest issues:** [top 2 problems]
**Quick wins:** [2 things to fix today]

📁 Đã lưu: `/outputs/assets/seo/on-page-seo-[page-name]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/technical-seo-audit` để kiểm tra site-wide issues, hoặc `/blog-writer` để tạo thêm content nhắm vào keyword clusters đã identify."

---
