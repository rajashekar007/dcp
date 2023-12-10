
class Node:
  def __init__(self, val: int) -> None:
    self.left = None
    self.right = None
    self.val = val

def bottom_view_util(node, depth, hd, bottom_view_map):
  if node is None:
    return
  if hd in bottom_view_map:
    _, cur_depth = bottom_view_map[hd]
    if cur_depth < depth:
      bottom_view_map[hd] = (node.val, depth)
  else:
    bottom_view_map[hd] = (node.val, depth)
  bottom_view_util(node.left, depth + 1, hd - 1, bottom_view_map)
  bottom_view_util(node.right, depth + 1, hd + 1, bottom_view_map)
      

def print_bottom_view(root):
  bottom_view_map = {}
  bottom_view_util(root, 0, 0, bottom_view_map)
  sorted_hds = sorted(bottom_view_map.keys())
  bottom_view = []
  for hd in sorted_hds:
    val, _ = bottom_view_map[hd]
    bottom_view.append(val)
  print(bottom_view)

if __name__ == "__main__":
  root = Node(5)
  a = root.left = Node(3)
  b = root.right = Node(7)
  c = a.left = Node(1)
  d = a.right = Node(4)
  e = c.left = Node(0)
  b.left = Node(6)
  b.right = Node(9)
  b.right.left = Node(8)
  print_bottom_view(root)
  