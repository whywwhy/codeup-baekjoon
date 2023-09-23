a, b = [], ['+', '-', '*', '/', '**']
n1, n2 = input().split()
a = [eval(n1+b[i]+n2) for i in range(len(b))]
for i in range(len(b)): a.append(eval(n2+b[i]+n1))
print('%.6f' % (max(a)))

