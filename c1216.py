a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if(b - c == a):
    print('does not matter')
elif(b - c > a):
    print('advertise')
else:
    print('do not advertise')
