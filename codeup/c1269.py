a, b, c, n = map(int, input().split())
number = a

for i in range(0, n-1):
    number = number * b + c

print(number)
