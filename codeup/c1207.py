a = list(map(int, input().split()))
result = a.count(1)
if result == 0:
    print('모')
elif result == 1:
    print('도')
elif result == 2:
    print('개')
elif result == 3:
    print('걸')
else:
    print('윷')
