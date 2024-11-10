Q = int(input())
pots = list()
for _ in range(Q):
  query = input().split()
  if query[0] == '1':
    pots.append(0)
  elif query[0] == '2':
    T = int(query[1])
    pots = [pot+T for pot in pots]
  elif query[0] == '3':
    H = int(query[1])
    before = len(pots)
    pots = [pot for pot in pots if pot < H]
    print(before-len(pots))