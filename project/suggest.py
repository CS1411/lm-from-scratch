"""Milestone 3: suggest next words and continue a partial response."""
from model import load

lm = load(n=3, k=0.1)

def continue_text(prefix, max_words=12):
    "Greedily extend `prefix` with the most likely next word until none/limit."
    words = prefix.lower().split()
    for _ in range(max_words):
        nxt = lm.suggest_next(" ".join(words), topk=1)[0]
        if nxt == "(no idea)":
            break
        words.append(nxt)
    return " ".join(words)

if __name__ == "__main__":
    for p in ["thanks for", "i have checked order", "your refund"]:
        print(f"{p!r}: {lm.suggest_next(p)} -> {continue_text(p)!r}")
