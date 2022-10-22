# 13.	Write a program that calculates values for the following fractions: 1/2, 1/3, ..., 1/10. Sample result:

for x in range(1,11):
    i = 1/x
    print(x, i)

# druga wersja

for i in range(1,11):
    print(f'1/{i} = {1/i}')