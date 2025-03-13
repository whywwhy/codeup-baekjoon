n = int(input())
ss = list(map(int, input().split()))
h = ss[0]
l = ss[0]

for s in ss:
    if s>h:
        h = s 
    if s<l:
        l = s 
        
print(h, l)
    