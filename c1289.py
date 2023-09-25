l = 0

for i in range(0, 3):
    h, v = map(int, input().split())
    if l < h*v:
        l = h*v

print(l)
