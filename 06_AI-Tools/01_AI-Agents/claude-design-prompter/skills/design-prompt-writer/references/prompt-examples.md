# Prompt Examples — Before & After

One before/after per output type. These show what "good" looks like.

---

## 7. Motion Graphic — Brand Reel / Animated Post

**❌ Before (vague):**
```
Làm reel giới thiệu thương hiệu cà phê, trông dynamic và có chữ chạy.
```

**✅ After (precise):**
```
Create a 15-second Instagram Reel for a Vietnamese specialty coffee brand.

PLATFORM: Instagram Reel, 1080x1920px (9:16). Duration: 15 seconds.

BRAND:
Colors: espresso brown (#2C1810) background, cream (#F5E6D3) text, muted gold (#C9A84C) accent
Typography: Playfair Display 700 (display headlines), Be Vietnam Pro 400 (body)
Tone: intimate, slow, artisan — không commercial, không stock

SCENE SEQUENCE:
Scene 1 (0–2s): Black screen → fade-in overhead flat-lay of ceramic coffee cup
  Text: none. Audio: sound of coffee pouring.

Scene 2 (2–5s): Cup stays. Text slides up from bottom:
  "RANG MỘC" — Playfair Display 700, 96px, cream (#F5E6D3), centered
  Below it: "Không pha trộn. Không vội vàng." — Be Vietnam Pro 400, 28px, cream, letter-spacing 0.08em
  Hold 2s.

Scene 3 (5–9s): Cut to close-up of coffee beans slowly falling — slow motion feel
  Kinetic type: word "ARABICA" fades in character by character (typewriter, 50ms/char), top-left
  Gold accent line (#C9A84C, 2px) wipes left-to-right under the word. Hold 1s.

Scene 4 (9–13s): Split to black. Logo appears at center (fade-in, 600ms ease-out)
  Tagline below: "Cà Phê Bản Địa" — tracked-out, letter-spacing 0.15em, 22px
  Hold 2s.

Scene 5 (13–15s): Fade to black. URL or handle fades in: @brandname — 18px, cream

ANIMATION STYLE:
All transitions: dissolve (400ms). No hard cuts except Scene 3 → Scene 4.
Text entries: slide-up (30px travel, 400ms ease-out). No bounce.
No zoom animations — static compositions only.

AUDIO CONTEXT:
Background: ambient coffee shop, low volume. No music beat sync needed.

CONSTRAINTS:
Safe zone: 120px top (status bar area), 200px bottom (Instagram UI overlap).
All text within safe zone. No text smaller than 22px. Contrast ratio minimum 4.5:1.
Export: MP4, H.264, 1080x1920px.
```

---

---

## 1. Deck — Fintech Pitch Deck

**❌ Before (vague):**
```
Làm pitch deck đẹp cho startup fintech, 
khoảng 10-12 slides, trông chuyên nghiệp.
```

**✅ After (precise):**
```
Create a 12-slide pitch deck for a B2B fintech startup targeting Series A VCs.

VISUAL DIRECTION:
Dark, authoritative. Navy base (#0A1628), electric blue accent (#2D7DD2),
white text (#FFFFFF). No stock photos — abstract geometric shapes only.
Inter font throughout: 700 weight for headlines, 400 for body.

SLIDE STRUCTURE:
1. Cover — company logo (centered) + one-line value prop below
2. Problem — 3 pain points, each with a stat. Icon left, text right.
3. Solution — product UI mockup placeholder (full bleed right half) + 3 bullets left
4. Market Size — TAM/SAM/SOM nested donut chart, labeled with $ values
5. Business Model — 3-column card layout (Freemium / Pro / Enterprise)
6. Traction — revenue growth bar chart (last 6 months) + 2 key metrics
7. Competition — 2x2 matrix, company positioned top-right
8. Team — headshot grid (4 people), name + title + 1-line bio each
9. Roadmap — horizontal timeline, 4 milestones, Q format
10. Ask — funding amount (large display type) + use-of-funds horizontal bar
11. Appendix placeholder
12. Thank you — logo + contact + tagline

CONSTRAINTS:
16:9 ratio. Consistent navy (#0A1628) header bar every slide (60px height).
Slide number bottom-right in small caps. Ready to export as PDF.
```

---

## 2. Landing Page — SaaS Product

**❌ Before (vague):**
```
Làm landing page cho tool quản lý task, trông như startup Silicon Valley.
```

**✅ After (precise):**
```
Create a landing page for a B2B task management SaaS targeting small engineering teams.

VISUAL DIRECTION:
Light mode. Off-white background (#F9FAFB), dark text (#111827),
purple accent (#7C3AED). Sans-serif dominant: Inter throughout.
Flat UI — no drop shadows on components, use border instead.

SECTIONS (top to bottom):
1. Navigation — logo left, 4 links center, "Start free" CTA button right
2. Hero — headline (2 lines max), subheadline (1 line), two buttons (primary + ghost),
   product screenshot below the fold at 80% width, slight drop shadow
3. Social proof — logo strip: "Trusted by teams at [6 company logos]"
4. Features — 3-column bento grid, each cell: icon + title + 2-line description
5. How it works — 3-step horizontal flow with numbered steps and illustrations
6. Pricing — 3-column card layout (Free / Pro / Team), highlighted card = Pro
7. CTA banner — full-width purple (#7C3AED), white headline, one button
8. Footer — 4-column links + copyright

ABOVE THE FOLD:
Headline: "Ship faster. Stay aligned." (Inter 700, 64px)
Subheadline: "Task management built for engineering teams." (Inter 400, 20px, #6B7280)
CTA: "Start for free" (purple fill) + "See how it works" (ghost button)

CONSTRAINTS:
Max width 1280px. Mobile responsive. No animations — static layout only.
```

