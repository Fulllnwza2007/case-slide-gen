# Generation Review Examples

Use these examples to understand what a review artifact should look like after a slide image is generated.

## Example 1: Slide-Level Review

```json
{
  "slide_number": 11,
  "shell_compliance": {
    "rating": "pass",
    "notes": [
      "Headline area is clearly at the top.",
      "Bottom flow strip remains at the bottom with the same thin top rule, centered labels, active top marker, and far-right brand mark as the deck family."
    ]
  },
  "body_fit": {
    "rating": "borderline",
    "notes": [
      "Hero KPI block is clear.",
      "The financial summary table is present but slightly too compressed."
    ]
  },
  "visual_hierarchy": {
    "rating": "pass",
    "notes": [
      "The hero KPI remains the dominant block.",
      "Supporting metrics do not overpower the main proof."
    ]
  },
  "consulting_quality": {
    "rating": "pass",
    "notes": [
      "The page feels structured and executive-ready.",
      "Visual polish is strong without drifting into poster style."
    ]
  },
  "copy_behavior": {
    "rating": "borderline",
    "notes": [
      "Metric labels are acceptable.",
      "Some finance-table text is too dense and should be simplified."
    ]
  },
  "overall_outcome": "revise",
  "revision_notes": [
    "Keep the same overall structure.",
    "Open up the finance table and reduce text density in the lower-right block."
  ]
}
```

## Example 2: Deck-Level Review

```json
{
  "shell_family_consistency": {
    "rating": "pass",
    "notes": [
      "All non-cover slides keep the same top headline family.",
      "Divider treatment is visually consistent."
    ]
  },
  "flow_family_consistency": {
    "rating": "borderline",
    "notes": [
      "Most slides keep the bottom flow strip correctly with the same centered labels and active marker treatment.",
      "Two slides render the flow too tall and visually heavy."
    ]
  },
  "visual_family_consistency": {
    "rating": "pass",
    "notes": [
      "The deck stays within one consulting visual language.",
      "No slides drift into poster or unrelated infographic styles."
    ]
  },
  "overall_deck_outcome": "revise",
  "deck_notes": [
    "Tighten the bottom flow strip on the two outlier slides so the active marker and centered label layout match the rest of the deck.",
    "No need to change the overall art direction."
  ]
}
```
