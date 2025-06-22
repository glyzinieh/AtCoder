N = int(input())
D = map(int, input().split())
distance = 0
distances = [0]
for i in D:
    distance += i
    distances.append(distance)
for i in range(0, N):
    ans = list()
    for j in range(i+1, N):
        ans.append(distances[j]-distances[i])
    print(*ans)