N,K = map(int,input().split())
result = 0

while True:
  if N != 1:
    if N%K != 0:
      N = N-1
      result += 1
    else:
      N = N/K
      result += 1
  else:
    break

print(result)
