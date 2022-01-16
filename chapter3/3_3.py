N,M = map(int,input().split())
mins = []
for _ in range(N):
  data = list(map(int, input().split()))
  mins.append(min(data))
result = max(mins)

print(result)

# result = 0
# for _ in range(N):
#   data = list(map(int, input().split()))
#   mins = min(data)
#   result = max(result,mins)

# print(result)
