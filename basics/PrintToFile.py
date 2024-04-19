from contextlib import redirect_stdout

with open('c:/temp/output.txt', 'w') as file:
  with redirect_stdout(file):
    print("This message will be written to a file.")

print('This message will be written to the screen.')
