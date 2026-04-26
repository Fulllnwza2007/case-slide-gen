# Body Decision Examples

Use these examples as style guides for what a good `body decision` should contain.

They are examples of decision structure, not final slide content.

## Example 1: Customer Journey Slide

```json
{
  "slide_number": 4,
  "key_message": "Customer anxiety rises at financing and repayment stages, creating the best intervention points for TTB.",
  "content_classes": ["customer-journey", "customer-pain", "customer-segmentation"],
  "decision_types": ["prove", "choose"],
  "data_shapes": ["journey", "comparison"],
  "analysis_proof_mode": null,
  "analysis_terminal_role": null,
  "implementation_mode": null,
  "retrieved_reference_candidates": [
    "2025_nordea_2nd_s014",
    "2026_loral_nordic_1st_s011",
    "2025_european_energy_1st_s009"
  ],
  "retrieved_visual_device_candidates": [
    "journey-path",
    "pain-point-cards",
    "callout-card",
    "persona-cards"
  ],
  "primary_reference": "2025_nordea_2nd_s014",
  "secondary_references": ["2026_loral_nordic_1st_s011"],
  "chosen_visual_devices": ["journey-path", "pain-point-cards", "persona-cards", "callout-card"],
  "grammar_selection": {
    "retrieved_candidates": [
      "top-journey-bottom-pain-cards",
      "distributed-card-grid",
      "two-pillar-comparison"
    ],
    "filtered_candidates": [
      "top-journey-bottom-pain-cards",
      "distributed-card-grid"
    ],
    "chosen_layout_family": "top-journey-bottom-pain-cards",
    "retrieved_variants": [
      "persona-left_journey-center_insights-right",
      "journey-top_friction-row_bottom"
    ],
    "chosen_variant_id": "persona-left_journey-center_insights-right",
    "chosen_dominance_structure": "split",
    "device_fit_notes": [
      "journey-path is directly supported by the chosen grammar",
      "pain-point-cards belong naturally beneath journey stages",
      "persona-cards can be absorbed as a compact context cue without replacing the journey hero"
    ],
    "variant_fit_notes": [
      "This slide has clear segment evidence, so a left persona panel improves context.",
      "The right insight stack helps this page synthesize more than a pure journey-plus-pain row would."
    ],
    "variant_reject_reasons": [
      {
        "variant_id": "journey-top_friction-row_bottom",
        "reason": "It weakens the persona and synthesis layers that this page can support."
      }
    ],
    "score_breakdown": [
      {
        "candidate_id": "top-journey-bottom-pain-cards",
        "content_class_score": 40,
        "decision_type_score": 18,
        "data_shape_score": 20,
        "visual_device_score": 15,
        "dominance_score": 5,
        "total_score": 98,
        "feasibility": "strong",
        "notes": [
          "Direct match for journey plus pain structure"
        ]
      },
      {
        "candidate_id": "distributed-card-grid",
        "content_class_score": 10,
        "decision_type_score": 8,
        "data_shape_score": 5,
        "visual_device_score": 4,
        "dominance_score": 1,
        "total_score": 28,
        "feasibility": "weak",
        "notes": [
          "Would flatten the journey into equal-weight cards"
        ]
      }
    ],
    "reject_reasons": [
      {
        "candidate_id": "distributed-card-grid",
        "reason": "It weakens the sequence logic and makes the pain points feel disconnected from the journey stages."
      }
    ]
  },
  "why_chosen": [
    "The page must read as a sequence before it reads as a list of issues.",
    "The chosen grammar preserves the customer flow and keeps pains tied to their stages.",
    "A compact persona cue helps explain which customer is experiencing the anxiety without turning the page into a full persona profile."
  ],
  "reject_reasons": [
    {
      "candidate_id": "2025_european_energy_1st_s009",
      "reason": "Its structure is more like a distributed insight page than a true journey-led page."
    }
  ]
}
```

## Example 2: Business Case Slide

