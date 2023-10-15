d = []
for i in range(19):
    d.append(input().split())
    for j in range(19):
        d[i][j] = int(d[i][j])
n = int(input())
for i in range(n):
    x,y = input().split()
    x = int(x)-1
    y = int(y)-1
    for j in range(19):
        if d[j][y] == 0:
            d[j][y]=1 
        else:
            d[j][y]=0
        if d[x][j]==0:
            d[x][j]=1 
        else:
            d[x][j]=0
for i in range(19):
    for j in range(19):
        print(d[i][j], end=" ")
    print()
