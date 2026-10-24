# Technical SEO Audit Skill

Your job is to audit a website's technical SEO health — crawlability, indexability, speed signals, Core Web Vitals readiness, and structural issues that block ranking. No APIs required; analysis based on user-provided data or URL inspection.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand name, website URL (Sections 1 + 4)
- Language (Section 4)

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided website URL or pasted HTML/sitemap**
Use what they gave. Go to Step 3.

**Path B — No website info**
Ask:
"Để audit technical SEO, mình cần:
1. **Website URL:** URL trang chủ
2. **Quyền truy cập:** Bạn có access vào Google Search Console không? (yes/no)
3. **Platform:** WordPress / Webflow / custom code / landing page builder (Lp-builder, ClickFunnels...)
4. **Vấn đề đã biết:** Có issue gì bạn đã nhận thấy? (slow loading, indexing errors...)"

Wait for answer.

## Step 3 — Audit framework

Run through each category systematically:

### Category 1 — Crawlability (can Google find all pages?)
- **robots.txt**: Is it accessible at `/robots.txt`? Any `Disallow` rules blocking important pages?
- **XML sitemap**: Exists at `/sitemap.xml`? Submitted to Google Search Console? Contains all important URLs?
- **Internal linking**: Are all important pages reachable within 3 clicks from homepage?
- **Orphan pages**: Any pages with no internal links pointing to them?
- **Canonical tags**: Are they set correctly? Any self-referencing canonicals that might confuse Google?
- **noindex tags**: Any important pages accidentally set to noindex?

### Category 2 — Indexability (is Google indexing the right pages?)
- **Duplicate content**: URL variations creating duplicates? (www vs non-www, http vs https, trailing slash)
- **Pagination**: Are paginated pages handled correctly (rel=next/prev or canonical)?
- **URL structure**: Clean, descriptive, no session IDs or excessive parameters
- **Redirect chains**: Any 301 chains longer than 1 hop?
- **Broken links (404s)**: Internal links pointing to removed pages?

### Category 3 — Page Speed (Core Web Vitals)
Vietnamese mobile users are the primary audience — mobile speed is critical.
- **LCP (Largest Contentful Paint)**: Target < 2.5s. Common culprits: unoptimized hero images, slow server response
- **CLS (Cumulative Layout Shift)**: Target < 0.1. Common culprits: images without dimensions, late-loading fonts
- **FID/INP (First Input Delay)**: Target < 100ms. Common culprits: heavy JavaScript
- **Image optimization**: WebP format? Lazy loading? Proper sizing?
- **Hosting**: Vietnamese users need server in VN/APAC for fast response. Check if hosting is global CDN vs local.

### Category 4 — Mobile-friendliness
- Responsive design (not just resizing — actually mobile-optimized)
- Tap targets: buttons and links at least 44px touch target
- Text readable without zooming (min 16px font)
- No horizontal scrolling

### Category 5 — HTTPS and security
- Full HTTPS (not just homepage)
- No mixed content (HTTP resources on HTTPS pages)
- Valid SSL certificate

### Category 6 — Structured data (cross-check with schema-markup skill)
- Any existing schema? Is it valid?
- Missing opportunities (FAQPage, LocalBusiness, Article)

### Vietnamese-specific technical issues to check:
- **Vietnamese characters in URLs**: Should be encoded or replaced with ASCII equivalents for stability
- **Font loading**: Vietnamese fonts (Noto Serif, Be Vietnam Pro) are larger — watch for font-induced LCP issues
- **Facebook Pixel / Zalo SDK**: Heavy tracking scripts can significantly slow Vietnamese sites
- **Shared hosting in Vietnam**: Many SMBs use cheap Vietnamese hosting with slow TTFB — recommend CDN or upgrade if TTFB > 600ms

## Step 4 — Score and prioritize

**Severity levels:**
- 🔴 Critical: Blocking indexing or causing major ranking loss — fix within 24 hours
- 🟡 High: Causing measurable ranking or traffic loss — fix this week
- 🟢 Medium: Best practice improvement — fix this month
- ⚪ Low: Nice to have — backlog

## Step 5 — Write output

Save to `/outputs/assets/seo/technical-seo-audit-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Technical SEO Audit — [Brand Name]
> Generated: [date] | Website: [URL] | Platform: [platform]

## Overall Health Score: [n]/10

| Category | Score | Top Issue |
|---|---|---|
| Crawlability | /10 | |
| Indexability | /10 | |
| Page Speed | /10 | |
| Mobile | /10 | |
| Security | /10 | |
| Structured Data | /10 | |

---

## 🔴 Critical Issues (Fix Today)

### Issue 1 — [Issue name]
**Problem:** 
**Impact:** 
**Fix:**
**How to verify fix worked:**

---

## 🟡 High Priority (Fix This Week)

### Issue 1 — [Issue name]
**Problem:**
**Impact:**
**Fix:**

---

## 🟢 Medium Priority (Fix This Month)

1. **[Issue]** — [Fix]
2. 
3. 

---

## ⚪ Low Priority / Nice to Have

1. 
2. 

---

## Page Speed Recommendations

**Current estimated scores:** (based on analysis)
- Mobile LCP: [estimate] — [status: good/needs work/critical]
- CLS: [estimate]

**Top 3 speed wins:**
1. 
2. 
3. 

---

## Crawl & Index Status

**Pages likely indexed:** [estimate]
**Pages that should be indexed:** [count]
**Robots.txt issues:** [none / list]
**Sitemap status:** [exists/missing/issues]

---

## Quick Win Checklist

- [ ] [Fix 1 — can be done today, high impact]
- [ ] [Fix 2]
- [ ] [Fix 3]
```

## Step 6 — Confirm

After writing:

---
"✅ **Technical SEO audit cho [Brand Name] hoàn chỉnh.**

**Overall score:** [n]/10
**Critical issues:** [n] — [top issue]
**Quick wins:** [n]

📁 Đã lưu: `/outputs/assets/seo/technical-seo-audit-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Fix critical issues trước, sau đó chạy `/on-page-seo` để optimize nội dung, hoặc `/schema-markup` để add structured data."

---
