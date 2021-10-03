def solve (A,N):
  ch=0
  a=(2**(N-1))
  for i in A:
    if i>=a:
      ch+=i
  return ch%((10 ** 9) + 7)
