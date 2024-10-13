import re
A, B = map(int, input().split())
S = input()
if re.fullmatch(r'[0-9]{{{}}}-[0-9]{{{}}}'.format(A, B), S):
  print('Yes')
else:
  print('No')