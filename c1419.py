s = input()
cnt = 0
for i in range(len(s)-4):
    if s[i:i+4] == 'love':
        cnt += 1
print(cnt)
