# 25.	The variables a and b contain the dimensions of the sides of the rectangle. 
# Write a program that creates the following rectangle with dimensions a and b. Example result for a = 4 and b = 15:
#***************
#*             *
#*             *
#***************

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(0, b):
    print('*', end='')
print('')
for i in range(0, a-2):
    print('*', end='')
    for j in range(0, b-2):
        print(' ', end='')
    print('*')
for i in range(0, b):
    print('*', end='')
print('')