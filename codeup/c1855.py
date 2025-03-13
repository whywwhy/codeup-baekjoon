#1855 
def fina(n):
    if n == 0:
        return 0 
    elif n == 1 or n==2:
        return 1 
    else:
        return fina(n-2)+fina(n-1)
n = int(input())
print(fina(n))
