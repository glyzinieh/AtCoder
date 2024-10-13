N = int(input())
S = input()

T = 0
A = 0

for i in S:
  match i:
    case 'T':
      T += 1
    case 'A':
      A += 1
  if T > A:
    winner = 'T'
  elif A > T:
    winner = 'A'

print(winner)