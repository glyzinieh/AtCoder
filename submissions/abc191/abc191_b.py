N, X = input().split()
A = input().split()
ans = list()
for Ai in A:
  if Ai != X:
    ans.append(Ai)
print(" ".join(ans))