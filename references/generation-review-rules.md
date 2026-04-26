# Generation Review Rules

Use these rules after a slide image has been generated.

The purpose of review is not to restate the plan. It is to judge whether the rendered image still obeys the shell, the body blueprint, and the intended consulting-slide quality.

## Review Levels

Review at two levels:

- `slide-level`
- `deck-level`

## Slide-Level Checks

For each slide, check these categories in order:

### 1. Shell Compliance

Check whether the slide still uses the fixed shell:

- the canvas is exact `16:9` widescreen
- the image reads as a full-slide presentation layout rather than a poster crop, square board, or portrait card
- fixed-height headline zone exists
- one short row-1 section/title line exists
- one dominant row-2 takeaway line exists
- one short row-3 supporting subdetail line exists
- no vertical left accent bar appears
- row hierarchy is preserved, with row 1 subordinate, row 2 dominant, and row 3 supportive
- divider treatment is visible
- divider sits directly below the headline zone
- body begins below the divider and does not creep upward into the headline area
- bottom flow strip remains at the bottom
- bottom flow keeps a thin top rule, centered section labels, one short active marker above the active label, and a far-right brand mark
- shell has not drifted into side rails, top tabs, pills, boxed footer navigation, or poster composition

### 2. Body Blueprint Fit

Check whether the rendered body still matches the blueprint:

- hero block is clearly visible
- support blocks are present
- reading order remains intact
- chosen visual devices are recognizable
- required emphasis is preserved
- optional persona or segment cue, when present in the blueprint, is visible but does not overpower the main journey or pain argument
- right-side insight synthesis, when present in the blueprint, is visible enough to sharpen the page rather than disappearing into generic support cards
- summary strip, when present in the blueprint, reads as one concise synthesis layer rather than another explanatory block

### 3. Visual Hierarchy

Check whether the page has the intended dominance:

- `hero` pages have one clear dominant block
- `split` pages keep the two major bodies balanced
- `distributed` pages do not accidentally invent a false hero

### 4. Consulting Slide Quality

Check whether the slide still feels like a polished competition slide:

- structured and argument-led
- not plain
- not poster-like
- not infographic clutter
- not overdecorated
- not visually dead
- headline proportion still feels stable and deck-like rather than ad hoc
- customer-analysis pages use color and surface hierarchy intentionally rather than flattening into equally styled cards
- analysis pages preserve a clear proof hierarchy rather than flattening context, proof, and synthesis into one generic card system
- analysis pages keep the strongest proof block visibly dominant when the source contains one
- summary strips stay restrained and do not outshout the hero or main proof area
- table-led analysis pages do not become text-heavy matrices with sentence-length cells
- diagnosis-board-led pages remain scannable and do not collapse into paragraph-heavy card boards
- final analysis slides feel directional enough to hand off into recommendation rather than ending as neutral observation
- final analysis slides include a clear strategic bridge layer when the page is meant to close the analysis section
- implementation pages keep their dominant execution logic clear: timeline, gate, or governance
- implementation pages do not collapse into generic gantt overload or unrelated equal cards
- roadmap-led implementation pages make the named phase overview readable before the user studies lane detail
- roadmap-led implementation pages make year or phase anchors clearly visible
- roadmap-led implementation pages make row labels legible enough to identify execution tracks quickly
- roadmap-led implementation pages keep primary rollout bars stronger than secondary actions
- lower support bands on implementation pages, when present, stay clearly separated and subordinate
- implementation pages do not invent governance, ownership, dependency, or risk bands unless the blueprint actually calls for them

### 5. Copy Behavior

Check whether text behavior is structurally acceptable:

- text zones exist where expected
- labels are compact
- tables or metrics remain believable
- the image does not collapse into unreadable dense text
- summary-strip text, when present, stays concise and does not expand into multiple explanatory lines
- table cells, when present, stay short enough to compare visually
- diagnosis cards, when present, stay short enough to scan visually
- bridge statements, when present on terminal analysis slides, stay concise and directional rather than turning into a paragraph
- workstream, gate, and owner labels on implementation pages stay short enough to scan at slide distance
- lane text on implementation pages stays phrase-length rather than sentence-length
- year and phase markers on implementation pages are readable enough to organize the page at a glance

Perfect text fidelity is not required at this stage, but structural readability is.

## Deck-Level Checks

After slide-level review, check the deck family:

- shell consistency across non-cover slides
- bottom flow family consistency
- shared consulting visual language
- no wild drift into unrelated styles
- active marker style stays the same across the deck
- footer labels remain centered and typographic across the deck

## Rating System

Use these ratings per category:

- `pass`
- `borderline`
- `fail`

Use overall slide outcomes:

- `accept`
- `revise`
- `regenerate`

## Escalation Rules

Use:

- `accept`
  - when shell, body fit, and consulting feel are all solid
- `revise`
  - when the structure is mostly right but one or two categories drift
- `regenerate`
  - when shell breaks, aspect ratio breaks, body grammar collapses, or the visual style is wrong

## Required Output

Each reviewed slide should produce:

- `slide_number`
- `shell_compliance`
- `body_fit`
- `visual_hierarchy`
- `consulting_quality`
- `copy_behavior`
- `overall_outcome`
- `revision_notes`

Deck review should produce:

- `shell_family_consistency`
- `flow_family_consistency`
- `visual_family_consistency`
- `overall_deck_outcome`
- `deck_notes`
