"""Lesson 6: cross-entropy and perplexity on held-out text."""
import sys, math, random
from collections import Counter
from pathlib import Path

L2 = Path(__file__).resolve().parent.parent / "lesson2"
sys.path.insert(0, str(L2))
from lesson2 import to_sentences, to_tokens, build  # reuse Lesson 2

sents = to_sentences((L2 / "corpus.txt").read_text())
rng = random.Random(0); rng.shuffle(sents)
cut = int(0.8 * len(sents)); train, test = sents[:cut], sents[cut:]
V = set(t for s in train for t in to_tokens(s)) | {"</s>", "<unk>"}

def perplexity(foll, n, data, k=1.0):
    log_sum, N = 0.0, 0
    for s in data:
        toks = ["<s>"] * (n - 1) + to_tokens(s) + ["</s>"]
        for i in range(len(toks) - n + 1):
            ctx, w = tuple(toks[i:i + n - 1]), toks[i + n - 1]
            c = foll.get(ctx, Counter()); total = sum(c.values())
            p = (c[w] + k) / (total + k * len(V))  # add-k, so never zero
            log_sum += math.log(p); N += 1
    return math.exp(-log_sum / N)

if __name__ == "__main__":
    bi, tri = build(train, 2), build(train, 3)
    print(f"bigram  perplexity  ->  train {perplexity(bi, 2, train):6.1f}   held-out {perplexity(bi, 2, test):6.1f}")
    print(f"trigram perplexity  ->  train {perplexity(tri, 3, train):6.1f}   held-out {perplexity(tri, 3, test):6.1f}")
