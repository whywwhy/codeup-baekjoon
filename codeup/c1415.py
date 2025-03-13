#1415
numbers = list(map(int, input().split()))
be = 0
bo = 0
for number in numbers:
    if (number % 2 == 0) and (number > be):
        be = number
    elif (number % 2 == 1) and (number > bo):
        bo = number
if be == 0:
    print(bo)
elif bo == 0:
    print(be)
else:
    print(bo, be)
