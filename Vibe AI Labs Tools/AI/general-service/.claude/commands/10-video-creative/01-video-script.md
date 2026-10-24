# Video Script Skill

Your job is to write complete video scripts for brand content — YouTube, Facebook video, TikTok long-form, and website explainer videos. Full two-column format: spoken word and visual direction on the same line, timestamped. The creator should be able to shoot without asking a single follow-up question.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — spoken word must match brand tone
- Target audience (Section 6) — pain points and language they use
- Core offer (Section 9) — the video should connect to this
- Key messages (Section 11) — reinforce throughout

If a blog post exists in `/outputs/assets/content/blog/`: read it — longer videos often distill a blog post.
If `/outputs/strategy/campaign-brief-*.md` exists: check if this video is part of a campaign.

If brand.md doesn't exist: ask user for brand name, voice tone, topic, and target viewer before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided topic, length, or format**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết video script, mình cần biết:
1. **Video về gì:** Topic cụ thể?
2. **Độ dài:** 60 giây / 2–3 phút / 5–10 phút?
3. **Platform:** TikTok/Reels / YouTube / Facebook / Website explainer?
4. **Format:** Talking head / Tutorial / Documentary / Animation voiceover / B-roll + narration?
5. **CTA cuối:** Subscribe / Comment / Link / Book call / DM?"

Wait for answer before continuing.

## Step 3 — Write the script

### Video formats and their rules

**Talking head (founder/expert on camera)**
- Most authentic format — builds trust fastest
- Script should sound conversational, not read
- Use short sentences, natural pauses, rhetorical questions
- Mark emphasis: [PAUSE], [SLOW DOWN], [LEAN IN]
- Avoid lists — on camera, lists feel like a presentation, not a conversation

**Tutorial / how-to**
- Screen recording or demo + voiceover
- Script narrates what viewer sees: "Bây giờ mình click vào đây..." matches the on-screen action
- Step numbers help: "Bước 1...", "Bước 2..." — gives viewer orientation
- Repeat key actions verbally even if visible on screen — some viewers listen without watching

**B-roll + narration (documentary style)**
- Separate voice track from visuals — voice tells story, visuals illustrate
- Script must work as audio-only (many watch on phones with screen down)
- Plan B-roll shots alongside the narration — label clearly in visual column

**Animation / explainer**
- Script drives everything — visuals are produced after
- Very tight word count: 130–150 words per minute of animation
- Simple language — no jargon, no idioms that don't translate visually
- Each concept needs a visual metaphor — note it in the visual column

### Script structure by length

**60–90 seconds (social/ads):**
- 0–5s: Hook — bold claim or question
- 5–45s: Core value — one main point with evidence
- 45–75s: Proof or demonstration
- 75–90s: CTA

**2–3 minutes (educational/YouTube):**
- 0–15s: Hook + promise ("In this video, you'll learn...")
- 15s–1:30: Problem — agitate the pain
- 1:30–2:30: Solution — walk through it
- 2:30–3:00: Proof + CTA

**5–10 minutes (deep dive/tutorial):**
- 0–30s: Hook + agenda (tell them what's coming)
- 30s–2min: Context / why this matters
- 2–7min: Core content (2–4 sections with clear transitions)
- 7–9min: Summary + key takeaway
- 9–10min: CTA + what's next

### Script format (always use this two-column layout)

```
[TIMESTAMP] SECTION NAME
VISUAL: [What appears on screen / camera angle / action]
SPOKEN: "[Exact words to say]"
NOTE: [Production direction — optional]
```

### Vietnamese video script rules
- Conversational register: "thật ra", "nói thật nhé", "bạn biết không" — warm, not formal
- Short sentences: spoken Vietnamese with 5–10 words per sentence reads naturally on camera
- Numbers first: "7 ngày. Không phải 7 tuần — 7 NGÀY." — emphasis through repetition
- Silence is OK: [PAUSE 2 SECONDS] after a key point lets it land
- End on energy: last line before CTA should be upbeat, not trailing off

## Step 4 — Write output

Save to `/outputs/assets/creative/video-script-[slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Video Script — [Title]
> Generated: [date] | Length: [X sec/min] | Format: [format] | Platform: [platform]

**Hook:** "[First line]"
**Core message:** [One sentence]
**CTA:** [Action]

**Assets needed before filming:**
- [list]

**Estimated filming time:** [X minutes]

---

## Full Script

[0:00–0:05] HOOK
VISUAL: [description]
SPOKEN: "[words]"
TEXT OVERLAY: "[text if different from spoken]"

---

[0:05–X:XX] [SECTION NAME]
VISUAL: [description]
SPOKEN: "[words]"
NOTE: [production note if needed]

---

[Continue through full script]

---

[X:XX–end] CTA
VISUAL: [description]
SPOKEN: "[words]"
TEXT OVERLAY: "[CTA text on screen]"

---

## Filming Notes
- Setup: [equipment, location, lighting]
- B-roll list: [cutaway shots needed]
- Screen recording: [yes/no — what to capture]
- Edit notes: [cuts, captions, music direction]

## Repurpose
- Short clip (15s): [which section to cut]
- Quote card: "[best soundbite]"
- Blog post: [link if exists]
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Video script '[Title]' đã hoàn chỉnh.**

**Stats:**
- Length: ~[X] seconds/minutes
- Format: [format]
- Hook: '[first line]'
- CTA: [action]
- Filming time: ~[X] minutes

📁 Đã lưu vào: `/outputs/assets/creative/video-script-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/creative-brief` để brief thumbnail và end card, hoặc `/ugc-script` nếu muốn phiên bản cho khách hàng quay."

---
