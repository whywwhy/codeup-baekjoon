a, b = map(int, input().split())
print('짝수+', end = '') if a % 2 == 0 else print('홀수+', end = '')
print('짝수=', end = '') if b % 2 == 0 else print('홀수=', end = '')
print('짝수') if (a+b)%2 == 0 else print('홀수')
