d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
r = 0
for i in range(len(a)):
    for j in d:
        if a[i] in j:
            r += d.index(j)+3 
print(r)