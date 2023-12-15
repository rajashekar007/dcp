
def min_jumps(ar):
  n = len(ar)
  if n < 1:
    return 0
  max_index = 0
  jumps = 1
  window_end = 0
  for i in range(0, n):
    print(i, ar[i], i+ar[i])
    if i + ar[i] >= n-1:
      return jumps
    if max_index + ar[max_index] < i + ar[i]:
        max_index = i
    if i == window_end:
      window_end = max_index + ar[max_index]
      jumps += 1
    
if __name__ == "__main__":
  ar = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
  print(min_jumps(ar))

  