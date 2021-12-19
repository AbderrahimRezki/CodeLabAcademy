random_names = ['Mustafa', 'Bachir', 'Nacera', 'Ahmad', 'Rana']
with open('students_names.txt', 'r+') as f:
    names = f.readlines()                                                       # TASK 1: the file's content in a single variable
    previous = names[-1] if names else '-' # default value if the file is empty
    for name in random_names:                                                   # TASK 2: writing random names to the file          
        # handling new line
        if previous[-1] == '\n' or previous[-1] == '-':
            f.write(name)
        else:
            f.write('\n' + name)
        previous = name


with open('students_names.txt', 'r') as f:                                      # TASK 3: Print first N names
    n = int(input('Enter the number of lines to show (from the beginning): '))
    for i in range(n):
        print(f.readline().strip())

with open('students_names.txt', 'r') as f:                                      # TASK 3: Print last N names
    n = int(input('Enter the number of lines to show (from the end): '))
    lines = f.readlines()
    if n > len(lines): n = len(lines)
    for i in range(len(lines) - n, len(lines)):
      print(lines[i].strip())


with open('students_names.txt', 'r') as f:
  name = input('Enter a name to check if it is in the file: ')
  isInFile = name in f.read()                                                   # TASK 4: Check name in file
  print("The name exists in the file: ", isInFile)


start = ord("A")
for i in range(26):                                                             # TASK 5: Generating files
  f = open(f'{chr(i+start)}.txt', 'w')
  f.close()
