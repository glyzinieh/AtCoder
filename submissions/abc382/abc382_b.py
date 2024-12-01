N, D = map(int, input().split())
S = [*reversed([*input()])]

for d in range(D):
  S[S.index('@')] = '.'
  
print(''.join(reversed(S)))