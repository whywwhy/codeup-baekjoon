import sys
a = int(sys.stdin.readline())

for i in range(a):
    n, m = map(int, sys.stdin.readline().split())
    print(n+m)