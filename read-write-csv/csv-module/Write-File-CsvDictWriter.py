import csv

# Sample data in dictionary format
data_dicts = [
  {'Name': 'Alice', 'Age': 29, 'City': 'New York', 'Occupation': 'Engineer', 'Email': 'alice@example.com'},
  {'Name': 'Bob', 'Age': 35, 'City': 'Los Angeles', 'Occupation': 'Doctor', 'Email': 'bob@example.com'},
  {'Name': 'Charlie', 'Age': 45, 'City': 'Chicago', 'Occupation': 'Teacher', 'Email': 'charlie@example.com'},
  {'Name': 'Diana', 'Age': 32, 'City': 'Miami', 'Occupation': 'Artist', 'Email': 'diana@example.com'}
]

# File path for the new CSV file
file_path_dict_writer = 'person_dict_written.csv'

# Writing the data to the new CSV file using DictWriter
with open(file_path_dict_writer, mode='w', newline='', encoding='utf-8') as file:
  fieldnames = ['Name', 'Age', 'City', 'Occupation', 'Email']
  writer = csv.DictWriter(file, fieldnames=fieldnames)

  writer.writeheader()
  for row in data_dicts:
    writer.writerow(row)
