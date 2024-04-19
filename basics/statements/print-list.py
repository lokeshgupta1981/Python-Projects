num_list = [1, 2, 3, 4, 5]

# Print list without square brackets and separator
# Output: 1 2 3 4 5
print(*num_list)

# Print list with square brackets
# Output: [1, 2, 3, 4, 5]
print(num_list)
print(num_list, sep=", ", end="\n")
print('[{}]'.format(', '.join(map(str, num_list))))

# Print list with curly braces
# Output: {1, 2, 3, 4, 5}
print('{{{}}}'.format(', '.join(map(str, num_list))))

# Print list without any separator
# Output: 1 2 3 4 5
print(' '.join(map(str, num_list)))

# Print list separated by a comma
# Output: 1, 2, 3, 4, 5
print(*num_list, sep=", ")
print(', '.join(map(str, num_list)))

# Print list with a specific separator
# Output: 1 | 2 | 3 | 4 | 5
print(' | '.join(map(str, num_list)))

# Print list with custom formatting
# Output: Numbers: 1, 2, 3, 4, 5
print('Numbers: {}'.format(', '.join(map(str, num_list))))

# Print List Item Index and Value
# Output: Item index is 0 and Item is 1 ... and so on
for i in range(len(num_list)):
    print("Item index is", i, "and Item is", num_list[i])
