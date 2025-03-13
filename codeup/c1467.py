n,m=map(int,input().split())
arr=[[0 for _ in range(m)] for _ in range(n)]
num=1
for y in reversed(range(m)):
    for x in range(n):
        arr[x][y]=num
        num+=1


for y in range(n):
    for x in range(m):
        print(arr[y][x],end=" ")
    print()
