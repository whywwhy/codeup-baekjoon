n = int(input())
dic = dict()

for i in range(n):
    name, score = map(str, input().split())
    dic[int(score)] = name

dic2 = sorted(dic.keys(), reverse=True)

print(dic.get(dic2[2]))
