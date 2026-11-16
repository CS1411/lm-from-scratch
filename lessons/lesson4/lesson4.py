"""Lesson 4: generate text by sampling from n-gram counts."""
import sys, random
from pathlib import Path

L2 = Path(__file__).resolve().parent.parent / "lesson2"
sys.path.insert(0, str(L2))
from lesson2 import to_sentences, build  # reuse Lesson 2

sents = to_sentences((L2 / "corpus.txt").read_text())

def generate(foll, n, seed=0, max_len=25):
    rng = random.Random(seed)
    ctx = ("<s>",) * (n - 1); out = []
    for _ in range(max_len):
        c = foll[ctx]
        if not c:
            break
        words, weights = zip(*c.items())
        nxt = rng.choices(words, weights=weights)[0]
        if nxt == "</s>":
            break
        out.append(nxt)
        ctx = (ctx + (nxt,))[-(n - 1):]
    return " ".join(out)

if __name__ == "__main__":
    bi, tri = build(sents, 2), build(sents, 3)
    print("BIGRAM (1 word of memory):")
    for s in range(4):
        print("  -", generate(bi, 2, seed=s))
    print("\nTRIGRAM (2 words of memory):")
    for s in range(4):
        print("  -", generate(tri, 3, seed=s))
    assert generate(bi, 2, seed=0) == generate(bi, 2, seed=0)  # seeded = reproducible
