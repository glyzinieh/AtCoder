S = input()
ans = 'No'
if S[0]=='<' and S[-1]=='>':
  for i in S[1:-1]:
    # print(i)
    if i != '=':
      break
  else:
    ans = 'Yes'
print(ans)