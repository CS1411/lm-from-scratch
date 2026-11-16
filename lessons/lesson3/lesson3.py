"""Lesson 3: MLE next-word probabilities and suggest_next()."""
import sys
from pathlib import Path

L2 = Path(__file__).resolve().parent.parent / "lesson2"
sys.path.insert(0, str(L2))
from lesson2 import to_sentences, build  # reuse Lesson 2

sents = to_sentences((L2 / "corpus.txt").read_text())
foll = build(sents, n=2)

def prob(context_word, word):
    c = foll[(context_word,)]; total = sum(c.values())
    return c[word] / total if total else 0.0  # MLE: count(ctx,w) / count(ctx)

def suggest_next(context_word, k=3):
    c = foll[(context_word,)]; total = sum(c.values())
    return [(w, round(n / total, 3)) for w, n in c.most_common(k)]

if __name__ == "__main__":
    print("P(coffee | morning) =", round(prob("morning", "coffee"), 3))
    print("P(train  | morning) =", round(prob("morning", "train"), 3))
    print()
    for w in ["i", "the", "morning", "good", "drink"]:
        print(f"after {w!r:9s}->", suggest_next(w))
    assert prob("morning", "coffee") == 0.125
    assert abs(sum(prob("the", w) for w in foll[("the",)]) - 1) < 1e-9
