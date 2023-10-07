a = int(input())
day = a//86400 
hour = (a-86400*day)//3600
minn = (a-86400*day-3600*hour)//60
sec = a%60
print(day, hour, minn, sec)
