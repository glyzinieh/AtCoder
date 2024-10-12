import math

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)] + [(0, 0)]
ans = 0
current = (0, 0)
for point in points:
    ans += math.sqrt((current[0] - point[0]) ** 2 + (current[1] - point[1]) ** 2)
    current = point
print(ans)
