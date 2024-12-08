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
        self.humidifiers = deque()

    def add_cell(self, x, y, cat):
        cell = Cell(x, y, cat)
        self.cells[(x, y)] = cell
        if cat == 'H':
            cell.distance = 0
            self.humidifiers.append(cell)

    def bfs(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while self.humidifiers:
            current_cell = self.humidifiers.popleft()
            current_distance = current_cell.distance + 1
            if current_distance > self.D:
                continue
            for dx, dy in directions:
                nx, ny = current_cell.x + dx, current_cell.y + dy
                if (nx, ny) in self.cells:
                    next_cell = self.cells[(nx, ny)]
                    if next_cell.cat == '.' and next_cell.distance > current_distance:
                        next_cell.distance = current_distance
                        self.humidifiers.append(next_cell)

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
