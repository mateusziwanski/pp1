# 16.	An array contains natural numbers: 15, 8, 31, 47, 2, 19. Create a program that displays the contents 
# of the array in reverse order. Use any loop statement. Sample result:
#existed array: 15 8 31 47 2 19 
#reverse array: 19 2 47 31 8 15

arr = [15, 8, 31, 47, 2, 19]
rev_arr = []

for i in range(len(arr),0,-1):
    rev_arr.append(arr[i-1])

print(f"existed: {arr}, reversed: {rev_arr}")