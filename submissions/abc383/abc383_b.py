import itertools

H, W, D = map(int, input().split())
S = list()
for h in range(H):
  S.append([*input()])

floors = list()
  
for h in range(H):
  for w in range(W):
    if S[h][w] == '.':
      floors.append((h,w))
    
ans = 0    
      
for hums in itertools.combinations(floors, 2):
  floor_in = set()
  for hum in hums:
    for floor in floors:
      if floor == hum:
        floor_in.add(floor)
      elif abs(floor[0]-hum[0]) + abs(floor[1]-hum[1]) <= D:
        floor_in.add(floor)
  ans = max(ans, len(floor_in))

print(ans)