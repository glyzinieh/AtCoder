N, m = map(int, input().split())
H = [*map(int, input().split())]

for i in range(N):
  m -= H[i]
  if m < 0:
    print(i)
    break
else:
  print(i+1)