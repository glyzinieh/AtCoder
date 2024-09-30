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
