N = int(input())
S = input()
a = False
b = False
c = False
for i,s in enumerate(S):
  if s == 'A':
    a = True
  elif s == 'B':
    b = True
  elif s == 'C':
    c = True
  if a and b and c:
    print(i+1)
    break