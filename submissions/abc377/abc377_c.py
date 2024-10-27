class Grid:
  def __init__(self, N):
    self.cnt = N ** 2
    self.never_cells = set()  # set に変更
    
  def add_attackable(self, i, j):
    if i >= 0 and i < N and j >= 0 and j < N:
      if (i, j) not in self.never_cells:
        self.never_cells.add((i, j))  # set に追加
        self.cnt -= 1

N, M = map(int, input().split())
grid = Grid(N)
for _ in range(M):
  i, j = map(lambda x: int(x)-1, input().split())
  grid.add_attackable(i, j)
  grid.add_attackable(i+2, j+1)
  grid.add_attackable(i+1, j+2)
  grid.add_attackable(i-1, j+2)
  grid.add_attackable(i-2, j+1)
  grid.add_attackable(i-2, j-1)
  grid.add_attackable(i-1, j-2)
  grid.add_attackable(i+1, j-2)
  grid.add_attackable(i+2, j-1)
print(grid.cnt)
