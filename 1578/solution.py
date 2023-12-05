
def find_min_max(ar):
  aMin = 0
  aMax = 0
  n = len(ar)
  start = 0

  if n%2 == 1:
    aMin = ar[0]
    aMax = ar[0]
    start = 1
  else:
    if ar[0] < ar[1]:
      aMin = ar[0]
      aMax = ar[1]
    else:
      aMin = ar[1]
      aMax = ar[0]
    start = 2

  for i in range(start, n - 1, 2):
    if ar[i] < ar[i+1]:
      aMin = min(aMin, ar[i])
      aMax = max(aMax, ar[i+1])
    else:
      aMin = min(aMin, ar[i+1])
      aMax = max(aMax, ar[i])
  return aMin, aMax

if __name__ == "__main__":
  arr = [3, 8, 2, 5, 1, 4, 7, 6]
  print(find_min_max(arr))



  
    