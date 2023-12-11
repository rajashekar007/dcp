
class Iterator2D:
  def __init__(self, ar) -> None:
    self.array2d = ar
    self.x = -1
    self.y = 0

  def next(self) -> (int, int):
    cur_len = len(self.array2d[self.y])
    if self.x + 1 < cur_len:
      self.x += 1
    else:
      self.x = 0
      if self.y + 1 < len(self.array2d):
        self.y += 1
      else:
        raise Exception("reached end of array, no next element")
    
    return self.array2d[self.y][self.x]

  def has_next(self) -> bool:
    if self.x + 1 < len(self.array2d[self.y]):
      return True
    else:
      if self.y + 1 < len(self.array2d):
        return True
    return False

if __name__ == "__main__":
  ar = [[1, 2, 3, 4],
        [5, 6],
        [7, 8, 9, 10, 11],
        [12, 13, 14]]
  iter = Iterator2D(ar)
  while iter.has_next():
    print(iter.next())