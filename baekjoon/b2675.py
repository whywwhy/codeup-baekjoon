a = int(input())
for i in range(a):
    n, s = input().split()
    t = ''
    for i in s:
        t += int(n)*i 
    print(t)