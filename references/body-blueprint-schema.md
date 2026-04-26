# Body Blueprint Schema

This contract captures the machine-readable body plan that sits between:

- body decision
- prompt building

## Purpose

The `body blueprint` should tell the renderer:

- what the main block is
- what the support blocks are
- which devices belong in which blocks
- what the reading order is
- what must stay visually dominant

This is the main anti-template layer. It lets two slides share one layout grammar without becoming the same slide.

## Required Fields

- `slide_number`
- `key_message`
- `layout_family`
- `layout_variant`
- `dominance_structure`
- `hero_block`
- `support_blocks`
- `reading_order`
- `device_placement`
- `must_remain_prominent`
- `copy_slots`
- `reference_links`

## Expectations

The blueprint must be:

- specific enough to drive prompt writing
- abstract enough to adapt to different content
- traceable back to the chosen references and chosen variant

## Canonical JSON Schema

Use:

- [body-blueprint.schema.json](contracts/body-blueprint.schema.json)

Construction rules:

- [body-blueprint-construction-rules.md](body-blueprint-construction-rules.md)

Examples:

- [body-blueprint-examples.md](body-blueprint-examples.md)
