# Layout Variant Schema

This contract captures the reusable composition variants that sit under one parent layout grammar.

## Purpose

A `layout family` is the broad body grammar.
A `layout variant` is the concrete composition pattern that gives that grammar different page shapes.

Use variants to prevent different slides from collapsing into the same composition when they share one grammar.

## Required Fields

- `variant_id`
- `parent_grammar`
- `summary`
- `composition_pattern`
- `hero_position`
- `support_structure`
- `reading_order`
- `common_device_mix`
- `best_for_classes`
- `best_for_data_shapes`
- `when_to_use`
- `avoid_when`
- `reference_slides`

## Expectations

The variant must be:

- derived from real reference slides in `Training`
- specific enough to change body composition materially
- reusable across similar content, not tied to one topic only
- subordinate to the parent grammar, not a replacement for it

## Canonical JSON Schema

Use:

- [memory-bank/layout-variants/schema.json](memory-bank/layout-variants/schema.json)

## Index Contract

Shortlist variants through:

- [memory-bank/index/layout-variant-index.jsonl](memory-bank/index/layout-variant-index.jsonl)

Then open the canonical JSON entries to decide:

- which variant best fits the slide
- why nearby variants are being rejected
