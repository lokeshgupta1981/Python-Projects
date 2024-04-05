from collections import Counter
import pandas as pd
import numpy as np

sequence = [1, 2, 3, 4, 1, 2, 1, 2, 1]
counter = Counter(sequence)
most_common = counter.most_common(2)  # Get top 2 most common items
print(most_common)

sequence = [1, 2, 3, 4, 1, 2, 1, 2, 1]
series = pd.Series(sequence)
most_common = series.value_counts().head(2)
print(most_common)

sequence = np.array([1, 2, 3, 4, 1, 2, 1, 2, 1])
unique, counts = np.unique(sequence, return_counts=True)
most_common_indices = np.argsort(-counts)[:2]
most_common = [(unique[i], counts[i]) for i in most_common_indices]
print(most_common)
