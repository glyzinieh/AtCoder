S = input()
ans = 'No'
for i in 'ABC':
  if i in S:
    continue
  else:
    break
else:
  ans = 'Yes'
print(ans)