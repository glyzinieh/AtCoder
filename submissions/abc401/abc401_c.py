N, K = map(int, input().split())
i = K

if i > N:
    print(1)
    exit()

A = dict()
Ai = K % (10**9)
while i < N + 1:
    A[i] = Ai
    i += 1
    prev = Ai
    Ai -= A[i-K-1] if not i-K-1 < K else 1
    Ai += prev
    # print(prev, Ai)
    Ai %= 10**9

# print(A)
print(prev)
