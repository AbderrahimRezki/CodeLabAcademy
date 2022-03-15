def isPalindrome(s):
  s = s.replace(' ', '')
  s = s.lower()
  for i in range(len(s)//2):
    if s[i] != s[len(s) - i - 1]:
      return False
  return True

def isPrime(n):
  if n <= 0: return False
  for i in range(2, int(n**0.5)):
    if n%i == 0:
      return False
  return True

def isInRange(n, start, end):
  return (n >= start and n <= end)

def factorial(n):
  # Assuming that all inputs are positive integers
  if n == 0 or n == 1: return 1
  return n * factorial(n - 1)

def reverse(s):
  if len(s) < 2: return s
  last = s[-1]
  return last + reverse(s[:-1])

def sumLs(ls):
  # Assuming that all the list's elements are numbers
  count = 0
  for element in ls:
    count += element
  return count

def maxOfThree(a, b, c):
  if b > a: a = b
  if c > a: a = c
  return a
