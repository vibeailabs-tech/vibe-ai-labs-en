---
name: market-research
description: Conducts live market research for a Vietnamese business using Perplexity via OpenRouter. Use this skill when the user wants to understand their market size, industry trends, customer behavior, or competitive landscape in Vietnam. Trigger whenever the user mentions market research, industry analysis, market size, or wants to understand their market.
---

# Market Research Skill

Your job is to pull live, specific market intelligence for this business — not generic industry overviews, but data that directly informs their marketing and positioning decisions.

## Step 1 — Read brand.md

Read `/outputs/profiles-output/brand.md`. Extract:
- Industry and business type
- Location (city/region)
- Target audience
- Competitors already identified

If brand.md doesn't exist: ask the user for their industry and location before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified a research focus**
Use their focus. Go to Step 3.

**Path B — No focus provided**
Ask:
"Bạn muốn mình tập trung vào khía cạnh nào của thị trường?
1. Quy mô và tăng trưởng thị trường (market size + growth)
2. Hành vi khách hàng (customer behavior + trends)
3. Cơ hội thị trường (gaps + opportunities)
4. Tất cả (full market overview)"

Wait for answer before continuing.

## Step 3 — Run market research via OpenRouter

Make a POST request to OpenRouter using the Perplexity Sonar model:

```
POST https://openrouter.ai/api/v1/chat/completions
Authorization: Bearer $OPENROUTER_API_KEY
Content-Type: application/json

{
  "model": "perplexity/sonar",
  "messages": [
    {
      "role": "user",
      "content": "Research the [INDUSTRY] market in Vietnam in 2024-2025. Provide: 1) Market size and growth rate with specific numbers, 2) Key customer segments and their behaviors, 3) Major trends shaping the industry, 4) Market gaps and opportunities for [BUSINESS TYPE] targeting [TARGET AUDIENCE]. Focus on Vietnam specifically — Ho Chi Minh City and Hanoi if relevant. Include specific statistics, growth rates, and actionable insights."
    }
  ]
}
```

Replace `[INDUSTRY]`, `[BUSINESS TYPE]`, `[TARGET AUDIENCE]` with values from brand.md.

Run 2 separate queries:
1. **Market size + trends query** — broad industry overview
2. **Customer behavior query** — specific to their target audience in Vietnam

## Step 4 — Synthesize and structure findings

From the API responses, extract and organize:

**Market Overview:**
- Market size (USD or VND)
- Growth rate (CAGR or YoY)
- Key market drivers
- Vietnam-specific dynamics

**Customer Insights:**
- How Vietnamese customers in this segment make buying decisions
- Online vs. offline behavior
- Platform preferences (Facebook, TikTok, Zalo, etc.)
- Price sensitivity and spending patterns

**Market Opportunities:**
- Gaps no one is filling well
- Underserved segments
- Emerging trends to ride early
- Geographic opportunities (HCMC vs Hanoi vs other cities)

**Threats & Risks:**
- Market saturation risks
- Regulatory or economic risks
- Competitor momentum

## Step 5 — Write output

Save findings to `/outputs/research/market-research-[Mon-DD-YYYY].md` using this structure:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Market Research — [Brand Name]
> Generated: [date] | Industry: [industry] | Market: Vietnam

## Market Overview
[size, growth, drivers]

## Customer Behavior
[how they buy, where they are, what they care about]

## Opportunities
[specific gaps and trends]

## Threats
[risks to watch]

## Key Data Points
[bullet list of most important stats to reference in content/strategy]

## Sources
[list sources from Perplexity response]
```

## Step 6 — Confirm

After writing, reply:

---
"✅ **Market research cho [Brand Name] đã hoàn chỉnh.**

**Highlights:**
- Quy mô thị trường: [market size]
- Tăng trưởng: [growth rate]
- Cơ hội lớn nhất: [top opportunity]
- Rủi ro cần chú ý: [top risk]

📁 Đã lưu vào: `/outputs/research/market-research-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/competitor-analysis` để phân tích đối thủ cụ thể."

---
