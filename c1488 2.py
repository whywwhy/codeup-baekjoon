n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]

flag = -1
num = 1
row = n-1
col = m
rn = n
rm = m

while(n != 0 and m != 0):
    for _ in range(m):
        col += flag
        array[row][col] = num
        num += 1
    n = n-1
    for _ in range(n):
        row += flag
        array[row][col] = num
        num += 1
    m = m-1
    flag *= -1

for i in range(rn):
    for j in range(rm):
        print(array[i][j], end=' ')
    print(' ')
