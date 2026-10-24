# Skill: Design Prompt Writer

**Role:** Receive the brief from design-discovery → write a complete, structured prompt for Claude Design.

---

## Reference Files (always read before writing)

- `references/output-types.md` — template structure per output type
- `references/vocabulary.md` — replace vague words with precise design language
- `references/prompt-examples.md` — learn what a good prompt looks like

---

## Writing Rules

**Never use:**
- "đẹp", "hiện đại", "chuyên nghiệp", "sáng tạo", "ấm áp và nghệ", "clean", "nice"
- Any descriptor that cannot be directly rendered by a design tool

**Always include:**
- HEX color codes (no "dark blue" without "#0A1628")
- Specific font names (no "sans-serif font" without "Inter" or "Be Vietnam Pro")
- Layout instructions (grid, sections, hierarchy)
- Hard constraints (ratio, canvas size, safe zone, export format)

---

## How to Use Brand Context

### If `brand_loaded: true`

**Tier 1 — always apply if the field is populated:**

| Field | Where to apply |
|---|---|
| `colors.primary/accent/background/text` | Use exact HEX everywhere — never substitute |
| `colors.secondary` | Supporting elements, backgrounds |
| `typography.heading/body` | Enforce exactly — never suggest alternatives |
| `tone` | Sets overall voice of VISUAL DIRECTION |
| `voice_dos` | Apply to copy direction in CONTENT section |
| `voice_donts` | Add to CONSTRAINTS as copy rules |
| `mission` + `tagline` | Use in CONTENT when copy is needed |
| `imagery_style` | Enforce in VISUAL DIRECTION and CONTENT |
| `never_do` | Every item → hard constraint in CONSTRAINTS |
| `platform_priority` | Informs default ratio and safe zone |
| `language` | Affects copy language and font choice |
| `brand_personality` | Translate adjectives → visual language using vocabulary.md |
| `reference_brands` | Use as STYLE REFERENCE |
| `avoid_brands` | Add to CONSTRAINTS: "Must not resemble: [brand]" |

**Tier 2 — apply only if the field is populated, skip if empty:**

| Field | Where to apply |
|---|---|
| `colors.rgb` | Screen-accurate specs in digital outputs |
| `colors.cmyk` | CONSTRAINTS for print outputs |
| `colors.pantone` | CONSTRAINTS for physical branding |
| `colors.semantic` | UI states in prototype/landing_page |
| `colors.dark_mode` | Apply if output is dark-mode context |
| `colors.gradient` | VISUAL DIRECTION if output benefits from it |
| `vocabulary.preferred` | Use in copy within CONTENT |
| `vocabulary.avoid` | Add to CONSTRAINTS as copy restrictions |
| `typography.display` | Hero headlines in deck/landing_page |
| `typography.caption` | Labels, footnotes, small UI text |
| `typography.scale` | Enforce size values exactly |
| `logo.min_size` | CONSTRAINTS when logo appears |
| `photography.*` | Enforce in VISUAL DIRECTION for photo-based outputs |
| `brand_pattern` | VISUAL DIRECTION as background/supporting element |
| `data_viz_style` | CONTENT for any chart/graph output |
| `layout.grid` | Apply to landing_page/prototype/collateral |
| `layout.border_radius` | All card/button/UI elements |
| `layout.shadow` | Elevated components |
| `motion_principles` | CONSTRAINTS for prototype and motion_graphic |
| `accessibility.min_contrast_ratio` | CONSTRAINTS |
| `print_specs` | CONSTRAINTS for collateral/deck print outputs |

### Partial Brand (some Tier 1 fields populated, others empty)

- Use whatever is populated — enforce those fields strictly
- For missing colors: suggest based on existing brand colors (complementary or neutral), prefix with "Suggested:"
- For missing fonts: suggest based on `tone` and `brand_personality`, prefix with "Suggested:"
- Never leave color or font fields blank in the output — always provide a specific HEX or font name

### If `[NO_BRAND]`

- Suggest full palette based on inferred tone + industry, prefix with "Suggested palette:"
- Suggest fonts based on output type and mood
- All suggestions must still be specific — HEX codes and font names, never descriptions

---

## Prompt Template

```
Create a [OUTPUT TYPE] for [PURPOSE/AUDIENCE].

BRAND:
[Brand name]
Colors: primary [HEX], accent [HEX], background [HEX], text [HEX]
[Secondary colors if relevant]
Typography: [heading font] (headings), [body font] (body)[, display font if populated]
Tone: [tone from brand context]
Personality: [brand_personality adjectives translated to visual language via vocabulary.md]

VISUAL DIRECTION:
[Mood and aesthetic — derived from tone + personality, no vague words]
[Color application — which color for what element]
[Imagery treatment — enforce imagery_style]
[Texture, effects, or treatment if relevant]

LAYOUT & COMPOSITION:
[Grid or layout type — use vocabulary.md terms]
[Section structure or hierarchy]
[Border radius, shadow if Tier 2 available]
[Key visual elements and their positions]

CONTENT:
[Text content — write actual copy when possible, in correct language]
[Data or charts — specify type and description]
[Images or illustrations — describe exactly, enforce imagery_style]

ANIMATION: ← include only for motion_graphic or prototype
[Scene or frame sequence]
[Transition types and timing]
[Text animation style]
[Export format: MP4 / GIF / HTML]

STYLE REFERENCE:
[reference_brands from brand context, or a well-known comparable brand]
[What specifically to borrow — not just a name]
[What to avoid]

CONSTRAINTS:
[Canvas size and ratio]
[Safe zones]
[Export format]
[never_do items — each as a hard rule]
[avoid_brands: "Must not resemble: X"]
[Accessibility: min contrast ratio]
[Print specs if applicable]
[Motion rules if prototype or motion_graphic]
```

---

## Section Rules

- **BRAND:** Omit only if truly no brand exists and none was provided — rare
- **ANIMATION:** Include only for `motion_graphic` and `prototype` output types
- **STYLE REFERENCE:** Always include something specific — brand reference or a named comparable
- **CONTENT:** Write actual headline copy when possible; never write "headline goes here"
- **CONSTRAINTS:** Never omit — minimum: canvas size + export format + any never_do rules

---

## Output

Produce the final prompt as a clean code block. No explanation after.

If an assumption was made (e.g. defaulted to 1:1 ratio, or suggested a color), state it in one line before the prompt block.
