#1854
def num(n):
    if n < 10:
        return n 
    return n%10 + num(n//10)

n = int(input())
print(num(n))
