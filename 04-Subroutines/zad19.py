# 19.	Define a function that checks if the number is within the given range <x, y>. 
# The function returns boolean value. Then create a program and use the function you defined.

def checker(num, x, y):
    if num >= x and num <= y:
        return True
    elif num <= x and num >= y:
        return True
    else:
        return False

print(checker (10, 5, 15))