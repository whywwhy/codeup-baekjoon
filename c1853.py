#1853
def num(n):
    if n==1:
        return n
    return n+ num(n-1)

n = int(input())
print(num(n))
