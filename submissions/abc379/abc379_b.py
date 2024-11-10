N, K = map(int, input().split())
S = input()

ans = 0
current = 0
for Si in S:
  if Si == 'O':
    current += 1
    if current == K:
      ans += 1
      current = 0
  else:
    current = 0
print(ans)