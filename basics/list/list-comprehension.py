import random

# Simple for-loop
even_numbers = []
for x in range(10):
  if x % 2 == 0:
    even_numbers.append(x)
print(even_numbers)  # [0, 2, 4, 6, 8]

# Equivalent list comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

# random numbers

numbers = [random.random() for _ in range(10)]
randoms = [x for x in numbers if x >= 0.5]
print(randoms)

# If-else with list comprehension

labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(labels)

# Two Lists Comprehension

list1 = [1, 2, 3]
list2 = [3, 2, 1]

combined = [(x, y) for x in list1 for y in list2 if x != y]

print(combined)


