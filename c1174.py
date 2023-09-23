h, m = map(int, input().split())
result = ((h * 60) + m) - 30
print(((result // 60) + 24) % 24, result % 60)