```json
{
  "slide_number": 11,
  "key_message": "The strategy creates positive financial upside with one headline KPI and supporting proof.",
  "content_classes": ["business-case", "impact-scorecard"],
  "decision_types": ["prove", "forecast"],
  "data_shapes": ["scorecard", "trend", "table"],
  "analysis_proof_mode": null,
  "analysis_terminal_role": null,
  "implementation_mode": null,
  "retrieved_reference_candidates": [
    "2025_nordea_1st_s022",
    "2025_european_energy_2nd_s018",
    "2026_loral_nordic_1st_s019"
  ],
  "retrieved_visual_device_candidates": [
    "metric-cards",
    "line-chart",
    "financial-summary-table",
    "callout-card"
  ],
  "primary_reference": "2025_nordea_1st_s022",
  "secondary_references": ["2025_european_energy_2nd_s018"],
  "chosen_visual_devices": ["metric-cards", "line-chart", "financial-summary-table"],
  "grammar_selection": {
    "retrieved_candidates": [
      "hero-metric-with-supporting-scorecards",
      "distributed-card-grid",
      "two-pillar-comparison"
    ],
    "filtered_candidates": [
      "hero-metric-with-supporting-scorecards",
      "distributed-card-grid"
    ],
    "chosen_layout_family": "hero-metric-with-supporting-scorecards",
    "retrieved_variants": [
      "hero-left_support-right_proof-bottom",
      "hero-top_metrics-row_proof-bottom",
      "hero-left_chart-center_insight-right"
    ],
    "chosen_variant_id": "hero-left_support-right_proof-bottom",
    "chosen_dominance_structure": "hero",
    "device_fit_notes": [
      "metric-cards and line-chart are native fits",
      "financial-summary-table works as compact proof beneath the hero KPI"
    ],
    "variant_fit_notes": [
      "The slide needs one left-anchored KPI hero and a clear side proof ring.",
      "A top-down variant would make the support proof feel flatter than needed."
    ],
    "variant_reject_reasons": [
      {
        "variant_id": "hero-top_metrics-row_proof-bottom",
        "reason": "It would underuse the side proof band and weaken the left-to-right business-case rhythm."
      },
      {
        "variant_id": "hero-left_chart-center_insight-right",
        "reason": "This slide should anchor on one KPI rather than let the chart become the dominant center mass."
      }
    ],
    "score_breakdown": [
      {
        "candidate_id": "hero-metric-with-supporting-scorecards",
        "content_class_score": 40,
        "decision_type_score": 20,
        "data_shape_score": 20,
        "visual_device_score": 15,
        "dominance_score": 5,
        "total_score": 100,
        "feasibility": "strong",
        "notes": [
          "Best fit for one headline KPI plus supporting proof"
        ]
      },
      {
        "candidate_id": "distributed-card-grid",
        "content_class_score": 12,
        "decision_type_score": 6,
        "data_shape_score": 8,
        "visual_device_score": 5,
        "dominance_score": 0,
        "total_score": 31,
        "feasibility": "medium",
        "notes": [
          "Would dilute the hero proof into equal-weight cards"
        ]
      }
    ],
    "reject_reasons": [
      {
        "candidate_id": "distributed-card-grid",
        "reason": "The message needs one dominant proof block, not a balanced card grid."
      }
    ]
  },
  "why_chosen": [
    "The slide needs one financial anchor and a supporting proof ring.",
    "This grammar matches both the quantified message and the device mix."
  ],
  "reject_reasons": [
    {
      "candidate_id": "2026_loral_nordic_1st_s019",
      "reason": "The page is visually strong but less suitable because it lacks compact finance-table support."
    }
  ]
}
```

## Example 3: Executive Summary Slide

