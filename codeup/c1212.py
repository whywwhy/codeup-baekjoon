a, b, c = map(int, input().split())
if a>=b>=c or a>=c>=b:
    if b+c>a:
        print('yes')
    else:
        print('no')
elif b>=a>=c or b>=c>=a:
    if a+c>b:
        print('yes')
    else:
        print('no')
elif c>=a>=b or c>=b>=a:
    if a+b>c:
        print('yes')
    else:
        print('no')
else:
    print('')
