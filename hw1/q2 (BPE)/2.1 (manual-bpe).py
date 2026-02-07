original_corpus = "low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new"
corpus = {
    "l o w _": 5,
    "l o w e s t _": 2,
    "n e w e r _": 6,
    "n e w _": 2,
    "w i d e r _": 3
}
vocabulary = ("_", "l", "o", "w", "e", "s", "t", "n", "r", "i", "d")

# ============================== Step 1 ==============================
pairs = {
    "lo": 7,
    "ow": 7,
    "w_": 7,
    "we": 8,
    "es": 2,
    "st": 2,
    "t_": 2,
    "ne": 8,
    "ew": 8,
    "er": 9,
    "r_": 9,    # most frequent pair 1: chosen to merge
    "wi": 3,
    "id": 3,
    "de": 3
}
merged_corpus = {
    "l o w _": 5,
    "l o w e s t _": 2,
    "n e w e r_": 6,
    "w i d e r_": 3,
    "n e w _": 2
}
vocabulary = ("_", "l", "o", "w", "e", "s", "t", "n", "r", "i", "d", "r_")

# ============================== Step 2 ==============================
pairs = {
    "lo": 7,
    "ow": 7,
    "w_": 7,
    "we": 8,
    "es": 2,
    "st": 2,
    "t_": 2,
    "ne": 8,
    "ew": 8,
    "er_": 9,    # most frequent pair 1: chosen to merge
    "wi": 3,
    "id": 3,
    "de": 3
}
merged_corpus = {
    "l o w _": 5,
    "l o w e s t _": 2,
    "n e w er_": 6,
    "n e w _": 2,
    "w i d er_": 3
}
vocabulary = ("_", "l", "o", "w", "e", "s", "t", "n", "r", "i", "d", "r_", "er_")

# ============================== Step 3 ==============================
pairs = {
    "lo": 7,
    "ow": 7,
    "w_": 7,
    "we": 2,
    "es": 2,
    "st": 2,
    "t_": 2,
    "ne": 8,    # most frequent pair 1: chosen to merge
    "ew": 8,
    "wer_": 6,
    "wi": 3,
    "id": 3,
    "der_": 3
}
merged_corpus = {
    "l o w _": 5,
    "l o w e s t _": 2,
    "ne w er_": 6,
    "ne w _": 2,
    "w i d er_": 3
}
vocabulary = ("_", "l", "o", "w", "e", "s", "t", "n", "r", "i", "d", "r_", "er_", "ne")

# ============================== Step 4 ==============================
pairs = {
    "lo": 7,
    "ow": 7,
    "w_": 7,
    "we": 2,
    "es": 2,
    "st": 2,
    "t_": 2,
    "new": 8,  # most frequent pair 1: chosen to merge
    "wer_": 6,
    "wi": 3,
    "id": 3,
    "der_": 3
}
merged_corpus = {
    "l o w _": 5,
    "l o w e s t _": 2,
    "new er_": 6,
    "new _": 2,
    "w i d er_": 3
}
vocabulary = ("_", "l", "o", "w", "e", "s", "t", "n", "r", "i", "d", "r_", "er_", "ne", "new")


# ============================== Step 5 ==============================
pairs = {
    "lo": 7,    # most frequent pair 1: chosen to merge
    "ow": 7,
    "w_": 5,
    "we": 2,
    "es": 2,
    "st": 2,
    "t_": 2,
    "newer_": 6,
    "new_": 2,
    "wi": 3,
    "id": 3,
    "der_": 3
}
merged_corpus = {
    "lo w _": 5,
    "lo w e s t _": 2,
    "new er_": 6,
    "new _": 2,
    "w i d er_": 3
}
vocabulary = ("_", "l", "o", "w", "e", "s", "t", "n", "r", "i", "d", "r_", "er_", "ne", "new", "lo")


# ============================== Step 6 ==============================
pairs = {
    "low": 7,    # most frequent pair 1: chosen to merge
    "w_": 5,
    "we": 2,
    "es": 2,
    "st": 2,
    "t_": 2,
    "newer_": 6,
    "new_": 2,
    "wi": 3,
    "id": 3,
    "der_": 3
}
merged_corpus = {
    "low _": 5,
    "low e s t _": 2,
    "new er_": 6,
    "new _": 2,
    "w i d er_": 3
}
vocabulary = ("_", "l", "o", "w", "e", "s", "t", "n", "r", "i", "d", "r_", "er_", "ne", "new", "lo", "low")


# ============================== Step 7 ==============================
pairs = {
    "low_": 5,
    "lowe": 2,
    "es": 2,
    "st": 2,
    "t_": 2,
    "newer_": 6,    # most frequent pair 1: chosen to merge
    "new_": 2,
    "wi": 3,
    "id": 3,
    "der_": 3
}
merged_corpus = {
    "low _": 5,
    "low e s t _": 2,
    "newer_": 6,
    "new _": 2,
    "w i d er_": 3
}
vocabulary = ("_", "l", "o", "w", "e", "s", "t", "n", "r", "i", "d", "r_", "er_", "ne", "new", "lo", "low", "newer_")


# ============================== Step 8 ==============================
pairs = {
    "low_": 5,    # most frequent pair 1: chosen to merge
    "lowe": 2,
    "es": 2,
    "st": 2,
    "t_": 2,
    "new_": 2,
    "wi": 3,
    "id": 3,
    "der_": 3
}
merged_corpus = {
    "low_": 5,
    "low e s t _": 2,
    "newer_": 6,
    "new _": 2,
    "w i d er_": 3
}
vocabulary = ("_", "l", "o", "w", "e", "s", "t", "n", "r", "i", "d", "r_", "er_", "ne", "new", "lo", "low", "newer_", "low_")

