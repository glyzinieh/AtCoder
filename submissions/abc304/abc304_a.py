N = int(input())
people = list()
for _ in range(N):
  stdin = input().split()
  Si = stdin[0]
  Ai = int(stdin[1])
  people.append((Si, Ai))
current = people.index(min(people, key=lambda x: x[1]))
for i in [*range(current, N)]+[*range(0, current)]:
  print(people[i][0])