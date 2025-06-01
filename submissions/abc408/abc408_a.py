N, S = map(int, input().split())
T = map(int, input().split())

last = 0
ans = 'No'

for Ti in T:
  if Ti >= last + S + 0.5:
    break
  last = Ti
else:
  ans = 'Yes'
  
print(ans)