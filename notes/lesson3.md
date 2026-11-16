# Lesson 3 - Counts to probabilities (MLE)
- MLE: P(w | ctx) = count(ctx, w) / count(ctx). Learning an n-gram model is counting and dividing; no gradients.
- `suggest_next(word)` returns the top-k most likely next words: a phone suggestion bar.
- A bigram only sees one word of context, so suggestions are shallow.
