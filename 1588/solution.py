
def number_of_ways(mat):
  row = len(mat)
  if row == 0:
    return 0
  col = len(mat[0])
  if mat[0][0] == 1 or mat[row-1][col-1] == 1:
    return 0
  ways = [[0]*col for i in range(row)]
  # ways[i][j] = ways[i-1][j] + ways[i][j-1] if mat[i][j] == 0 else 0
  ways[0][0] = 1
  for i in range(row):
    for j in range(col):
      if i == 0 and j == 0:
        continue
      ways[i][j] = (ways[i-1][j] if i>0 else 0) + \
                   (ways[i][j-1] if j>0 else 0) \
                    if mat[i][j] == 0 else 0
  
  return ways[row-1][col-1]


if __name__ == "__main__":
  mat = [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
  print(number_of_ways(mat))
  