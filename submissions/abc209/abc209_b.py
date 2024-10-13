N, X = map(int, input().split())
A = list(map(int, input().split()))
total = 0
for i, Ai in enumerate(A):
  if (i+1)%2 == 0:
    total += Ai-1
  else:
    total += Ai
print("Yes" if total <= X else "No")