#!/usr/bin/env python3
"""Group near-duplicate candidate cards for human review; does not auto-publish."""
from __future__ import annotations
import json
import math
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "training" / "candidate-inbox.jsonl"
CORPUS = [ROOT / "data" / "fa" / "core.jsonl", ROOT / "data" / "en" / "core.jsonl"]
REPORT = ROOT / "artifacts" / "candidate-review.json"
THRESHOLD = 0.68

def normal(text: str) -> str:
    return unicodedata.normalize("NFKC", text).lower().replace("ي", "ی").replace("ك", "ک")

def grams(text: str) -> set[str]:
    value = " " + normal(text) + " "
    return {value[i:i+3] for i in range(max(0, len(value)-2))}

def similarity(a: str, b: str) -> float:
    ga, gb = grams(a), grams(b)
    denom = math.sqrt(len(ga) * len(gb))
    return len(ga & gb) / denom if denom else 0.0

def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]

def main() -> None:
    candidates = read_jsonl(INBOX)
    current = []
    for path in CORPUS:
        current.extend(read_jsonl(path))
    report = []
    for candidate in candidates:
        candidate_text = " ".join([candidate.get("title", ""), candidate.get("claim", ""),
                                   " ".join(candidate.get("tags", []))])
        matches = []
        for card in current:
            text = " ".join([card["title"], card["brief"], card["expanded"], " ".join(card["tags"])])
            score = similarity(candidate_text, text)
            if score >= THRESHOLD:
                matches.append({"id": card["id"], "similarity": round(score, 4), "title": card["title"]})
        matches.sort(key=lambda item: item["similarity"], reverse=True)
        report.append({
            "candidate_id": candidate.get("candidate_id", "UNASSIGNED"),
            "source_id": candidate.get("source_id"),
            "title": candidate.get("title"),
            "suggested_topic": candidate.get("topic", "needs-human-classification"),
            "duplicate_candidates": matches[:5],
            "decision": "human_review_required",
            "suggested_action": "merge_or_rewrite" if matches else "review_as_new_card"
        })
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Reviewed {len(candidates)} candidates against {len(current)} existing cards.")
    print(f"Report: {REPORT}")
    print("No candidate is approved or published automatically.")

if __name__ == "__main__":
    main()
