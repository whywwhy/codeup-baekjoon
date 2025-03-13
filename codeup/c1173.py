h, m = map(int, input().split())
if m >= 30: print(h, m - 30)
else:
    if h != 0: print(h - 1, 60 - abs(m - 30))
    else: print(23, 60 - abs(m - 30))
