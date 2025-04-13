N = int(input())
H = [*map(int, input().split())]
ans = H[0]
for i in range(N-1):
  if ans < H[i+1]:
    ans = H[i+1]
  else:
    break
print(ans)