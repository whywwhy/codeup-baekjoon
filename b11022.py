a = int(input())

for i in range(1, a+1):
    n, m = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(i, n, m, n+m))