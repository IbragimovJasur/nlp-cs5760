from collections import defaultdict

corpus = [
    "<s> I love NLP </s>",
    "<s> I love deep learning </s>",
    "<s> deep learning is fun </s>"
]
unigram_counts = defaultdict(int)
bigram_counts = defaultdict(int)

# counts words for both unigram and bigram
for sentence in corpus:
    tokens = sentence.split()
    for i in range(len(tokens)):
        unigram_counts[tokens[i]] += 1  # count unigram

        if i < len(tokens) - 1:         # count bigram
            bigram = (tokens[i], tokens[i+1])
            bigram_counts[bigram] += 1


# function to calculate bigram probability (MLE)
def get_bigram_prob(w_prev, w_curr):
    count_prev = unigram_counts[w_prev]
    count_bigram = bigram_counts[(w_prev, w_curr)]
    if count_prev == 0:
        return 0
    return count_bigram / count_prev


# function to calculate sentence probability
def calculate_sentence_prob(sentence):
    tokens = sentence.split()
    probability = 1.0

    # loop bigrams in the sentence
    for i in range(len(tokens) - 1):
        w_prev = tokens[i]
        w_curr = tokens[i+1]        
        prob = get_bigram_prob(w_prev, w_curr)
        probability *= prob

    return probability

# testing the function
s1 = "<s> I love NLP </s>"
s2 = "<s> I love deep learning </s>"

prob_s1 = calculate_sentence_prob(s1)
prob_s2 = calculate_sentence_prob(s2)
print(f"Probability of S1: {prob_s1:.4f}")
print(f"Probability of S2: {prob_s2:.4f}")
print()

# checking which one is more probable
if prob_s1 > prob_s2:
    print(f"The model prefers '{s1}'. Because prob of S1: {prob_s1:.4f} is bigger than S2: {prob_s2:.4f}")
elif prob_s2 > prob_s1:
    print(f"The model prefers: '{s2}'. Because prob of S2: {prob_s2:.4f} is bigger than S1: {prob_s1:.4f}")
else:
    print("The probabilities are equal.")
