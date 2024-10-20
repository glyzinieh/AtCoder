from collections import deque

class Point:
  def __init__(self):
    self.to = list()
    self.dist = None
    
class Graph:
  def __init__(self, n):
    self.points = [Point() for i in range(n)]
  
  def add_edge(self, a, b):
    self.points[a].to.append(b)
  
  def bfs(self):
    q = deque()
    self.points[0].dist = 0
    q.append(0)
    while q:
      a = q.popleft()
      a_point = self.points[a]
      # print(f"a: {a, a_point.dist}")
      for b in a_point.to:
        b_point = self.points[b]
        # print(f"b: {b, b_point.dist}")
        if b_point.dist == 0:
          return a_point.dist + 1
        if b_point.dist is not None:
          continue
        b_point.dist = a_point.dist + 1
        q.append(b)
    else:
      return -1
  
N, M = map(int, input().split())
g = Graph(N)
for _ in range(M):
  a, b = map(int, input().split())
  g.add_edge(a-1, b-1)
print(g.bfs())