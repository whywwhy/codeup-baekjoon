n = int(input())
a = list(map(int, input().split()))
r = 0

for a in a:
    if a%5==0:
        r += a 
print(r)
