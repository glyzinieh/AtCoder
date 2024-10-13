N = int(input())
S = input()
T = input()

ans = "No"

for x,y in zip(S,T):
  if x==y or (x=='1' and y=='l') or (x=='l' and y=='1') or (x=='0' and y=='o') or (x=='o' and y=='0'):
    pass
  else:
    break
else:
  ans = 'Yes'
  
print(ans)