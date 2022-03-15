try:
  a = 12
  s = "hello"
  print(a+s)
except TypeError:
  print(str(a) + str(s))
