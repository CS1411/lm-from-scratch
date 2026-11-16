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

# --- Lesson text: hand-made table + suggest() ---
next_word = {
    "the": {"morning": 0.30, "train": 0.20, "park": 0.15, "city": 0.10, "weekend": 0.08},
    "good": {"book": 0.5, "coffee": 0.5},
}

def suggest(context, table, k=3):
    ranked = sorted(table.get(context, {}).items(), key=lambda kv: -kv[1])
    return ranked[:k]

if __name__ == "__main__":
    print("after 'the' :", suggest("the", next_word))
    print("after 'good':", suggest("good", next_word))
    assert suggest("the", next_word)[0] == ("morning", 0.3)

    # chain rule + bigram (Markov) shortcut: P(sentence) = prod P(w_i | w_{i-1})
    p = 1.0
    sent = "the cat sat on the mat".split()
    for a, b in zip(sent, sent[1:]):
        p *= next_word_probs(a).get(b, 0.0)
    print("P('the cat sat on the mat' | bigram) =", round(p, 4))
