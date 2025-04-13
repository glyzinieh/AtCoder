N = int(input())
A = input().split()

left_set = set()
left_lst = list()
left_cnt = 0 
for a in A:
  if not a in left_set:
    left_set.add(a)
    left_cnt += 1
  left_lst.append(left_cnt)
  
right_set = set()
right_lst = list()
right_cnt = 0
# print([*reversed(A)])
for a in reversed(A):
  if not a in right_set:
    right_set.add(a)
    right_cnt += 1
  right_lst.append(right_cnt)
# print(right_lst)
  
# print(left_lst[:-1], right_lst[1:])
  
print(
  max(
    [l+r for l, r in zip(left_lst[:-1], reversed(right_lst[:-1]))]
    )
  )