N = int(input())
H = [*map(int, input().split())]
H1 = H[0]
for i, Hi in enumerate(H):
  if Hi > H1:
    print(i+1)
    break
else:
  print(-1)