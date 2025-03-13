sum = 0
for _ in range(3):
    percent, score = input().split()
    sum = sum + (float(percent) * int(score))
print('%.1f' % sum)

