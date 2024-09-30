S = input()

ans = 0
last_Sx = S.index('A')

for i in 'BCDEFGHIJKLMNOPQRSTUVWXYZ':
  Sx = S.index(i)
  ans += abs(Sx-last_Sx)
  last_Sx = Sx
  
print(ans)