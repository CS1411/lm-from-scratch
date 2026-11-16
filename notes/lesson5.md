# Lesson 5 - The zero-probability problem
- MLE gives unseen pairs probability 0, which zeroes a whole sentence's probability and makes perplexity infinite.
- Add-k smoothing: P = (count + k) / (total + k * |V|). Every word gets a little mass.
- Trade-off: large k steals mass from observed words; use small k, or back-off / interpolation.
