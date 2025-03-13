h, w = map(float, input().split())
sw = 0
ol = 0
if h<150:
    sw = h - 100
elif 150 <= h < 160:
    sw = (h-150)/2+50 
else:
    sw = (h-100)*0.9 

ol = (w-sw)*100/sw 

if ol<=10:
    print("정상")
elif 10<= ol <= 20:
    print("과체중")
else:
    print("비만")
