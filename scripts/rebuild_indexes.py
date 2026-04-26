#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MEMORY_ROOT = ROOT / "references" / "memory-bank"
INDEX_ROOT = MEMORY_ROOT / "index"


def rel(path: Path) -> str:
    return path.relative_to(MEMORY_ROOT).as_posix()


def load_json_files(folder: Path) -> list[tuple[Path, dict]]:
    rows = []
    for path in sorted(folder.glob("*.json")):
        if path.name == "schema.json":
            continue
        rows.append((path, json.loads(path.read_text())))
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def build_visual_device_index() -> None:
    rows = []
    for path, record in load_json_files(MEMORY_ROOT / "visual-devices"):
        rows.append(
            {
                "device_id": record["device_id"],
                "entry_path": rel(path),
                "device_type": record["device_type"],
                "best_for_classes": record["best_for_classes"],
                "best_for_data_shapes": record["best_for_data_shapes"],
                "typical_role": record["typical_role"],
            }
        )
    write_jsonl(INDEX_ROOT / "visual-device-index.jsonl", rows)


def build_layout_grammar_index() -> None:
    rows = []
    for path, record in load_json_files(MEMORY_ROOT / "layout-grammars"):
        rows.append(
            {
                "grammar_id": record["grammar_id"],
                "entry_path": rel(path),
                "fits_classes": record["fits_classes"],
                "common_decision_types": record["common_decision_types"],
                "common_data_shapes": record["common_data_shapes"],
                "dominance_structure": record["dominance_structure"],
                "allowed_visual_devices": record["allowed_visual_devices"],
            }
        )
    write_jsonl(INDEX_ROOT / "layout-grammar-index.jsonl", rows)


def build_layout_variant_index() -> None:
    rows = []
    for path, record in load_json_files(MEMORY_ROOT / "layout-variants"):
        rows.append(
            {
                "variant_id": record["variant_id"],
                "entry_path": rel(path),
                "parent_grammar": record["parent_grammar"],
                "hero_position": record["hero_position"],
                "best_for_classes": record["best_for_classes"],
                "best_for_data_shapes": record["best_for_data_shapes"],
                "common_device_mix": record["common_device_mix"],
            }
        )
    write_jsonl(INDEX_ROOT / "layout-variant-index.jsonl", rows)


def ensure_slide_memory_index() -> None:
    path = INDEX_ROOT / "slide-memory-index.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("")


def main() -> None:
    build_visual_device_index()
    build_layout_grammar_index()
    build_layout_variant_index()
    ensure_slide_memory_index()
    print("Rebuilt portable memory-bank indexes.")


if __name__ == "__main__":
    main()
