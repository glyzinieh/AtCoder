N, Q = map(int, input().split())

pigeons = [i for i in range(N)]
holes = [1]*N

output = 0

for _ in range(Q):
  query = input().split()
  
  if query[0] == '1':
    P, H = map(lambda x: int(x)-1, query[1:])
    holes[pigeons[P]] -= 1
    if holes[pigeons[P]] == 1:
      output -= 1
    holes[H] += 1
    if holes[H] == 2:
      output += 1
    pigeons[P] = H
    
  elif query[0] == '2':
    print(output)
  