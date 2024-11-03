H = [*map(int, open(0).readlines()[1].split())]
print(H.index(max(H))+1)