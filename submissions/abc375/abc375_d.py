import re
S = input()
ans = 0
for i, Si in enumerate(S[:-2]):
  Si_match = [m.span() for m in re.finditer(Si, S[i+2:])]
  for k, _ in Si_match:
    ans += k+1
print(ans)
