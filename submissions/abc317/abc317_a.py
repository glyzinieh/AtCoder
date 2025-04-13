N, H, X = map(int, input().split())
print(
  min(
    ((i+1, Pi) for i, Pi in enumerate(map(int, input().split())) if Pi >= X-H),
    key=lambda x: x[1]
    )[0]
  )