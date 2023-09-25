dna = input()
ds = 0

for i in range(0, 10):
    ds += int(dna[i])
    
if ds%7==4:
    print('suspect')
else:
    print('citizen')
