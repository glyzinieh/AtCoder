N = int(input())
t = 0
ans = 0
for _ in range(N):
  T, V = map(int, input().split())
  ans -= T-t
  if ans < 0:
    ans = 0
  ans += V
  t = T
print(ans)