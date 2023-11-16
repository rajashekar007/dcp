# import pdb
def find_closing_bracket(s):
  num_opening = 1
  ind = 1
  n = len(s)
  while(num_opening and ind < n):
    if s[ind] == ')':
      num_opening-=1
    elif s[ind] == '(':
      num_opening+=1
    ind += 1
  return ind


def height(tree):
  if tree == "0":
    return 0
  # that means tree will be (lr)
  lr = tree[1:-1]
  if lr[0] == '0':
    l, r = '0', lr[1:]
  else:
    closing_index = find_closing_bracket(lr)
    l, r = lr[:closing_index], lr[closing_index:]
    
  return max(height(l), height(r)) + 1

def solve():
  tree = input()
  h = height(tree)
  print(h)

if __name__ == '__main__':
  solve()