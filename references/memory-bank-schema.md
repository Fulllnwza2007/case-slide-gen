# Memory Bank Schema

The memory bank stores three different kinds of canonical JSON entries:

1. `reference slides`
2. `layout grammars`
3. `visual devices`
4. `layout variants`

Do not collapse them into one record type.

## Meanings

- `content classes`
  - what the slide is about
  - example: `pricing-strategy`, `customer-journey`, `risk-mitigation`

- `visual devices`
  - the body-level visual tools used to tell the story
  - example: `bar-chart`, `line-chart`, `phase-lanes`, `journey-path`, `risk-matrix`, `comparison-table`

- `layout family`
  - how those devices are arranged on the page
  - example: `hero-metric-with-supporting-scorecards`, `top-journey-bottom-pain-cards`

- `layout variant`
  - the composition pattern inside one layout family
  - example: `hero-left_support-right_proof-bottom`, `persona-left_journey-center_insights-right`

## Canonical JSON Files

- `references/memory-bank/slide-memory/*.json`
  - one entry per reference slide
- `references/memory-bank/layout-grammars/*.json`
  - one entry per reusable body grammar
- `references/memory-bank/visual-devices/*.json`
  - one entry per controlled visual device
- `references/memory-bank/layout-variants/*.json`
  - one entry per reusable composition variant under a parent grammar

## Index Files

Indexes are derived JSONL tables used for shortlist retrieval.

- `index/slide-memory-index.jsonl`
- `index/layout-grammar-index.jsonl`
- `index/visual-device-index.jsonl`
- `index/layout-variant-index.jsonl`

Each index record must point back to its canonical entry path.

## Required Fields by Entry Type

### Reference Slide

Every slide-memory entry must contain:

- `slide_id`
- `source_deck`
- `source_file`
- `page`
- `image_path`
- `content_classes`
- `decision_types`
- `data_shapes`
- `visual_devices`
- `layout_family`
- `dominance_structure`
- `body_goal`
- `body_structure`
- `when_to_use`
- `avoid_when`
- `why_it_works`
- `adaptation_notes`

The `body_structure` field must include:

- `hero_block`
- `support_blocks`
- `reading_order`

### Layout Grammar

Every layout grammar entry must contain:

- `grammar_id`
- `fits_classes`
- `not_for`
- `dominance_structure`
- `required_blocks`
- `allowed_visual_devices`
- `reading_order`
- `usage_notes`

### Visual Device

Every visual device entry must contain:

- `device_id`
- `device_type`
- `description`
- `best_for_classes`
- `best_for_data_shapes`
- `typical_role`
- `notes`

The recommended device vocabulary should cover at least:

- chart devices
  - `bar-chart`
  - `stacked-bar-chart`
  - `line-chart`
  - `area-chart`
  - `waterfall-chart`
  - `scatter-plot`
  - `heatmap`
- table devices
  - `comparison-table`
  - `prioritization-table`
  - `financial-summary-table`
  - `risk-mitigation-table`
- card devices
  - `metric-cards`
  - `initiative-cards`
  - `pain-point-cards`
  - `persona-cards`
  - `callout-card`
- flow and sequence devices
  - `timeline`
  - `phase-lanes`
  - `journey-path`
  - `process-flow`
  - `decision-tree`
  - `funnel`
- matrix and map devices
  - `risk-matrix`
  - `prioritization-matrix`
  - `ecosystem-map`
  - `stakeholder-map`

### Layout Variant

Every layout variant entry must contain:

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

Executive-summary pages should not be forced into ordinary strategy or impact families when the reference clearly behaves like a synthesis board. In those cases, use the dedicated `executive-synthesis-board` grammar and select one of its variants.

## Retrieval Contract

Retrieval is a two-step process.

### Step 1: Shortlist from Indexes

Use these fields first:

- `content_classes`
- `decision_types`
- `data_shapes`
- `density_hint` when available

This step returns:

- top slide-memory candidates
- top layout-grammar candidates
- top visual-device candidates
- top layout-variant candidates once one grammar family has been selected

### Step 2: Open Canonical Entries

After shortlisting, inspect the underlying JSON entries to decide:

- which slide reference is primary
- whether a secondary reference should be borrowed
- which visual devices fit this slide
- which layout grammar should drive the body
- which layout variant should prevent the chosen grammar from collapsing into one repeated composition

The shell is never part of retrieval.

## Downstream Contracts

After retrieval, the system should create two more machine-readable artifacts:

1. `grammar selection`
   - the shortlisted grammars
   - the filtered grammars
   - the chosen layout family
   - the retrieved variants for that family
   - the chosen variant
   - the chosen dominance structure
   - the device fit notes
   - the reject reasons

1. `body decision`
   - the chosen references, devices, grammar selection, and reject reasons
2. `body blueprint`
   - the concrete body plan that the prompt builder will use

Do not jump from retrieval metadata straight into image prompts.
