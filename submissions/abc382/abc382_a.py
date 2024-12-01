N, D = map(int, input().split())
S = list(input())
ans = 0
for Si in S:
  if Si == '.':
    ans += 1
ans += D
print(ans)