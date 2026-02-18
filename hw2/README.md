# NLP Homework 2 (Jasurbek Ibragimov)

---

## Repository Structure

```
hw2/
├── part2.py          # Bigram Language Model (MLE)
├── q5.py             # Confusion Matrix — Precision & Recall
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## Part 2 — Bigram Language Model (`part2.py`)

### Objective

Build a **bigram language model** using Maximum Likelihood Estimation (MLE) and use it to compute and compare the probabilities of two sentences.

### Approach

1. **Corpus** — Three sentences are used as training data:

   ```
   <s> I love NLP </s>
   <s> I love deep learning </s>
   <s> deep learning is fun </s>
   ```

2. **Counting** — The script iterates over the corpus and collects:
   - **Unigram counts** — frequency of each individual token.
   - **Bigram counts** — frequency of each consecutive token pair.

3. **Bigram Probability (MLE)** — For a word *w* given the previous word *w₋₁*:

   ```
   P(w | w₋₁) = Count(w₋₁, w) / Count(w₋₁)
   ```

4. **Sentence Probability** — The probability of a full sentence is the product of all its bigram probabilities:

   ```
   P(S) = ∏ P(wᵢ | wᵢ₋₁)
   ```

5. **Comparison** — Two test sentences are evaluated:
   - **S1:** `<s> I love NLP </s>`
   - **S2:** `<s> I love deep learning </s>`

### Output

```
Probability of S1: 0.3333
Probability of S2: 0.1667

The model prefers '<s> I love NLP </s>'. Because prob of S1: 0.3333 is bigger than S2: 0.1667
```

### Interpretation

S1 is preferred by the model because its bigram chain encounters higher individual probabilities. Even though S2 is a longer sentence (more bigrams to multiply), the key differentiator is the transition probabilities along each path. S1's shorter path results in fewer multiplications and higher cumulative probability.

---

## Question 5 — Confusion Matrix Evaluation (`q5.py`)

### Objective

Given a **3 × 3 confusion matrix** for a multi-class classifier (Cat, Dog, Rabbit), compute **per-class precision and recall**, **macro-averaged**, and **micro-averaged** metrics.

### Confusion Matrix

|  | **Actual Cat** | **Actual Dog** | **Actual Rabbit** |
|---|---|---|---|
| **Predicted Cat** | 5 | 10 | 5 |
| **Predicted Dog** | 15 | 20 | 10 |
| **Predicted Rabbit** | 0 | 15 | 10 |

### Formulas

| Metric | Formula |
|--------|---------|
| **Precision (per class)** | TP / Row Sum (total predicted as that class) |
| **Recall (per class)** | TP / Column Sum (total actual of that class) |
| **Macro Precision** | Average of all per-class precisions |
| **Macro Recall** | Average of all per-class recalls |
| **Micro Precision** | Total TP / Total Samples |
| **Micro Recall** | Total TP / Total Samples |

### Output

```
Precision & Recall Results
Class: Cat. Precision: 0.250. Recall = 0.250
Class: Dog. Precision: 0.444. Recall = 0.444
Class: Rabbit. Precision: 0.400. Recall = 0.400

Macro-Averaged Results
Macro Precision: 0.365
Macro Recall: 0.365

Micro-Averaged Results
Micro Precision: 0.389
Micro Recall: 0.389
```

### Interpretation

- **Cat** has the lowest precision and recall (0.250), meaning the classifier struggles the most with this class.
- **Dog** achieves the highest per-class scores (0.444), making it the easiest class for the model to identify.
- **Macro averages** (0.365) treat all classes equally, while **micro averages** (0.389) weight by total sample counts — both indicate moderate overall performance with room for improvement.

---

## How to Run

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scripts
python part2.py
python q5.py
```

---

## Dependencies

- **Python 3.10+**
- **NumPy 2.4.2** (used in `q5.py`)

All dependencies are listed in `requirements.txt`.

