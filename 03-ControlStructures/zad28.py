# 28.	Write a program that displays the first fifty words of the Fibonacci sequence. 
# The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum 
# of the previous two. Sample result below. 
#https://en.wikipedia.org/wiki/Fibonacci_number
#0 1 1 2 3 5 8 13 21 34 ...

# nie do końca o to chodzi

def fibonacci(num):
    for i in range (num):
        if num == 0:
            return 0
        if num == 1 or num ==2:
            return 1
        if num >2:
            return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(15))