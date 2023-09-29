n,m=map(int,input().split())
numbers=[[0 for _ in range(100)] for _ in range(100)]

cnt=1
for k in reversed(range(0,n+m-1)):
   for x in reversed(range(m)):
        for y in range(n):
            if y+(m-1-x)==k:
                numbers[y][x]=cnt
                cnt+=1

for y in range(n):
    for x in range(m):
        print(numbers[y][x],end=" ")
    print()
