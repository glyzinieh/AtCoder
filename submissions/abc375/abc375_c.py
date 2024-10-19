N = int(input())
A = [list(input()) for _ in range(N)]
B = [[None]*N for _ in range(N)]

for x in range(N):
  for y in range(N):
    nx, ny = x, y
    times = min(x+1, y+1, N-x, N-y)%4
    for _ in range(times):
      nx, ny = ny, nx
      ny = N-1-ny
    B[nx][ny] = A[x][y]
    
for row in B:
  print("".join(row))