class Point:
    def __init__(self):
        self.next_to_points = list()
        
ans = 'No'
        
N, M = map(int, input().split())
if N != M:
    print(ans)
    exit()
    
graph = {i: Point() for i in range(1, N+1)}
# print(graph)

for _ in range(N):
    A_i, B_i = map(int, input().split())
    graph[A_i].next_to_points.append(B_i)
    graph[B_i].next_to_points.append(A_i)

# 現在の頂点A
# Aにつながる頂点が2つか
# うち1つをBとする

for i in range(1, N+1):
    if len(graph[i].next_to_points) != 2:
        print(ans)
        exit()

A = graph[1].next_to_points.pop()
# print(A)
graph[A].next_to_points.remove(1)

while A != 1:
    if len(graph[A].next_to_points) != 1:
        break
    B = graph[A].next_to_points.pop()
    # print(B, graph[B].next_to_points)
    graph[B].next_to_points.remove(A)
    A = B
else:
    if A == 1:
        ans = 'Yes'
        for i in range(1, N+1):
            if len(graph[i].next_to_points) != 0:
                ans = 'No'
                break

print(ans)
    