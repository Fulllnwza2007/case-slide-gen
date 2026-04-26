# Case Slide Gen

This skill is designed for use in Codex.

Case Slide Gen is a Codex skill for turning business, strategy, finance, and case-competition content into consulting-style slide images.

Generate consulting-style case competition slide images from structured content using a fixed shell and adaptive body logic.

## Installation

Clone this repository and copy it into your Codex skills directory.

```bash
git clone https://github.com/Fulllnwza2007/case-slide-gen.git
cp -R case-slide-gen ~/.codex/skills/Case-Slide-Gen
```

Then restart Codex so it reloads the skill metadata.

## Quick Start

Use this prompt:

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

Typical flow:

1. The skill analyzes the source and plans the deck.
2. It builds prompts for every slide.
3. You review the full prompt set.
4. You approve generation.
5. It generates the slide images.

## Why I Built This

After seeing the capabilities of GPT Image 2, I felt it had enough potential to generate slides directly.

That made me think about a recurring problem I face in case competitions: the hard part is not only analyzing the problem and developing the right solution, but also turning that thinking into a presentation that is structured well, visually strong, and easy to read.

That is why I built Case Slide Gen for ChatGPT and Codex: a skill designed to help turn case-competition thinking into presentation-ready slide images.

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

Notes:

- Use `adaptive` unless you have a hard slide limit.
- `Theme` is optional.
- If slides feel too sparse, keep the `Prefer` line.

## Repository Structure

- `SKILL.md`
  - main skill instructions
- `agents/openai.yaml`
  - display name and default prompt
- `scripts/`
  - helper scripts for rebuilding portable indexes and creating slide-memory from your own local corpus
- `references/`
  - workflow, schemas, styling rules, and examples
- `references/memory-bank/layout-grammars/`
  - curated body layout families
- `references/memory-bank/layout-variants/`
  - curated composition variants
- `references/memory-bank/visual-devices/`
  - reusable visual device definitions
- `references/memory-bank/index/`
  - portable public indexes for grammars, variants, and visual devices
- `references/contracts/`
  - machine-readable prompt and decision schemas

## Bundled Public Memory Bank

This package already includes:

- curated layout grammars
- curated layout variants
- curated visual devices
- portable public indexes for those components

That means the public repo carries the reusable layout brain, not just documentation.

## Optional: Improve Performance With Your Own Local Corpus

If you want stronger retrieval on your own machine, you can build local slide-memory entries from your own structured source files.

1. Prepare a local folder of `.txt` or `.md` content files.
2. Set `TRAINING_ROOT` to that folder.
3. Run:

```bash
python3 scripts/build_slide_memory.py
python3 scripts/rebuild_indexes.py
```

This lets you keep the public skill package while improving local retrieval quality with your own content.

## Important Notes

- Generated content may not be fully accurate. Always review the logic, numbers, and conclusions before using the slides in a real presentation.
- Text, icons, charts, or small visual details may occasionally render imperfectly or appear distorted.
- Layout balance, spacing, and proportions may vary from slide to slide, especially when the source content differs in structure or density.
- Output quality depends heavily on the quality and clarity of the input content.
- This skill is best used as an acceleration tool, not as a final source of truth. Human review is still required.

## Public Package Notes

This public package is intentionally curated.

It excludes:

- local absolute paths
- private training paths
- raw reference decks
- generated slide-memory dumps
- machine-specific retrieval indexes

The included memory-bank files are the reusable public-facing definitions and portable indexes, not a private training dataset export.
