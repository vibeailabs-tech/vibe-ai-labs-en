# Partnership Brief Skill

Your job is to write partnership outreach briefs — for co-marketing, distribution partnerships, referral programs, and content collaborations. A partnership brief is not a sponsorship deck. It's a focused proposal that answers one question for the other party: "What's in it for us?"

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Core offer (Section 9) — what you bring to the partnership
- Target audience (Section 6) — whose audience you want access to
- USP (Section 8) — why you're worth partnering with
- Competitors (Section 10) — who NOT to partner with

If brand.md doesn't exist: ask user for offer, audience, and partnership goal before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User specified partner type or specific company**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết partnership brief, mình cần biết:
1. **Partner type:** Co-marketing / Referral program / Content collab / Distribution / Tech integration?
2. **Target partner:** Công ty cụ thể, hoặc loại công ty? (VD: Công ty training, SaaS tools, business communities)
3. **What you offer:** Bạn mang đến gì cho partnership? (audience, content, revenue share, tools)
4. **What you want:** Bạn muốn gì từ partner? (their audience, distribution, credibility)
5. **Structure:** Bạn muốn đề xuất deal structure thế nào?"

Wait for answer before continuing.

## Step 3 — Write the partnership brief

### Partnership types and their value propositions

**Co-marketing partnership**
Both parties promote something together. Each gets access to the other's audience.
Value frame: "Cả hai audience đều cần điều này — và mình + bạn cùng reach được nhiều hơn riêng lẻ."

**Referral program**
One party refers clients to the other in exchange for commission or reciprocal referrals.
Value frame: "Mỗi client bạn refer sang mình = [commission]% / [fixed amount]. Mình làm tương tự."

**Content collaboration**
Co-create content (webinar, joint article, podcast episode) that both parties distribute.
Value frame: "Mình bring content expertise + AI marketing angle. Bạn bring [their expertise]. Output: content cả hai publish."

**Distribution partnership**
One party distributes the other's product or content to their audience.
Value frame: "Bạn có [audience size/type]. Mình có [product/content] they need. Revenue share: [structure]."

**Tech integration**
Two tools or services integrate to serve the same customer better.
Value frame: "Khách của bạn đang dùng mình. Khách của mình đang dùng bạn. Integration makes both better."

### Partnership brief structure (6 sections)

**1. The match (why us, why now)**
- Who you are in one sentence
- Why you're reaching out to THEM specifically (not a generic pitch)
- Why this timing makes sense (market trend, audience overlap, complementary offer)

**2. The audience overlap**
- Your audience: who, size, platform
- Their audience: what you've observed/researched
- The overlap: specific shared characteristics
- Why the overlap creates value for both

**3. What you bring**
- Concrete assets: audience size, content output, distribution reach, tools
- Unique angle: what you uniquely contribute that they can't get elsewhere
- Track record: one result that signals credibility

**4. What you're proposing**
- Specific deal structure — not "let's explore collaboration" — a concrete proposal
- What happens first, what happens next
- Duration: one-off or ongoing?
- Revenue/value split if applicable

**5. What they get**
- Quantified if possible: "Access to [X] subscribers", "Expected [Y] referrals/quarter"
- Qualitative: credibility, content, audience quality
- Risk: low — explain why this is easy to try

**6. Next step**
- One specific ask: 30-minute call / email exchange / review the terms doc
- Timeline: "Mình available tuần này hoặc tuần sau"
- Contact: Zalo + email

### Vietnamese partnership specifics

**Trust first, deal second:** Vietnamese business partnerships often start with relationship. A cold brief may need to be preceded by LinkedIn connection, mutual introduction, or attending the same event. Reference any shared connection.

**Revenue share expectations:** Vietnamese partners often expect 15–30% for referrals in B2B services. Be specific upfront — "mình đề xuất 20% trên mỗi deal thành công" removes ambiguity.

**Reciprocal vs one-way:** Vietnamese business culture values reciprocity. "Mình giúp bạn distribute đến audience mình, bạn làm tương tự" lands better than one-sided proposals.

**Community partnerships:** Startup Vietnam, YBA (Young Business Association), various Facebook groups for SMB owners — these are distribution channels, not just communities. Partnership with their admins can reach thousands of SMB owners directly.

## Step 4 — Write output

Save to `/outputs/distribution/partnership-brief-[partner-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Partnership Brief — [Partner Name/Type]
> Generated: [date] | Type: [partnership type] | Proposed by: [brand name]

---

## Outreach Email / Message

**Subject:** [6 words max — specific, not generic]

---

[Full outreach — 6 sections condensed into email format, 200–300 words]

---

## Full Partnership Brief (for follow-up)

### The Match
[Why us + why them + why now]

### Audience Overlap
| | [Your Brand] | [Partner] |
|---|---|---|
| Audience | [description] | [description] |
| Size | [number] | [estimate] |
| Platform | [channels] | [channels] |
| Overlap | [shared characteristics] | |

### What We Bring
[Your assets and unique contribution]

### Proposed Structure
**Type:** [co-marketing / referral / content / distribution]
**Duration:** [one-off / 3-month pilot / ongoing]
**What happens:** [step by step]
**Revenue/value split:** [specific terms]

### What They Get
[Quantified + qualitative value]

### Next Step
[Specific ask + timeline + contact]

---

## Alternative Proposals (if main proposal doesn't fit)
**Option B:** [Simpler/smaller version]
**Option C:** [Content collab only — lower commitment]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Partnership brief cho '[Partner]' đã hoàn chỉnh.**

**Type:** [partnership type]
**Proposed structure:** [one-line summary]
**What they get:** [key value point]
**Next step ask:** [specific action]

📁 Đã lưu vào: `/outputs/distribution/partnership-brief-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Send outreach email + LinkedIn DM same day. Follow up in 5 days if no response."

---
