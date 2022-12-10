file = open('numbers.txt','r')

sum = 0

for numbers in file:
    sum+= int(numbers)

file.close()

print(sum)

