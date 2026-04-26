# Body Blueprint Examples

Use these as examples of what a good `body blueprint` looks like after a `body decision` has already been made.

## Example 1: Journey-Led Slide

```json
{
  "slide_number": 4,
  "key_message": "Customer anxiety peaks at financing and repayment stages, making them the best intervention points.",
  "layout_family": "top-journey-bottom-pain-cards",
  "layout_variant": "persona-left_journey-center_insights-right",
  "dominance_structure": "split",
  "hero_block": "A horizontal journey path across the upper body covering discovery, financing, purchase, and repayment.",
  "support_blocks": [
    "A compact persona snapshot near the upper-left edge introducing the priority customer type and need-state",
    "Pain-point cards directly beneath financing and repayment stages",
    "A right-side key-insight stack synthesizing the main customer tensions",
    "A quiet summary strip at the lower-right edge closing the page with one concise takeaway"
  ],
  "reading_order": [
    "persona snapshot",
    "journey path",
    "pain-point cards",
    "key-insight stack",
    "summary strip"
  ],
  "device_placement": [
    {
      "device_id": "persona-cards",
      "placement_role": "support",
      "target_block": "upper-left persona snapshot"
    },
    {
      "device_id": "journey-path",
      "placement_role": "hero",
      "target_block": "upper journey path"
    },
    {
      "device_id": "pain-point-cards",
      "placement_role": "support",
      "target_block": "lower pain-point band"
    },
    {
      "device_id": "callout-card",
      "placement_role": "support",
      "target_block": "right-side key-insight stack"
    },
    {
      "device_id": "callout-card",
      "placement_role": "bridge",
      "target_block": "summary strip"
    }
  ],
  "must_remain_prominent": [
    "The financing and repayment stages on the journey",
    "The priority customer cue that frames whose anxiety matters most",
    "The pain cards tied to those stages",
    "The right-side insight stack that translates frictions into sharper conclusions"
  ],
  "copy_slots": [
    {
      "slot_id": "persona_label",
      "slot_type": "support-title",
      "target_block": "upper-left persona snapshot"
    },
    {
      "slot_id": "persona_need_state",
      "slot_type": "callout",
      "target_block": "upper-left persona snapshot"
    },
    {
      "slot_id": "journey_stage_labels",
      "slot_type": "caption",
      "target_block": "upper journey path"
    },
    {
      "slot_id": "pain_title_1",
      "slot_type": "support-title",
      "target_block": "lower pain-point band"
    },
    {
      "slot_id": "pain_title_2",
      "slot_type": "support-title",
      "target_block": "lower pain-point band"
    },
    {
      "slot_id": "insight_title_1",
      "slot_type": "support-title",
      "target_block": "right-side key-insight stack"
    },
    {
      "slot_id": "insight_title_2",
      "slot_type": "support-title",
      "target_block": "right-side key-insight stack"
    },
    {
      "slot_id": "summary_takeaway",
      "slot_type": "summary-takeaway",
      "target_block": "summary strip"
    }
  ],
  "reference_links": [
    "2025_nordea_2nd_s014",
    "2026_loral_nordic_1st_s011"
  ]
}
```

## Example 2: Business Case Slide

```json
{
  "slide_number": 11,
  "key_message": "The strategy creates strong upside with one headline KPI supported by compact financial proof.",
  "layout_family": "hero-metric-with-supporting-scorecards",
  "layout_variant": "hero-left_support-right_proof-bottom",
  "dominance_structure": "hero",
  "hero_block": "A dominant KPI block in the upper-left body showing the single most important business impact number.",
  "support_blocks": [
    "A right-side band of supporting metric cards",
    "A compact line chart below the hero block",
    "A narrow financial summary table aligned beneath the metric cards"
  ],
  "reading_order": [
    "hero KPI",
    "supporting metric cards",
    "line chart",
    "financial summary table"
  ],
  "device_placement": [
    {
      "device_id": "metric-cards",
      "placement_role": "hero",
      "target_block": "upper-left hero KPI block"
    },
    {
      "device_id": "metric-cards",
      "placement_role": "support",
      "target_block": "right-side supporting metrics"
    },
    {
      "device_id": "line-chart",
      "placement_role": "proof",
      "target_block": "lower-left proof chart"
    },
    {
      "device_id": "financial-summary-table",
      "placement_role": "proof",
      "target_block": "lower-right finance table"
    }
  ],
  "must_remain_prominent": [
    "The headline KPI in the hero block",
    "The proof relationship between the line chart and the finance table"
  ],
  "copy_slots": [
    {
      "slot_id": "hero_kpi_value",
      "slot_type": "hero-number",
      "target_block": "upper-left hero KPI block"
    },
    {
      "slot_id": "hero_kpi_label",
      "slot_type": "hero-label",
      "target_block": "upper-left hero KPI block"
    },
    {
      "slot_id": "support_metric_titles",
      "slot_type": "support-title",
      "target_block": "right-side supporting metrics"
    },
    {
      "slot_id": "support_metric_values",
      "slot_type": "support-metric",
      "target_block": "right-side supporting metrics"
    },
    {
      "slot_id": "chart_labels",
      "slot_type": "axis-label",
      "target_block": "lower-left proof chart"
    },
    {
      "slot_id": "finance_cells",
      "slot_type": "table-cell",
      "target_block": "lower-right finance table"
    }
  ],
  "reference_links": [
    "2025_nordea_1st_s022",
    "2025_european_energy_2nd_s018"
  ]
}
```

