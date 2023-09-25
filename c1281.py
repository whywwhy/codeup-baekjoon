a,b = map(int, input().split())

r = 0

for i in range(a,b+1):
    if i % 2 !=0:
        if a==i:
            print(str(i),end='')
            r += i
        else:
            print('+' + str(i),end ='')
            r += i
    elif i % 2 ==0:
        print('-' + str(i),end='')
        r -= i
print('=' + str(r))
