
def solve(mat, lt, gt):
  ans = 0
  if(len(mat) == 0):
    return ans
  row, col = len(mat), len(mat[0])
  i, j = row-1, 0
  while i>=0:
    while j<col:
      if mat[i][j] > gt:
        break
      j += 1
    ans += (col - j)
    i -= 1
  
  i, j = row-1, 0
  while i>=0:
    while j<col:
      if mat[i][j] >= lt:
        break
      j += 1
    ans += (j)
    i -= 1
  return ans
  


if __name__ == "__main__":
  mat = [[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
  lt = 6
  gt = 23
  ans = solve(mat, lt, gt)
  print(ans)