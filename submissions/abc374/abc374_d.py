import math
import itertools

def calculate_time(x1, y1, x2, y2, speed):
  distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return distance / speed

class Edge:
  def __init__(self, A, B, C, D, speed):
    self.A, self.B, self.C, self.D = A, B, C, D
    self.time = calculate_time(A, B, C, D, speed)

N, S, T = map(int, input().split())

edges = list()

for _ in range(N):
  A, B, C, D = map(int, input().split())
  edges.append(Edge(A, B, C, D, T))
  
ans = float('inf')

# すべての順番をループ
for order in itertools.permutations(edges):
  # それぞれの向きでループ
  for bit in range(1 << N):
    time = 0
    current = (0, 0)
    # すべての辺をループ
    for i, edge in enumerate(order):
      if bit & (1 << i):
        x1, y1 = edge.A, edge.B
        x2, y2 = edge.C, edge.D
      else:
        x1, y1 = edge.C, edge.D
        x2, y2 = edge.A, edge.B
      time += calculate_time(*current, x1, y1, S)
      time += edge.time
      current = (x2, y2)
    ans = min(ans, time)
    
print(ans)