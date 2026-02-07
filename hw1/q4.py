# Given: P(−)=3/5, P(+)=2/5. Vocabulary size = 20.

# Task 1:
# Formula for the likelihood estimation with Laplace (add-1) smoothing:
# P(w[k] | c[j]) = (n[k] + a) / n + a|Vocab|, where
# denominator = n + a|Vocab| = 14 + 1 * 20 = 34


# Task 2:
# Without smoothing:
# P(predictable∣−) = 2 / 14 = 1/7

# With smoothing:
# P(predictable∣−) = (2 + 1) / 14 + 20 = 3/34


# Task 3:
# Compute P(fun∣−) if “fun” never appeared in any negative documents.
# P(fun|-) = (0 + 1) / 14 + 20 = 1/34
