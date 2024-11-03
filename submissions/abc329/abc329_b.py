N = int(input())
A = [*map(int, input().split())]
exclude_max = [i for i in A if i != max(A)]
print(max(exclude_max))