import numpy as np

#           Cat  Dog  Rabbit
matrix = [ [5,   10,  5 ],  # Predicted Cat
           [15,  20,  10],  # Predicted Dog
           [0,   15,  10] ] # Predicted Rabbit

classes = ["Cat", "Dog", "Rabbit"]
conf_matrix = np.array(matrix)

precisions = {}
recalls = {}

# Compute Per-Class Metrics
total_tp = 0
for i, label in enumerate(classes):
    tp = conf_matrix[i, i]
    total_tp += tp

    # Precision = TP / Total Predicted (Row Sum)
    precision = tp / np.sum(conf_matrix[i, :])
    
    # Recall = TP / Total Actual (Column Sum)
    recall = tp / np.sum(conf_matrix[:, i])
    
    precisions[label] = precision
    recalls[label] = recall

# Compute Macro-Averages
macro_precision = sum(precisions.values()) / len(classes)
macro_recall = sum(recalls.values()) / len(classes)

# Compute Micro-Averages
total_samples = np.sum(conf_matrix)
micro_precision = total_tp / total_samples
micro_recall = total_tp / total_samples

# Print Results
print("Precision & Recall Results")
for label in classes:
   print(f"Class: {label}. Precision: {precisions[label]:.3f}. Recall = {recalls[label]:.3f}")

print()
print("Macro-Averaged Results")
print(f"Macro Precision: {macro_precision:.3f}")
print(f"Macro Recall: {macro_recall:.3f}")
print()

print("Micro-Averaged Results")
print(f"Micro Precision: {micro_precision:.3f}")
print(f"Micro Recall: {micro_recall:.3f}")
