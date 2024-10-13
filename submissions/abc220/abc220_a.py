A, B, C = map(int, input().split())

num = B//C
ans = C * num
if ans >= A:
  print(ans)
else:
  print(-1)