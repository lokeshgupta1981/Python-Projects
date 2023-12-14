import csv

# File path of the CSV file
file_path = 'person.csv'

# Reading the data from the CSV file
with open(file_path, mode='r', newline='', encoding='utf-8') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)
