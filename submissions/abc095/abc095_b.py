N, X = map(int, input().split())
remain = X
m = list()
ans = 0
for _ in range(N):
  mi = int(input())
  m.append(mi)
  remain -= mi
  ans += 1
ans += remain//min(m)
print(ans)
