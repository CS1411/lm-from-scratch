# Language Models from Scratch

A pure-Python implementation of an n-gram language model, built while working through the **Language Models from Scratch** course on [askThili](https://ask.thili.ai) (TinyVerse program). It starts from word counts and ends with a working next-word predictor, with no neural network and no third-party libraries.

The repository has two parts:

1. **`lessons/`** - one folder per course lesson, each building one idea on the previous one.
2. **`project/`** - the course project, **Support Response Generator**: a command-line tool that suggests the next words for a customer-support reply.

## Progress

| Item | Status |
|---|---|
| Lessons 1-7 | Done |
| Completion test | Passed |
| Project: Support Response Generator | Done |

## Quick start

Requirements: Python 3.8 or newer. There are no packages to install.

```bash
git clone https://github.com/CS1411/lm-from-scratch.git
cd lm-from-scratch

# try the project
cd project
python cli.py "thanks for"
```

Example output:

```text
next words: your, contacting
draft     : thanks for your patience
```

Run `python cli.py` with no arguments for interactive mode (press Enter on an empty line to quit).

## Repository layout

```text
lm-from-scratch/
├── lessons/
│   ├── lesson1/   hand-made probability table, suggest()
│   ├── lesson2/   corpus, tokenizer, n-gram counting
│   ├── lesson3/   counts to probabilities (MLE)
│   ├── lesson4/   text generation by sampling
│   ├── lesson5/   add-k (Laplace) smoothing
│   ├── lesson6/   cross-entropy and perplexity
│   └── lesson7/   NgramLM class: fit / suggest_next / generate / perplexity
├── notes/         short study notes for each lesson
├── project/       Support Response Generator (CLI)
└── README.md
```

## The lessons

| # | Topic | What it covers |
|---|---|---|
| 1 | What a language model is | A language model assigns P(next word given the words so far). The chain rule and the Markov assumption turn this into something we can count. |
| 2 | Count the n-grams | Tokenize a small corpus, add start and end markers, and count which words follow each context. |
| 3 | Counts to probabilities (MLE) | Maximum-likelihood estimates: count(context, word) / count(context). |
| 4 | Make it write | Generate text by sampling from the next-word distribution. |
| 5 | The zero-probability problem | Add-k (Laplace) smoothing so unseen word pairs are not impossible. |
| 6 | How good is it? | Cross-entropy and perplexity, measured on held-out text. |
| 7 | Ship the engine | Everything in one reusable `NgramLM` class. |

Run a lesson from its folder, for example:

```bash
cd lessons/lesson2
python lesson2.py
```

Lesson 2 reads `corpus.txt` from the current folder, so run it from inside `lessons/lesson2`. The other lessons reuse its code and locate the corpus themselves.

### Results from Lesson 6

On the small 60-sentence lesson corpus, with an 80/20 train/held-out split:

| Model | Train perplexity | Held-out perplexity |
|---|---|---|
| Bigram | 52.7 | 94.1 |
| Trigram | 60.6 | 115.8 |

Held-out perplexity is much higher than train perplexity, so the model partly memorizes. The trigram does worse on held-out text because 60 sentences are too few to cover two-word contexts.

## Project: Support Response Generator

A command-line tool that helps a customer-support agent draft replies. The agent types the start of a reply, and the tool shows the most likely next words and a short continuation.

| File | Purpose |
|---|---|
| `corpus.txt` | 399 synthetic support-reply lines (refunds, delivery, apologies, closings). |
| `make_corpus.py` | Builds the synthetic corpus and anonymizes it: emails, phone numbers and order IDs are masked. |
| `model.py` | Loads the `NgramLM` from Lesson 7. Run it to compare n and k on held-out data. |
| `suggest.py` | Next-word suggestions and greedy continuation of a partial reply. |
| `cli.py` | The command-line interface. |

```bash
cd project
python make_corpus.py     # optional: rebuild the corpus
python model.py           # compare n and k
python suggest.py         # sample suggestions
python cli.py "your refund"
```

### Results

Held-out perplexity (lower is better):

| n | k = 1.0 | k = 0.1 | k = 0.01 |
|---|---|---|---|
| 2 (bigram) | 4.52 | 2.60 | 2.36 |
| 3 (trigram) | 3.85 | 1.79 | **1.56** |

The CLI uses a trigram with k = 0.1.

### Limitations

- The corpus is **synthetic and templated**, with no real customer data. That is why perplexity is so low. Real support text is far less repetitive, so expect much higher numbers.
- A trigram only sees the last two words, so greedy continuation can drift from one template into another. For example, a reply that starts with "your refund" can end up talking about shipping.
- Placeholders such as `orderid` and `phonenum` appear in suggestions, because they are masked tokens in the corpus.
- Unseen words get only the small smoothed probability, so suggestions for unusual input are weak.

## Course

- Course: *Language Models from Scratch* (Build a Next-Word Predictor from Scratch), on askThili.
- Program: TinyVerse.
- Reading material: Jurafsky and Martin, *Speech and Language Processing*, Chapter 3 (N-gram Language Models); Shannon, *Prediction and Entropy of Printed English* (1951).
