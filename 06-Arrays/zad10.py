# 10.	An array contains integer numbers. Create a program that calculates and displays the number of even and odd values in the array. 
# Use the “while” loop statement.

arr = [1,2,3,4,5,6,7,8,9]

even = 0
odd = 0

for i in arr:
    if i %2 == 0:
        even += 1
    else:
        odd += 1

print (f"Even is: {even}, odd is {odd}")