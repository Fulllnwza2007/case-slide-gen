---
name: Case Slide Gen
description: "Generate consulting competition slide images from PDF, docs, notes, or raw text using a fixed shell and an adaptive body. Use when the task is to turn business, marketing, or finance case content into slide-by-slide image prompts by classifying each slide, retrieving suitable body references from a memory bank, choosing visual devices and layout, then generating actual slide images."
---

# Case Slide Gen

Use this skill when the user wants a new slide-image workflow built around:

- fixed shell
- adaptive body
- memory-bank-driven body selection
- slide classes, visual devices, and layout families

This skill is format-agnostic. The source can be:

- PDF
- docs
- notes
- transcript
- raw pasted content

Do not anchor the workflow to PDF pages unless the source is actually a PDF. Think in content blocks and slide messages first.

## Read First

1. Read [references/input-contract.md](references/input-contract.md).
2. Read [references/workflow.md](references/workflow.md).
3. Read [references/deck-narrative-sequencing-rules.md](references/deck-narrative-sequencing-rules.md) when planning section order and adaptive slide allocation.
4. Read [references/shell-spec.md](references/shell-spec.md).
5. Read [references/taxonomy-v2.md](references/taxonomy-v2.md).
6. Read [references/memory-bank-schema.md](references/memory-bank-schema.md) when deciding how classes, visual devices, and layouts should be stored or retrieved.
7. Read [references/analysis-proof-modes.md](references/analysis-proof-modes.md) when the slide is market-, competitor-, diagnosis-, or other analysis-led.
8. Read [references/layout-variant-schema.md](references/layout-variant-schema.md) when deciding how a grammar family should split into reusable composition variants.
9. Read [references/grammar-selection-logic.md](references/grammar-selection-logic.md) when choosing a layout grammar from retrieved candidates.
10. Read [references/variant-selection-logic.md](references/variant-selection-logic.md) when choosing a composition variant inside the selected grammar.
11. Read [references/grammar-scoring-rules.md](references/grammar-scoring-rules.md) when comparing nearby grammar candidates.
12. Read [references/body-decision-schema.md](references/body-decision-schema.md) when choosing references, devices, grammar selection, and variant selection.
13. Read [references/body-decision-examples.md](references/body-decision-examples.md) for concrete examples of strong decisions.
14. Read [references/body-blueprint-schema.md](references/body-blueprint-schema.md) when converting that choice into a machine-readable body plan.
15. Read [references/body-blueprint-construction-rules.md](references/body-blueprint-construction-rules.md) when building the body plan.
16. Read [references/body-blueprint-examples.md](references/body-blueprint-examples.md) for concrete blueprint patterns.
17. Read [references/customer-analysis-body-styling-rules.md](references/customer-analysis-body-styling-rules.md) when the slide is customer-, persona-, or journey-led.
18. Read [references/analysis-body-styling-rules.md](references/analysis-body-styling-rules.md) when the slide is market-, competitor-, diagnosis-, or other analysis-led.
19. Read [references/analysis-terminal-bridge-rules.md](references/analysis-terminal-bridge-rules.md) when the slide is the final analysis page before recommendation.
20. Read [references/implementation-modes.md](references/implementation-modes.md) when the slide is implementation-, rollout-, or governance-led.
21. Read [references/implementation-body-styling-rules.md](references/implementation-body-styling-rules.md) when the slide is implementation-, rollout-, or governance-led.
22. Read [references/prompt-construction-rules.md](references/prompt-construction-rules.md) when assembling image prompts.
23. Read [references/prompt-package-examples.md](references/prompt-package-examples.md) for prompt package examples.

## Core Model

Treat the slide as two separate layers:

- `shell`
  - fixed across the deck
  - headline
  - detail line
  - divider treatment
  - bottom flow

- `body`
  - adaptive per slide
  - chosen from slide class + visual device + layout family
  - guided by memory bank precedents

The shell is not retrieved from the memory bank.
The body is.

Non-cover slide outputs must always be exact `16:9` widescreen presentation slides.

## Workflow

1. Normalize the input source into usable content blocks.
2. Build the deck-level section spine and adaptive section allocation.
3. Build a slide-by-slide deck plan inside that section spine.
4. For each slide, classify:
   - `content classes`
   - `decision type`
   - `data shape`
5. Retrieve suitable body precedents from the memory bank.
6. Choose:
   - analysis proof mode when relevant
   - terminal bridge role when the slide is the last analysis page before recommendation
   - implementation mode when relevant
   - primary body reference
   - optional secondary reference
   - visual devices
   - grammar selection
   - layout variant selection
   - explicit reject reasons for nearby alternatives
7. Build a body blueprint for each slide.
8. Apply the fixed shell to every non-cover slide.
9. Build one image-generation prompt per slide, including an optional theme instruction when the user has specified one.
10. Present the complete prompt set to the user for approval.
11. Generate actual slide images only after explicit user confirmation.
12. Review:
   - shell consistency across the deck
   - body fit for each slide

Before finalizing review notes:

1. Read [references/generation-review-rules.md](references/generation-review-rules.md).
2. Read [references/generation-review-examples.md](references/generation-review-examples.md).

## Non-Negotiables

- Do not let memory-bank retrieval change the shell.
- Do not choose layout directly from topic words alone.
- Do not treat `class`, `visual device`, and `layout` as the same thing.
- Do not use a single reference deck as the global template for the whole presentation unless the user explicitly asks for it.

## Output

Return:

1. assumptions
2. deck plan
3. per-slide class summary
4. per-slide body choices
5. image prompts for every slide
6. a prompt approval checkpoint before generation
7. generated slide images after approval
8. review notes

For each slide, include:

- slide number
- section
- key message
- content classes
- decision type
- data shape
- chosen visual devices
- chosen layout family
- body reference choice
- shell mode

If the user has not yet approved generation, stop after returning the full prompt set and ask whether to proceed with generating all slide images.
