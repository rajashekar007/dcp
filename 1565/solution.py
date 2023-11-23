
def isPossible(ar, i, n, target_sum, dp):
  if target_sum < 0 or i == n:
    return 0
  if target_sum == 0:
    dp[i][target_sum] = 1
    return 1
  # print(i, target_sum)
  if dp[i][target_sum] != -1:
    return dp[i][target_sum]
  for j in range(i, n):
    if isPossible(ar, j+1, n, target_sum - ar[j], dp) or isPossible(ar, j+1, n, target_sum, dp):
      dp[i][target_sum] = 1
      return 1
  dp[i][target_sum] = 0
  return 0

def solve(ar):
  n = len(ar)
  total_sum = sum(ar)
  if total_sum % 2 !=0:
    return False
  
  target_sum = total_sum//2
  dp = [[-1]*(target_sum+1)]*n
  # print(len(dp), len(dp[0]))
  return isPossible(ar, 0, n, target_sum, dp)

if __name__ == "__main__":
  ar = [2, 8, 8, 2, 14]
  if solve(ar):
    print("Possible")
  else:
    print("ImPossible")

