n=int(input())
number=[[0 for _ in range(100)]for _ in range(100)]

flag=False
cnt=1

for y in range(n):
    if flag:
        for x in range(n):
            number[y][x]=cnt
            cnt+=1
        flag=False
    else:
        for x in reversed(range(n)):
            number[y][x]=cnt
            cnt+=1
        flag=True

for y in range(n):
    for x in range(n):
        print(number[y][x],end=" ")
    print()
