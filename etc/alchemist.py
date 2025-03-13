############################################################################

# 1. 연금술사
# 빨(R), 초(G), 파(B) 각 색을 가진 물약이 있다. 빨, 초, 파 물약은 각각 1개씩 섞이면 증발해
# 없어지며(예를 들어, 빨간색/초록색/파란색 물약이 각각 3개씩 존재하는 경우 빨/초/파가 쌍을
# 이루어 증발되기에 남은 물약의 개수는 0개가 된다), 빨간색과 초록색이 섞이면 노란색(Y),
# 빨간색과 파란색이 섞이면 보라색(P), 초록색과 파란색이 섞이면 하늘색(C)이 된다. 섞이는
# 수량은 상관 없으며, 빨, 초, 파 중 한 색의 물약만 남으면 그 색 그대로 결과물이 된다. 섞인
# 후 결과물의 색상을 리턴하라. 만약 모두 증발하여 결과물이 없다면 X를 리턴한다. 입출력 예

# 입력 : “RRRRBRRR”
# 출력 : “P”
# 입력 : “BBB”
# 출력 : “B”
# 입력 : “BRGBRG”
# 출력 : “X”
# 입력 : “RGRGB”
# 출력 : “Y”
# 입력 : “BBBGBBGBBR”
# 출력 : “C”

############################################################################

# def alchemist(a:str) -> str:
#     if set("RGB").issubset(a): return "X"
#     if "R" in a and "G" in a: return "Y"
#     if "R" in a and "B" in a: return "P"
#     if "G" in a and "B" in a: return "C"
#     return a[0] if a else "X"

# print(alchemist("RRRRBRRR"))   
# print(alchemist("BBB"))       
# print(alchemist("BRGBRG"))    
# print(alchemist("RGRGB"))     
# print(alchemist("BBBGBBGBBR"))


# def alchemist(a:str) -> str:
#     r, g, b = a.count("R"), a.count("G"), a.count("B")

#     if r and g: return "Y"
#     if r and b: return "P"
#     if g and b: return "C"
#     if r: return "R"
#     if g: return "G"
#     if b: return "B"
#     return "X"

# print(alchemist("RRRRBRRR"))   
# print(alchemist("BBB"))       
# print(alchemist("BRGBRG"))    
# print(alchemist("RGRGB"))     
# print(alchemist("BBBGBBGBBR"))

def alchemy_potion(potions: str) -> str:
    r, g, b = potions.count("R"), potions.count("G"), potions.count("B")
    
    while r > 0 and g > 0 and b > 0:
        least = min(r, g, b)
        r, g, b = r - least, g - least, b - least
    
    if r and g: return "Y"
    if r and b: return "P"
    if g and b: return "C"
    if r: return "R"
    if g: return "G"
    if b: return "B"
    return "X"

print(alchemy_potion("RRRRBRRR"))
print(alchemy_potion("BBB"))
print(alchemy_potion("BRGBRG"))
print(alchemy_potion("RGRGB"))
print(alchemy_potion("BBBGBBGBBR"))
