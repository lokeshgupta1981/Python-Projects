import heapq
import numpy as np

my_list = [4, 7, 1, 9, 3, 5, 8]

# using sorting

sorted_list = sorted(my_list)
largest_n_items = sorted_list[-3:]  # Replace 3 with the desired N
smallest_n_items = sorted_list[:3]  # Replace 3 with the desired N
print(f"Largest N items: {largest_n_items}")
print(f"Smallest N items: {smallest_n_items}")

# using heapq

largest_n_items = heapq.nlargest(3, my_list)
smallest_n_items = heapq.nsmallest(3, my_list)
print(f"Largest N items: {largest_n_items}")
print(f"Smallest N items: {smallest_n_items}")

# using numpy array
my_array = np.array([4, 7, 1, 9, 3, 5, 8, 10, 80, 100, -4, -5, -1])

largest_n_items = np.partition(my_array, -5)[-5:]  # Replace 3 with the desired N
smallest_n_items = np.partition(my_array, 5)[:5]  # Replace 3 with the desired N

print(f"Largest N items: {largest_n_items}")
print(f"Smallest N items: {smallest_n_items}")
