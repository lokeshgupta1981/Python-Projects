import csv

# Sample data to be written to the CSV file
data = [
  ['Name', 'Age', 'City', 'Occupation', 'Email'],
  ['Alice', 29, 'New York', 'Engineer', 'alice@example.com'],
  ['Bob', 35, 'Los Angeles', 'Doctor', 'bob@example.com'],
  ['Charlie', 45, 'Chicago', 'Teacher', 'charlie@example.com'],
  ['Diana', 32, 'Miami', 'Artist', 'diana@example.com']
]

# File path for the CSV file
file_path = 'person_new.csv'

# Writing the data to the CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
  writer = csv.writer(file)
  writer.writerows(data)
