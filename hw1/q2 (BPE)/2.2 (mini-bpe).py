from collections import Counter

# Initial corpus
corpus = {
    "l o w _": 5,
    "l o w e s t _": 2,
    "n e w e r _": 6,
    "n e w _": 2,
    "w i d e r _": 3
}
# Initial vocabulary contains all unique letters in the corpus
vocab = {letter for word in corpus.keys() for letter in word.split()}

# Number of merges need to be performed for this toy corpus
merges = []
num_of_merges = 12

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

    # print the results of the current step
    print(f"Step {step}:")
    print(f"Best pair: {best} with frequency {pairs[best]}")
    print(f"Merged: {merged}")
    print(f"Vocabulary size: {len(vocab)}")


# Segmenter in BPE
print("========= Segmenter in BPE ==========")
words = ["new", "newer", "lowest", "widest", "newestest"]
for word in words:
    # convert the word to a list of symbols
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





# ============================== Q&A ==============================
# Question: How subword tokens solved the OOV (out-of-vocabulary) problem. 
# Answer:
# No matter how big our corpus is, it's always possible to come across a word that hasn't been seen before.
# In subword learning & segmentation:
    # - When a model encounters an unseen word, it breaks it down into known sub-components or individual letters
    # - This allows the tokenizer to process any sequence of characters using the known sub tokens to form the unknown word
    # - Ex: "widest" was never in our training corpus, but BPE segments it as ['wid', 'e', 's', 't', '_']

# Question:	One example where subwords align with a meaningful morpheme (e.g., er_ as English agent/comparative suffix).
# Answer:
# It's the suffix "ing_", which often appears frequently across many verbs to denote a continuous action. Ex: "running", "walking", "swimming", etc.

