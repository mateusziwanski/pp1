# 7.An array contains values: 1, 2, 3, 4, 5. 
# Create a program that modifies the array values. 
# Display the array after each change.
# a.	subtract one from the first element of the array
# b.	increase the last array element by 4
# c.	multiple the middle array element by 2
# d.	adds 3 to each value of the array (use a loop statement)

arr = [1,2,3,4,5]
print (arr)

arr[0] = arr[0] - 1
print (arr)

arr[-1] = arr[-1] +4
print (arr)

arr[len(arr)//2] = arr[len(arr)//2] *2
print (arr)

for i in range(len(arr)):
    arr[i] = arr[i] + 3
print (arr)
