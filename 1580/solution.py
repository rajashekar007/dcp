
def max_divis_set(ar):
  n = len(ar)
  if n <= 1:
    return ar
  sar = ar
  sar.sort()
  divis_set = {}
  if sar[0] == 1:
    return ar
  else:
    divis_set[sar[0]] = [sar[0]]
  
  max_len, max_key = 1, sar[0]
  for i in range(1, n):
    divisible = False
    for l in divis_set.keys():
      if sar[i] % l == 0:
        divis_set[l].append(sar[i])
        if len(divis_set[l]) > max_len:
          max_len = len(divis_set[l])
          max_key = l
        divisible = True
        # break
    if not divisible:
      divis_set[sar[i]] = [sar[i]]
    
  return divis_set[max_key]

if __name__ == "__main__":
  ar = [3, 5, 10, 20, 21]
  print(max_divis_set(ar))
  ar = [3, 5, 15, 6]
  print(max_divis_set(ar))
  ar = [3, 5, 15, 20]
  print(max_divis_set(ar))
  ar = [1, 3, 6, 24]
  print(max_divis_set(ar))
  