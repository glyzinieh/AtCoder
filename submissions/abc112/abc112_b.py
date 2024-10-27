N, T = map(int, input().split())
c = list()
for _ in range(N):
  ci, ti = map(int, input().split())
  if ti <= T:
    c.append(ci)
if c:
  print(min(c))
else:
  print('TLE')