---

## 3. Prototype — Mobile Onboarding Flow

**❌ Before (vague):**
```
Làm prototype app mobile cho onboarding user mới, trông đẹp và đơn giản.
```

**✅ After (precise):**
```
Create a mobile app prototype for a 4-screen onboarding flow (iOS style).

PLATFORM: Mobile, 390x844px (iPhone 14 base), iOS design conventions.

SCREEN FLOW:
Screen 1 (Welcome) → tap "Get started" → Screen 2
Screen 2 (Name input) → tap "Continue" → Screen 3
Screen 3 (Goal selection) → select 1 of 3 options → tap "Next" → Screen 4
Screen 4 (Setup complete) → tap "Enter app" → exits onboarding

VISUAL DIRECTION:
White background (#FFFFFF), dark text (#1C1C1E), green accent (#34C759).
SF Pro Display font (or Inter as fallback). Progress bar at top of screens 2–4.

COMPONENT BEHAVIOR:
- "Continue" button: disabled (gray #C7C7CC) until input is filled, active (green) when filled
- Goal selection: each option is a card; tap highlights with green border + checkmark
- Screen 4: animated checkmark icon (CSS animation, 0.4s ease-in) on load

CONSTRAINTS:
Safe area: 44px top (status bar), 34px bottom (home indicator).
Tap targets minimum 44x44px. No gesture navigation — buttons only.
```

---

## 4. Social Asset — Coffee Brand Facebook Post

**❌ Before (vague):**
```
Làm ảnh Facebook post về cà phê, nhìn ấm áp và nghệ.
```

**✅ After (precise):**
```
Create a Facebook post visual for a Vietnamese specialty coffee brand.

FORMAT: 1:1 ratio, 1080x1080px.

VISUAL DIRECTION:
Overhead flat-lay composition — ceramic cup on dark wooden surface,
soft morning light from top-left corner. Film grain texture overlay (subtle).
Warm palette: deep espresso brown (#2C1810), cream (#F5E6D3), muted gold (#C9A84C).

COPY ON VISUAL:
Headline (top-center, 8% from top edge): "Sáng nào cũng vậy."
Font: Playfair Display 700, 72px, cream (#F5E6D3)
Subtext (bottom-center, 8% from bottom edge): "Cà phê rang mộc — không pha trộn."
Font: Be Vietnam Pro 400, 28px, cream (#F5E6D3), letter-spacing 0.05em

MOOD: intimate, slow, analog — không commercial, không happy stock photo.

CONSTRAINTS:
80px safe zone all sides. Text contrast ratio minimum 4.5:1 against background.
No logo placement (organic post, not ad). PNG export.
```

---

## 5. Illustration — Vietnamese Rice Field

**❌ Before (vague):**
```
Vẽ cánh đồng Việt Nam dạng cartoonic.
```

**✅ After (precise):**
```
Create a flat cartoonic illustration of a Vietnamese rice field at golden hour.

STYLE:
Flat illustration — bold outlines (3px, #1A1A1A), no gradients, solid fills only.
Inspired by Studio Ghibli color sensitivity but simplified to flat shapes.
No texture, no grain — clean vector aesthetic.

COMPOSITION:
Foreground: rice stalks in dense rows, bright lime green, slight height variation
Midground: flooded paddy field reflecting sky, pale blue still water
Far midground: simple wooden farmhouse with thatched roof, partially obscured
Background: rolling hills in 2 shades, simple village silhouette
Sky: golden hour gradient — amber to pale pink at horizon (simulate with 2 flat bands)
3 rounded cumulus clouds, white with light gray underside

COLOR PALETTE:
Rice stalks: #7AB648 (light), #5A9E2F (shadow)
Water reflection: #A8D8EA, #87C1D4
Sky: #FFB347 (lower), #FF8C69 (upper)
Hills: #4A7C59 (near), #2D5A3D (far)
Outline: #1A1A1A

MOOD: nostalgic, warm, peaceful — evokes late afternoon in the Mekong Delta.

CANVAS: 1920x1080px, SVG preferred, PNG fallback.
```

---

## 6. Collateral — Annual Report

**❌ Before (vague):**
```
Làm annual report cho công ty, khoảng 8 trang, trông corporate nhưng không nhàm.
```

**✅ After (precise):**
```
Create an 8-page annual report for a mid-size Vietnamese tech company (digital PDF format).

VISUAL DIRECTION:
Dark editorial — deep navy (#0D1B2A) page backgrounds for section openers,
white (#FFFFFF) for content pages. Accent: electric teal (#00BFA6).
Typography: Sora 700 for headlines, Sora 400 for body, 16px base size.

PAGE STRUCTURE:
Page 1 (Cover): Full-bleed navy. Company name top-left. Year "2024" as oversized
  display type (300px, 10% opacity watermark). Tagline bottom-left.
Page 2 (Letter from CEO): Two-column. Left: headshot + signature. Right: letter body.
  Pull quote in teal, Sora 700, 28px, centered.
Page 3 (Highlights): 4-cell bento grid. Each cell: large number (metric) + descriptor.
  Navy background, teal numbers (#00BFA6), white labels.
Page 4–5 (Business Review): Single column, editorial grid. Large section headers.
  Inline charts (bar/line) at 60% column width.
Page 6 (Financials): Table layout. Revenue, profit, key ratios. Teal row highlights
  for YoY growth rows.
Page 7 (Team): Photo grid (6 people, 3-column). Name + title below each.
Page 8 (Back Cover): Navy full-bleed. Logo centered. Website + contact footer.

CONSTRAINTS:
A4 format (210x297mm). Margins: 20mm all sides. Digital PDF — screen colors (RGB).
No bleed required. Font embed in export.
```
