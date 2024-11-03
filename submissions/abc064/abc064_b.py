N = int(input())
a = sorted(map(int, input().split()))
current = a[0]
ans = 0
for ai in a:
  ans += ai - current
  current = ai
print(ans)