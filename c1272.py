k, h = map(int, input().split())
sm = 0

def gc(n):
    c = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            c = int(i / 2) * 10
        else:
            c = int(i / 2) + 1
    return c

sm += gc(k)
sm += gc(h)
print(sm)
