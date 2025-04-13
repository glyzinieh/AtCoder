S = input()
ans = 0
cnt = 0
for s in S:
  cnt += 1
  # 奇数文字目
  if cnt%2!=0:
    if s != 'i':
      ans += 1
      cnt += 1
  else:
    if s != 'o':
      ans += 1
      cnt += 1
if (len(S)+ans)%2!=0:
  ans += 1
print(ans)