
def solve(mice, holes):
  mice.sort()
  holes.sort()
  ans = 0
  for m,h in zip(mice, holes):
    ans = max(ans, abs(m-h))
  return ans

if __name__ == "__main__":
  mice = list(map(int, input().split(',')))
  holes = list(map(int, input().split(',')))
  best_max_steps = solve(mice, holes)
  print(best_max_steps)