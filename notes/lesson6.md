# Lesson 6 - Cross-entropy and perplexity
- PP = exp(-(1/N) * sum log P(wi | ctx)). Read as: how many equally likely words the model is torn between per step. Lower is better.
- Always measure on held-out text (80/20 split here), never the training text.
- Results: bigram train 52.7 / held-out 94.1; trigram train 60.6 / held-out 115.8.
- Train << held-out means partial memorization. Trigram loses on held-out because ~60 sentences are too sparse for 2-word contexts.
