ans = 0

for i in range(1,13):
  S_i = input()
  ans += 1 if len(S_i) == i else 0
  
print(ans)