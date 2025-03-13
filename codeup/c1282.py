import math
n = int(input())

for i in range(1,n+1):
    t = math.sqrt(n-i)
    if t==round(t,1):
        print(i,int(t))
        break
