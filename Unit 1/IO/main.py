random_names = ['Mustafa', 'Bachir', 'Nacera', 'Ahmad', 'Rana']
with open('students_names.txt', 'r+') as f:
    names = f.readlines()
    previous = names[-1] if names else '-' # default value if the file is empty
    for name in random_names:
        # handling new line
        if previous[-1] == '\n' or previous[-1] == '-':
            f.write(name)
        else:
            f.write('\n' + name)
        previous = name

# read the n-first lines
with open('students_names.txt', 'r') as f:
    n = int(input('Enter the number of lines to show (from the beginning): '))
    for i in range(n):
        print(f.readline().strip())

# read the n-last lines
with open('students_names.txt', 'r') as f:
    n = int(input('Enter the number of lines to show (from the end): '))
    lines = f.readlines()
    if n > len(lines): n = len(lines)
    for i in range(len(lines) - n, len(lines)):
      print(lines[i].strip())

# checking whether a name x is in the file

with open('students_names.txt', 'r') as f:
  name = input('Enter a name to check if it is in the file: ')
  isInFile = name in f.read()
  print("The name exists in the file: ", isInFile)


# generating files
start = ord("A")
for i in range(26):
  f = open(f'{chr(i+start)}.txt', 'w')
  f.close()
