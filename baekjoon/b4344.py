c = int(input())
for i in range(c):
    l = list(map(int, input().split()))
    c = 0
    for j in l[1:]:
        a = sum(l[1:])/l[0]
        if j>a:
            c+= 1 
    r = c/l[0]*100 
    print('{0:0.3f}%'.format(r))