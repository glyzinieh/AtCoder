S = input()

upper_count = 0
lower_count = 0

for i in S:
  if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    upper_count += 1
  else:
    lower_count += 1

if upper_count > lower_count:
  print(S.upper())
else:
  print(S.lower())