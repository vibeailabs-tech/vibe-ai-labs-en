# Local SEO Skill

Your job is to optimize a Vietnamese business for local search — Google Business Profile signals, local keyword targeting, location-specific content, and citation strategy. No APIs required; pure analysis and recommendations.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Location (Section 3) — district, city
- Industry and core offer (Sections 2 + 9)
- Target audience (Section 6) — especially how they search locally

If location is blank or "toàn quốc" (nationwide): note that local SEO is less critical but still relevant for Vietnamese search behavior.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided Google Business Profile URL or local search info**
Use what they gave. Go to Step 3.

**Path B — No local info provided**
Ask:
"Để tối ưu local SEO, mình cần biết:
1. **Địa chỉ chính xác:** Số nhà, đường, phường/xã, quận/huyện, tỉnh/thành phố
2. **Google Business Profile:** Bạn đã có chưa? Link nếu có.
3. **Từ khóa địa phương:** Khách hàng thường tìm bạn bằng từ khóa nào? (VD: 'spa quận 7', 'kế toán TPHCM')
4. **Đối thủ local:** 2–3 đối thủ cùng khu vực"

Wait for answer.

## Step 3 — Analyze local SEO opportunities

### Vietnamese local search context:
- **Google Maps dominance**: Vietnamese users search heavily on Google Maps for local services
- **"Gần đây" searches**: "quán cà phê gần đây", "spa gần đây" — proximity signals matter
- **Zalo as local discovery**: Many Vietnamese businesses are found via Zalo — recommend Zalo Official Account if applicable
- **Facebook local presence**: Facebook is often searched for local businesses in Vietnam — business page optimization is part of local SEO
- **Review platforms**: Google Reviews, Facebook Reviews, and local directories like YellowPages Vietnam

### Google Business Profile audit checklist:
- Business name matches exactly what's on website
- Primary category is the most specific match available
- Secondary categories added for all services
- Complete address with correct district format for Vietnamese addresses
- Phone number: Vietnamese format (+84 or 0xxx-xxx-xxx)
- Website URL linked
- Business hours complete including holidays (Tết, lễ)
- Photos: exterior, interior, team, products/services (minimum 10)
- Description: 750 characters, keywords in first 250
- Q&A section seeded with common customer questions

### Local keyword strategy:
Build keyword variations for:
- `[service] [city]` (e.g., "thiết kế website TPHCM")
- `[service] quận [district]` (e.g., "spa quận 7")
- `[service] gần [landmark]` (e.g., "nhà hàng gần Bến Thành")
- Vietnamese question format: "ở đâu", "tại TPHCM", "chất lượng"

### Local content recommendations:
1. Location landing page: `/[city]/[service]` or `/[service]-[city].html`
2. Local blog content: "[Top X] + [service] + [location]" format
3. Neighborhood/district-specific pages if multiple locations

### Citation building:
Vietnamese directories to list on:
- Google Business Profile (critical)
- Facebook Business Page (critical)
- Zalo Official Account
- Foody / Eatigo (restaurants/F&B)
- Booking.com / Agoda (hospitality)
- YellowPages Vietnam (yp.vn)
- Vietnam Business Directory (doanhnghiep.vn)
- Industry-specific directories

## Step 4 — Write output

Save to `/outputs/assets/seo/local-seo-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Local SEO Strategy — [Brand Name]
> Generated: [date] | Location: [city/district]

## Local SEO Score (Current State)

| Factor | Status | Priority |
|---|---|---|
| Google Business Profile | Exists / Missing / Incomplete | High/Med/Low |
| NAP consistency (Name/Address/Phone) | | |
| Local keyword targeting | | |
| Location pages on website | | |
| Local citations | | |
| Reviews strategy | | |

---

## Google Business Profile — Action List

### Must fix immediately:
- 

### Should add this week:
- 

### Ongoing (monthly):
- 

---

## Local Keyword Map

### Primary local keywords (target these first):
| Keyword | Search intent | Recommended page |
|---|---|---|
| | | |

### Secondary (blog/supporting content):
| Keyword | Content angle |
|---|---|
| | |

---

## Location Page Recommendations

**Create these pages:**
1. URL: `/[slug]` — Target keyword: [keyword] — Content brief: [summary]
2. 
3. 

**Template structure for each location page:**
- H1: [Service] tại [City/District]
- Intro: 150 words with local keyword
- Why choose us in [location]: 3 points
- Service details
- Local testimonials / reviews
- Map embed
- Local CTA: "Gọi ngay" or "Book hẹn"

---

## Citation Building — Priority List

| Directory | URL | Status | Priority |
|---|---|---|---|
| Google Business Profile | | | Critical |
| Facebook Business Page | | | Critical |
| Zalo Official Account | | | High |
| [Industry-specific] | | | High |

---

## Reviews Strategy

**Request timing:** [when to ask — after service completion, specific trigger]
**Request method:** [Zalo message template, QR code, email]
**Response template for positive reviews:**
[template]
**Response template for negative reviews:**
[template]

---

## 30-Day Local SEO Quick Win Plan

Week 1:
- 

Week 2:
- 

Week 3–4:
- 
```

## Step 5 — Confirm

After writing:

---
"✅ **Local SEO strategy cho [Brand Name] hoàn chỉnh.**

**Ưu tiên ngay:**
- [Top 1 action]
- [Top 2 action]

**Keywords địa phương quan trọng nhất:** [top 3]

📁 Đã lưu: `/outputs/assets/seo/local-seo-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/on-page-seo` để optimize location pages, hoặc `/technical-seo-audit` để check site-wide issues."

---
