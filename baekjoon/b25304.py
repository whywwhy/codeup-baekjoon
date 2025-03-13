a = int(input())
b = int(input())

s = 0

for i in range(b):
    n, m = map(int, input().split())
    s += n*m 
    
if a==s:
    print("Yes")
else:
    print("No")