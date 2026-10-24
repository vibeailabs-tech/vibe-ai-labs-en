# ROI Calculator Skill

Your job is to calculate the true return on investment for marketing activities — paid ads, content, email, and the full system cost — and present it in a format the business owner can use to make budget decisions.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — price points for revenue calculation
- Target audience (Section 6) — context for LTV and conversion expectations

Read any campaign data from `/outputs/performance/`.

If no data available: ask user for the key numbers before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided the numbers**
Use their input. Go to Step 3.

**Path B — No numbers provided**
Ask:
"Để tính ROI, mình cần một số con số:
1. **Revenue:** Tổng doanh thu từ campaign/period này là bao nhiêu?
2. **Ad spend:** Tổng chi phí quảng cáo?
3. **Other costs:** Chi phí content, tools, agency (nếu có)?
4. **Leads:** Bao nhiêu leads được tạo ra?
5. **Closes:** Bao nhiêu deals đã chốt?
6. **Avg deal size:** Giá trị trung bình mỗi deal?
7. **LTV estimate:** Khách hàng này thường mua lại bao nhiêu lần / giá trị vòng đời?"

Wait for answer before continuing.

## Step 3 — Calculate ROI

### Core calculations

**Marketing ROI:**
```
ROI = (Revenue - Total Marketing Cost) / Total Marketing Cost × 100
```

**ROAS (Return on Ad Spend — paid only):**
```
ROAS = Revenue / Ad Spend
```

**CAC (Customer Acquisition Cost):**
```
CAC = Total Marketing Cost / Number of New Customers Acquired
```

**CPL (Cost per Lead):**
```
CPL = Total Marketing Cost / Leads Generated
```

**LTV:CAC Ratio:**
```
LTV:CAC = Customer Lifetime Value / CAC
- <1:1 = losing money on every customer
- 1:1 to 3:1 = marginal
- 3:1 = healthy
- 5:1+ = strong — may be under-investing
```

**Funnel conversion rates:**
```
Lead → Demo rate = Demos / Leads × 100
Demo → Close rate = Closes / Demos × 100
Overall close rate = Closes / Leads × 100
```

**Payback period:**
```
Payback period = CAC / (Monthly Revenue per Customer)
```

### Channel ROI comparison

If multi-channel data is available, calculate ROI per channel:
- Paid social (Facebook/TikTok)
- Google Search
- Email marketing
- Organic content (estimate based on attributed conversions)
- Cold outreach

### Vietnamese market benchmarks

**Healthy B2B SaaS/services benchmarks:**
- LTV:CAC ratio: 3:1 minimum, 5:1 strong
- Payback period: under 12 months
- Lead → Close rate: 10–20% for warm leads, 2–5% for cold outreach
- Email open rate attribution: 20–30% of email revenue is attributable

**Healthy B2C/SMB benchmarks:**
- ROAS: 3× minimum, 5×+ strong
- CPL: 50,000–150,000 VND for qualified leads
- CAC payback: under 3 months for repeat-purchase businesses

## Step 4 — Write output

Save to `/outputs/performance/roi-calculator-[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# ROI Analysis — [Campaign / Period]
> Generated: [date] | Period: [date range] | Currency: VND

## Bottom Line
**Marketing ROI: [X]%**
**ROAS: [X]× **
**LTV:CAC: [X]:1**
**Verdict:** [Healthy / Marginal / Losing money — one sentence explanation]

---

## Investment Summary
| Cost category | Amount (VND) |
|---|---|
| Paid advertising | |
| Content creation | |
| Tools / Software | |
| Agency / Freelance | |
| **Total cost** | |

---

## Revenue Attributed
| Revenue source | Amount (VND) |
|---|---|
| Direct conversions (tracked) | |
| Assisted conversions (estimated) | |
| **Total revenue** | |

---

## Core Metrics

| Metric | Value | Benchmark | Status |
|---|---|---|---|
| Marketing ROI | [X]% | >100% | ✅ / ⚠️ / ❌ |
| ROAS | [X]× | >3× | ✅ / ⚠️ / ❌ |
| CAC | [VND] | | |
| CPL | [VND] | 50k–150k VND | ✅ / ⚠️ / ❌ |
| LTV:CAC | [X]:1 | >3:1 | ✅ / ⚠️ / ❌ |
| Payback period | [months] | <12 months | ✅ / ⚠️ / ❌ |

---

## Funnel Conversion
| Stage | Count | Rate |
|---|---|---|
| Impressions → Clicks | | [CTR]% |
| Clicks → Leads | | [CVR]% |
| Leads → Demos | | [%]% |
| Demos → Closes | | [Close rate]% |
| Overall: Impressions → Customer | | [%]% |

---

## Channel ROI Breakdown (if multi-channel)
| Channel | Spend | Revenue attributed | ROAS | CPL |
|---|---|---|---|---|
| Facebook Ads | | | | |
| Google Ads | | | | |
| Email | | | | |
| Organic | | | | |

---

## LTV Analysis
- Avg deal size: [VND]
- Avg purchases per year: [n]
- Avg customer lifespan: [months]
- **Estimated LTV: [VND]**
- **LTV:CAC ratio: [X]:1**

---

## Scaling Projection
If we increase budget by 50%, assuming current efficiency holds:
- Projected spend: [VND]
- Projected revenue: [VND]
- Projected new customers: [n]
- Risk: [efficiency drop assumption]

---

## Recommendations
1. [Where to increase budget]
2. [Where to cut]
3. [What to test to improve the weakest metric]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **ROI analysis cho '[Period/Campaign]' đã hoàn chỉnh.**

**ROI: [X]% | ROAS: [X]× | LTV:CAC: [X]:1**
**Verdict:** [One-sentence health assessment]
**Top recommendation:** [Specific action]

📁 Đã lưu vào: `/outputs/performance/roi-calculator-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/monthly-strategy-review` để đưa data này vào chiến lược tháng sau."

---
