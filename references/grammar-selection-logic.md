# Grammar Selection Logic

This stage sits between:

- retrieval
- body decision

Its job is to choose the body `layout grammar` for one slide from a shortlist, not to design the whole slide from scratch.

## Purpose

Grammar selection answers:

- which layout family best fits this slide
- which layout variant inside that family best fits this slide
- why that grammar fits the slide better than the nearby alternatives
- which retrieved grammars should be rejected before body blueprinting

## Inputs

The stage should use:

- `content_classes`
- `decision_types`
- `data_shapes`
- `analysis_proof_mode` when relevant
- `analysis_terminal_role` when relevant
- `implementation_mode` when relevant
- shortlisted `visual_devices`
- shortlisted `layout_grammars`
- shortlisted `layout_variants` for the chosen family
- the intended `key_message`

Do not select grammar from topic words alone.

## Selection Order

Apply the logic in this order:

1. Remove grammars that conflict with the slide's classes via `not_for`.
2. Prefer grammars whose `fits_classes` overlap most with the slide's `content_classes`.
3. Prefer grammars whose `common_decision_types` fit the slide's `decision_types`.
4. Prefer grammars whose `common_data_shapes` fit the slide's `data_shapes`.
5. Prefer grammars whose `allowed_visual_devices` can accommodate the shortlisted devices.
6. Prefer grammars whose `dominance_structure` fits the message:
   - `hero` when one proof block should clearly dominate
   - `split` when two major bodies should share the page
   - `distributed` when several points carry similar weight
7. For customer pages, if the source contains clear segment or persona evidence:
   - prefer grammars that can absorb a compact persona or segment cue
   - do not let the persona cue replace the true hero if the slide is still journey-led
   - treat persona context as a support cue unless the slide is explicitly classified as `persona` or `customer-segmentation`
8. For executive-summary pages:
   - if `executive-summary` appears together with at least one of `key-question`, `problem-frame`, `strategy-pillars`, or `impact-scorecard`, prefer `executive-synthesis-board` before defaulting to ordinary hero-metric or two-pillar grammars
   - use `hero-metric-with-supporting-scorecards` for executive pages only when one dominant KPI or proof claim should clearly lead the page
   - use `two-pillar-comparison` for executive pages only when the page is truly a balanced two-move comparison and does not need an explicit challenge frame plus impact proof on the same page
9. For analysis-heavy pages, use `analysis_proof_mode` to constrain the family:
   - `chart-led`
     - prefer grammars and variants with one dominant proof block
   - `stat-led`
     - prefer grammars and variants that can center 2-4 large numeric anchors without inventing a chart
   - `table-led`
     - prefer grammars and variants that can let a criteria table or structured comparison carry the proof
   - `diagnosis-board-led`
     - prefer grammars and variants that can support balanced evidence clusters rather than forcing a center chart
10. For final analysis pages, use `analysis_terminal_role` to constrain the family:
   - `bridge-to-recommendation`
     - prefer grammars that can host one core proof or diagnosis anchor, minimal support structure, and one explicit directional bridge block
     - reject grammars that naturally end in neutral evidence display without a clear bridge layer
11. For implementation-heavy pages, use `implementation_mode` to constrain the family:
   - `timeline-led`
     - prefer grammars that let phases and rollout sequence dominate the page
   - `decision-gate-led`
     - prefer grammars that can surface checkpoints and go / no-go transitions clearly
   - `governance-led`
     - prefer grammars that can make owners, dependencies, or control structure visible without forcing everything into one horizontal timeline
     - prefer `execution-board-with-control-points` when execution control matters more than elapsed time
12. After choosing the family, shortlist variants whose `parent_grammar` matches.
13. Prefer variants whose `best_for_classes`, `best_for_data_shapes`, and `common_device_mix` fit the slide best.
14. Prefer the variant whose `hero_position` and `support_structure` best fit the intended reading rhythm.

## Required Output

This stage must produce a machine-readable `grammar_selection` object.

That object must record:

- retrieved grammar candidates
- filtered grammar candidates
- chosen layout family
- retrieved variants
- chosen variant id
- chosen dominance structure
- device fit notes
- variant fit notes
- score breakdown per candidate
- variant reject reasons for nearby alternatives in the same family
- reject reasons for nearby alternatives

## Non-Negotiables

- Do not choose a grammar that explicitly conflicts with the slide's classes.
- Do not choose a grammar whose required blocks cannot be satisfied by the slide content.
- Do not let a rare visual device force the wrong grammar if the message structure is different.
- Do not treat one matching device as stronger than overall class and decision fit.
- Do not let `persona-cards` force a persona-led grammar when the slide's main job is to explain a journey or pain sequence.
- Do not force `chart-led` analysis composition when the proof is actually table-led, stat-led, or diagnosis-board-led.
- Do not let the last analysis slide end in a neutral grammar that fails to pull the deck into recommendation.

## Canonical JSON Schema

Use:

- [grammar-selection.schema.json](contracts/grammar-selection.schema.json)
