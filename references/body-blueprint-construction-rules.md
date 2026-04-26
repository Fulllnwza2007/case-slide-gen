# Body Blueprint Construction Rules

Use these rules after `body decision` and before prompt building.

The purpose of the body blueprint is to turn a chosen grammar into a slide-specific body plan.

## Purpose

The blueprint must answer:

- what is the hero block on this slide
- what are the support blocks
- which visual devices go into which blocks
- what must stay visually dominant
- where the main copy slots should live

## Construction Order

Build the blueprint in this order:

1. start from the chosen `layout_family`
2. inherit the chosen `layout_variant`
3. inherit its `dominance_structure`
4. define one `hero_block`
5. define the minimum `support_blocks` needed to complete the message
6. assign each chosen `visual_device` to a target block
7. define the `reading_order`
8. define `must_remain_prominent`
9. define the `copy_slots`

## Block Rules

### Hero Block

The hero block should carry the page's main proof or main structural anchor.

Typical hero block types:

- hero KPI
- hero chart
- journey path
- ecosystem map
- risk matrix
- phase roadmap
- pillar pair

There should only be one hero block.

### Support Blocks

Support blocks should widen or clarify the argument without stealing dominance.

Typical support block roles:

- supporting metrics
- rationale cards
- pain-point cards
- summary strip
- compact proof table
- owner or milestone strip

Support blocks should be specific enough that the prompt builder can place content intentionally.

For analysis-focused slides:

- if the slide is `market-trend`, `market-gap`, `competitive-landscape`, `problem-frame`, `capability-gap`, or `benchmarking`, prefer one dominant proof block when the source contains one clear quantified gap, trend, or comparison
- if the source supports a three-mass logic, use a compact left context block or context card cluster, one dominant center or side proof block, and a right-side insight or diagnosis stack
- keep context cards quieter than proof blocks
- keep the insight or diagnosis stack sharper than the context cards, but still subordinate to the hero proof
- if several barriers or failure points exist, allow one most-important diagnosis card to carry a stronger emphasis state than the others
- use a distributed card grid only when no single proof block should dominate the page
- if `analysis_proof_mode` is `table-led`, keep the proof table compact:
  - use only the minimum comparison dimensions needed
  - prefer short row labels, short column labels, ticks, symbols, or short phrases
  - avoid sentence-length cell text
- if `analysis_proof_mode` is `diagnosis-board-led`, keep diagnosis clusters compressed:
  - one short cluster title
  - one short evidence line or one sharp clause
  - no paragraph-length support text inside diagnosis cards
- if the slide is the final analysis page before recommendation, add one explicit `bridge` support block:
  - it should convert the proof into one directional implication
  - it should not introduce new evidence
  - it should be stronger than a quiet summary strip but still subordinate to the hero proof
  - it should use one short directional takeaway only

For customer-focused slides:

- if the slide is `customer-journey` or `customer-pain` and the source includes clear segment or persona evidence, add one compact persona or segment cue as a support block
- the cue should usually sit near the start of the reading path or adjacent to the journey context
- the cue must not replace the journey hero unless the slide is explicitly persona-led
- keep the cue concise: role, need-state, or one-line profile, not a full biography
- if the source contains several synthesized customer insights, prefer a right-side insight stack or insight column as an additional support block
- when several friction points exist, allow one most-critical friction card to carry a stronger emphasis state than the others

For implementation-focused slides:

- if `implementation_mode` is `timeline-led`, let the phase progression stay dominant and keep workstream labels compact
- if `implementation_mode` is `decision-gate-led`, make checkpoints or evaluation points visibly scannable and avoid burying them inside tiny milestone markers
- if `implementation_mode` is `governance-led`, allow one execution control anchor plus owner/dependency structure to dominate more than elapsed time
- do not overload implementation pages with every task from the source; keep only the execution structure needed to make the page legible
- for roadmap-led implementation pages, explicitly reserve blueprint space for:
  - dominant named phase overview before detailed execution text
  - readable year or phase anchors
  - strong left-side initiative labels
  - dominant primary rollout bars
  - lighter secondary sub-action bars
- keep lane text to short action phrases only
- do not add ownership, dependency, risk, or enabler blocks by default
- only add a separate lower support band when the source truly requires extra execution context that cannot be omitted or moved to another slide

### Summary Strip Rules

When a slide needs one bottom or edge synthesis block, treat it as a summary strip, not as a second argument block.

Use a summary strip only when it helps close the page with one concise takeaway.

The summary strip should:

- restate the meaning of the page, not introduce new analysis
- contain one short takeaway sentence or one headline plus one short clause only
- stay visually subordinate to the hero block and main proof area
- use quieter surface treatment than the hero and major support blocks
- sit at the edge of the body, usually lower or outer, without competing for dominance

Do not turn the summary strip into:

- a multi-point explanation area
- a second insight stack
- a dense callout with several clauses
- a dark banner that competes with the main body

For terminal analysis slides, prefer a `bridge strip` or `bridge block` over a neutral summary strip when the page must pull into recommendation.

## Device Placement Rules

Each chosen device must be assigned to one target block.

Use `placement_role` like this:

- `hero`
  - the device is the main anchor of the slide
- `support`
  - the device widens the story
- `proof`
  - the device provides secondary evidence
- `bridge`
  - the device links two major blocks or helps the reading flow

Do not leave a chosen device unplaced.

## Copy Slot Rules

Copy slots are not raw text. They are placeholders for what kind of text belongs in each block.

Use only the minimum slots needed for the chosen body.

Examples:

- `hero-number`
- `hero-label`
- `support-title`
- `support-metric`
- `callout`
- `caption`
- `table-cell`
- `axis-label`
- `summary-takeaway`

Do not create many tiny copy slots unless the chosen visual device truly needs them.

## Anti-Template Rules

Even when two slides share one grammar:

- the hero block should reflect the slide's actual key message
- the support blocks should change based on the slide's content classes
- the chosen devices should match the data shape of the slide
- the copy slots should reflect the real evidence structure
- optional persona or segment cues should appear only when the source actually supports them

The blueprint should preserve the grammar family without cloning the same page.

The chosen variant should be the first defense against repetition inside one grammar family.

## Required Output

A complete blueprint must define:

- `hero_block`
- `support_blocks`
- `reading_order`
- `device_placement`
- `must_remain_prominent`
- `copy_slots`
- `reference_links`
- `layout_variant`
