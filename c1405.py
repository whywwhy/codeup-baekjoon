n = int(input())
num = list(map(int, input().split()))

for i in num:
    print(i, end=' ')
print(' ')
for i in range(n-1):
    list = num[i+1:]+num[:i+1]
    for j in list:
        print(j, end=' ')
    list = []
    print(' ')
