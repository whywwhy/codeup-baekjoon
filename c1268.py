n = int(input())
nd = list(map(int, input().split()))
c = 0

for i in nd:
    if i % 2 == 1:
        c += 1

print(c)
