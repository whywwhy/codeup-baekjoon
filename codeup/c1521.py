k, n = map(int, input().split())
a = 0
b = []

for i in range(k):
    bb = list(map(int, input().split()))
    b.append(bb)

for i in range(0, k):
    for j in range(0, k):
        if (b[i][j] != -1) and (1 <= b[i][j]+n <= 5):
            a += 1
print(a)
    
    
    
