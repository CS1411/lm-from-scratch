"""Milestone 2: smoothed n-gram model (reuses NgramLM from Lesson 7)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "lessons" / "lesson7"))
from ngram_lm import NgramLM

def load(n=3, k=0.1):
    return NgramLM(n=n, k=k).fit((Path(__file__).parent / "corpus.txt").read_text())

if __name__ == "__main__":
    text = (Path(__file__).parent / "corpus.txt").read_text()
    sents = text.split("\n")
    cut = int(0.8 * len(sents)); tr, te = "\n".join(sents[:cut]), "\n".join(sents[cut:])
    for n in (2, 3):
        for k in (1.0, 0.1, 0.01):
            print(f"n={n} k={k:<5} held-out perplexity {NgramLM(n, k).fit(tr).perplexity(te):.2f}")
