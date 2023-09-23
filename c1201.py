n = input()
if int(n) < 10: n = '0' + n
f, s = n[0], n[1]
result = (2 * int(s+f)) % 100
print(result, 'GOOD', sep='\n') if result <= 50 else print(result, 'OH MY GOD', sep='\n')
