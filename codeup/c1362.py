n = int(input())

def mn(n):
    num = 0
    for i in range(1, n+1):
        num += i
    return num

a = mn(n)
for i in range(1, n+1):
    for j in range(0, i):
        print(a, end=' ')
        a -= 1 
    print()

