import re

# Input String
text = "HowToDoInJava.com"

# Specified substrings to check
start = "How"
end = "com"

# Using Regex

# Using regex to check if the string starts with the specified substring
if re.search(f"^{re.escape(start)}", text):
    print("String starts with the specified substring.")
else:
    print("String does not start with the specified substring.")

# Using regex to check if the string ends with the specified substring
if re.search(f"{re.escape(end)}$", text):
  print("String ends with the specified substring.")
else:
  print("String does not end with the specified substring.")

# Using regex to check if the string starts and ends with the specified substring
if re.match(f"^{re.escape(start)}.*{re.escape(end)}$", text):
    print("String starts and ends with the specified substring.")
else:
    print("String does not start and end with the specified substring.")

# Methods startswith() and endswith()

# Check if the string starts with the specified substring
if text.startswith(start):
    print("String starts with the specified substring.")
else:
    print("String does not start with the specified substring.")

# Check if the string ends with the specified substring
if text.endswith(end):
    print("String ends with the specified substring.")
else:
    print("String does not end with the specified substring.")

# Check if the string starts and ends with the specified substring
if text.startswith(start) and text.endswith(end):
    print("String starts and ends with the specified substring.")
else:
    print("String does not start and end with the specified substring.")

# Slicing

# Check if the string starts with the specified substring using slicing
if text[:len(start)] == start:
    print("String starts with the specified substring.")
else:
    print("String does not start with the specified substring.")

if text[-len(end):] == end:
    print("String ends with the specified substring.")
else:
    print("String does not end with the specified substring.")

# in operator

# Check if the string starts with the specified substring using the in operator
if start in text:
    print("String starts with the specified substring.")
else:
    print("String does not start with the specified substring.")

# Check if the string ends with the specified substring using the in operator
if text[-len(end):] == end:
    print("String ends with the specified substring.")
else:
    print("String does not end with the specified substring.")