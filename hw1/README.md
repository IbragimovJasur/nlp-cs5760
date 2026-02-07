# NLP Homework 1 (Jasurbek Ibragimov)

## Q1: Regular Expressions
Pattern matching exercises covering:
- **Task 1**: U.S. ZIP codes (`12345`, `12345-6789`, `12345 6789`)
- **Task 2**: Words not starting with a capital letter (includes apostrophes/hyphens)
- **Task 3**: Numbers with optional signs, thousands separators, decimals, and scientific notation
- **Task 4**: Email spelling variations (`email`, `e-mail`, `e mail`)
- **Task 5**: Interjections (`go`, `goo`, `gooo...`) with optional punctuation
- **Task 6**: Lines ending with `?` followed by optional closing quotes/brackets

## Q2: Byte Pair Encoding (BPE)

### 2.1 Manual BPE
Step-by-step manual demonstration of 8 BPE merge operations on a toy corpus (`low`, `lowest`, `newer`, `new`, `wider`), tracking vocabulary growth at each step.

### 2.2 Mini BPE Implementation
Python implementation of BPE learner and segmenter. Includes Q&A on:
- How subword tokenization solves OOV (out-of-vocabulary) problems
- Morpheme-aligned subwords (e.g., `er_` as comparative suffix)

### 2.3 English BPE
Applied BPE to an English paragraph with 30 merges. Analysis includes:
- Top 5 most frequent merges
- 5 longest subword tokens
- Reflection on learned subword types (prefixes, suffixes, stems, whole words)
- Pros/cons of subword tokenization

## Q3: Naive Bayes Theory
Explanations of key terms in Naive Bayes classification:
- **P(c)**: Prior probability of class `c`
- **P(d|c)**: Likelihood of document `d` given class `c`
- **P(c|d)**: Posterior probability of class `c` given document `d`
- Why P(d) can be ignored when comparing classes (constant denominator)

## Q4: Laplace Smoothing
Probability calculations with add-1 smoothing:
- Likelihood formula with Laplace smoothing
- P(predictable|−) with and without smoothing
- P(fun|−) for unseen words (zero-count handling)

## Q5: Uzbek Text Tokenization

### Tasks
1. **Naive vs Manual Tokenization**: Compared space-based splitting with morphologically-aware manual tokenization
2. **Tool Comparison**: NLTK's `word_tokenize` vs manual — NLTK struggles with apostrophes (o', g') and agglutinative suffixes
3. **Multiword Expressions**: Examples like *sog'ayib ketmoq* (recover), *Qo'shma Shtatlar* (United States), *O'rta Osiyo* (Central Asia)
4. **Reflection**: Apostrophes in Uzbek are letters, not punctuation; suffixes like `-ga`, `-dir` require "peeling" unlike English space-based tokenization

## Setup
```bash
pip install -r requirements.txt
```
