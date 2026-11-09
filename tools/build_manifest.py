#!/usr/bin/env python3
"""Build a versioned manifest with SHA-256 hashes for safe public sync."""
from __future__ import annotations
import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.2.2"
FILES = [
    "data/fa/core.jsonl",
    "data/en/core.jsonl",
    "data/reference/planetary-parameters.json",
    "sources/sources.json",
    "schemas/knowledge.schema.json",
    "schemas/planetary-reference.schema.json",
    "artifacts/ranker-model.json"
]

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def count_lines(path: Path) -> int:
    return sum(1 for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip())

def main() -> None:
    items = {}
    for name in FILES:
        path = ROOT / name
        if not path.exists():
            raise SystemExit(f"Required release file missing: {name}")
        items[name] = {
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
            "entries": count_lines(path) if name.endswith(".jsonl") else None
        }
    manifest = {
        "name": "AstroLife Knowledge Base",
        "version": VERSION,
        "schema_version": "1.0",
        "release_date": date.today().isoformat(),
        "languages": ["fa", "en"],
        "total_cards": items["data/fa/core.jsonl"]["entries"] + items["data/en/core.jsonl"]["entries"],
        "files": items,
        "sync_policy": "HTTPS GET only; verify every SHA-256 before replacing the active local snapshot."
    }
    path = ROOT / "manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Manifest written: {path}")
    print(f"Cards: {manifest['total_cards']} | Version: {VERSION}")

if __name__ == "__main__":
    main()
