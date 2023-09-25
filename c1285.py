e = input()
r = 0
s =''
ln = 0
ls = ''
li = 0
f = True

for i in range(0, len(e)):
    if e[i] in ('+', '-', '*', '/', '='):
        s = e[i]
        num = int(e[li:i])
        li = i+1 
        
        if f:
            f = False
            r += int(num)
            ln = num
            ls = s 
            continue 
        if ls == '+':
            r += num
            r = int(r)
        elif ls == '-':
            r -= num
            r = int(r)
        elif ls == '*':
            r *= num
            r = int(r)
        elif ls == '/':
            r /= num 
            r = int(r)
            
        ls = s 

print(int(r))
