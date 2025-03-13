m, a, b = map(int, input().split())

while m<90:
    m+=5
    a+=1
    
if a>b:
    print("win")
elif a==b:
    print("same")
else:
    print("lose")
