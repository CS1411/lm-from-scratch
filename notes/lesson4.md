# Lesson 4 - Make it write
- Generate by sampling: start at `<s>`, draw next word from the distribution, append, repeat until `</s>`.
- Always taking the top word gets stuck in loops; sampling gives variety.
- Bigram text wanders; trigram reads better but mostly copies corpus phrases (trigrams seen once).
- More context = more fluent but needs far more data.
