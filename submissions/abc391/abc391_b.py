N, M = map(int, input().split())
S = [[*input()] for _ in range(N)]
T = [[*input()] for _ in range(M)]

for i in range(N-M+1):
  for j in range(N-M+1):
    # print(i, j)
    if S[i][j] == T[0][0]:
      for k in range(M):
        for l in range(M):
          if S[i+k][j+l] != T[k][l]:
            break
        else:
          continue
        break
      else:
        print(f'{i+1} {j+1}')
        break
  else:
    continue
  break