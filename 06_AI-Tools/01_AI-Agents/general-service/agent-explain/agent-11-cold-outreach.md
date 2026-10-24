# Agent 11 — Cold Outreach Agent
> Deep-dive explanation | Layer 3 — Execution

## What this agent does

The Cold Outreach Agent produces everything needed to start and maintain conversations with cold prospects — before they know who you are. Cold emails, LinkedIn DMs, multi-touch follow-up sequences, objection responses, and the personalization system that makes each message feel written specifically for the recipient.

It covers the full cold-to-warm pipeline: first touch → follow-up → objection → next step.

---

## 5 Skills

### 1. `/cold-email` — 3-Version Cold Emails
**What it does:** Writes 3 versions of a cold email for A/B testing — problem-led, proof-led, and referral/trigger-led — with subject lines, preview text, and testing notes.

**The PASTE framework:** Every cold email follows Problem → Acknowledge → Solution hint → Tease proof → Easy ask. This structure ensures the email is about the prospect (not the sender), qualifies them, and ends with the lowest-friction possible ask.

**Why 3 versions:** Problem-led works best for prospects who don't yet know a solution exists. Proof-led works for prospects who know the problem but need evidence. Referral-led works when there's a specific trigger (recent post, job change, mutual connection). You don't know which until you test.

**The negative qualifier:** Every cold email includes copy that filters out wrong-fit prospects — "Phù hợp nếu bạn đang trả >$300/tháng cho agency." This intentionally makes bad-fit readers self-select out, reducing wasted follow-up and improving reply quality.

**Output:** `/outputs/assets/outreach/cold-email-[slug].md`

---

### 2. `/linkedin-dm` — LinkedIn DM Sequence
**What it does:** Writes connection request notes (300 chars), opening DMs, follow-up DMs, and pitch DMs — with language choice guidance (Vietnamese vs English based on prospect's profile language).

**The connection request problem:** Most people waste this 300-character real estate with "Xin chào, mình muốn kết nối để mở rộng mạng lưới." This is generic and often ignored. The skill writes connection notes that reference something specific about the prospect, signaling genuine attention.

**No pitch in opening DM:** The opening DM after connection asks ONE question about them. Never pitches. The pitch comes only after they've replied — that's when the door is open.

**Vietnamese LinkedIn context:** LinkedIn in Vietnam is primarily used by startup founders, corporate marketing managers, and international-facing roles. Pure SMB owners are more active on Facebook and Zalo. The skill notes when LinkedIn outreach may not be the right channel for a given ICP.

**Output:** `/outputs/assets/outreach/linkedin-dm-[slug].md`

---

### 3. `/follow-up-sequence` — Multi-Touch Follow-Up
**What it does:** Writes a complete 5–7 touch sequence with new value at every touch, across email + LinkedIn + Zalo, with a break-up email at the end.

**The "new value" rule:** The most common follow-up mistake is "Just following up on my previous email." It adds nothing and wastes everyone's time. Every touch in this sequence introduces something new — a different proof point, a relevant insight, a case study, a reframe of the ask.

**Angle rotation:** Touch 1 (problem) → Touch 2 (new proof) → Touch 3 (value add/content) → Touch 4 (case study) → Touch 5 (lower friction ask) → Touch 6 (break-up). Each touch changes the angle so the sequence doesn't feel repetitive.

**Break-up email gets the highest reply rate:** "Mình hiểu bạn bận và không muốn làm phiền thêm — nếu thời điểm chưa phù hợp, chỉ cần reply 'chưa phù hợp' là đủ." This email converts because it removes pressure. Prospects feel safe replying because there's no consequence.

**Multi-channel timing:** Email on days 0, 5, 12, 25, 32. LinkedIn DM on days 1, 8. Zalo on day 18 if number available. Multi-channel increases reply rate — different people respond to different channels first.

**Output:** `/outputs/assets/outreach/follow-up-sequence-[slug].md`

---

### 4. `/objection-handler` — ACCA Objection Responses
**What it does:** Writes responses to 7 universal sales objections for email, Zalo, and call contexts — with a quick-reference cheat sheet.

**The ACCA framework:** Acknowledge → Clarify → Counter → Ask. Never skip Acknowledge — arguing with an objection never works. The Clarify step is critical: most surface objections ("giá cao quá") hide a different real objection ("I don't see the ROI yet"). Asking one clarifying question surfaces what's actually blocking them.

**7 universal objections covered:**
1. "Giá cao quá" — usually ROI uncertainty, not actual budget
2. "Để suy nghĩ thêm" — insufficient conviction, not time
3. "Đang dùng competitor" — information, not rejection
4. "Không có budget" — sometimes true, sometimes "I don't see value"
5. "AI không phù hợp với ngành mình" — fear of change
6. "Đã thử AI rồi, không hiệu quả" — real experience — don't dismiss
7. "Tự làm được" — objection to outsourcing, not to the outcome

**Vietnamese cultural note:** Vietnamese B2B buyers rarely say "no" directly. "Để xem xét thêm" can be a soft no or a genuine "not now." The skill helps distinguish between them and respond appropriately — without pressure tactics.

**Output:** `/outputs/assets/outreach/objection-handler.md`

---

### 5. `/personalization-framework` — Scale Personalization System
**What it does:** Builds a repeatable research + template system so every cold outreach feels personally written — even when sending at volume.

**The 1-3-1 rule:** 1 minute of research → find 3 personalization signals → use 1 per message. Using all 3 feels like surveillance. Using 0 feels like a mass blast. 1 specific, genuine signal hits the sweet spot.

**5-tier signal hierarchy:** Recent post/article they wrote > company news > job change > relevant industry trend > job title alone. Most salespeople default to job title (lowest quality). This framework trains the habit of going higher in the hierarchy first.

**Research process (5 min per prospect):**
1. LinkedIn profile — recent posts, opinions (1 min)
2. Company LinkedIn — news, hiring patterns (1 min)
3. Website — messaging, blog, team size (1 min)
4. Google search — interviews, press (1 min)
5. Write the personalization line (1 min)

**High-volume variant (2 min):** For when you're sending 20+ per day — faster research process with minimum viable personalization that still beats generic outreach.

**Output:** `/outputs/assets/outreach/personalization-framework.md`

---

## No APIs Required

Agent 11 writes all outreach content without API access. Integration with outreach tools (Apollo, Lemlist, Instantly, or manual Gmail) happens after the content is written. The agent produces the content; the human or automation tool delivers it.

---

## Layer Position and Data Flow

```
brand.md (L1) ──────────────────────┐
campaign-brief.md (L2) ─────────────┤──→ Agent 11 Cold Outreach ──→ /assets/outreach/
ICP from audience-profile (L1) ──────┘
                                                    ↓
                                       Prospect replies
                                                    ↓
                                       Sales Enablement Agent (Agent 12)
                                       → proposals, case studies, closes
```

---

## Recommended Sequence

```
1. /personalization-framework → build research system
2. /cold-email → write 3-version first touch
3. /linkedin-dm → connection + opening DM
4. /follow-up-sequence → full 6-touch sequence
5. /objection-handler → prepare for replies
```

Then: send outreach → prospect replies → hand off to Sales Enablement Agent.

---

## What This Agent Doesn't Do

- Send emails or DMs (no automation API)
- Find prospect contact info (no Apollo/Hunter integration yet)
- Manage a CRM or track replies
- Write proposals or close deals (Sales Enablement Agent)
- Write paid ad copy (Ads Agent)
