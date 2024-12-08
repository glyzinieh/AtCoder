S = input()
ans = str()
for Si in S:
  if not (Si == 'a' or Si == 'e' or Si == 'i' or Si == 'o' or Si == 'u'):
    ans += Si
print(ans)