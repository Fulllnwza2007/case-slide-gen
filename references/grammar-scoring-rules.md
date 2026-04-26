# Grammar Scoring Rules

Use these scoring rules after retrieval and before final body decision.

This stage does not replace judgment. It creates a consistent shortlist order so grammar choice is not arbitrary.

## Purpose

Score each retrieved grammar against the target slide using the same four core signals:

- `content class fit`
- `decision type fit`
- `data shape fit`
- `visual device fit`

Then apply one adjustment signal:

- `dominance fit`

## Weighting

Use this weighting by default unless the user explicitly asks for a different bias.

- `content class fit`: 40
- `decision type fit`: 20
- `data shape fit`: 20
- `visual device fit`: 15
- `dominance fit`: 5

Total possible score: `100`

## How to Score

### 1. Content Class Fit: 40

Score high when the grammar's `fits_classes` overlaps strongly with the slide's `content_classes`.

- `40`: primary class fits directly
- `25-35`: strong partial overlap
- `10-20`: weak overlap
- `0`: no meaningful overlap

If any slide class appears in the grammar's `not_for`, the grammar should usually be filtered out before scoring.

### 2. Decision Type Fit: 20

Score based on overlap between slide `decision_types` and grammar `common_decision_types`.

- `20`: clear match
- `10-15`: partial match
- `0-5`: poor match

### 3. Data Shape Fit: 20

Score based on overlap between slide `data_shapes` and grammar `common_data_shapes`.

- `20`: clear shape match
- `10-15`: usable but imperfect
- `0-5`: poor fit

### 4. Visual Device Fit: 15

Score based on whether the shortlisted or chosen devices are supported by `allowed_visual_devices`.

- `15`: all major devices fit
- `8-12`: most fit
- `1-7`: only one minor device fits
- `0`: grammar cannot accommodate the selected devices

### 5. Dominance Fit: 5

Use this only as an adjustment layer.

- `5`: dominance clearly fits the key message
- `2-4`: acceptable
- `0-1`: message structure fights the grammar

## Feasibility Gate

Before final choice, check whether the slide can satisfy the grammar's `required_blocks`.

If the required blocks cannot be satisfied, reject the grammar even if its weighted score is high.

## Tie-Break Rules

If two grammars score similarly:

1. prefer the grammar with better `content class fit`
2. then prefer better `required-block feasibility`
3. then prefer simpler device usage over more forced device combinations

## Required Output

Record a per-candidate score breakdown for each shortlisted grammar:

- `candidate_id`
- `content_class_score`
- `decision_type_score`
- `data_shape_score`
- `visual_device_score`
- `dominance_score`
- `total_score`
- `feasibility`
- `notes`

This score breakdown belongs inside the `grammar_selection` object.
