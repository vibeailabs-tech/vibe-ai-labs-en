# Audience Update Skill

Your job is to update the target audience profile in brand.md based on what performance data has revealed about who actually buys, what they respond to, and how they behave. The ICP you built at the start was a hypothesis. Real customer data is the truth. This skill closes the gap.

## Step 1 — Read inputs

Read ALL of the following:
- `/outputs/profiles-output/brand.md` — current Section 6 (Target Audience) — this is what you're updating
- `/outputs/performance/monthly-review-*.md` — what the data revealed about audience behavior
- `/outputs/performance/campaign-report-*.md` — which audience segments performed
- `/outputs/performance/weekly-report-*.md` — engagement patterns
- `/outputs/strategy/campaign-brief-*.md` — original audience assumptions

If no performance data exists: ask user what they've learned from real customers before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User described what they've learned from customers**
Use their input. Go to Step 3.

**Path B — No input provided**
Ask:
"Để cập nhật audience profile, mình cần biết:
1. **Segment hoạt động tốt nhất:** Nhóm khách hàng nào convert tốt nhất trong 30–90 ngày qua?
2. **Insight mới:** Bạn học được điều gì về khách hàng mà trước đây bạn không biết?
3. **Messaging resonated:** Angle nào, headline nào, hay câu nói nào khiến khách hàng phản hồi nhiều nhất?
4. **Objections:** Phản đối phổ biến nhất mà khách hàng tiềm năng đưa ra là gì?
5. **Unexpected buyers:** Có ai mua mà bạn không expect không? Họ là ai?"

Wait for answer before continuing.

## Step 3 — Analyze and update

### What to update in audience Section 6

**Demographics:** Have you discovered the real buyer is different from who you assumed? Update age range, job title, company size, industry.

**Pain points:** Which pain points drove conversions? Reorder — put the highest-converting pain points first. Remove pain points that consistently failed to resonate.

**Buying triggers:** What event or situation causes someone to start looking for a solution? Update based on sales conversations and conversion data.

**Objections:** What did prospects actually push back on? This is ground-truth data, more reliable than assumptions. Update the objections list.

**ICP (Ideal Customer Profile):** The named persona may need updating. If a new segment is outperforming the original ICP assumption, update the persona description.

**Online behavior:** Where are they actually discovering you? Which platforms drive your best leads? Update platform priorities based on attribution data.

**Content pillars (Section 12):** Which content topics drove the most engagement and conversions? Adjust pillar emphasis accordingly.

### What NOT to change based on one month of data

Don't change the fundamental ICP based on one unusual month. Look for patterns across at least 60–90 days before making structural changes to the profile.

One strong month from an unexpected segment = interesting signal, not confirmed ICP shift. Note it as an emerging segment, don't overwrite the core profile yet.

### Vietnamese audience update specifics

**Zalo behavior:** If Zalo is active, Zalo response patterns often reveal more about buying intent than social media engagement. High Zalo response but low email response = audience prefers direct messaging.

**Regional differences:** Note if buyers from different cities (HCM vs Hanoi vs Da Nang) behave differently. Vietnamese buyers in different regions have different decision speeds and trust signals.

**Group/community buyers:** Vietnamese SMBs often buy based on what peers in their industry group are doing. If referrals from specific communities are converting well, note the community as a primary acquisition channel.

## Step 4 — Write updates to brand.md

Update `/outputs/profiles-output/brand.md`:
- Section 6 (Target Audience) — update demographics, pain points, triggers, objections, ICP, behavior
- Section 12 (Content Pillars) — reorder or adjust based on content performance
- Update `Last updated` date
- Never touch other sections

Also save a change log to `/outputs/performance/audience-update-[YYYY-MM].md`:

```markdown
# Audience Update Log — [Month YYYY]
> Generated: [date] | Based on: [data sources used]

## What Changed

### ICP Updates
**Before:** [Previous ICP description]
**After:** [Updated ICP description]
**Why:** [Data that drove this change]

### Pain Points — Reordered
**Previous order:**
1. 
2. 
3. 

**New order (based on conversion data):**
1. [Highest converting pain point]
2. 
3. 

**Removed:** [Pain point that consistently underperformed]
**Added:** [New pain point discovered from customer conversations]

### Objections — Updated
**New objection identified:** [Objection + frequency]
**Objection that's less common than assumed:** [Objection]

### Emerging Segments
[Any new audience segment worth watching — not yet confirmed ICP but showing signal]

### Content Pillar Adjustments
**Increased emphasis:** [Pillar] — [why]
**Decreased emphasis:** [Pillar] — [why]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Audience profile đã được cập nhật dựa trên performance data.**

**Thay đổi chính:**
- ICP: [What changed about the persona]
- Pain points: [Reordering or additions]
- New objection: [If any]
- Emerging segment: [If any]

📁 brand.md Section 6 + 12 đã cập nhật
📁 Change log lưu tại: `/outputs/performance/audience-update-[YYYY-MM].md`

**Bước tiếp theo:** Chạy `/messaging-refinement` để cập nhật key messages dựa trên audience mới này."

---
