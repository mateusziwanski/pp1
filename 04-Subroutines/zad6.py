# 6.	Define a function that displays numbers in the layout as below (like on a phone keypad). Apply an loop statement. Then call the function.

def phone_keypad():
    for i in range(1,8,3):
        print(f'{i} {i+1} {i+2}')

phone_keypad()