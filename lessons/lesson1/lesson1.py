"""Lesson 1: a language model = P(next word | previous words).
Simplest version: condition on ONE previous word, by counting."""
from collections import Counter

corpus = "the cat sat on the mat . the cat ate the fish . the dog sat on the rug .".split()

def next_word_probs(prev):
    # count which words follow `prev`, then normalise counts to probabilities
    follows = Counter(b for a, b in zip(corpus, corpus[1:]) if a == prev)
    total = sum(follows.values())
    return {w: c / total for w, c in follows.items()}

if __name__ == "__main__":
    for prev in ["the", "cat", "sat"]:
        p = next_word_probs(prev)
        print(f"P(next | {prev!r}) =", {w: round(x, 2) for w, x in p.items()})
        assert abs(sum(p.values()) - 1) < 1e-9  # a distribution sums to 1
    best = max(next_word_probs("the").items(), key=lambda kv: kv[1])[0]
    print("suggest after 'the':", best)
