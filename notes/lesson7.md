# Lesson 7 - Ship your predictive-text engine
- `NgramLM(n, k)` wraps Lessons 2-6: `fit(text)`, `suggest_next(text)`, `generate(seed)`, `perplexity(text)`.
- `suggest_next` never suggests `</s>`; add-k smoothing keeps perplexity finite.
- Portfolio project: rebuild on a large corpus (e.g. Project Gutenberg), compare n and k on held-out perplexity, check whether more data lets the trigram win, write up findings.
- Limit of n-grams: context beyond a couple of words causes sparsity; neural transformers fix that.
