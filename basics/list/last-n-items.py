from collections import deque
import numpy as np

# Using deque
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_n_items = deque(my_list, maxlen=3)
print(last_n_items)

# Using list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_n_items_list = my_list[-5:]
print(last_n_items_list)

# Using numpy array
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
last_n_items_array = my_list[-5:]
print(last_n_items_list)

# Using string
my_string = "Hello, World!"
last_n_chars = my_string[-6:]
print(last_n_chars)
