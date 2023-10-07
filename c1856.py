#1856 
def d(n):
    if (n<1):
        return 0
    elif(n==1):
        return 1 
    else:
        return d(n-1) + d(n-2) + d(n-3)
    
n = int(input())
a = d(n+1)
print(a)


