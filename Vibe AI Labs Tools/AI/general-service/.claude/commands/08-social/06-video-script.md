# Video Script Skill

Your job is to write TikTok and Reels scripts — hook, build, payoff, CTA. Format: spoken word and visual direction on the same line so the creator knows exactly what to say AND what to show simultaneously. Not a traditional screenplay. A practical shooting script for solo creators.

## Step 1 — Read inputs

Read `/outputs/profiles-output/brand.md`. Extract:
- Brand voice (Section 5) — spoken word must match written voice
- Target audience (Section 6) — what problems they have, language they use
- Key messages (Section 11) — what the script should reinforce
- Core offer (Section 9) — the CTA connects back to this

If a blog post exists in `/outputs/assets/content/blog/`: read it — the script can be a 60-second distillation of the post.
If `/outputs/assets/social/social-calendar-*.md` exists: check if this topic is scheduled.

If brand.md doesn't exist: ask user for brand name, voice, topic, and target viewer before continuing.

## Step 2 — Collect input

Look at what the user has already provided. Then choose the right path:

**Path A — User provided a topic, blog post, or specific angle**
Use their input. Go to Step 3.

**Path B — No direction provided**
Ask:
"Để viết video script, mình cần biết:
1. **Topic:** Bạn muốn video về gì? (VD: 'so sánh Claude Design vs Figma', '3 lỗi AI marketing', 'cách mình setup hệ thống trong 9 ngày')
2. **Độ dài:** 30 giây / 60 giây / 90 giây?
3. **Format:** Talking head (chỉ nói camera) / Tutorial (screen/demo) / Faceless (voiceover + visual) / B-roll + voiceover?
4. **CTA cuối:** Follow / Comment / Link in bio / DM?
5. **Có sản phẩm demo không?** (laptop, app, tool nào cần show screen không)"

Wait for answer before continuing.

## Step 3 — Write the script

### TikTok/Reels script structure

**The 4-part structure:**

**1. Hook (0–3 seconds) — THE MOST IMPORTANT PART**
If the viewer doesn't stay past 3 seconds, nothing else matters. The hook must:
- State a bold claim, surprising fact, or relatable problem — immediately
- Create a reason to keep watching ("wait for the result" / "this changed how I work" / "most people get this wrong")
- Work WITHOUT sound (a significant portion of viewers watch on mute — show something visually interesting in the first frame)

Hook formulas that work in Vietnamese market:
- Contrast hook: "Agency $3,000/tháng vs hệ thống AI $80/tháng — đây là sự khác biệt thật sự."
- Problem hook: "Nếu bạn đang dùng ChatGPT như thế này, bạn đang lãng phí 80% tiềm năng của nó."
- Curiosity hook: "Mình vừa test Claude Design trong 1 tuần. Đây là điều mình không ngờ tới."
- Result-first hook: "Từ 3 giờ/ngày xuống 45 phút/tuần — đây là cách mình làm được."

**2. Build (3–45 seconds) — Deliver the value**
- One main point per 10–15 seconds
- Each point: claim → demonstration or evidence → next point
- For tutorials: show the screen, show the action, narrate what you're doing
- Keep sentences short — spoken word is different from written word
- Use numbers: "3 bước", "2 phút", "7 ngày" — specifics are more credible on video

**3. Payoff (last 10–15 seconds before CTA) — the "aha" moment**
- The resolution of the hook's promise
- Show the result if you teased a result
- The emotional or practical takeaway — what should the viewer feel or know now?

**4. CTA (final 5 seconds)**
- One action only — never two
- Make it specific and low-friction:
  - "Follow để xem phần 2" — best for growth
  - "Comment '[keyword]' mình gửi bạn tài liệu miễn phí" — best for engagement signal + lead gen
  - "Link in bio để đọc bài đầy đủ" — best for traffic
  - "Nhắn mình qua Zalo để tư vấn miễn phí" — best for Vietnamese B2B

