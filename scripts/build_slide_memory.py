#!/usr/bin/env python3

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MEMORY_ROOT = ROOT / "references" / "memory-bank"
OUTPUT_ROOT = MEMORY_ROOT / "slide-memory" / "generated"
INDEX_PATH = MEMORY_ROOT / "index" / "slide-memory-index.jsonl"


def infer_classes(text: str) -> list[str]:
    lowered = text.lower()
    classes = []
    mapping = [
        ("executive summary", "executive-summary"),
        ("market", "market-trend"),
        ("customer", "customer-journey"),
        ("competitor", "competitive-landscape"),
        ("strategy", "strategy-pillars"),
        ("implementation", "roadmap"),
        ("impact", "impact-scorecard"),
        ("risk", "risk-mitigation"),
        ("finance", "business-case"),
    ]
    for needle, label in mapping:
        if needle in lowered:
            classes.append(label)
    return sorted(set(classes)) or ["problem-frame"]


def infer_decisions(classes: list[str]) -> list[str]:
    decisions = set()
    if "executive-summary" in classes:
        decisions.add("summarize")
    if any(c in classes for c in ["market-trend", "competitive-landscape", "impact-scorecard", "business-case"]):
        decisions.add("prove")
    if "strategy-pillars" in classes:
        decisions.add("choose")
    if "roadmap" in classes:
        decisions.add("sequence")
    if "risk-mitigation" in classes:
        decisions.add("de-risk")
    return sorted(decisions or {"summarize"})


def infer_shapes(classes: list[str]) -> list[str]:
    shapes = set()
    if "market-trend" in classes:
        shapes.add("trend")
    if "competitive-landscape" in classes:
        shapes.add("comparison")
        shapes.add("table")
    if "customer-journey" in classes:
        shapes.add("journey")
    if "strategy-pillars" in classes:
        shapes.add("pillars")
    if "roadmap" in classes:
        shapes.add("roadmap")
    if any(c in classes for c in ["impact-scorecard", "business-case"]):
        shapes.add("scorecard")
    if "risk-mitigation" in classes:
        shapes.add("matrix")
    return sorted(shapes or {"comparison"})


def infer_devices(classes: list[str], shapes: list[str]) -> list[str]:
    devices = set()
    if "journey" in shapes:
        devices.update(["journey-path", "pain-point-cards"])
    if "roadmap" in shapes:
        devices.add("phase-lanes")
    if "scorecard" in shapes:
        devices.add("metric-cards")
    if "trend" in shapes:
        devices.add("line-chart")
    if "table" in shapes:
        devices.add("comparison-table")
    if "matrix" in shapes:
        devices.add("risk-matrix")
    if "pillars" in shapes:
        devices.add("initiative-cards")
    devices.add("callout-card")
    return sorted(devices)


def infer_layout(classes: list[str], shapes: list[str]) -> tuple[str, str]:
    if "executive-summary" in classes:
        return "executive-synthesis-board", "question-banner_solution-triplet_impact-strip"
    if "journey" in shapes:
        return "top-journey-bottom-pain-cards", "persona-left_journey-center_insights-right"
    if "roadmap" in shapes:
        return "roadmap-with-phase-lanes", "phase-overview_dominant-lanes-below"
    if "scorecard" in shapes:
        return "hero-metric-with-supporting-scorecards", "hero-left_support-right_proof-bottom"
    if "table" in shapes:
        return "distributed-card-grid", "balanced-pillars_top_with_synthesis-bottom"
    return "distributed-card-grid", "balanced-pillars_top_with_synthesis-bottom"


def build_entries(training_root: Path) -> list[dict]:
    entries = []
    slide_number = 1
    for path in sorted(training_root.rglob("*")):
        if path.suffix.lower() not in {".txt", ".md"}:
            continue
        text = path.read_text(errors="ignore").strip()
        if not text:
            continue
        classes = infer_classes(text)
        decisions = infer_decisions(classes)
        shapes = infer_shapes(classes)
        devices = infer_devices(classes, shapes)
        layout_family, layout_variant = infer_layout(classes, shapes)
        entry_id = f"{path.stem}_{slide_number:03d}"
        entry = {
            "slide_id": entry_id,
            "source_deck": path.parent.name,
            "page": slide_number,
            "content_classes": classes,
            "decision_types": decisions,
            "data_shapes": shapes,
            "visual_devices": devices,
            "layout_family": layout_family,
            "layout_variant": layout_variant,
            "dominance_structure": "hero" if "scorecard" in shapes else "distributed",
            "density_hint": "high",
            "primary_message": text[:400],
        }
        entries.append(entry)
        slide_number += 1
    return entries


def write_outputs(entries: list[dict]) -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with INDEX_PATH.open("w", encoding="utf-8") as index_fh:
        for entry in entries:
            deck_dir = OUTPUT_ROOT / entry["source_deck"]
            deck_dir.mkdir(parents=True, exist_ok=True)
            entry_path = deck_dir / f"{entry['slide_id']}.json"
            entry_path.write_text(json.dumps(entry, ensure_ascii=False, indent=2))
            index_row = {
                "slide_id": entry["slide_id"],
                "entry_path": entry_path.relative_to(MEMORY_ROOT).as_posix(),
                "source_deck": entry["source_deck"],
                "page": entry["page"],
                "content_classes": entry["content_classes"],
                "decision_types": entry["decision_types"],
                "data_shapes": entry["data_shapes"],
                "visual_devices": entry["visual_devices"],
                "layout_family": entry["layout_family"],
                "dominance_structure": entry["dominance_structure"],
                "density_hint": entry["density_hint"],
                "tags": sorted(
                    set(
                        entry["content_classes"]
                        + entry["decision_types"]
                        + entry["data_shapes"]
                        + entry["visual_devices"]
                        + [entry["layout_family"], entry["layout_variant"], entry["dominance_structure"]]
                    )
                ),
            }
            index_fh.write(json.dumps(index_row, ensure_ascii=False) + "\n")


def main() -> None:
    training_root_env = os.environ.get("TRAINING_ROOT")
    if not training_root_env:
        raise SystemExit("Set TRAINING_ROOT to a folder containing .txt or .md slide-source files.")
    training_root = Path(training_root_env).expanduser().resolve()
    if not training_root.exists():
        raise SystemExit(f"TRAINING_ROOT does not exist: {training_root}")
    entries = build_entries(training_root)
    write_outputs(entries)
    print(f"Built {len(entries)} slide-memory entries from {training_root}")


if __name__ == "__main__":
    main()
