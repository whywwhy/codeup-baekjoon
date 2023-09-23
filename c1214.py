y, m = map(int, input().split())
february = 0
if(((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)):
    february = 29
else:
    february = 28
if(m < 8):
    if(m == 2):
        print(february)
    elif(m % 2 == 0):
        print('30')
    else:
        print('31')
else:
    if(m % 2 == 0):
        print('31')
    else:
        print('30')