### Script format

Use this two-column format: [VISUAL] on left, [SPOKEN] on right, timestamped.

```
[0:00–0:03] HOOK
VISUAL: [What appears on screen / what creator does]
SPOKEN: "[Exact words to say]"
TEXT OVERLAY: "[Text that appears on screen]" (if different from spoken)

[0:03–0:15] BUILD — Point 1
VISUAL: [Scene description / screen action / camera angle]
SPOKEN: "[Exact words]"
NOTE: [Any production direction — pause here, emphasize this word, show this specific thing]

[Continue through full script]
```

### Length guidelines

| Length | Use for | Word count (spoken) |
|---|---|---|
| 15–30 sec | Hook only / teaser / trending audio | 40–80 words |
| 30–60 sec | Single tip / quick tutorial / hot take | 80–150 words |
| 60–90 sec | Mini tutorial / case study / comparison | 150–225 words |
| 2–3 min | Full tutorial / deep dive (use sparingly) | 300–450 words |

**Optimal for most Vietnamese B2B content: 45–60 seconds.** Long enough to deliver value, short enough to hold attention.

### Vietnamese video script rules
- Speak like you'd speak to a friend — not how you'd write an email
- Drop the formal connectors: "Vì vậy", "Tuy nhiên", "Hơn nữa" — too stiff for video
- Use "thật ra", "thực ra", "thật sự", "nói thật" — these feel authentic on camera
- Pause beats: mark [PAUSE] in the script where creator should let something land
- Numbers and stats: say the number first, then explain — "7 ngày. Không phải 7 tuần, 7 NGÀY."
- Vietnamese viewers respond strongly to "behind the scenes" and "honest review" framing

## Step 4 — Write output

Save to `/outputs/assets/social/video-script-[topic-slug]-[Mon-DD-YYYY].md`:

> **Date format:** Use today's date formatted as `Mon-DD-YYYY` (e.g., `Apr-22-2026`) for the `[Mon-DD-YYYY]` placeholder in the filename. Run `date +"%b-%d-%Y"` to get it.

```markdown
# Video Script — [Title]
> Generated: [date] | Length: [X sec] | Format: [talking head/tutorial/etc] | Platform: TikTok/Reels

**Hook preview:** "[First line]"
**CTA:** [What the CTA drives to]
**Assets needed:** [List of what to prepare before filming]

---

## Full Script

[0:00–0:03] HOOK
VISUAL: [Description]
SPOKEN: "[Words]"
TEXT OVERLAY: "[Text if different]"

---

[0:03–0:XX] BUILD — [Point name]
VISUAL: [Description]
SPOKEN: "[Words]"
NOTE: [Production note if needed]

---

[Continue]

---

[X:XX–end] CTA
VISUAL: [Description]
SPOKEN: "[Words]"
TEXT OVERLAY: "[CTA text on screen]"

---

## Filming Notes
- Setup: [equipment, location, lighting]
- B-roll needed: [list of cutaway shots]
- Screen recording: [yes/no — what to record]
- Estimated filming time: [X minutes]
- Edit notes: [cuts, captions, music direction]

## Repurpose
- TikTok caption: [link to or note to run /social-copy]
- Blog post: [link if exists]
- Quote for static post: "[best soundbite from script]"
```

## Step 5 — Confirm

After writing, reply:

---
"✅ **Video script '[Title]' đã hoàn chỉnh.**

**Stats:**
- Length: ~[X] seconds
- Format: [format]
- Hook: '[first line]'
- CTA: [CTA type]
- Filming time: ~[X] minutes

📁 Đã lưu vào: `/outputs/assets/social/video-script-[slug]-[Mon-DD-YYYY].md`

**Bước tiếp theo:** Chạy `/social-creative` để brief thumbnail và cover frame, hoặc `/social-copy` để viết caption kèm theo video này."

---
