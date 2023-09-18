a = input()
key = a.index('H')
n1 = a[1:key]
n2 = a[key+1:]
print(int(n1)*12 + int(n2)*1)
