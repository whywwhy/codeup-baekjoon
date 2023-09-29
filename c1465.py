n, m = map(int,input().split())
a=[[0 for _ in range(m)] for _ in range(n)]
num=1
for y in reversed(range(n)):
    for x in range(m):
        a[y][x]=num
        num+=1


for y in range(n):
    for x in range(m):
        print(a[y][x],end=" ")
    print()
