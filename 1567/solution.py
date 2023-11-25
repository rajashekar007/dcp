

def solve(ar):
  max_sum = 0
  sum = 0
  for a in ar:
    sum = sum + a
    if sum < 0:
      sum = 0
    max_sum = max(max_sum, sum)
  return max_sum

if __name__ == "__main__":
  a = map(int, input().split())
  print(solve(a))
  

      