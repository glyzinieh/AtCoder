p = [*map(int, [*open(0)][1:])]
min_p = p.pop(p.index(max(p)))
print(int(sum(p)+ min_p/2))