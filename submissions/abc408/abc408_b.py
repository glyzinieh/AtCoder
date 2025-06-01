N = int(input())
A = sorted(list({*map(int, input().split())}))
print(len(A))
print(*A)