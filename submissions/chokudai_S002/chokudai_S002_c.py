N = int(input())
ans = 0
for _ in range(N):
  ans = max(ans, sum(map(int, input().split())))
print(ans)