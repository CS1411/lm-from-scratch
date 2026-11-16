# Lesson 1 - What a language model is
- A language model = P(next word | words so far). Autocomplete shows the top few; generation samples from it.
- Chain rule: P(w1..wm) = prod P(wi | w1..wi-1). Full history is impossible to estimate.
- Markov assumption: only the last n-1 words matter. Bigram uses 1 previous word, trigram uses 2.
- Result: an impossible problem becomes one solved by counting.
