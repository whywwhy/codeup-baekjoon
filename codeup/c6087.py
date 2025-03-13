a = int(input())
i = 0
for i in range(1, a+1):
    if i%3 == 0:
        continue
    else:
        print(i)
