n=int(input())
number=[[0 for _ in range(100)]for _ in range(100)]

flag=False
cnt=1

for x in range(n):
    if flag:
        for y in range(n):
            number[y][x]=cnt
            cnt+=1
        flag=False
    else:
        for y in reversed(range(n)):
            number[y][x]=cnt
            cnt+=1
        flag=True



for y in range(n):
    for x in range(n):
        print(number[y][x],end=" ")
    print()
