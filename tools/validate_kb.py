#!/usr/bin/env python3
"""Validate the bilingual AstroLife knowledge corpus without third-party packages."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "sources" / "sources.json"
FILES = {"fa": ROOT / "data" / "fa" / "core.jsonl", "en": ROOT / "data" / "en" / "core.jsonl"}
REQUIRED = {
    "id", "revision", "language", "topic", "entity_type", "entity", "title",
    "brief", "expanded", "reflection_question", "evidence_class", "source_ids",
    "source_note", "tags", "license", "status", "updated_at"
}
EVIDENCE = {"astronomical_measurement", "historical_tradition", "symbolic_reflection",
            "empirical_research", "editorial_method"}
STATUSES = {"candidate", "reviewed", "approved", "retired"}

def fail(message: str) -> None:
    print("FAIL:", message)
    raise SystemExit(1)

def main() -> None:
    sources = json.loads(SOURCE_FILE.read_text(encoding="utf-8"))
    source_ids = {item["id"] for item in sources["sources"]}
    all_ids: set[str] = set()
    per_language: dict[str, list[dict]] = {"fa": [], "en": []}
    errors: list[str] = []

    for lang, path in FILES.items():
        if not path.exists():
            errors.append(f"Missing corpus file: {path}")
            continue
        for line_no, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not raw.strip():
                continue
            try:
                card = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{path.name}:{line_no}: invalid JSON: {exc}")
                continue
            missing = REQUIRED - card.keys()
            if missing:
                errors.append(f"{path.name}:{line_no}: missing fields {sorted(missing)}")
                continue
            if card["language"] != lang:
                errors.append(f"{card['id']}: language does not match folder {lang}")
            if card["id"] in all_ids:
                errors.append(f"Duplicate ID: {card['id']}")
            all_ids.add(card["id"])
            per_language[lang].append(card)
            if card["evidence_class"] not in EVIDENCE:
                errors.append(f"{card['id']}: unsupported evidence_class")
            if card["status"] not in STATUSES:
                errors.append(f"{card['id']}: unsupported status")
            if card["license"] != "CC-BY-4.0":
                errors.append(f"{card['id']}: original card must use CC-BY-4.0")
            unknown = set(card["source_ids"]) - source_ids
            if unknown:
                errors.append(f"{card['id']}: unknown sources {sorted(unknown)}")
            if not card["brief"].strip() or not card["expanded"].strip():
                errors.append(f"{card['id']}: empty explanation")
            if card["evidence_class"] == "symbolic_reflection" and not card["limitations"]:
                errors.append(f"{card['id']}: symbolic content must disclose limitations")

    for lang, cards in per_language.items():
        if len(cards) < 20:
            errors.append(f"{lang}: only {len(cards)} cards; initial release requires at least 20")
    fa_ids = {c["id"].replace("fa.", "", 1) for c in per_language["fa"]}
    en_ids = {c["id"].replace("en.", "", 1) for c in per_language["en"]}
    if fa_ids != en_ids:
        errors.append(f"Persian/English coverage mismatch: fa-only={sorted(fa_ids-en_ids)}, en-only={sorted(en_ids-fa_ids)}")

    if errors:
        for error in errors:
            print(" -", error)
        fail(f"{len(errors)} validation issue(s)")
    print(f"PASS: {len(all_ids)} unique cards ({len(per_language['fa'])} fa, {len(per_language['en'])} en)")
    print(f"PASS: all source IDs resolve ({len(source_ids)} registered sources)")
    print("PASS: language parity, evidence labels, license fields and limitations")
    print("NOTE: 'reviewed' means editorially checked for this seed; maintainer approval is still required before public release.")

if __name__ == "__main__":
    main()
