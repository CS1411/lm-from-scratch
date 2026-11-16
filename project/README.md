# Support Response Generator

CLI that suggests next words for customer-support replies, using a smoothed trigram model (pure Python).

- `make_corpus.py` - builds a synthetic support corpus, then anonymizes it (emails, phones, order ids masked). No real customer data.
- `model.py` - loads `NgramLM` (Lesson 7); running it compares n and add-k on held-out perplexity.
- `suggest.py` - next-word suggestions and greedy continuation of a partial reply.
- `cli.py` - `python cli.py "your refund"` or run with no args for interactive mode.

## Findings
On this small templated corpus, trigram beats bigram (held-out perplexity 1.56 vs 2.36 at k=0.01) and smaller k is better. Real support text is far less repetitive, so expect higher perplexity. Greedy continuation can drift between templates because trigram context is only two words.
