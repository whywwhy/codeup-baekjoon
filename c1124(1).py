chemical_equation = input()
key = chemical_equation.index('H')
first_num = chemical_equation[1:key]
second_num = chemical_equation[key+1:]
print(int(first_num)*12 + int(second_num)*1)
