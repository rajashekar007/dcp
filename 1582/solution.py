from enum import Enum

class Color(Enum):
  NAA = 0
  RED = 1
  BLK = 2

class Grid:

  def __init__(self, rows, cols) -> None:
    self.rows = rows
    self.cols = cols
    self.grid = [[Color.NAA]*cols for _ in range(rows)]
  
  def drop(self, col, color):
    r = 0
    while r < self.rows:
      if self.grid[r][col] != Color.NAA:
        break
      r += 1
    if r == 0:
      raise Exception('invalid move')
    self.grid[r-1][col] = color  
    print(self)
  
  def __str__(self):
    s = ""
    for i in range(self.rows):
      s += " ".join(str(c) for c in self.grid[i])
      s += '\n'
    return s

class Player:
  def __init__(self, name, color) -> None:
    self.name = name
    self.disc = color
  def select_col(self, grid):
    print(grid)
    col = int(input(f'Please select col for player {self.name} :'))
    return col


class Connect4:
  def __init__(self) -> None:
    self.grid = Grid(7, 6)
    self.players = [Player("red_player", Color.RED), Player("black_player", Color.BLK)]
  
  def check4_h(self, i, j):
    cnt = 0
    color = self.grid.grid[i][j]
    while j < self.grid.cols and color == self.grid.grid[i][j]:
      cnt += 1
      j += 1
    return cnt == 4
      
  def check4_v(self, i, j):
    cnt = 0
    color = self.grid.grid[i][j]
    while i < self.grid.rows and color == self.grid.grid[i][j]:
      cnt += 1
      i += 1
    return cnt == 4
  
  def check4_d(self, i, j):
    cnt = 0
    color = self.grid.grid[i][j]
    while i < self.grid.rows and j < self.grid.cols and color == self.grid.grid[i][j]:
      cnt += 1
      i += 1
      j += 1
    return cnt == 4

  def consecutive_discs_found(self):
    for i in range(self.grid.rows):
      for j in range(self.grid.cols):
        if self.grid.grid[i][j] == Color.NAA:
          continue
        if self.check4_h(i, j) or self.check4_v(i, j) or self.check4_d(i, j):
          return True
    return False
        
  def is_grid_full(self):
    for j in range(self.grid.cols):
      if self.grid.grid[0][j] == Color.NAA:
        return False
    return True

  def play(self):
    turn = 0
    while True:
      col = self.players[turn].select_col(self.grid)
      self.grid.drop(col, self.players[turn].disc)
      if self.consecutive_discs_found():
        print(f"Winner is {self.players[turn].name}")
        break
      if self.is_grid_full():
        print("Game over")
        break
      turn = (turn + 1)%2
  
if __name__ == "__main__":
  game = Connect4()
  game.play()

