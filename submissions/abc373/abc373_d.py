from collections import deque


class Edge:
  def __init__(self, u, v, w):
    self.u = u
    self.v = v
    self.w = w


class Point:
  def __init__(self):
    self.connects = list()
    self.x = None
    
  def __str__(self):
    return str(self.x)
    
    
class Graph:
  def __init__(self, N):
    self.points = [Point() for _ in range(N)]
    self.edge_queue = deque()
    
  def add_edge(self, u:int, v:int, w:int):
    self.points[u].connects.append(Edge(u, v,  w))
    self.points[v].connects.append(Edge(v, u, -w))
    
  def append_edge_queue(self, point):
    for edge in point.connects:
      if self.points[edge.v].x is None:
        self.edge_queue.append(edge)
    
  def solve(self):
    for point in self.points:
      if point.x is not None:
        continue
      point.x = 0
      self.append_edge_queue(point)
      while self.edge_queue:
        edge = self.edge_queue.popleft()
        point_u, point_v, w = self.points[edge.u], self.points[edge.v], edge.w
        if point_v.x is not None:
          continue
        point_v.x = point_u.x + w
        self.append_edge_queue(point_v)
    return self.points
    
    
N, M = map(int, input().split())
graph = Graph(N)
for _ in range(M):
  u, v, w = map(int, input().split())
  graph.add_edge(u-1, v-1, w)
ans = graph.solve()
print(*ans)