n,m=map(int,input().split())
number=[[0 for _ in range(100)]for _ in range(100)]

flag = True
cnt=1

for x in reversed(range(m)):
    if flag:
        for y in reversed(range(n)):
            number[y][x]=cnt
            cnt+=1
        flag = False
    else:
        for y in range(n):
            number[y][x]=cnt
            cnt+=1 
        flag = True

for y in range(n):
    for x in range(m):
        print(number[y][x],end=" ")
    print()

