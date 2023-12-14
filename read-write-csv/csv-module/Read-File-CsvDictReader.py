import csv

# File path of the CSV file
file_path = 'person.csv'

# Reading the data from the CSV file as dictionaries
data_dict_read = []
with open(file_path, mode='r', newline='', encoding='utf-8') as file:
  reader = csv.DictReader(file)
  for row in reader:
    data_dict_read.append(row)
    print(row)
