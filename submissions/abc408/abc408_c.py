N, M = map(int, input().split())
joheki = [0 for _ in range(N*2)]
for _ in range(M):
  L, R = map(int, input().split())
  joheki[(L-1)*2] += 1
  joheki[(R-1)*2+1] -= 1
# print(joheki)
ans = float('inf')
current = 0
# debug = list()
for i, v in enumerate(joheki[:-1]):
  current += v
  if i%2 == 0 and current < ans:
    ans = current
  # debug.append(current)
# print(debug)
print(ans)