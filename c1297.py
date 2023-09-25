n = int(input())
m = 0
ml = 1 

for b in range(1, n//2):
    s = b*(n-2*b )
    
    if s>m:
        m = s 
        ml = b 
        
print(ml)
