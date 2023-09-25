n = input()
ns = list(map(int, input().split()))
mn = 0
for nm in ns:
    if(nm>mn):
        mn = nm
        
print(mn)
