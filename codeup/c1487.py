#1487
n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]

row = -1
col = m-1
flag = 1
num = n*m
ln = n
lm = m

while(ln != 0 and lm != 0):
    for _ in range(ln):
        row += flag
        array[row][col] = num
        num -= 1
    flag *= -1
    lm -= 1
    for _ in range(lm):
        col += flag
        array[row][col] = num
        num -= 1
    ln -= 1

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
