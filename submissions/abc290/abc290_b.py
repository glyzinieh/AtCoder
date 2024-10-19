N, K = map(int, input().split())
S = input()

ans = ['x' for _ in range(N)]
count = 0

for i, Si in enumerate(S):
  if count >= K:
    break
  if Si == 'o':
    ans[i] = 'o'
    count += 1
    
print("".join(ans))