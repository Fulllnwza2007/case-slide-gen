# Analysis Body Styling Rules

Use these rules when a slide is primarily about:

- `market-trend`
- `market-gap`
- `competitive-landscape`
- `problem-frame`
- `capability-gap`
- `benchmarking`

These rules control the look of the body, not the shell.

## Purpose

Analysis slides should feel:

- argument-led
- evidence-first
- sharp
- intentional

They should not feel like:

- a flat card dashboard
- a generic infographic
- a decorative market poster

## Body Composition Pattern

Prefer one of these compositions when the source supports them:

- three-mass analysis page
  - left mass: market context, segment context, or comparison frame
  - center mass: hero proof, usually the strongest chart or gap visual
  - right mass: barrier stack, insight stack, or synthesized diagnosis
- proof-led split page
  - dominant proof block on one side
  - compact supporting comparison or diagnosis blocks on the other
- distributed diagnosis page
  - several equal-weight cards only when the page truly has no single dominant proof

Do not default to equal cards if the source contains one obvious proof anchor.

## Proof Mode First

Before choosing a grammar for an analysis page, identify the page's proof mode:

- `stat-led`
- `table-led`
- `chart-led`
- `diagnosis-board-led`

Do not assume all analysis pages should become `left context / center chart / right insight`.

Examples:

- `stat-led`
  - a market trend page anchored by 2-4 large headline stats
- `table-led`
  - a competitor or criteria page anchored by a comparison table or score grid
- `chart-led`
  - a market gap page anchored by one dominant trend or comparison chart
- `diagnosis-board-led`
  - a strengths/constraints or issue-cluster page without one chart strong enough to dominate

If the page is the final analysis slide before recommendation, also apply:

- [analysis-terminal-bridge-rules.md](analysis-terminal-bridge-rules.md)

## Color Discipline

Use a restrained consulting palette with role-based color:

- dark navy or deep blue for structural blocks, proof framing, and key labels
- green only for emphasis, advantage, unlock, or highlighted opportunity
- warm neutral or light gray for quiet surfaces and secondary cards
- keep strong color concentrated in the hero proof and a few emphasis cues

Do not turn the whole page into a dark board unless the proof really needs that weight.

## Surface Design

Analysis pages should look crisp and evidence-led:

- context cards should look quiet and informative
- proof blocks should feel more grounded and more visually resolved than support cards
- insight stacks should feel executive, not decorative
- diagnosis cards may use one stronger state for the most important barrier or gap

Avoid:

- glossy billboard proof panels
- identical styling across every block
- decorative chart containers that overpower the data itself

## Visual Rhythm

Analysis pages should read as:

1. context
2. proof
3. synthesis

or:

1. claim
2. evidence
3. implication

The page should not force the user to discover the main proof by scanning every card equally.

## Proof Block Rules

When a slide includes percentages, trends, or comparisons:

- use a chart or structured visual proof when the metric is mainly about gap, trend, or comparison
- use metric cards or typographic proof when the value is a single supporting fact
- let one proof block dominate when the page's argument hinges on one chart, one gap, or one quantified claim

Do not convert every percentage into a chart. Convert only the ones that carry comparison, trend, or gap logic.

### `table-led` compression rules

When the selected proof mode is `table-led`:

- let the table or criteria grid carry the proof
- limit the comparison to the minimum dimensions needed to make the choice legible
- prefer 3-5 proof rows and 3-4 meaningful comparison columns
- use short labels, ticks, markers, short phrases, or score states instead of sentence-length cells
- keep supporting notes outside the table very compact

Avoid:

- paragraph-like cells
- turning every comparison dimension into a full sentence
- adding a second major proof block that competes with the table

### `diagnosis-board-led` compression rules

When the selected proof mode is `diagnosis-board-led`:

- use one clear core diagnosis anchor
- use 3-4 supporting diagnosis clusters only
- give each cluster a short title and one short evidence fragment or one sharp clause
- let one cluster carry the strongest emphasis when one issue is clearly most important
- keep the board structured and scannable before it becomes explanatory

Avoid:

- mini paragraphs inside each diagnosis card
- equal-length explanatory text across every cluster
- turning the board into a text wall with decorative boxes

## Context and Insight Rules

For left-side context or frame blocks:

- keep them compact
- use them to orient the user before the proof
- prefer 2-3 strong cards over many small facts

For right-side insights or diagnosis blocks:

- use a clean stack or controlled column
- synthesize what the proof means
- keep language sharper than the context cards
- do not let the insight stack visually overpower the proof block

## Terminal Analysis Bridge Rules

When an analysis page is the last analysis slide before recommendation:

- make the page more directional than a normal analysis page
- reduce non-essential support material
- reserve one explicit bridge block that converts the diagnosis into strategic direction
- let that bridge block feel stronger than a quiet summary strip but weaker than the hero proof
- avoid ending the page on neutral evidence alone

This page should answer:

- what the analysis now makes unavoidable
- what kind of recommendation must logically follow

## Summary Strip Rules

When an analysis page uses a summary strip:

- keep it extremely short
- use it to close the argument, not to add another layer of detail
- keep it quieter than the proof and quieter than the insight stack

## Prompt Translation Notes

When converting these rules into prompts:

- ask for a dominant proof block when the page has one clear chart or quantified gap
- ask for a three-mass layout when the source supports context + proof + synthesis
- ask for restrained context cards and a sharper right-side insight stack
- ask for evidence-led surfaces rather than generic dashboard cards

## Anti-Patterns

Avoid:

- turning every analysis page into the same left-cards / center-chart / right-cards template without reason
- making the proof block too small to lead the page
- giving context, proof, and synthesis equal weight when they should not be equal
- using color as decoration instead of argument emphasis
- turning the summary strip into another explanatory paragraph
