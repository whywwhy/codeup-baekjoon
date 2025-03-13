def v(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1%n2 
    return n1 

v1, v2, v3 = map(int, input().split())
v12 = v(v1, v2)
cv = v(v12, v3)

print(cv)
