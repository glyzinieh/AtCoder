N, C = map(int, input().split())
T = list(map(int, input().split()))
last = float('-inf')
ans = 0
for Ti in T:
  if Ti-last >= C:
    ans += 1
    last = Ti
print(ans)
