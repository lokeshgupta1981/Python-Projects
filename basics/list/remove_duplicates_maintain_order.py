from collections import OrderedDict
import numpy as np
import pandas as pd


# Method 1 - Seen Set
def remove_duplicates_seen(lst):
  seen = set()
  result = []
  for item in lst:
    if item not in seen:
      seen.add(item)
      result.append(item)
  return result


# Method 2 - OrderedDict

def remove_duplicates_ordered(lst):
  return list(OrderedDict.fromkeys(lst))


# Method 3 Numpy Array

def remove_duplicates_numpy(lst):
  return list(np.unique(lst, return_index=True)[0])


# Method 4 Pandas Dataframe

def remove_duplicates_pandas(lst):
  return pd.DataFrame(lst, columns=['Original']).drop_duplicates()['Original'].tolist()


original_list = [5, 1, 2, 4, 2, 3, 1]

print(remove_duplicates_seen(original_list))
print(remove_duplicates_ordered(original_list))
print(remove_duplicates_numpy(original_list))
print(remove_duplicates_pandas(original_list))
