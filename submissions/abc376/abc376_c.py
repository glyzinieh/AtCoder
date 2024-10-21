N = int(input())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()))

added_box = None

for a in A:
  if B:
    b = B[-1]
    if a <= b:
      B.pop()
    else:
      if added_box is None:
        added_box = a
      else:
        added_box = -1
        break
  else:
    if added_box is None:
      added_box = a

print(added_box)
