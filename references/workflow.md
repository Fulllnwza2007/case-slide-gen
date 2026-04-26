# Workflow

## Stage 1: Normalize Content

Turn the source into content blocks:

- problem
- context
- evidence
- metrics
- recommendations
- implementation items
- risks
- appendix candidates

Do not over-focus on the original source format. Use the content itself.

## Stage 2: Build the Deck-Level Section Spine

Before creating individual slides, map the content into a deck-level section spine.

Use:

- [deck-narrative-sequencing-rules.md](deck-narrative-sequencing-rules.md)

Default section order:

1. `Executive Summary`
2. `Analysis`
3. `Last Analysis`
4. `Overview Strategy`
5. `Strategy`
6. `Implementation`
7. `Impact`
8. `Risk & Mitigation`

This stage should decide:

- which sections are present
- which sections are merged or omitted
- which section is likely largest
- which slide will be the last analysis bridge

Do not assign fixed slide counts yet.

## Stage 3: Plan the Slides Inside the Spine

Create a slide plan with:

- slide number
- section
- slide purpose
- key message
- supporting evidence

This is the story layer, not the visual layer.

Allocate slide count adaptively inside the section spine, not before it.

## Stage 4: Classify Each Slide

For each slide, decide:

- `content classes`
- `decision type`
- `data shape`
- whether it is the final analysis slide before recommendation

These three fields explain what the slide is trying to do.

## Stage 5: Retrieve Body Precedents

Use the memory bank to find the best body precedents for the slide.

Retrieve based on:

- content classes
- decision type
- data shape
- density need

Return top candidates, not one forced answer.

Use this order:

1. shortlist from `slide-memory-index.jsonl`
2. shortlist from `layout-grammar-index.jsonl`
3. shortlist from `visual-device-index.jsonl`
4. shortlist from `layout-variant-index.jsonl` after a grammar family has been chosen
5. open the shortlisted canonical JSON entries

## Stage 6: Choose Body Construction

Choose:

- analysis proof mode when the slide is analysis-heavy
- terminal analysis bridge role when the slide is the last analysis page before recommendation
- primary reference
- optional secondary reference
- visual devices
- grammar selection
- layout variant selection

This is the real body decision.

At the end of this stage, the system should be able to explain:

- why this body choice fits the content classes
- why the chosen grammar fits the decision type
- why the chosen visual devices fit the data shape

This stage must produce a machine-readable `body decision` object, not just prose notes.

Before finalizing the body decision:

1. for analysis-heavy pages, choose an `analysis_proof_mode` first:
   - `stat-led`
   - `table-led`
   - `chart-led`
   - `diagnosis-board-led`
2. if the slide is the final analysis page before recommendation, set `analysis_terminal_role` to `bridge-to-recommendation`
3. shortlist layout grammars
4. filter grammars that conflict with `not_for`
5. score the remaining grammars using:
   - content class fit
   - decision type fit
   - data shape fit
   - visual device fit
   - dominance fit
6. apply a feasibility gate based on required blocks
7. select one grammar and record reject reasons for the nearby alternatives
8. within that grammar family, select one variant and record why nearby variants are being rejected

## Stage 7: Build Body Blueprint

Define:

- hero block
- support blocks
- reading order
- visual devices used
- what must stay prominent

This stage should produce a machine-readable body blueprint, not prose only.

Build the blueprint in this order:

1. inherit the chosen `layout_family`
2. inherit the chosen `layout_variant`
3. define one `hero_block`
4. define the minimum `support_blocks`
5. assign each chosen device to a target block
6. define `reading_order`
7. define `must_remain_prominent`
8. define `copy_slots`

## Stage 8: Apply Fixed Shell

Lock:

- headline family
- headline proportion
- detail-line family
- divider family
- bottom flow family

The shell must remain consistent across non-cover slides.
Use the shell family defined in [shell-spec.md](shell-spec.md), especially the fixed-height three-row headline zone with no left accent bar, and the slim bottom flow with centered section labels, one short active marker above the active label, and a far-right brand mark.

## Stage 9: Build Prompt

Build one prompt per slide from:

- shell instructions
- body blueprint
- chosen references
- language mode
- density mode
- optional theme instruction

The prompt should be assembled in blocks:

1. `prompt_intent`
2. `shell_block`
3. `body_block`
4. `theme_block`
5. `style_block`
6. `negative_block`
7. `final_prompt`

The shell block must explicitly restate that the output is an exact `16:9` widescreen presentation slide, not a poster or square composition.

## Stage 10: Present Prompt Package for Approval

Before generating any images, present the full prompt package for all slides to the user.

This stage must:

- show the prompt set for every slide in the deck
- preserve slide numbers and section labels
- make it easy to inspect prompt wording slide by slide
- stop and wait for explicit approval before generation

Do not generate partial slides by default once the approval checkpoint is reached.
Do not silently continue into image generation after prompt construction.

If the user asks for changes, revise the prompt packages first, then present the updated full set again.

## Stage 11: Generate Images

Generate slide images only after explicit approval of the complete prompt set.

## Stage 12: Review

Two levels:

- slide-level body fit
- deck-level shell consistency

At slide level, review:

- shell compliance
- body fit
- visual hierarchy
- consulting quality
- copy behavior

At deck level, review:

- shell family consistency
- flow family consistency
- visual family consistency
