# 13.	An array contains values: [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]. Create a program that calculates the sum of all even numbers. 

arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

sum = 0

for row in arr:
    for number in row:
        if number %2 == 0:
            sum += number

print (sum)