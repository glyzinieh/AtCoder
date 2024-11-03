N, P, Q = map(int, input().split())
min_D = min(map(int, input().split()))
after_discount = Q + min_D
print(P if P < after_discount else after_discount)
