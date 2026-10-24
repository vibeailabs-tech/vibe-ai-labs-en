# Skill: Brand Voice Loader

**Role:** Gate skill. Runs before every other skill. Reads `memory/brand-context.json` and injects brand context into the session.

---

## How to Run

1. Read `memory/brand-context.json`
2. If the file does not exist or cannot be read → treat as `brand_loaded: false`
3. Check the `brand_loaded` field
4. Output structured brand context for downstream skills

---

## Logic

**If `brand_loaded: true`:**
- Parse tier1 and tier2 fields from the JSON
- Output the brand block below — **skip any field that is empty string `""` or empty array `[]`**
- Do not ask the user anything

**If `brand_loaded: false`, file missing, or file unreadable:**
- Output flag `[NO_BRAND]`
- Check if user opened with a design request:
  - Yes → pass `[NO_BRAND]` to design-discovery; it will ask brand questions inline
  - No → run `skills/brand-onboarding/SKILL.md` to collect brand info first

---

## Structured Output Format

When `brand_loaded: true`, produce this block and pass it to all downstream skills.
**Only output fields that have actual values — omit blank strings and empty arrays entirely.**

```yaml
brand_loaded: true

# TIER 1 (output only populated fields)
name: ""
industry: ""
target_audience: ""
brand_personality: []
mission: ""
tagline: ""
reference_brands: []
avoid_brands: []
colors:
  primary: "#HEX"
  accent: "#HEX"
  background: "#HEX"
  text: "#HEX"
  secondary: []
typography:
  heading: ""
  body: ""
tone: ""
voice_dos: []
voice_donts: []
imagery_style: ""
never_do: []
platform_priority: []
language: ""
logo: ""
design_notes: ""

# TIER 2 — include this block only if at least one Tier 2 field is populated
# Output only non-empty Tier 2 fields
brand_values: []
vision: ""
vocabulary:
  preferred: []
  avoid: []
colors_extended:
  rgb: { primary: "", accent: "" }
  cmyk: { primary: "", accent: "" }
  pantone: { primary: "", accent: "" }
  semantic: { error: "", success: "", warning: "", info: "" }
  dark_mode: { background: "", surface: "", text: "" }
  gradient: ""
typography_extended:
  display: ""
  caption: ""
  scale: { h1: "", h2: "", h3: "", h4: "", body: "", caption: "" }
  weights: ""
  line_height: ""
  letter_spacing: ""
logo_extended:
  variants: []
  safe_zone: ""
  min_size: ""
  file_formats: []
  dont: []
  animated: { has_animation: false, duration: "", easing: "" }
photography:
  lighting: ""
  composition: ""
  color_grading: ""
brand_pattern: ""
data_viz_style: ""
document_templates:
  business_card: ""
  letterhead: ""
  presentation_master: ""
layout:
  grid: ""
  spacing_scale: ""
  border_radius: ""
  shadow: ""
iconography_style: ""
motion_principles: ""
accessibility:
  min_contrast_ratio: ""
  min_font_size: ""
print_specs:
  color_mode: ""
  bleed: ""
  margin: ""
```

When `brand_loaded: false`:

```yaml
brand_loaded: false
flag: [NO_BRAND]
```

---

## Updating Brand Memory

When user provides brand info at any point in the session:

1. Parse the new info — identify exactly which fields changed
2. Write **only** the changed fields to `memory/brand-context.json` — preserve all existing values in other fields
3. Set `brand_loaded: true` in the JSON if it was previously false
4. Confirm: "Brand saved. I'll use this automatically from now on."
5. Do not re-ask brand questions in this session
6. Do not restart the flow — continue from where the session left off
