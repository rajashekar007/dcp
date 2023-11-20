# If there are (M-1)(->) & (N-1)(|)
#                               (V)
# then it's (M+N-2)!/(M-1)!(N-1)!

def factorial(f):
  if f == 1 or f == 0:
    return f
  return f * factorial(f-1)

def solve(m, n):
  return int(factorial(m+n-2)/(factorial(m-1) * factorial(n-1)))

if __name__ == "__main__":
  m = int(input())
  n = int(input())
  print(solve(m, n))