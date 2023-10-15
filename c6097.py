h,w = map(int, input().split())
n = int(input())

d = [[0 for i in range(w)]for j in range(h)]
for i in range(n):
    l, m, x, y = map(int, input().split())
    x=x-1
    y=y-1
    if m==0:
        for j in range(l):
            d[x][y+j]=1 
    else:
        for j in range(l):
            d[x+j][y]=1 
for i in range(h):
    for j in range(w):
        print(d[i][j], end=' ')
    print()
