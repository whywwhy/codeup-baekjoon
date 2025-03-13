#1852
def num(n):
    if n == 0:
        return n 
    num(n-1)
    print(n, end=" ")

n = int(input())
num(n)
