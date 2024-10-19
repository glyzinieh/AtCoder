def count_chars(s):
  chars = chars = {i:0 for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
  for i in s:
    chars[i] += 1
  return chars
  
S = input()
j = 1
left_chars  = count_chars(S[:1])
right_chars = count_chars(S[2:])

ans = 0
while j <= len(S)-2:
  # print({k:v for k, v in left_chars.items() if v!=0}, {k:v for k, v in right_chars.items() if v!=0})
  for key, value in left_chars.items():
    # if value and right_chars[key]:
    ans += value * right_chars[key]
  left_chars[S[j]]  += 1
  right_chars[S[j+1]] -= 1
  j += 1
print(ans)