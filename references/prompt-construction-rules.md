# Prompt Construction Rules

Use these rules after the `body blueprint` is complete.

The goal is to turn the fixed shell and adaptive body into one image-generation prompt that is specific, readable, and not overconstrained.

## Prompt Structure

Build each prompt in this order:

1. slide type and overall intent
2. fixed shell instructions
3. body layout instructions from the blueprint
4. visual device instructions
5. content and copy behavior
6. optional theme instruction
7. visual style and polish
8. negative instructions

## Shell Rules

The shell must always be described before the body.

For non-cover slides, the prompt should establish:

- an exact `16:9` widescreen presentation slide canvas
- full-slide landscape framing from edge to edge
- a fixed-height top headline zone
- one short row-1 section/title line only
- one dominant row-2 takeaway line only
- one short row-3 supporting subdetail line only
- no vertical left accent bar
- row 1 remains compact and subordinate
- row 2 remains dominant but contained within the fixed headline zone
- row 3 remains compact and supportive beneath row 2
- one divider directly below the headline zone
- a consistent divider treatment
- a slim bottom flow strip in the same family across the deck
- a thin top rule across the flow area
- centered section labels on one horizontal line
- one short, thick active marker above the current section label
- a far-right brand mark at the edge of the flow area

Do not let the prompt invent alternate shell treatments.
Do not let the prompt reinterpret the bottom flow as pills, tabs, banners, or boxed footer navigation.
Do not let the prompt add extra headline rows, let body content creep upward into the headline zone, or solve overflow by shrinking the shell structure.
Do not let the prompt drift into square, poster, portrait, cropped, or floating-card framing.

## Body Rules

The body section of the prompt should come from the blueprint, not from topic words alone.

The prompt must describe:

- the hero block
- the support blocks
- the reading order
- the chosen visual devices
- what must stay prominent

For customer-focused pages:

- if the blueprint includes a persona or segment cue, describe it as a compact context cue
- keep the cue supportive, not dominant, unless the slide is explicitly persona-led
- use it to frame whose journey or pain matters, not to replace the journey or pain argument
- if the blueprint includes multiple insights, describe them as a clean right-side insight stack or column
- if one friction is the dominant pain, explicitly ask for one elevated friction state rather than several equally loud cards

When the blueprint includes a summary strip:

- describe it as one concise page takeaway
- keep it visually quieter than the hero and major proof blocks
- place it at the lower edge or outer edge as a closing synthesis layer
- keep it to one short sentence or one short headline-plus-clause
- use it to summarize the implication of the page, not to add new evidence

Do not describe the slide as a generic template.

## Copy Rules

The prompt should guide text behavior without requiring perfect text rendering.

Prefer instructions like:

- short consulting-style headline
- short row-1 section label
- rewritten-short row-2 takeaway when needed
- short row-3 supporting subdetail
- compact metric labels
- short callout titles
- concise table text
- one concise summary-strip takeaway only

Do not ask the model to render long exact paragraphs.

## Style Rules

The visual direction should stay within the consulting competition style:

- clean business slide
- structured hierarchy
- high visual polish
- restrained decorative noise
- strong focal logic

Use style language that supports the chosen grammar, not random art direction.

If the user specifies a theme:

- describe it as a deck-level color and surface direction, not a new shell system
- keep shell structure unchanged
- keep role-based color logic intact
- use the theme to steer accent hue, card surface mood, and emphasis treatment
- do not let theme override block hierarchy or turn the page into branding-heavy art direction

Good theme wording should sound like:

- `Use a navy-and-green consulting theme with restrained green emphasis`
- `Use a charcoal-and-gold executive theme with warm neutral support surfaces`
- `Use a cool blue logistics theme with muted teal emphasis and light industrial neutrals`

Avoid theme wording that is too vague or too decorative.

For customer-analysis pages, add body styling cues like:

- role-based color use with navy for structure and green for emphasis
- clean persona panel, not decorative character poster
- one highlighted friction state, not equal emphasis everywhere
- clear left/center/right rhythm when the source supports persona + journey + insight structure

For analysis pages, add body styling cues like:

- one dominant proof block when the page revolves around a clear gap, trend, or comparison
- quiet context cards that orient the user without stealing dominance
- a sharper right-side insight or diagnosis stack when the source contains synthesized implications
- restrained color with navy for structure, green only for emphasis, and quiet neutral surfaces for context
- evidence-led surfaces rather than decorative dashboard panels
- for `table-led` analysis pages, ask for a compact comparison table or score grid with short labels, short phrases, ticks, or simple markers rather than text-heavy cells
- for `diagnosis-board-led` analysis pages, ask for one core diagnosis anchor plus 3-4 short diagnosis clusters with terse evidence fragments, not explanatory paragraphs

For implementation pages, add body styling cues like:

- for `timeline-led` pages, ask for a clean phased rollout with compact workstream lanes and visible milestones
- for `decision-gate-led` pages, ask for visible checkpoints or evaluation gates that shape how scaling proceeds
- for `governance-led` pages, ask for an execution control anchor with clear owner or dependency structure and only a lighter sequencing rail
- make the named phase overview the first thing the user understands on the page
- keep labels terse and execution-led, not paragraph-heavy
- make the page feel executable and controlled, not like a generic gantt board
- make year or phase anchors large and immediately readable
- make left-side initiative labels clear before the user reads small task text
- use darker, stronger primary rollout bars and lighter secondary sub-action bars
- keep lane text to short action phrases, not explanatory clauses
- do not add governance, ownership, dependency, or risk bands by default on implementation pages
- if support context such as risks, enablers, or dependencies is truly required, place it in a clearly separated lower band

For terminal analysis pages, add body styling cues like:

- the page should feel like the last analytical step before recommendation
- include one explicit bridge block or bridge strip that turns evidence into strategic direction
- make the bridge statement concise, directional, and unavoidable rather than neutral
- keep the bridge visually stronger than a quiet summary strip but weaker than the hero proof
- reduce non-essential support clutter so the page lands decisively

For summary strips on any page:

- keep the strip narrow, restrained, and synthesis-led
- avoid heavy banners, oversized pills, or dense explanatory blocks
- let the hero or proof area stay visually dominant

## Negative Rules

Each prompt should explicitly avoid:

- non-16:9 canvas
- poster crop
- square composition
- portrait card composition
- floating isolated board on a larger background
- poster-like composition
- infographic overload
- floating unstructured elements
- alternate shell placements
- decorative illustration
- equal visual weight across all body blocks when one block should dominate
- generic flat dashboard composition on analysis pages when the source supports a stronger proof hierarchy
- sentence-length comparison-table cells
- paragraph-length diagnosis cards
- paragraph-length workstream descriptions
- lane bars carrying long sentence-like task text
- gantt-like overload with unreadable tiny labels
- weak year markers that fail to organize the roadmap
- phase overview weaker than the lane detail
- equal visual weight between primary rollout bars and secondary action bars
- default ownership, dependency, or risk bands on implementation pages when the source does not require them
- support bands that compete with the roadmap for dominance
- neutral ending on the final analysis slide
- a final analysis page that stops at observation without pointing toward the recommendation

## Output Expectation

Each slide should produce a machine-readable `prompt package` with:

- `slide_number`
- `prompt_intent`
- `shell_block`
- `body_block`
- `theme_block`
- `style_block`
- `negative_block`
- `final_prompt`

After prompt packages are built for the whole deck:

- present the complete set to the user before any image generation
- keep prompts grouped by slide number and section
- wait for explicit approval before generating all slide images
- if the user requests edits, revise prompts first and re-present the full set
