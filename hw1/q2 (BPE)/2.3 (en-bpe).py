import re
from collections import Counter


paragraph = """
The sun is shining brightly today. Small birds sing songs in the green trees. 
A little dog is running fast on the grass and playing with a ball.
The children are playing in the park. Birds, children, and the dog are all having fun.
"""

# Tokenize: lowercase, remove punctuation, count frequencies
words = re.findall(r'[a-zA-Z]+', paragraph.lower())
word_freq = Counter(words)

# Create corpus: each word as space-separated chars + end marker "_"
corpus = {}
for word, freq in word_freq.items():
    corpus[" ".join(list(word)) + " _"] = freq

# Print the corpus with frequencies
print("Corpus with Frequencies:")
for word, freq in sorted(corpus.items(), key=lambda x: -x[1]):
    print(f"'{word}' -> {freq}")

# Initial vocabulary: all unique characters + end marker
vocab = {letter for word in corpus.keys() for letter in word.split()}
print("Initial Vocabulary: ", vocab)
# Initial Vocabulary:  {'y', 'l', 'h', 'c', 'g', 'p', 'd', 'v', 'k', 'o', 'w', 'm', 'n', 'b', 's', 'i', 'r', 'f', 'u', '_', 'a', 't', 'e'}

# Number of merges need to be performed
merges = []
num_of_merges = 30


print("========= Learner in BPE ==========")
for step in range(num_of_merges):
    # count pairs in the corpus
    pairs = Counter()
    for word, freq in corpus.items():
        syms = word.split()
        for i in range(len(syms) - 1):
            pairs[(syms[i], syms[i+1])] += freq

    # get the best pair
    best = max(pairs, key=lambda x: pairs[x])
    merged = best[0] + best[1]

    # merge the best pair in the corpus
    corpus = {word.replace(f"{best[0]} {best[1]}", merged): freq for word, freq in corpus.items()}
    vocab.add(merged)
    merges.append(best)

print("Final Vocabulary: ", vocab)
# Final Vocabulary:  {'y', 'l', 'ing_', 'play', 'h', 'birds_', 'bir', 'is_', 'c', 'th', 'g', 'the_', 'as', 'un_', 'and_', 'tl', 'ree', 'p', 'd', 'al', 'v', 'all_', 'dog_', 're', 'k', 'n_', 'o', 'e_', 'w', 's_', 'bird', 'm', 'a_', 'an', 'n', 'b', 'in', 's', 'pl', 'all', 'i', 'g_', 'r', 'ay', 'and', 'f', 'bi', 'u', '_', 'a', 't', 'e', 'do'}


print("Five Most Frequent Merges:")
# Sort merges by their frequency (stored during learning)
merge_freqs = []
temp_corpus = {" ".join(list(word)) + " _": freq for word, freq in word_freq.items()}
for i, m in enumerate(merges[:5]):
    pairs = Counter()
    for word, freq in temp_corpus.items():
        syms = word.split()
        for j in range(len(syms) - 1):
            pairs[(syms[j], syms[j+1])] += freq
    freq = pairs[m]
    print(f"{i+1}. '{m[0]}' + '{m[1]}' -> '{m[0]+m[1]}' (freq: {freq})")
    temp_corpus = {word.replace(f"{m[0]} {m[1]}", m[0]+m[1]): f for word, f in temp_corpus.items()}

print("Five Longest Subword Tokens:")
sorted_by_len = sorted(vocab, key=lambda x: -len(x))
for i, token in enumerate(sorted_by_len[:5]):
    print(f"{i+1}. '{token}' -> {len(token)}")

# Five Longest Subword Tokens:
# 1. 'birds_' -> 6
# 2. 'ing_' -> 4
# 3. 'play' -> 4
# 4. 'the_' -> 4
# 5. 'and_' -> 4


# Segmenter in BPE
print("========= Segmenter in BPE ==========")
words = ["bird", "green", "playing", "falling", "the"]
for word in words:
    syms = list(word) + ["_"]

    # merge the symbols in the word
    for p in merges:
        # iterate through the symbols in the word
        i = 0
        while i < len(syms) - 1:
            # if the symbols are the same as the pair, merge them
            if syms[i] == p[0] and syms[i+1] == p[1]:
                syms = syms[:i] + [p[0] + p[1]] + syms[i+2:]
            else:
                # if the symbols are not the same as the pair, move to the next symbol
                i += 1
    print(f"{word} -> {syms}")

# ========= Segmenter in BPE ==========
# bird -> ['bird', '_']
# green -> ['g', 'ree', 'n_']
# playing -> ['play', 'ing_']
# falling -> ['f', 'all', 'ing_']
# the -> ['the_']


# ============================== Reflection ==============================
# Q1: What kinds of subwords were learned (prefixes, suffixes, stems, whole words)?
# Suffixes: ing_, s_
# Stems: bird, play
# Whole words: the_, birds_, dog_, and_, is_
# Common patterns: th, ree, ay, all

# Q2: Two concrete pros/cons of subword tokenization for the above English paragraph
#   - pros: handles unseen words effectively: "falling" segments into ['f', 'all', 'ing_']
#   - pros: reduces vocabulary size while preserving meaning: common morphemes like 'ing_', 's_', 'ree', 'all' are reused
#   - cons: splits can be arbitrary (ex: 'tl' from "little" — not a very meaningful unit)
