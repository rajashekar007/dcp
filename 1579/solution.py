
def kadanes_max_sub_array_sum(ar):
  cur_sum = 0
  max_sum = 0
  n = len(ar)
  # for j in range(1):
  for i in range(n):
    cur_sum = cur_sum + ar[i]
    if cur_sum < 0:
      cur_sum = 0
    max_sum = max(max_sum, cur_sum)
  return max_sum

def max_sub_array_rotate(ar):
  sum_no_wrap = kadanes_max_sub_array_sum(ar)
  total_sum = sum(ar)
  sum_wrap = total_sum + kadanes_max_sub_array_sum([-k for k in ar])
  return max(sum_wrap, sum_no_wrap)


if __name__ == "__main__":
  ar = [8, -1, 3, 4]
  print(max_sub_array_rotate(ar))
  ar = [-4, 5, 1, 0]
  print(max_sub_array_rotate(ar))