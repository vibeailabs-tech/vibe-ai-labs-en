# Content Brief Skill

Your job is to write a research-backed content brief before any content is created. No writer — human or AI — should produce a blog post, article, or website copy without a brief. This is the brief.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice and tone (Section 5)
- Target audience and pain points (Section 6)
- Content pillars (Section 12)
- Key messages (Section 11)
- Positioning (Section 7)

If `/outputs/research/keyword-research-*.md` exists: read it — use Tier 1–3 keywords and PAA questions.
If `/outputs/strategy/campaign-brief-*.md` exists: read it — align brief to campaign goals.

If brand.md doesn't exist: ask user for brand info before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified a topic or keyword**
Use their topic. Go to Step 3.

**Path B — No topic provided**
Ask:
"Bạn muốn mình viết brief cho loại content nào?
1. Blog post (SEO — target keyword cụ thể)
2. Thought leadership article (opinion / industry commentary)
3. Website copy (homepage / about / services)
4. Case study (customer success story)

Và topic hoặc keyword cụ thể là gì?"

Wait for answer before continuing.

## Step 3 — Build the brief

### Brief components (fill all of them)

**1. Content goal**
What should this piece accomplish? Pick one primary:
- Rank for a keyword (SEO)
- Build trust with cold audience (awareness)
- Convert warm leads (consideration/decision)
- Establish thought leadership (authority)

**2. Target audience**
Not "SMB owners" — the specific person reading this piece right now. What's their situation? What brought them to this article? What do they already believe?

**3. Target keyword (for SEO pieces)**
- Primary keyword: [exact phrase]
- Secondary keywords: 2–3 related terms
- Search intent: informational / commercial / navigational
- Estimated difficulty: low / medium / high (based on keyword-research.md or content of SERP)

**4. Headline options (3)**
- Option 1: SEO-optimized (keyword in headline)
- Option 2: Curiosity/emotion angle
- Option 3: Specific outcome/number angle
Mark the recommended one.

**5. Article structure**
- Hook (first 2–3 sentences — what makes them keep reading)
- H2 sections (4–6 sections with specific subheading copy — not "Introduction", "Conclusion")
- For each section: what argument/point is made, what evidence supports it
- CTA placement: where and what

**6. Key argument**
One sentence: what is the single most important thing this piece proves or argues?

**7. Proof points to include**
- Statistics (from research files or brand.md)
- Examples or case studies
- Comparisons or analogies

**8. What NOT to include**
- Topics that distract from the main argument
- Competitor mentions that don't serve the piece
- Generic advice anyone could give

**9. SEO requirements**
- Primary keyword in: title, H1, first 100 words, at least 2 H2s, meta description
- Meta description: 150–160 characters, includes keyword + benefit
- Internal link suggestions: which other pages/posts to link to
- Recommended word count: [based on what ranks for this keyword]

**10. CTA**
What should the reader do after finishing this piece? One specific action.

## Step 4 — Write output

Save to `/outputs/assets/content/briefs/[topic-slug]-brief-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Content Brief — [Title]
> Generated: [date] | Type: [blog/article/website copy] | Keyword: [keyword]

## Goal
[Primary goal — one sentence]

## Target Reader
[Specific person — situation, what they already know, what they're looking for]

## Keyword Strategy
- Primary: [keyword]
- Secondary: [keyword 1], [keyword 2]
- Intent: [informational/commercial/navigational]
- Word count target: [count]

## Headline Options
1. [Option 1] — SEO angle ← Recommended
2. [Option 2] — Curiosity angle
3. [Option 3] — Outcome angle

## Key Argument
[One sentence: what this piece proves]

## Article Structure

### Hook
[What the opening 2–3 sentences accomplish]

### H2: [Exact subheading copy]
- Point: [what's argued]
- Evidence: [stat, example, or analogy to use]

### H2: [Exact subheading copy]
- Point:
- Evidence:

[Repeat for 4–6 sections]

### CTA Section
[Where it goes + what it says]

## Proof Points
- [Stat or data point]
- [Example or case study]
- [Comparison or analogy]

## Do NOT Include
- [Topic to avoid]
- [Framing to avoid]

## SEO Checklist
- [ ] Primary keyword in title
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in at least 2 H2s
- [ ] Meta description written (150–160 chars)
- [ ] Internal links suggested

## Meta Description
[150–160 character meta description with keyword]

## Internal Link Suggestions
- Link to: [page/post] — anchor text: [text]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Content brief cho '[Title]' đã hoàn chỉnh.**

**Summary:**
- Keyword: [primary keyword]
- Key argument: [one sentence]
- Structure: [count] sections
- Word count target: [count] từ
- CTA: [CTA text]

📁 Đã lưu vào: `/outputs/assets/content/briefs/[slug]-brief-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/blog-writer` với brief này để viết bài hoàn chỉnh."

---
