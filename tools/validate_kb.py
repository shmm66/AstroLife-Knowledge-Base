#!/usr/bin/env python3
"""Validate the bilingual AstroLife knowledge corpus and structured JPL reference."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "sources" / "sources.json"
FILES = {"fa": ROOT / "data" / "fa" / "core.jsonl", "en": ROOT / "data" / "en" / "core.jsonl"}
PLANETARY_FILE = ROOT / "data" / "reference" / "planetary-parameters.json"
PLANETARY_SCHEMA = ROOT / "schemas" / "planetary-reference.schema.json"
MODEL_FILE = ROOT / "artifacts" / "ranker-model.json"
LABEL_FILE = ROOT / "training" / "seed-labels.jsonl"
REQUIRED = {
    "id", "revision", "language", "topic", "entity_type", "entity", "title",
    "brief", "expanded", "reflection_question", "evidence_class", "source_ids",
    "source_note", "tags", "limitations", "license", "status", "updated_at"
}
EVIDENCE = {"astronomical_measurement", "historical_tradition", "symbolic_reflection",
            "empirical_research", "editorial_method"}
STATUSES = {"candidate", "reviewed", "approved", "retired"}
PLANETS = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
DWARFS = {"Ceres", "Pluto", "Eris", "Makemake", "Haumea"}
NUMERIC_FIELDS = (
    "mean_radius_km", "bulk_density_g_cm3", "sidereal_rotation_period_days",
    "sidereal_orbital_period_years", "visual_magnitude_v_1_0", "geometric_albedo",
    "equatorial_gravity_m_s2", "escape_velocity_km_s"
)

def fail(message: str) -> None:
    print("FAIL:", message)
    raise SystemExit(1)

def validate_planetary_reference(source_ids: set[str]) -> None:
    if not PLANETARY_FILE.exists() or not PLANETARY_SCHEMA.exists():
        fail("Missing structured JPL reference file or its JSON Schema.")
    data = json.loads(PLANETARY_FILE.read_text(encoding="utf-8-sig"))
    schema = json.loads(PLANETARY_SCHEMA.read_text(encoding="utf-8-sig"))
    if schema.get("title") != "AstroLife JPL Planetary Physical Reference":
        fail("Unexpected planetary-reference schema title.")
    if data.get("source_id") != "JPL_PHYSICAL_PARAMETERS" or data["source_id"] not in source_ids:
        fail("Planetary reference source ID is missing or unresolved.")
    if data.get("source_url") != "https://ssd.jpl.nasa.gov/planets/phys_par.html":
        fail("Planetary reference must use the official JPL physical-parameters URL.")
    if set(x.get("name") for x in data.get("planets", [])) != PLANETS:
        fail("Expected the eight IAU planets in the JPL reference.")
    if set(x.get("name") for x in data.get("dwarf_planets", [])) != DWARFS:
        fail("Expected the five dwarf planets listed in the JPL reference.")
    for group_name in ("planets", "dwarf_planets"):
        for body in data[group_name]:
            for field in NUMERIC_FIELDS:
                if field not in body or not isinstance(body[field], (int, float)):
                    fail(f"{body.get('name')}: missing numeric field {field}.")
            if body["mean_radius_km"] <= 0 or body["bulk_density_g_cm3"] <= 0:
                fail(f"{body['name']}: invalid physical reference value.")
            uncertainty = body.get("uncertainties", {})
            for key, value in uncertainty.items():
                if key not in body or not isinstance(value, (int, float)) or value < 0:
                    fail(f"{body['name']}: invalid published uncertainty for {key}.")
            if group_name == "dwarf_planets" and body.get("iau_classification") != "dwarf planet":
                fail(f"{body['name']}: dwarf-planet classification is missing.")
    if "Only explicit ± values" not in data.get("uncertainty_policy", ""):
        fail("JPL uncertainty policy is missing.")
    # Validate against the machine-readable schema when the optional package is installed.
    try:
        import jsonschema
        jsonschema.Draft202012Validator(schema).validate(data)
        print("PASS: JPL structured reference matches planetary-reference.schema.json")
    except ImportError:
        print("PASS: JPL structured reference shape and constraints (jsonschema package not installed)")
    except Exception as exc:
        fail(f"JPL reference JSON Schema validation failed: {exc}")
    print("PASS: 8 planets + 5 dwarf planets, units, source and explicit uncertainty policy")

def validate_ranker(labels: list[dict], known_ids: set[str]) -> None:
    if not MODEL_FILE.exists():
        fail("Missing trained relevance ranker.")
    model = json.loads(MODEL_FILE.read_text(encoding="utf-8-sig"))
    if len(model.get("weights", [])) != 9 or len(model.get("means", [])) != 9 or len(model.get("standard_deviations", [])) != 9:
        fail("Ranker does not contain the expected nine features.")
    groups: dict[str, dict] = {}
    for row in labels:
        if row.get("entry_id") not in known_ids:
            fail(f"Training label references unknown card: {row.get('entry_id')}")
        family = row.get("query_group")
        if not family:
            fail("Training label is missing its bilingual query_group.")
        bucket = groups.setdefault(family, {"languages": set(), "labels": set()})
        bucket["languages"].add(row.get("language"))
        bucket["labels"].add(row.get("relevant"))
    for family, bucket in groups.items():
        if bucket["languages"] != {"fa", "en"} or bucket["labels"] != {0, 1}:
            fail(f"Training family {family} must include both languages and both relevance labels.")
    if len(groups) < 8:
        fail("Too few bilingual query families for grouped holdout evaluation.")
    print(f"PASS: ranker model feature dimensions and {len(labels)} labelled judgements across {len(groups)} bilingual query families")

def main() -> None:
    sources = json.loads(SOURCE_FILE.read_text(encoding="utf-8-sig"))
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
    labels = [json.loads(x) for x in LABEL_FILE.read_text(encoding="utf-8-sig").splitlines() if x.strip()]
    validate_planetary_reference(source_ids)
    validate_ranker(labels, all_ids)
    print("NOTE: 'reviewed' means editorially checked for this seed; it is not an independent peer review.")

if __name__ == "__main__":
    main()
