N = input()
bank = [500,100,50,10]

a=0

for i in bank:
  a += N//i
  N %= i
  # if N<=0:
  #   break

print(a)