n, r = map(int, input().split())
def f(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * f(n-1)
print(int(f(n) / (f(r) * f(n-r))))
