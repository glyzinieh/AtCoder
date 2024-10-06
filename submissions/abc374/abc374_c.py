N = int(input())
K = list(map(int, input().split()))

ans = float('inf')

# 全てのビットパターンを試す
for i in range(1 << N):
    A, B = 0, 0
    for j in range(N):
        if i & (1 << j):
            A += K[j]
        else:
            B += K[j]
    ans = min(ans, max(A, B))

print(ans)
