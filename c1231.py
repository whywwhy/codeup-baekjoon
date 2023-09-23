a = input()
for i in range(0, len(a)):
    if(a[i] == '+'):
        num1 = int(a[:i])
        num2 = int(a[i+1:])
        result = num1 + num2
        print(num1 + num2)
    elif(a[i] == '-'):
        num1 = int(a[:i])
        num2 = int(a[i+1:])
        result = num1 - num2
        print(num1 - num2)
    elif(a[i] == '*'):
        num1 = int(a[:i])
        num2 = int(a[i+1:])
        result = num1 * num2
        print(num1 * num2)
    elif(a[i] == '/'):
        num1 = int(a[:i])
        num2 = int(a[i+1:])
        result = float(num1) / float(num2)
        print('%.2f' % result)
