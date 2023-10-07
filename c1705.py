str = input()
sum = str.count('3') + str.count('9') + str.count('6')

if sum == 0:
    print(str)
print("K"*sum)