```json
{
  "slide_number": 2,
  "key_message": "The case answer should be visible in one synthesis page: the challenge, the three recommendation moves, and the expected impact.",
  "content_classes": ["executive-summary", "recommendation", "impact-scorecard", "strategy-pillars", "key-question"],
  "decision_types": ["summarize", "choose", "prove"],
  "data_shapes": ["pillars", "scorecard", "comparison"],
  "analysis_proof_mode": null,
  "analysis_terminal_role": null,
  "implementation_mode": null,
  "retrieved_reference_candidates": [
    "2024_boozt_1st_s002",
    "2025_nordea_1st_s002",
    "2020_ramboll_1st_s002"
  ],
  "retrieved_visual_device_candidates": [
    "callout-card",
    "initiative-cards",
    "metric-cards",
    "card-grid"
  ],
  "primary_reference": "2024_boozt_1st_s002",
  "secondary_references": ["2025_nordea_1st_s002"],
  "chosen_visual_devices": ["callout-card", "initiative-cards", "metric-cards"],
  "grammar_selection": {
    "retrieved_candidates": [
      "executive-synthesis-board",
      "hero-metric-with-supporting-scorecards",
      "two-pillar-comparison"
    ],
    "filtered_candidates": [
      "executive-synthesis-board",
      "hero-metric-with-supporting-scorecards",
      "two-pillar-comparison"
    ],
    "chosen_layout_family": "executive-synthesis-board",
    "retrieved_variants": [
      "question-banner_solution-triplet_impact-strip",
      "issue-question_strategy-impact_board",
      "context-panel_strategy-triplet_metric-right"
    ],
    "chosen_variant_id": "question-banner_solution-triplet_impact-strip",
    "chosen_dominance_structure": "board",
    "device_fit_notes": [
      "initiative-cards support a recommendation triplet better than a pure pillar split",
      "metric-cards can stay compact because impact is not the only job of the page",
      "callout-card works well for issue cues and the question banner"
    ],
    "variant_fit_notes": [
      "This slide is driven by one visible question and three named recommendation moves.",
      "The page needs a compact impact strip rather than a KPI billboard."
    ],
    "variant_reject_reasons": [
      {
        "variant_id": "issue-question_strategy-impact_board",
        "reason": "The source does not need a separate issue strip because the question banner already frames the case tightly."
      },
      {
        "variant_id": "context-panel_strategy-triplet_metric-right",
        "reason": "The source does not need a heavy narrative context panel before the recommendation board."
      }
    ],
    "score_breakdown": [
      {
        "candidate_id": "executive-synthesis-board",
        "content_class_score": 40,
        "decision_type_score": 20,
        "data_shape_score": 18,
        "visual_device_score": 15,
        "dominance_score": 5,
        "total_score": 98,
        "feasibility": "strong",
        "notes": [
          "Best fit for a page that must combine challenge, answer, and impact in one board"
        ]
      },
      {
        "candidate_id": "hero-metric-with-supporting-scorecards",
        "content_class_score": 18,
        "decision_type_score": 12,
        "data_shape_score": 10,
        "visual_device_score": 8,
        "dominance_score": 4,
        "total_score": 52,
        "feasibility": "medium",
        "notes": [
          "Would over-dominant one KPI and under-represent the recommendation structure"
        ]
      },
      {
        "candidate_id": "two-pillar-comparison",
        "content_class_score": 20,
        "decision_type_score": 10,
        "data_shape_score": 12,
        "visual_device_score": 9,
        "dominance_score": 3,
        "total_score": 54,
        "feasibility": "medium",
        "notes": [
          "Too narrow if the page must also hold the challenge frame and impact proof"
        ]
      }
    ],
    "reject_reasons": [
      {
        "candidate_id": "hero-metric-with-supporting-scorecards",
        "reason": "The page would become too KPI-led and lose the strategy board."
      },
      {
        "candidate_id": "two-pillar-comparison",
        "reason": "The page would become too strategy-led and lose the case-question framing."
      }
    ]
  },
  "why_chosen": [
    "The page must summarize the answer to the case, not prove one narrow claim.",
    "The chosen grammar preserves the question frame, the recommendation structure, and the impact layer together.",
    "This variant keeps impact visible without turning the page into a finance-led executive summary."
  ],
  "reject_reasons": [
    {
      "candidate_id": "2020_ramboll_1st_s002",
      "reason": "Useful reference, but more issue-led than needed for this source."
    }
  ]
}
```

