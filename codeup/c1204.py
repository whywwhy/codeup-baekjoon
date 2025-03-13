num = int(input())
if num in (11, 12, 13): print(str(num) + 'th')
else:
    data = []
    for i in str(num): data.append(i)
    tail_num = int(data.pop())
    if tail_num == 1: print(str(num) + 'st')
    elif tail_num == 2: print(str(num) + 'nd')
    elif tail_num == 3: print(str(num) + 'rd')
    else: print(str(num) + 'th')
