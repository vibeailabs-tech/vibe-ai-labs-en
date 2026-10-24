# Schema Markup Skill

Your job is to write valid JSON-LD structured data for Vietnamese business pages — helping Google understand page content and display rich results (FAQs, reviews, business info, breadcrumbs).

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand name, location, industry (Sections 1–3)
- Core offer and pricing (Section 9)

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified page type and content**
Use what they gave. Go to Step 3.

**Path B — No specifics**
Ask:
"Để viết schema markup, mình cần biết:
1. **Loại trang:** Homepage / Service page / Blog post / FAQ page / Contact page
2. **Nội dung trang:** Paste nội dung chính (hoặc mô tả ngắn)
3. **Thông tin business:** Địa chỉ, phone, email, giờ mở cửa (nếu relevant)
4. **Đã có schema chưa?** Nếu có, paste code để mình check"

Wait for answer.

## Step 3 — Select schema types

### Vietnamese business schema priority:

**Always include on every page:**
- `WebPage` or page-specific type
- `BreadcrumbList` (if site has navigation depth)

**By page type:**

**Homepage / About:**
- `Organization` — business name, URL, logo, contact, social profiles
- `LocalBusiness` (if physical location or serving local area)
  - Vietnamese specific: use `addressRegion` for tỉnh/thành, `addressLocality` for quận/huyện

**Service/Product pages:**
- `Service` — name, description, provider, areaServed
- `Product` (if e-commerce) — name, description, offers, aggregateRating
- `Offer` — price, priceCurrency (VND), availability

**Blog posts:**
- `Article` or `BlogPosting` — headline, author, datePublished, dateModified, image
- `BreadcrumbList`

**FAQ pages (high value for Vietnamese market):**
- `FAQPage` with `Question` and `Answer` — this generates FAQ rich results in SERP, which significantly improves CTR

**Local business:**
- `LocalBusiness` with full address, openingHoursSpecification, geo coordinates
- `PostalAddress` with Vietnamese address format

**Reviews/Testimonials pages:**
- `AggregateRating` — ratingValue, reviewCount, bestRating

### Vietnamese-specific schema notes:
- `addressCountry`: "VN"
- `priceCurrency`: "VND"
- Phone format: "+84-xxx-xxx-xxxx"
- Language: `inLanguage`: "vi" for Vietnamese content

## Step 4 — Write schema code

For each applicable schema type:
1. Write valid JSON-LD (not Microdata or RDFa — JSON-LD is Google's preferred format)
2. Fill in real values from brand.md and user input
3. Add implementation instructions (where to paste in HTML)
4. Validate mentally against Google's requirements (check for required vs. recommended properties)

**JSON-LD format:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "...",
  ...
}
</script>
```

**Where to place:** Inside `<head>` tag or at bottom of `<body>` — both work for Google.

## Step 5 — Write output

Save to `/outputs/assets/seo/schema-markup-[page-name]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Schema Markup — [Page Name]
> Generated: [date] | Page type: [type] | Schema types: [list]

## Implementation Instructions

Paste each block inside the `<head>` section of [page name]. 
Test with Google's Rich Results Test after implementation.

---

## Schema Block 1 — [Type]

**Purpose:** [what this schema does / what rich result it enables]

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "[Type]",
  ...
}
</script>
```

---

## Schema Block 2 — [Type] (if applicable)

**Purpose:** 

```html
<script type="application/ld+json">
{
  ...
}
</script>
```

---

## Validation Checklist

- [ ] Test with Google Rich Results Test (search.google.com/test/rich-results)
- [ ] No errors in Google Search Console after deploying
- [ ] JSON is valid (no syntax errors)
- [ ] Required fields for [schema type] are all present

## Expected Rich Results

After implementing and Google indexing:
- [What rich result should appear in SERP]
- [Estimated CTR improvement]
```

## Step 6 — Confirm

After writing:

---
"✅ **Schema markup cho [page name] hoàn chỉnh.**

**Schema types viết:** [list]
**Rich results có thể xuất hiện:** [what Google might show]
**Cách test:** Google Rich Results Test

📁 Đã lưu: `/outputs/assets/seo/schema-markup-[page-name]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/technical-seo-audit` để check toàn bộ site, hoặc `/on-page-seo` để optimize page content."

---
