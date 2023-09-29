#1414
s = input().upper()
c1 = 0
c2 = 0
for i in range(len(s)):
    if s[i] == 'C':
        c1 += 1
        if i < len(s)-1 and s[i+1] == 'C':
            c2 += 1

print(c1)
print(c2)

