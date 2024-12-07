from collections import deque

class Cell:
  def __init__(self, x, y, cat):
    self.x = x
    self.y = y
    self.cat = cat
    self.distance = float('inf')

class Grid:
  def __init__(self, H, W, D):
    self.H = H
    self.W = W
    self.D = D
    self.cells = dict()
    self.humidifiers = list()

  def add_cell(self, x, y, cat):
    cell = Cell(x, y , cat)
    self.cells[(x, y)] = cell
    if cat == 'H':
      cell.distance = 0
      self.humidifiers.append(cell)

  def get_adjacent_cells(self, cell):
    adjacent_cells: list[Cell] = list()
    if cell.x - 1 >= 0:
      next_cell = self.cells[(cell.x - 1, cell.y)]
      if next_cell.cat == '.':
        adjacent_cells.append(next_cell)
    if cell.x + 1 < self.H:
      next_cell = self.cells[(cell.x + 1, cell.y)]
      if next_cell.cat == '.':
        adjacent_cells.append(next_cell)
    if cell.y - 1 >= 0:
      next_cell = self.cells[(cell.x, cell.y - 1)]
      if next_cell.cat == '.':
        adjacent_cells.append(next_cell)
    if cell.y + 1 < self.W:
      next_cell = self.cells[(cell.x, cell.y + 1)]
      if next_cell.cat == '.':
        adjacent_cells.append(next_cell)
    return adjacent_cells

  def bfs(self):
    for humidifier in self.humidifiers:
      q = deque([humidifier])
      while q:
        current_cell: Cell = q.popleft()
        distance = current_cell.distance + 1
        if distance > self.D:
          break
        next_cells = self.get_adjacent_cells(current_cell)
        for next_cell in next_cells:
          next_cell.distance = min(next_cell.distance, distance)
          q.append(next_cell)

H, W, D = map(int, input().split())

grid = Grid(H, W, D)

for i in range(H):
  row = input()
  for j in range(W):
    cat = row[j]
    grid.add_cell(i, j, cat)

grid.bfs()

ans = len([cell for cell in grid.cells.values() if cell.distance <= D])
print(ans)
