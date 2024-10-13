import sys
sys.setrecursionlimit(2000000)

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


class Point:
    def __init__(self):
        self.connects = []
        self.x = None

    def __str__(self):
        return str(self.x)


class Graph:
    def __init__(self, N):
        self.points = [Point() for _ in range(N)]

    def add_edge(self, u: int, v: int, w: int):
        self.points[u].connects.append(Edge(u, v, w))
        self.points[v].connects.append(Edge(v, u, -w))

    def dfs(self, point_u):
        """再帰的に接続された頂点に対して値を設定"""
        for edge in point_u.connects:
            point_v = self.points[edge.v]
            if point_v.x is None:
                point_v.x = point_u.x + edge.w
                self.dfs(point_v)

    def solve(self):
        for point in self.points:
            if point.x is None:  # まだ値が設定されていない場合
                point.x = 0  # 基準となる値を設定
                self.dfs(point)  # 再帰的に設定
        return self.points


# 入力の処理
N, M = map(int, input().split())
graph = Graph(N)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph.add_edge(u - 1, v - 1, w)

# 結果の出力
ans = graph.solve()
print(*ans)
