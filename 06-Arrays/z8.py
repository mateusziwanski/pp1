# 8. An array contains numbers: -15, 8, -31, 47, -2, 19. 
# Create a program that finds and displays the maximum and minimum number. 
# Do not use available functions.

arr = [-15, 8, -31, 47, -2, 19]

max = arr[0]
min = arr[0]

for i in arr:
    if i >= max:
        max = i
    else:
        if i < min:
            min = i

print (max, min)