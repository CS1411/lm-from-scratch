# Lesson 2 - Count the n-grams
- Corpus: 60 short sentences in `lessons/lesson2/corpus.txt` (493 tokens, 169-word vocabulary).
- Tokenize: lowercase, split into words; wrap each sentence in `<s>` ... `</s>` so the model learns starts and ends.
- `build(sents, n)` maps a context (n-1 words) to a Counter of the words that follow it.
- Those counters ARE the model: raw evidence of what follows what.
