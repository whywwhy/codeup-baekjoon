n = int(input())
prime ="prime"

for i in range(2, n):
    if n%i ==0:
        prime="not prime"

print(prime)
