# Variant Selection Logic

This stage sits after grammar selection and before body blueprinting.

Its job is to choose the best composition variant within the chosen layout family.

## Purpose

Variant selection answers:

- which composition pattern inside the chosen grammar best fits this slide
- why this slide should use this variant instead of another variant from the same family
- how to avoid template repetition across different slides that share one grammar

## Inputs

Use:

- `content_classes`
- `decision_types`
- `data_shapes`
- `analysis_proof_mode` when relevant
- `analysis_terminal_role` when relevant
- `implementation_mode` when relevant
- chosen `layout_family`
- shortlisted `visual_devices`
- intended `key_message`
- the canonical `layout variant` entries for that family

## Selection Order

Apply the logic in this order:

1. Start from the already chosen `layout_family`.
2. Open all variants whose `parent_grammar` matches that family.
3. Prefer variants whose `best_for_classes` overlaps most with the slide's classes.
4. Prefer variants whose `best_for_data_shapes` overlaps most with the slide's data shape.
5. Prefer variants whose `common_device_mix` matches the shortlisted devices.
6. Prefer the variant whose `hero_position` and `support_structure` best fit the message:
   - use left-anchored hero when one proof block should lead and supporting proof can sit to the side
   - use top-anchored hero when the slide should read top-down before it reads side-to-side
   - use three-mass compositions when the slide needs a left context, central proof, and right synthesis rhythm
   - use executive-summary board variants when the page must combine the challenge, recommendation moves, and impact proof on one page
   - prefer `question-banner_solution-triplet_impact-strip` when the executive page is organized around one core question and three named moves
   - prefer `issue-question_strategy-impact_board` when the executive page must restate issues or the case question before presenting the answer
   - prefer `context-panel_strategy-triplet_metric-right` when the executive page needs a visible context block before the recommendation board
   - for analysis-heavy pages:
     - `stat-led`: prefer variants that elevate numeric anchors without fabricating a hero chart
     - `table-led`: prefer variants that leave enough width and hierarchy for a comparison table or criteria grid to carry the proof
     - `chart-led`: prefer variants with one strong proof zone and quieter support masses
     - `diagnosis-board-led`: prefer variants with balanced structured clusters rather than a center-chart template
   - for terminal analysis pages:
     - prefer variants that visibly reserve room for one directional bridge layer
     - prefer variants with one core anchor over evenly weighted clusters
     - if `analysis_terminal_role` is `bridge-to-recommendation`, prefer `board-led_cluster-with-core-anchor` inside `distributed-card-grid`
   - for implementation-heavy pages:
     - `timeline-led`: prefer variants with a dominant phase overview and compact workstream support beneath it
     - `decision-gate-led`: prefer variants that keep the phase overview dominant while still reserving clear room for checkpoints or evaluation points between phases
     - `governance-led`: prefer variants that make ownership, dependencies, or execution control visible rather than forcing a pure horizontal roadmap
     - prefer `phase-overview_dominant-lanes-below` inside `roadmap-with-phase-lanes` for classical phased rollout pages where one source-derived phase overview should be the first thing the user sees
     - prefer `phase-overview_with_gate-transitions` inside `roadmap-with-phase-lanes` when checkpoints or evaluation points matter but should still support the phase story
     - use `timeline-led_rollout-with-lanes` only when the page truly needs a more uniform lane-led timeline treatment
     - use `roadmap_with_decision-gates` only when the gate logic itself must be unusually prominent
     - prefer `control-tower_board_with_dependency-strip` inside `execution-board-with-control-points` when owners, dependencies, or control structure are the real proof of execution quality
7. Reject variants that would flatten the page back into the same composition used for a different content shape.

## Non-Negotiables

- Do not choose a variant just because it is visually familiar.
- Do not let the same grammar collapse into one default composition every time.
- Do not choose a variant whose support structure fights the slide's message.
- Do not force a persona-heavy variant when the slide lacks persona evidence.
- Do not force a centered hero when the slide needs strong left-to-right argument flow.
- Do not force a chart-centered variant when the selected analysis proof mode is not `chart-led`.
- Do not use a neutral or purely descriptive variant for the final analysis slide when it must hand off into recommendation.

## Required Output

Record:

- `retrieved_variants`
- `chosen_variant_id`
- `variant_fit_notes`
- `variant_reject_reasons`

This output belongs inside the `grammar_selection` object and must be carried into the body blueprint.
