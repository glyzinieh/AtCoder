N = int(input())
is_logined = False
ans = 0
for i in range(N):
  S = input()
  if S == 'login':
    is_logined = True
  elif S == 'logout':
    is_logined = False
  elif S == 'private':
    if is_logined is False:
      ans += 1
print(ans)
    