ln = input().split()
jns = input().split()
wn = ln[:6]
bn = ln[-1]
wnc = 0 
b = False 
for jn in jns:
    if jn in wn:
        wnc  += 1 
if bn in jns:
    b = True
if wnc == 6:
    print(1)
elif wnc == 5 and b:
    print(2)
elif wnc == 5:
    print(3)
elif wnc == 4:
    print(4)
elif wnc == 3:
    print(5)
else:
    print(0)
    
