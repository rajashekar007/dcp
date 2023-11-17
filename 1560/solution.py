def intersection(a, b):
  if b[0] < a[0]:
    return intersection(b, a)
  if a[1] < b[0]:
    return None
  else:
    return [max(a[0], b[0]), min(a[1], b[1])]
    
def solve():
  ll = [[0, 3], [2, 6], [3, 4], [6, 9]]
  ans = [ll[0]]
  n = len(ll)
  i = 1
  while i<n:
    overlap = intersection(ans[-1], ll[i])
    if(overlap == None):
      ans.append(ll[i])
    else:
      ans[-1] = overlap
    i += 1
  fans = []
  for a in ans:
    fans.append(a[0])
  print(fans)

if __name__ == "__main__":
  # ll = input().split(',')
  solve()