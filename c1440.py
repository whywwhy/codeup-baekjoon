n = int(input())
list = list(map(int, input().split()))

for i in range(n):
    print('{0}:'.format(i+1), end=' ')
    num = list[i]
    if (i == 0):
        rl = list[1:]
    elif (i == n-1):
        rl = list[:-1]
    else:
        rl = list[0:i]+list[i+1:]

    for j in rl:
        if (num == j):
            print('=', end=' ')
        elif (num > j):
            print('>', end=' ')
        elif (num < j):
            print('<', end=' ')
    print(' ')
