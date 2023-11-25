

def solve(n):
  cnt = 0
  cnt1s = 0
  while n:
    b = n&1
    cnt = b * (cnt + b)
    cnt1s = max(cnt1s, cnt)
    n = n>>1
  return cnt1s

if __name__ == "__main__":
  print(solve(156))