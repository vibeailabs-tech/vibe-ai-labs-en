# Design Vocabulary Library

Replace vague words with precise, renderable design language.

---

## Vague Word Replacements

| Vague | Replace with |
|---|---|
| đẹp / beautiful / nice | high-contrast, editorial, refined, considered |
| hiện đại / modern | flat, minimal, geometric, sans-serif dominant |
| chuyên nghiệp / professional | structured grid, consistent spacing, muted palette |
| sáng tạo / creative | unexpected layout, pattern interrupt, asymmetric |
| sang trọng / luxury | dark background, gold/cream accent, serif headline, generous white space |
| trẻ trung / youthful | vibrant, rounded corners, playful type, bright accent, high energy |
| ấm áp / warm | warm tone palette (amber, terracotta, cream), soft light treatment |
| tối giản / minimal | max 3 colors, single typeface, heavy negative space |
| năng động / dynamic | diagonal elements, bold weight contrast, saturated accent |
| tin cậy / trustworthy | blue-dominant palette, structured grid, no decorative elements |
| độc đáo / unique | unexpected crop, off-grid element, rule-breaking type hierarchy |
| cao cấp / premium | tight letter-spacing (0.08–0.12em), generous padding, minimal color count |
| vui vẻ / fun | high-saturation palette, rounded sans-serif, irregular grid, overlapping elements |
| nghệ thuật / artistic | mixed type scales, hand-drawn texture, asymmetric whitespace |

---

## Layout Vocabulary

- `bento layout` — uneven grid of cells, each cell highlights one feature; cells vary in size
- `editorial grid` — multi-column, text and image interleaved, large typographic anchors
- `hero section` — full-width banner, single headline dominant, minimal competing elements
- `card grid` — uniform items in cards with consistent shadow/border radius
- `sticky sidebar` — sidebar fixed on scroll, main content scrolls alongside
- `split screen` — left text / right visual, 50/50 or 60/40 split
- `masonry grid` — variable-height cards, Pinterest-style
- `full-bleed` — content or image extends to canvas edge, no margin
- `floating card` — content in elevated card with shadow, isolated from background
- `data-forward` — numbers/metrics are the visual hero, decoration minimal

---

## Visual Style Vocabulary

