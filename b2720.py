t = int(input())
m = [25, 10, 5, 1]
c = [0]*4 
for i in range(t):
    s = int(input())

    for j in range(len(m)):
        c[j] = s//m[j]
        s = s%m[j]
    print(' '.join(map(str, c)))