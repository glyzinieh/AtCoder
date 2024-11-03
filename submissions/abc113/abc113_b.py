N = int(input())
T, A = map(int, input().split())
H = map(int, input().split())
min_diff = float('inf')
for i, Hi in enumerate(H):
  temp = T - Hi*0.006
  diff = abs(temp-A)
  if diff < min_diff:
    ans = i + 1
    min_diff = diff
print(ans)