- `glassmorphism` — semi-transparent surface, frosted blur background, thin border (1px rgba white)
- `neumorphism` — soft extruded/inset shadows, monochromatic, tactile feel
- `brutalist` — raw aesthetic, thick borders, stark black/white contrast, no decoration
- `editorial` — magazine-style, large asymmetric typography, high white space, black anchors
- `cartoonic` — flat illustration, bold outline (2-4px), saturated color, rounded shapes
- `data-forward` — charts/numbers as hero visual, minimal decoration, structured grid
- `dark mode` — dark background (#0D0D0D–#1E1E2E range), light text, accent for CTAs
- `organic` — soft rounded shapes, natural color palette, hand-drawn texture feel
- `geometric` — sharp angles, mathematical grids, abstract shape composition
- `film grain` — texture overlay, analog photography feel, slightly desaturated
- `aurora` — soft gradient blobs in cool hues (purple, teal, indigo), blurred to 80–120px, on dark base
- `Y2K` — chrome text, iridescent surface, pixel elements, bright saturated palette (#FF00FF, #00FFFF, #FFFF00)
- `claymorphism` — 3D-looking soft clay shapes, pastel fills, thick soft drop shadow, no sharp edges
- `layered depth` — multiple overlapping elements at different opacities, creates sense of z-depth without true 3D
- `typographic poster` — type IS the layout; headline fills 70%+ of canvas, minimal imagery
- `Swiss/International` — grid-strict, Helvetica or Neue Haas, red/black/white, mathematical whitespace

---

## Typography Vocabulary

- `display` — headline-only font, decorative or high-personality, never used at small sizes
- `sans-serif dominant` — geometric sans (Inter, DM Sans, Plus Jakarta Sans) as primary voice
- `serif accent` — serif for headings only (Playfair Display, Lora), body stays sans
- `monospace` — code/data aesthetic, technical feel (JetBrains Mono, Space Mono)
- `variable font` — weight shifts responsively with viewport; creates motion feel in static
- `oversized type` — headline at 80–120px+, typography as layout element not just copy
- `tight leading` — line-height 1.0–1.1, compressed stacking, editorial density
- `tracked out` — letter-spacing 0.15–0.25em; spacious, premium, label-style
- `weight contrast` — pair Ultra Bold (900) headline with Regular (400) body for hierarchy punch
- `mixed script` — Latin + Vietnamese diacritics in same line; choose a font that handles both well (Be Vietnam Pro, Lexend)
- `stacked type` — words arranged vertically, each on its own line; poster or cover format

---

## Color Tone Vocabulary

- `muted palette` — desaturated, all colors <40% saturation; cohesive, understated
- `high contrast` — background/foreground delta >7:1; bold, legible, graphic
- `tonal palette` — single hue in 4-6 shades; calm, sophisticated
- `accent pop` — neutral base + one saturated accent color used sparingly (<15% of canvas)
- `earth tones` — terracotta, warm brown, dusty green, cream; organic, grounded
- `neon accent` — dark background + single fluorescent accent; tech, energy, nightlife
- `pastel` — low saturation, high lightness; soft, approachable, feminine
- `duotone` — entire image rendered in 2 colors (e.g., deep navy + electric yellow); graphic, punchy
- `monochrome` — single hue at varying lightness/opacity; cohesive, photography-friendly
- `split complementary` — one base hue + two colors adjacent to its complement; vibrant but balanced
- `Vietnamese street palette` — terracotta (#C1440E), electric blue (#1B4FD8), gold (#D4A017), off-white (#F5F0E8)

---

## Animation Vocabulary (for motion_graphic)

- `fade-in` — element appears from 0% to 100% opacity; 300–600ms ease-out
- `slide-up` — element enters from 20–40px below target position; 400ms ease-out
- `scale-pop` — element scales from 80% to 100%, slight overshoot to 105% then settles; 300ms
- `typewriter` — text characters appear one by one; 30–60ms per character
- `kinetic type` — words or letters animate individually on beat; energetic, music-video feel
- `wipe reveal` — content revealed by a moving mask (left-to-right or top-to-bottom)
- `loop` — animation cycles seamlessly; specify loop point explicitly
- `stagger` — multiple elements animate in sequence with 80–150ms delay between each
- `hold` — element stays static on screen; specify hold duration explicitly (e.g., "hold 2s")
- `cut` — instant transition, no blend; punchy, editorial
- `dissolve` — cross-fade between scenes; 400–600ms overlap

---

## Common Vietnamese Context Phrases → Precise Output

| User says | Prompt should say |
|---|---|
| "nhìn như agency lớn" | editorial grid, oversized display type, monochrome base with single accent |
| "như app nước ngoài" | iOS-style sans-serif dominant, 8pt grid system, flat color fills, SF Pro or Inter |
| "giống Behance" | dark background showcase, project cover layout, large image-first |
| "kiểu Sài Gòn trendy" | high contrast, Vietnamese street palette (terracotta + electric blue), mixed Latin + Vietnamese type |
| "minimalist Nhật" | max 3 colors, generous white space, single weight typeface, no drop shadows, centered composition |
| "nhìn như startup Y Combinator" | white bg (#FFFFFF), orange accent (#FF6600), Inter 700 headline, clean card grid |
| "kiểu luxury Hàn" | black (#0A0A0A) and off-white (#F5F0E8), tracked-out serif headline, full-bleed imagery |
| "như TikTok viral" | bold text overlay (white, 700 weight, 60–80px), high-saturation bg, kinetic type animation |
| "trông như tạp chí" | editorial grid, oversized type at 120px+, black and white dominant, 1 accent color max |
| "giống Notion / Linear" | light mode, Inter, 8px border-radius, subtle shadow, monochrome with single accent |
| "phong cách retro / vintage" | film grain overlay, warm muted palette, serif or slab-serif, distressed texture, aged paper bg |