## Example 4: Terminal Analysis Slide

```json
{
  "slide_number": 6,
  "key_message": "The market and capability gaps now make one strategy direction unavoidable: the recommendation must prioritize the network model that solves both speed and visibility together.",
  "content_classes": ["market-gap", "capability-gap", "problem-frame"],
  "decision_types": ["prove", "choose"],
  "data_shapes": ["comparison", "issue-cluster"],
  "analysis_proof_mode": "diagnosis-board-led",
  "analysis_terminal_role": "bridge-to-recommendation",
  "implementation_mode": null,
  "retrieved_reference_candidates": [
    "2024_boozt_1st_s004",
    "2025_nordea_1st_s006",
    "2020_ramboll_1st_s003"
  ],
  "retrieved_visual_device_candidates": [
    "callout-card",
    "metric-cards",
    "comparison-table"
  ],
  "primary_reference": "2024_boozt_1st_s004",
  "secondary_references": ["2025_nordea_1st_s006"],
  "chosen_visual_devices": ["callout-card", "metric-cards"],
  "grammar_selection": {
    "retrieved_candidates": [
      "distributed-card-grid",
      "two-pillar-comparison",
      "hero-metric-with-supporting-scorecards"
    ],
    "filtered_candidates": [
      "distributed-card-grid",
      "two-pillar-comparison"
    ],
    "chosen_layout_family": "distributed-card-grid",
    "retrieved_variants": [
      "board-led_cluster-with-core-anchor"
    ],
    "chosen_variant_id": "board-led_cluster-with-core-anchor",
    "chosen_dominance_structure": "distributed",
    "device_fit_notes": [
      "callout-card supports compressed diagnosis clusters without forcing a chart-led page",
      "metric-cards can carry one compact proof anchor without turning the page into a KPI board"
    ],
    "variant_fit_notes": [
      "The slide needs one core diagnosis anchor plus a directional bridge into recommendation.",
      "A board-led variant preserves multiple related issues without flattening them into equal paragraphs."
    ],
    "variant_reject_reasons": [
      {
        "variant_id": "balanced-pillars_top_with_synthesis-bottom",
        "reason": "The page is still diagnosing the problem space rather than comparing finished strategy pillars."
      }
    ],
    "score_breakdown": [
      {
        "candidate_id": "distributed-card-grid",
        "content_class_score": 34,
        "decision_type_score": 18,
        "data_shape_score": 18,
        "visual_device_score": 12,
        "dominance_score": 4,
        "total_score": 86,
        "feasibility": "strong",
        "notes": [
          "Best fit for diagnosis-board-led proof with one core anchor and compressed support clusters."
        ]
      },
      {
        "candidate_id": "two-pillar-comparison",
        "content_class_score": 14,
        "decision_type_score": 8,
        "data_shape_score": 6,
        "visual_device_score": 5,
        "dominance_score": 1,
        "total_score": 34,
        "feasibility": "weak",
        "notes": [
          "Would imply the recommendation structure too early instead of closing the analysis logic first."
        ]
      }
    ],
    "reject_reasons": [
      {
        "candidate_id": "two-pillar-comparison",
        "reason": "The page must still land the diagnosis before shifting into recommendation structure."
      }
    ]
  },
  "why_chosen": [
    "The page needs to close the analysis section with one clear diagnosis anchor and a directional bridge.",
    "Diagnosis-board-led composition allows multiple related issues while still landing one unavoidable implication.",
    "The final bridge block turns evidence into the strategic handoff the recommendation section needs."
  ],
  "reject_reasons": [
    {
      "candidate_id": "2020_ramboll_1st_s003",
      "reason": "Useful as a reference for clustered diagnosis, but weaker as a directional bridge into recommendation."
    }
  ]
}
```

## Example 5: Implementation Slide

