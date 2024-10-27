N, M = map(int, input().split())
maxL = {i: -1 for i in range(1, M+1)}
for _ in range(N):
  l, r = map(int, input().split())
  maxL[r] = max(maxL[r], l)

ans = 0
l = 1
for r in range(1, M+1):
  while l <= maxL[r]:
    l += 1
  ans += r - l + 1
print(ans)
