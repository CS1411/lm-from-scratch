"""Lesson 5: add-k (Laplace) smoothing so unseen pairs aren't impossible."""
import sys
from pathlib import Path

L2 = Path(__file__).resolve().parent.parent / "lesson2"
sys.path.insert(0, str(L2))
from lesson2 import to_sentences, to_tokens, build  # reuse Lesson 2

sents = to_sentences((L2 / "corpus.txt").read_text())
foll = build(sents, n=2)
V = set(t for s in sents for t in to_tokens(s)) | {"</s>"}  # vocabulary

def prob_mle(ctx, w):
    c = foll[(ctx,)]; total = sum(c.values())
    return c[w] / total if total else 0.0

def prob_addk(ctx, w, k=1.0):
    c = foll[(ctx,)]; total = sum(c.values())
    return (c[w] + k) / (total + k * len(V))

if __name__ == "__main__":
    print("MLE   P(coffee | drinks) =", prob_mle("drinks", "coffee"), " <- zero, so 'she drinks coffee' is 'impossible'")
    print("add-1 P(coffee | drinks) =", round(prob_addk("drinks", "coffee"), 5), " <- small but non-zero")
    print("add-1 P(green  | drinks) =", round(prob_addk("drinks", "green"), 5), " <- a word we DID see still ranks higher")
    assert prob_mle("drinks", "coffee") == 0 < prob_addk("drinks", "coffee") < prob_addk("drinks", "green")
    assert abs(sum(prob_addk("drinks", w) for w in V) - 1) < 1e-9  # still a distribution
