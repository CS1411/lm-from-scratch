"""Lesson 2: tokenize corpus.txt and count n-grams."""
import re
from collections import Counter, defaultdict

def to_sentences(text):
    return [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]

def to_tokens(sentence):
    return re.findall(r"[a-z']+", sentence.lower())

def build(sents, n):
    """context (n-1 words) -> Counter of the words that follow it."""
    foll = defaultdict(Counter)
    for s in sents:
        toks = ["<s>"] * (n - 1) + to_tokens(s) + ["</s>"]
        for i in range(len(toks) - n + 1):
            foll[tuple(toks[i:i + n - 1])][toks[i + n - 1]] += 1
    return foll

if __name__ == "__main__":
    CORPUS = open("corpus.txt").read().strip()
    sents = to_sentences(CORPUS)
    tokens = [t for s in sents for t in to_tokens(s)]
    print("sentences:", len(sents), "| tokens:", len(tokens), "| vocabulary:", len(set(tokens)))
    foll = build(sents, n=2)
    print("after 'the':", foll[("the",)].most_common(6))
    print("after 'morning':", foll[("morning",)].most_common(5))
    print("sentence starts:", foll[("<s>",)].most_common(5))
    assert (len(sents), len(tokens), len(set(tokens))) == (60, 493, 169)
