N, M = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

C = [(0, float('inf'))]
min_A = float('inf')

for i, Ai in enumerate(A):
  if Ai < min_A:
    C.append((i+1, Ai))
    min_A = Ai

C.append((-1, 0))

# print(C)

for Bj in B:
  wa = 0
  ac = len(C)-1
  while ac-wa > 1:
    wj = (wa+ac)//2
    if Bj >= C[wj][1]:
      ac = wj
    else:
      wa = wj
  print(C[ac][0])
