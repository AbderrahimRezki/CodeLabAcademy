ls = [i for i in range(1, 300) if i % 2 == 0]
print("The length of the list: ", len(ls))
for number in ls:
  print(f"The square of {number} is: {number * number}")
print("Checking if 57 in ls", 57 in ls)