## Example 3: Executive Summary Slide

```json
{
  "slide_number": 2,
  "key_message": "The answer to the case should be legible in one page: what problem matters, what three moves solve it, and what impact they create.",
  "layout_family": "executive-synthesis-board",
  "layout_variant": "question-banner_solution-triplet_impact-strip",
  "dominance_structure": "board",
  "hero_block": "A top question or answer banner that frames the whole page.",
  "support_blocks": [
    "A compact row of issue or situation cues immediately below the banner",
    "A central recommendation triplet with three named moves",
    "A compact lower impact strip summarizing the upside or business effect"
  ],
  "reading_order": [
    "question banner",
    "issue or situation cues",
    "recommendation triplet",
    "impact strip"
  ],
  "device_placement": [
    {
      "device_id": "callout-card",
      "placement_role": "hero",
      "target_block": "top question banner"
    },
    {
      "device_id": "callout-card",
      "placement_role": "support",
      "target_block": "issue or situation cue row"
    },
    {
      "device_id": "initiative-cards",
      "placement_role": "support",
      "target_block": "central recommendation triplet"
    },
    {
      "device_id": "metric-cards",
      "placement_role": "proof",
      "target_block": "lower impact strip"
    }
  ],
  "must_remain_prominent": [
    "The case question or core claim at the top",
    "The three recommendation moves in the center",
    "The compact impact line at the bottom"
  ],
  "copy_slots": [
    {
      "slot_id": "question_banner",
      "slot_type": "hero-label",
      "target_block": "top question banner"
    },
    {
      "slot_id": "issue_cue_titles",
      "slot_type": "support-title",
      "target_block": "issue or situation cue row"
    },
    {
      "slot_id": "move_titles",
      "slot_type": "support-title",
      "target_block": "central recommendation triplet"
    },
    {
      "slot_id": "move_descriptions",
      "slot_type": "callout",
      "target_block": "central recommendation triplet"
    },
    {
      "slot_id": "impact_metric_labels",
      "slot_type": "support-title",
      "target_block": "lower impact strip"
    },
    {
      "slot_id": "impact_metric_values",
      "slot_type": "support-metric",
      "target_block": "lower impact strip"
    }
  ],
  "reference_links": [
    "2024_boozt_1st_s002",
    "2025_nordea_1st_s002"
  ]
}
```

## Example 4: Implementation Slide

```json
{
  "slide_number": 9,
  "key_message": "The rollout should move from pilot to scale through visible decision gates, with years and execution tracks readable at a glance.",
  "layout_family": "roadmap-with-phase-lanes",
  "layout_variant": "phase-overview_with_gate-transitions",
  "dominance_structure": "distributed",
  "hero_block": "A dominant three-phase rollout band spanning the top of the body, with Pilot, Integrate, and Scale clearly named before the user reads the lane detail.",
  "support_blocks": [
    "A left-side column of strong initiative row labels aligned to the roadmap lanes",
    "Dark primary rollout bars aligned beneath the phase overview",
    "Lighter secondary sub-action bars beneath the primary rollout bars",
    "Visible checkpoint or decision-gate markers between phases"
  ],
  "reading_order": [
    "phase overview",
    "year anchors",
    "initiative row labels",
    "primary rollout bars",
    "secondary sub-action bars and decision gates"
  ],
  "device_placement": [
    {
      "device_id": "timeline",
      "placement_role": "hero",
      "target_block": "top phase overview and year anchor rail"
    },
    {
      "device_id": "phase-lanes",
      "placement_role": "hero",
      "target_block": "main rollout lanes"
    },
    {
      "device_id": "callout-card",
      "placement_role": "proof",
      "target_block": "decision-gate checkpoints"
    }
  ],
  "must_remain_prominent": [
    "The year or phase anchors that organize the roadmap",
    "The named Pilot, Integrate, and Scale overview that frames the rollout",
    "The initiative row labels that define each execution track",
    "The darker primary rollout bars showing the main implementation path",
    "The visible decision gates that control scale-up"
  ],
  "copy_slots": [
    {
      "slot_id": "year_labels",
      "slot_type": "axis-label",
      "target_block": "top phase overview and year anchor rail"
    },
    {
      "slot_id": "phase_labels",
      "slot_type": "hero-label",
      "target_block": "top phase overview and year anchor rail"
    },
    {
      "slot_id": "initiative_labels",
      "slot_type": "support-title",
      "target_block": "left-side initiative label column"
    },
    {
      "slot_id": "primary_lane_labels",
      "slot_type": "caption",
      "target_block": "main rollout lanes"
    },
    {
      "slot_id": "gate_labels",
      "slot_type": "callout",
      "target_block": "decision-gate checkpoints"
    }
  ],
  "reference_links": [
    "2025_nordea_1st_s035",
    "2020_novo_nordisk_1st_s011",
    "2024_boozt_1st_s021"
  ]
}
```
