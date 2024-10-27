grid = [[True]*8 for _ in range(8)]
for i in range(8):
  for j, S_ji in enumerate(input()):
    if S_ji == '#':
      # i行目
      for column in range(8):
        grid[i][column] = False

      # j列目
      for row in range(8):
        grid[row][j] = False
        
cnt = 0
for i in range(8):
  for j in range(8):
    if grid[i][j]:
      cnt += 1
print(cnt)
  