```json
{
  "slide_number": 9,
  "key_message": "The rollout should scale only after pilot validation and visible execution checkpoints, not as one flat timeline.",
  "content_classes": ["roadmap", "pilot-scale-rollout", "milestones", "change-management"],
  "decision_types": ["sequence", "choose"],
  "data_shapes": ["roadmap", "table", "comparison"],
  "analysis_proof_mode": null,
  "analysis_terminal_role": null,
  "implementation_mode": "decision-gate-led",
  "retrieved_reference_candidates": [
    "2025_nordea_1st_s035",
    "2024_berlingske_3rd_s014",
    "2020_novo_nordisk_1st_s011"
  ],
  "retrieved_visual_device_candidates": [
    "phase-lanes",
    "timeline",
    "callout-card",
    "metric-cards"
  ],
  "primary_reference": "2025_nordea_1st_s035",
  "secondary_references": ["2024_berlingske_3rd_s014"],
  "chosen_visual_devices": ["phase-lanes", "timeline", "callout-card"],
  "grammar_selection": {
    "retrieved_candidates": [
      "roadmap-with-phase-lanes",
      "execution-board-with-control-points",
      "distributed-card-grid"
    ],
    "filtered_candidates": [
      "roadmap-with-phase-lanes",
      "execution-board-with-control-points"
    ],
    "chosen_layout_family": "roadmap-with-phase-lanes",
    "retrieved_variants": [
      "phase-overview_with_gate-transitions",
      "phase-overview_dominant-lanes-below",
      "timeline-led_rollout-with-lanes",
      "roadmap_with_decision-gates"
    ],
    "chosen_variant_id": "phase-overview_with_gate-transitions",
    "chosen_dominance_structure": "distributed",
    "device_fit_notes": [
      "Phase lanes and timeline naturally support a gated rollout page.",
      "Callout-card can make decision points visible without turning the page into text-heavy notes."
    ],
    "variant_fit_notes": [
      "This page depends on review and scale checkpoints, but the named phase overview should still lead the story.",
      "The chosen variant keeps the source-derived phase overview dominant while using gates as transition logic rather than as oversized standalone objects."
    ],
    "variant_reject_reasons": [
      {
        "variant_id": "timeline-led_rollout-with-lanes",
        "reason": "It would make the page too uniformly lane-led and underplay the gate transitions."
      },
      {
        "variant_id": "roadmap_with_decision-gates",
        "reason": "It risks making the gates more visually dominant than the phase rollout itself."
      }
    ],
    "score_breakdown": [
      {
        "candidate_id": "roadmap-with-phase-lanes",
        "content_class_score": 38,
        "decision_type_score": 19,
        "data_shape_score": 20,
        "visual_device_score": 14,
        "dominance_score": 3,
        "total_score": 94,
        "feasibility": "strong",
        "notes": [
          "Best family for a phased page where visible gates shape progression."
        ]
      },
      {
        "candidate_id": "execution-board-with-control-points",
        "content_class_score": 24,
        "decision_type_score": 14,
        "data_shape_score": 12,
        "visual_device_score": 10,
        "dominance_score": 3,
        "total_score": 63,
        "feasibility": "medium",
        "notes": [
          "Relevant, but the page still wants a strong timeline backbone."
        ]
      }
    ],
    "reject_reasons": [
      {
        "candidate_id": "execution-board-with-control-points",
        "reason": "This page still needs a clear phased timeline as the main proof, with gates layered onto it."
      }
    ]
  },
  "why_chosen": [
    "The page is not just a rollout; it is a gated rollout where pilot and evaluation points matter.",
    "The chosen variant keeps the three-phase backbone dominant while still making control points visible.",
    "This matches the implementation refs better than a generic lane-only roadmap."
  ],
  "reject_reasons": [
    {
      "candidate_id": "2020_novo_nordisk_1st_s011",
      "reason": "Useful for timeline sequencing, but weaker as a checkpoint-led execution page."
    }
  ]
}
```
