from math import sqrt

N = int(input())

for d in range(1, 10**6):
    if d**3 >= N:
        continue
    c = N - d**3
    if c % (3 * d):
        continue
    c /= 3 * d
    x = int((d + sqrt(d**2 + 4 * c)) / 2)
    if x**2 - d * x - c != 0:
        continue
    print(f"{x} {x-d}")
    break
else:
    print(-1)
