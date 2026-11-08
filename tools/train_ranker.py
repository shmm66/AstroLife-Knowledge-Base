#!/usr/bin/env python3
"""Train a tiny offline logistic ranker from reviewed relevance labels."""
from __future__ import annotations
import json
import math
import random
import re
import unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = ROOT / "training" / "seed-labels.jsonl"
CORPUS = [ROOT / "data" / "fa" / "core.jsonl", ROOT / "data" / "en" / "core.jsonl"]
OUT = ROOT / "artifacts" / "ranker-model.json"
FEATURES = ["char_3gram_cosine", "token_jaccard", "title_overlap", "tag_overlap",
            "entity_match", "language_match", "topic_match", "source_coverage",
            "research_intent_match"]

def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return text.replace("ي", "ی").replace("ك", "ک").replace("ۀ", "ه").replace("ة", "ه")

def tokens(text: str) -> set[str]:
    return {x for x in re.findall(r"[^\W_]+", normalize(text), flags=re.UNICODE) if len(x) > 1}

def chargrams(text: str, n: int = 3) -> dict[str, int]:
    value = " " + normalize(text) + " "
    counts: dict[str, int] = {}
    for i in range(max(0, len(value) - n + 1)):
        gram = value[i:i+n]
        counts[gram] = counts.get(gram, 0) + 1
    return counts

def cosine(a: dict[str, int], b: dict[str, int]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(value * b.get(key, 0) for key, value in a.items())
    na = math.sqrt(sum(v*v for v in a.values()))
    nb = math.sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0

def load_cards() -> dict[str, dict]:
    cards = {}
    for path in CORPUS:
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if line.strip():
                item = json.loads(line)
                if item["status"] in {"reviewed", "approved"}:
                    cards[item["id"]] = item
    return cards

def features(query: str, language: str, topic: str, card: dict) -> list[float]:
    q = tokens(query)
    body = " ".join([card["title"], card["brief"], card["expanded"], card["entity"], *card["tags"]])
    d = tokens(body)
    title = tokens(card["title"])
    tags = tokens(" ".join(card["tags"]))
    entity = tokens(card["entity"].replace("_", " "))
    union = q | d
    jaccard = len(q & d) / len(union) if union else 0.0
    title_overlap = len(q & title) / len(q) if q else 0.0
    tag_overlap = len(q & tags) / len(q) if q else 0.0
    entity_match = 1.0 if q & entity else 0.0
    lang_match = 1.0 if card["language"] == language else 0.0
    topic_match = 1.0 if topic in card.get("topic", []) else 0.0
    source_coverage = min(len(card.get("source_ids", [])), 3) / 3.0
    research_terms = {"علم", "پژوهش", "شواهد", "اعتبار", "science", "research", "evidence", "empirical"}
    research_intent = 1.0 if (q & research_terms and card["evidence_class"] == "empirical_research") else 0.0
    return [
        cosine(chargrams(query), chargrams(body)),
        jaccard, title_overlap, tag_overlap, entity_match, lang_match,
        topic_match, source_coverage, research_intent
    ]

def sigmoid(z: float) -> float:
    if z >= 0:
        e = math.exp(-min(z, 60.0))
        return 1.0 / (1.0 + e)
    e = math.exp(max(z, -60.0))
    return e / (1.0 + e)

def main() -> None:
    cards = load_cards()
    examples = []
    for raw in LABELS.read_text(encoding="utf-8-sig").splitlines():
        if not raw.strip():
            continue
        row = json.loads(raw)
        card = cards.get(row["entry_id"])
        if card is None:
            raise SystemExit(f"Unknown or unreviewed card in labels: {row['entry_id']}")
        examples.append((features(row["query"], row["language"], row["topic"], card), int(row["relevant"])))

    if len(examples) < 30 or len({y for _, y in examples}) != 2:
        raise SystemExit("Need at least 30 labelled pairs with both relevant and irrelevant examples.")

    rng = random.Random(42)
    rng.shuffle(examples)
    split = max(1, int(len(examples) * 0.8))
    train, test = examples[:split], examples[split:]
    if not test:
        raise SystemExit("Holdout set is empty.")

    means = [sum(row[j] for row, _ in train) / len(train) for j in range(len(FEATURES))]
    stds = []
    for j, mean in enumerate(means):
        variance = sum((row[j] - mean) ** 2 for row, _ in train) / len(train)
        stds.append(math.sqrt(variance) or 1.0)
    x_train = [[(row[j] - means[j]) / stds[j] for j in range(len(FEATURES))] for row, _ in train]
    y_train = [y for _, y in train]

    weights = [0.0] * len(FEATURES)
    bias = 0.0
    learning_rate = 0.04
    regularization = 0.02
    for _epoch in range(1800):
        grad = [0.0] * len(FEATURES)
        grad_bias = 0.0
        for x, y in zip(x_train, y_train):
            p = sigmoid(sum(w*v for w, v in zip(weights, x)) + bias)
            error = p - y
            for j, value in enumerate(x):
                grad[j] += error * value
            grad_bias += error
        n = float(len(x_train))
        weights = [w - learning_rate * (grad[j] / n + regularization * w) for j, w in enumerate(weights)]
        bias -= learning_rate * grad_bias / n

    def predict(row: list[float]) -> int:
        x = [(row[j] - means[j]) / stds[j] for j in range(len(FEATURES))]
        return int(sigmoid(sum(w*v for w, v in zip(weights, x)) + bias) >= 0.5)

    tp = fp = tn = fn = 0
    for row, y in test:
        pred = predict(row)
        if pred and y: tp += 1
        elif pred and not y: fp += 1
        elif not pred and not y: tn += 1
        else: fn += 1
    accuracy = (tp + tn) / len(test)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    model = {
        "model_name": "astrolife-local-relevance-ranker",
        "model_version": "0.1.0",
        "algorithm": "standardized logistic regression trained with batch gradient descent",
        "feature_names": FEATURES,
        "means": means,
        "standard_deviations": stds,
        "weights": weights,
        "bias": bias,
        "metrics": {"holdout_size": len(test), "accuracy": accuracy, "precision": precision,
                    "recall": recall, "f1": f1, "true_positive": tp, "false_positive": fp,
                    "true_negative": tn, "false_negative": fn},
        "training_examples": len(examples),
        "seed": 42,
        "trained_at": date.today().isoformat(),
        "note": "Seed labels are editorial examples, not user data. Metrics are preliminary and are not evidence of interpretation accuracy."
    }
    OUT.write_text(json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Model written: {OUT}")
    print(f"Pairs: {len(examples)} (train {len(train)}, holdout {len(test)})")
    print(f"Holdout: accuracy={accuracy:.3f}, precision={precision:.3f}, recall={recall:.3f}, F1={f1:.3f}")
    print("Do not promote this ranker until it passes a larger, independently labelled Persian/English test set.")

if __name__ == "__main__":
    main()
