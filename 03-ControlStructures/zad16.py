# 16.	Write a program that displays two numbers entered from the keyboard in ascending order.
#Enter first number: 27
#Enter second number: 14
#Numbers in ascending order: 14, 27

first = int(input("Enter first number"))
second = int(input("Enter second number"))

if first > second:
    print (second, first)
else:
    print (first, second)
    