from collections import Counter

a = {'x': 1, 'y': 2, 'z': 3}
b = {'u': 1, 'v': 2, 'w': 3, 'x': 1, 'y': 2}

commonKeys = a.keys() & b.keys()
print(commonKeys)   # {'y', 'x'}

commonItems = a.items() & b.items()
print(commonItems)  # {('x', 1), ('y', 2)}

setA = set(a)
setB = set(b)
commonKeys = setA & setB
print(commonKeys)

commonKeys = setA.intersection(setB)
print(commonKeys)

commonKeys = (Counter(a) & Counter(b)).keys()
print(set(commonKeys))

commonItems = {key: a[key] for key in a if key in b}
print(commonItems)
