P = map(int, input().split())
alphabets = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
for Pi in P:
  ans += alphabets[Pi-1]
print(ans)