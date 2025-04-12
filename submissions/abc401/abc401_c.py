import sys

sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
i = K

if i >= N:
    print(1)
    exit()

A = dict()
ans = K
while i < N:
    if i - K < K:
        later = ans - 1
    else:
        later = ans - A[i - K]
    later += ans
    later %= 10**9
    A[i] = later
    # print(A, ans)
    ans = later
    i += 1

# print(A)
print(ans)
