s = input()
sum = 0
sum2 = 0
for i in s:
    if (i == '('):
        sum += 1
    elif (i == ')'):
        sum2 += 1

print(sum, sum2)
