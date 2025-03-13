a, b = input().split()
print((100 - (int(str(a)[:2])) + 13)) if int(b) in (1,2) else print(12 - int(str(a)[:2]) + 1)
