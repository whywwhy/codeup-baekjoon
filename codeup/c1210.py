m = [0, 400, 340, 170, 100, 70]
a, b = map(int, input().split())

c = m[a]+m[b]

if c>500:
    print('angry')
else:
    print('no angry')
