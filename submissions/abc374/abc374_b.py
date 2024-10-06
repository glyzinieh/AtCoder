import itertools

S = input()
T = input()
if S == T:
  ans = 0
else:
  for i, (Si, Ti) in enumerate(itertools.zip_longest(S, T)):
    # print(Si, Ti)
    if Si != Ti:
      ans = i + 1
      break
  
print(ans)