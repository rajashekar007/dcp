

def min_jumps(ar):
  n = len(ar)
  jumps = [n]*n
  jumps[0] = 0
  for i in range(0, n):
    j = 1
    while j <= ar[i] and i+j < n:
      jumps[i+j] = min(jumps[i+j], jumps[i] + 1)
      j += 1
  
  return jumps[n-1]

if __name__ == "__main__":
  ar = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
  print(min_jumps(ar))
      