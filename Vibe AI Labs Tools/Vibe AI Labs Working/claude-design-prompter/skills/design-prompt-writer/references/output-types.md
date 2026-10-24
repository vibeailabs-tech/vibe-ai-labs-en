# Output Types Library

Seven output types Claude Design can produce. Each has specific prompt requirements.

---

## 1. `deck` — Pitch Deck / Presentation

**What Claude Design outputs:** HTML slides, exportable to PPTX/PDF

**Required prompt elements:**
- Total slide count
- Slide-by-slide structure (title + content type per slide)
- Chart types if data is present (bar, donut, line — specify)
- Ratio: always 16:9
- Consistent header/footer treatment across all slides

**Key constraint:** Each slide must work standalone — no "continued from previous slide" layouts.

**Prompt section order:** Visual Direction → Slide Structure (list each slide) → Typography → Constraints

---

## 2. `landing_page` — Landing Page / One-Pager

**What Claude Design outputs:** Live HTML/CSS/JS, deployable

**Required prompt elements:**
- Section list in order (hero, features, testimonials, CTA, footer — specify which)
- Above-the-fold content: headline, subheadline, primary CTA button text
- Interaction states: hover, active, scroll behavior
- Mobile responsiveness requirement

**Key constraint:** Above-the-fold content is the most critical section — describe it in detail first.

**Prompt section order:** Visual Direction → Section Structure → Above-the-Fold Detail → Interactions → Constraints

---

## 3. `prototype` — App / UI Prototype

**What Claude Design outputs:** Interactive HTML, clickable flows

**Required prompt elements:**
- Platform: mobile (specify iOS/Android style) or web
- Screen list and flow (Screen A → action → Screen B)
- Component behavior (modals, drawers, tabs — describe trigger and result)
- Hover/active/disabled states for interactive elements

**Key constraint:** Describe interactions explicitly — "button triggers confirmation modal" not just "confirm button".

**Prompt section order:** Platform → Screen Flow → Component Behavior → Visual Direction → Constraints

---

## 4. `social_asset` — Social Media Visual

**What Claude Design outputs:** HTML canvas → export as image

**Required prompt elements:**
- Platform: Facebook / Instagram / TikTok / LinkedIn (determines ratio)
- Ratio: 1:1 (feed), 4:5 (portrait feed), 9:16 (Stories/Reels)
- Canvas size in px: 1080x1080, 1080x1350, 1080x1920
- Safe zone: minimum 80px all sides
- Text overlay: headline and body copy, font, size, position
- Text contrast ratio: minimum 4.5:1 for accessibility

**Key constraint:** All text must be readable at mobile screen size — test mentally at 375px wide.

**Prompt section order:** Format/Ratio → Visual Direction → Copy on Visual → Mood → Constraints

---

## 5. `illustration` — Artwork / Visual

**What Claude Design outputs:** SVG or HTML canvas

**Required prompt elements:**
- Style: flat / isometric / cartoonic / editorial / geometric
- Composition: describe foreground, midground, background separately
- Color palette: every color as HEX, maximum 6 colors recommended
- Mood: one clear adjective + what it should evoke
- Intended use: hero image, icon, standalone artwork, texture

**Key constraint:** Describe composition in layers — foreground / midground / background. No "draw a scene".

**Prompt section order:** Style → Composition (by layer) → Color Palette → Mood → Canvas + Format

---

## 6. `motion_graphic` — Reel / Animated Post / Short Video

**What Claude Design outputs:** Animated HTML → export as MP4 or GIF

**Required prompt elements:**
- Platform and duration: Instagram Reel (15s / 30s / 60s), TikTok (15s / 30s / 60s), YouTube Short (60s)
- Canvas size: 1080x1920px (9:16), or 1080x1080px for square animated posts
- Scene sequence: describe each scene (Scene 1 → Scene 2 → ...) with what appears and when
- Text animation style: fade-in, slide-up, typewriter, scale-pop — be specific
- Transitions between scenes: cut / dissolve / slide / zoom — specify
- Music/beat: if content syncs to music, describe the rhythm feel (e.g., "cuts on beat, energetic")

**Key constraint:** Describe timing explicitly — "Scene 1: 0–3s", not just "intro scene". Every text and element needs an entry timing.

**Prompt section order:** Platform + Duration → Scene Sequence (with timing) → Animation Style → Audio Context → Constraints

---

## 7. `collateral` — Report / Brochure / Email Template

**What Claude Design outputs:** HTML → export to PDF

**Required prompt elements:**
- Final format: print PDF (CMYK-safe), digital PDF, or HTML email
- Page/section count
- Content hierarchy per page (what's primary, secondary, tertiary)
- Margins: specify in px or mm (print: min 15mm, digital: min 40px)
- If print: use CMYK-safe colors (avoid pure RGB neons)

**Key constraint:** Print-bound outputs need explicit margin and bleed specs. Digital PDFs need clear safe zones.

**Prompt section order:** Format → Page Structure → Content per Page → Typography → Constraints
