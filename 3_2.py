N,M,K = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
first_iter = M//(K+1)
second_iter = M%(K+1)

result=0

# for _ in range(first_iter):
#     result += data[N-1]*K
#     result += data[N-2]
# for _ in range(second_iter):
#     result += data[N-1]

# print (result)
  
#for문 없이
result += (data[N-1]*K+data[N-2])*first_iter
result += (data[N-1]*K)*second_iter
print (result)