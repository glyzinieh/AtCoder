M = int(input())
A = list()

A_i = range(10, -1, -1)
power = [3**i for i in A_i]

while M != 0:
  for i, i_power in zip(A_i, power):
    while M >= i_power:
      M -= i_power
      A.append(i)

print(len(A))
print(" ".join(map(str, A)))
