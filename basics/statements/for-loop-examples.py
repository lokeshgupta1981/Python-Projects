names = ["alex", "brian", "charles"]
for x in names:
  print('Current name is :', x)

  mytuple = ("item1", "item1", "item3")

  for e in mytuple:
    print("Current item is", e)

colors_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

for key in colors_dict.keys():
  print(key)

for item in colors_dict.items():
  print(item)

myset = {"item1", "item2", "item3"}

for e in myset:
  print("Current item is", e)

name = "alex"
for x in name:
  print("Current char is", x)

for i in range(5):
	print(i)

names = ["alex", "brian", "charles"]

print("Loop started")

for x in names:
  print(x)
  if x == "brian":
  	break;

print("Loop ended")

names = ["alex", "brian", "charles"]

print("Loop started")

for x in names:
  if x == "brian":
  	continue;
  print(x)

print("Loop ended")

names = ["alex", "brian", "charles"]

for x in names:
  print(x)
else:
  print("No name is left in the list")