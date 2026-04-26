# Visual Devices

This folder is the controlled vocabulary for `body-level visual tools`.

Use visual devices to answer:

- what visual tool should tell this message
- what role that tool should play in the body
- which classes and data shapes it usually supports

Do not confuse visual devices with:

- `content classes`
  - what the slide is about
- `layout grammars`
  - how the body is arranged

## Recommended Device Groups

### Charts

- `bar-chart`
- `stacked-bar-chart`
- `line-chart`
- `area-chart`
- `waterfall-chart`
- `scatter-plot`
- `heatmap`

### Tables

- `comparison-table`
- `prioritization-table`
- `financial-summary-table`
- `risk-mitigation-table`

### Cards

- `metric-cards`
- `initiative-cards`
- `pain-point-cards`
- `persona-cards`
- `callout-card`

### Flow / Sequence

- `timeline`
- `phase-lanes`
- `journey-path`
- `process-flow`
- `decision-tree`
- `funnel`

### Matrix / Maps

- `risk-matrix`
- `prioritization-matrix`
- `ecosystem-map`
- `stakeholder-map`

## Usage Rules

- A slide can use more than one visual device.
- One device should usually be the dominant device.
- Choose devices from the content class and data shape, not from topic words alone.
- Avoid generic device labels when a more specific one exists.
- Treat bubble-style positioning visuals as part of the `scatter-plot` family until the training set shows a strong reason to split them.
- The shell is fixed and is not part of the visual device vocabulary.

## File Format

Each device lives in one JSON file and should follow `schema.json`.

Each file should describe:

- what the device is
- what classes it is best for
- what data shapes it is best for
- what role it usually plays
- when not to use it
- practical notes for adaptation
