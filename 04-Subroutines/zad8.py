# 8.	Define a function that displays integer numbers from 1 to N. Then call the function and display numbers from 1 to 15.

def display_numbers(N):
    for numbers in range(1, N + 1):
        print(numbers, end = " ")

display_numbers(15)