h, w = map(float, input().split())
sw = (h-100)*0.9
a = (w-sw)*100/sw 
if a <= 10:
    print('정상')
elif 10<=a<=20:
    print("과체중")
else:
    print("비만")
