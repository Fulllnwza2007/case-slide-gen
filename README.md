# Case Slide Gen

Case Slide Gen is a Codex skill for turning business, strategy, finance, and case-competition content into consulting-style slide images.

It uses:

- a fixed shell across the deck
- an adaptive body per slide
- a memory-bank-driven layout workflow
- prompt review before image generation

## What It Does

Case Slide Gen analyzes source content, plans a deck narrative, classifies each slide, chooses appropriate body patterns, builds image prompts, and then generates slide images after prompt approval.

It is designed for:

- case competition decks
- strategy presentations
- business analysis decks
- implementation and impact slides
- slide-by-slide visual synthesis from structured content

## Best Inputs

Best results come from:

- `PDF`
- `DOCX`
- structured text notes

The content should already contain:

- clear sections
- key arguments
- supporting evidence
- metrics or comparisons
- implementation logic
- impact assumptions where relevant

## Recommended Usage

Use this short prompt:

```text
Use Case Slide Gen with this file: [ABSOLUTE_FILE_PATH]

Language: English
Audience: judges
Slide count: adaptive
Source strictness: close
Prefer: denser body composition and stronger supporting evidence per slide
Theme: [optional]

Build the full prompt set first, then stop and show me the prompts before generating any images.
```

Notes:

- Use `adaptive` unless you have a hard slide limit.
- `Theme` is optional.
- If slides feel too sparse, keep the `Prefer` line.

## Approval Flow

Case Slide Gen is intended to run in two steps:

1. Build the full prompt set for every slide.
2. Let the user review and approve prompts before generating images.

This keeps the deck controllable before rendering starts.

## Input Settings

- `Language`
  - Example: `English`, `Thai`, `Match source`
- `Audience`
  - Example: `judges`, `executives`, `investors`
- `Slide count`
  - Recommended: `adaptive`
- `Source strictness`
  - `close`: stay near the source
  - `balanced`: rewrite lightly when useful
  - `allow synthesis`: restructure more aggressively
- `Theme`
  - Optional color and surface direction
  - Example: `cool blue logistics theme with muted teal emphasis`

## Workflow Summary

Case Slide Gen works in this order:

1. Normalize the content.
2. Build the deck-level section spine.
3. Plan the slides inside that spine.
4. Classify each slide.
5. Retrieve body precedents from the memory bank.
6. Choose devices, grammar, and layout variant.
7. Build a body blueprint.
8. Apply the fixed shell.
9. Build the prompt set.
10. Stop for prompt approval.
11. Generate images after approval.
12. Review deck consistency.

## Repository Contents

- `SKILL.md`
  - main skill instructions
- `agents/openai.yaml`
  - display name and default prompt
- `references/`
  - workflow, schemas, styling rules, examples
- `references/memory-bank/layout-grammars/`
  - curated body layout families
- `references/memory-bank/layout-variants/`
  - curated composition variants
- `references/memory-bank/visual-devices/`
  - reusable visual device definitions
- `references/contracts/`
  - machine-readable prompt and decision schemas

## Public Package Notes

This public package is intentionally curated.

It excludes:

- local absolute paths
- private training paths
- raw reference decks
- generated slide-memory dumps
- machine-specific retrieval indexes

The included memory-bank files are the reusable public-facing definitions, not a private training dataset export.
