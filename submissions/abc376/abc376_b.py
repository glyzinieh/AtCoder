class Ring:
  def __init__(self, n):
    self.n = n
    self.l = 0
    self.r = 1
    
  def left_adjacent(self, i):
    return i-1 if i!=0 else self.n-1
  
  def right_adjacent(self, i):
    return i+1 if i!=self.n-1 else 0

  def move(self, h, t):
    if h == 'L':
      forepos = self.l
      backpos = self.r
    else:
      forepos = self.r
      backpos = self.l
      
    # print((forepos, backpos))
    
    # 反時計回り
    otherwise_count = 0
    current = forepos
    while current!=t:
      current = self.left_adjacent(current)
      # print(f"otherwise:{current}")
      if current == backpos:
        otherwise_count = float('inf')  
        break
      otherwise_count += 1
    
    # 時計回り
    clockwise_count = 0
    current = forepos
    while current!=t:
      current = self.right_adjacent(current)
      # print(f"clockwise:{current}")
      if current == backpos:
        clockwise_count = float('inf')  
        break
      clockwise_count += 1
    
    if h == 'L':
      self.l = t
    else:
      self.r = t
    # print((otherwise_count, clockwise_count))
    return min(otherwise_count, clockwise_count)
      

N, Q = map(int, input().split())
ring = Ring(N)
ans = 0
for _ in range(Q):
  Hi, Ti = input().split()
  ans += ring.move(Hi, int(Ti)-1)
  # diff = ring.move(Hi, int(Ti)-1)
  # print({'r':ring.r, 'l':ring.l, 'diff':diff})
  # ans += diff
print(ans)